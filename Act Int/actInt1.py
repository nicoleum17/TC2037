
# *..........................Actividad Integradora 1...........................
#   Convertir una expresión regular a NFA y luego a DFA.
# 
#   By: Joanna Nicole Uriostegui Magaña
#       A01711853
#       14/03/25

# *.............................. FUNCIONES ...................................

# ? Agregar Concatenacion .....................................................
#   Agrega la concatenación a la expresión regular.
#   Parámetros: expresion: la expresión regular a concatenar.
#   Return: la expresión regular en formato con concatenacion explicita.
#   Complejidada: O(n)
# ? ...........................................................................

def agregar_concatenacion(expresion):
    # Para los que no se tienen que concatgenar
    salida = ""
    operadores = {'|', '*', '+', '?', '('}
    
    for i in range(len(expresion)):
        actual = expresion[i]
        salida += actual
        
        # Si no es el último carácter, revisamos si se requiere concatenación
        if i < len(expresion) - 1:
            siguiente = expresion[i + 1]
            
            # Se agrega '.' si:
            # 1. Un ( es seguido por un ) o un símbolo
            # 2. Un símbolo es seguido por otro símbolo o un (
            # 3. Un operador de cierre (*, +, ?) es seguido por un símbolo o un ()
            if (actual not in operadores and siguiente not in {'|', ')', '*', '+'}) or \
               (actual in {'*', '+'} and i < len(expresion) - 1) or \
               (actual in {'*', '+', '?'} and siguiente not in operadores and siguiente not in {')', '|', '+'}) or \
               (actual == ')' and siguiente not in {'|', ')', '*', '+'}) or \
               (actual == '*' and siguiente not in operadores and siguiente != ')'):
                salida += '.'
    
    return salida

# ? Shuting Yard ..............................................................
#   Convierte la expresión regular en formato infijo
#   a formato posfijo.
#   Parámetros: la expresión regular a convertir
#   Return: la expresión regular en formato posfijo
#   Complejidada: O(n)
# ? ...........................................................................
def shunting_yard(regEx):
    precedence = {'*': 3, '+': 3, '.': 2, '|': 1}
    output = []
    stack = []

    for i in regEx:
        if i.isalnum(): 
            # pasar el alphabet
            output.append(i)
        elif i == '(':
            stack.append(i) 
        elif i == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            # Cuando ya llega al final de operadores
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[i]:
                output.append(stack.pop())
            stack.append(i)
    while stack:
        # Se agrega el resto de la expresión
        output.append(stack.pop())
    return ''.join(output)

# ? RegEx to NFA...............................................................
#   Convierte la expresión regular en formato posfijo
#   a un automata no determinista finito (NFA).
#   Parámetros:  la expresión regular en posfijo
#   Return:  el automata NFA
#   Complejidada: O(n)
# ? ...........................................................................
def regEx_to_nfa(regEx):
    stack = []
    estado = 0

    for i in regEx:
        if i.isalnum():
            # Agregar un estado
            nfa = {estado: [(estado + 1, i)]}
            estado += 2
            stack.append((nfa, estado - 2, estado - 1))
        elif i == '|':
            # Cuando hay un OR
            nfa2, start2, end2 = stack.pop()
            nfa1, start1, end1 = stack.pop()
            nfa = {
                estado: [(start1, '#'), (start2, '#')],
                end1: [(estado + 1, '#')],
                end2: [(estado + 1, '#')]
            }
            nfa.update(nfa1)
            nfa.update(nfa2)
            estado += 2
            stack.append((nfa, estado - 2, estado - 1))
        elif i == '.':
            # Concatenar
            nfa2, start2, end2 = stack.pop()
            nfa1, start1, end1 = stack.pop()
            nfa = nfa1
            nfa[end1] = [(start2, '#')]
            nfa.update(nfa2)
            stack.append((nfa, start1, end2))
        elif i == '*':
            # Cero o más veces
            nfa1, start1, end1 = stack.pop()
            nfa = {
                estado: [(start1, '#'), (estado + 1, '#')],
                end1: [(start1, '#'), (estado + 1, '#')]
            }
            nfa.update(nfa1)
            estado += 2
            stack.append((nfa, estado - 2, estado - 1))
        elif i == '+':
            # Una o más veces
            nfa1, start1, end1 = stack.pop()
            nfa = {
                estado: [(start1, '#')],
                end1: [(start1, '#'), (estado + 1, '#')]
            }
            nfa.update(nfa1)
            estado += 2
            stack.append((nfa, estado - 2, estado - 1))

    # Regresamos el NFA
    nfa, start, end = stack.pop()
    return nfa, start, end

# ? Cerrandura epsilon.........................................................
#   Cerramos el clousure de epsilon para el NFA.
#   Parámetros: el automata NFA
#   Return: el NFA con el clousure de epsilon cerrado.
#   Complejidada: O(n_estados + n_transiciones)
# ? ...........................................................................
def e_closure(nfa, estados):
    closure = set(estados)
    stack = list(estados)  # Usamos una pila para recorrer los estados

    while stack:
        estado = stack.pop()
        if estado in nfa:  # Verificamos si el estado tiene transiciones
            for siguiente, simbolo in nfa[estado]:
                # Agregamos los estados a los que se puede llegar mediante #
                if simbolo == "#" and siguiente not in closure:
                    closure.add(siguiente)
                    stack.append(siguiente)
    
    return closure

# ? Move.......................................................................
#   Por cada símbolo en el alfabeto, se mueve a la siguiente transición
#   Parámetros: el automata NFA, conjunto de estados, símbolo del alfabeto
#   Return: estados a los que se puede llegar con dicho peso
#   Complejidada: O(n_estados)
# ? ...........................................................................
def move(nfa, estados, simbolo):
    resultado = set()
    # Para recorrer obtener los valores a los que se puede llegar desde los
    # estados del conjunto mediante algun simbolo del alfabeto.
    for estado in estados:
        if estado in nfa:
            for siguiente, s in nfa[estado]:
                if s == simbolo:
                    resultado.add(siguiente)
    return resultado

# ? NFA a DFA .................................................................
#   Convierte el NFA a DFA
#   Parámetros: el automata NFA
#   Return: el automata DFA
#   Complejidada: O(2 ^(n_estados))
# ? ...........................................................................
def nfa_to_dfa(nfa, start, end, alphabet):
    dfa = {}
    estados_dfa = {}
    aceptacion_dfa = set()
    
    # Para el primer estado obtenemos su conjunto por cerrandura epsilon
    estado_inicial = frozenset(e_closure(nfa, {start}))
    estados_dfa[estado_inicial] = "A"
    pendientes = [estado_inicial]
    # Para obtener la numeración de estados pero en orden alfabético
    contador = ord("A") 
    
    # Recorremos todos los conjuntos que se obtienen de los estados
    while pendientes:
        actual = pendientes.pop(0)
        estado_nombre = estados_dfa[actual]
        dfa[estado_nombre] = []
        
        # Para cada simbolo del alfabeto realizamos un move
        for simbolo in alphabet:
            mov = move(nfa, actual, simbolo)
            # Comparamos si el conjunto obtenido es nuevo
            if mov:
                nuevo_estado = frozenset(e_closure(nfa, mov))
                if nuevo_estado not in estados_dfa:
                    contador += 1
                    estados_dfa[nuevo_estado] = chr(contador)
                    pendientes.append(nuevo_estado)
                
                # Si es nuevo, se agrega a la cola
                dfa[estado_nombre].append((estados_dfa[nuevo_estado], simbolo))
                
                # Agregamos si es estado de aceptación
                if end in nuevo_estado:
                    aceptacion_dfa.add(estados_dfa[nuevo_estado])
    
    # Imprimimos en pantalla el DFA ordenado
    print("\nDFA:")
    for estado in sorted(dfa.keys()):
        print(estado, "=>", dfa[estado])
    
    # Y los estados de aceptación
    print("Accepting states:", sorted(list(aceptacion_dfa)))
# *............................... CODIGO ......................................

alphabet = input("Alphabet: ")
regEx = input("RegEx: ")

# Agregar los puntos para indicar concatenación 
# y pasamos la expresión a formato posfijo.
posExp = shunting_yard(agregar_concatenacion(regEx))

print(posExp)

print("\n----RESULTS----")
print("INPUT:")
print(regEx)

# Obtenemos el NFA
nfa, start, end = regEx_to_nfa(posExp)

# Lo mostramos en pantalla
print("\nNFA:")
for estado in sorted(nfa.keys()):
    print(estado, "=>", nfa[estado])
print("Accepting state:", end)

# Obtenemos y mostramos el DFA
nfa_to_dfa(nfa, start, end, alphabet)

# *Refencias ...................................................
#  - OpenAI. (2025). ChatGP https://chat.openai.com/chat
#  - DeepSeek. (2025). Into the Unknown. https://chat.deepseek.com/
#  - Chaves, S. (2023, July 31). 
#    ¿Cuáles son las principales funciones en Python? Formadores IT. 
#    https://formadoresit.es/cuales-son-las-principales-funciones-en-python/