
# *.............................. FUNCIONES ...................................

# ? Agregar Concatenacion .....................................................
#   Agrega la concatenación a la expresión regular.
#   @param {str} expresion: la expresión regular a concatenar
#   @return {str} la expresión regular en formato con concatenacion explicita
# ? ...........................................................................

def agregar_concatenacion(expresion):
    salida = ""
    operadores = {'|', '*', '+', '?', '('}  # Operadores que no requieren concatenación antes
    
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
#   @param {str} regEx: la expresión regular a convertir
#   @return {str} la expresión regular en formato posfijo
# ? ...........................................................................
def shunting_yard(regEx):
    precedence = {'*': 3, '+': 3, '.': 2, '|': 1}
    output = []
    stack = []

    for i in regEx:
        if i.isalnum(): 
            # 
            output.append(i)
        elif i == '(':
            stack.append(i) 
        elif i == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[i]:
                output.append(stack.pop())
            stack.append(i)
    while stack:
        output.append(stack.pop())
    return ''.join(output)

# ? RegEx to NFA...............................................................
#   Convierte la expresión regular en formato posfijo
#   a un automata no determinista finito (NFA).
#   @param {str} regEx: la expresión regular en posfijo
#   @return {str} el automata NFA
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

# ? Bubble Sort ...............................................................
#   Ordena el nfa de menor a mayor.
#   @param {str} nfa: el automata NFA
#   @return {str} el nfa con los estados ordenados.
# ? ...........................................................................
def bubble_Sort(nfa):
    keys = list(nfa.keys())
    n = len(keys)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if keys[j] > keys[j + 1]:
                keys[j], keys[j + 1] = keys[j + 1], keys[j]
                swapped = True
    
        if not swapped:
            break
    
    # Volvemos al diccionario 
    return {key: nfa[key] for key in keys}


def e_closure(nfa, estados):
    """ Calcula la cerradura epsilon de un conjunto de estados """
    closure = set(estados)
    stack = list(estados)  # Usamos una pila para recorrer los estados

    while stack:
        estado = stack.pop()
        if estado in nfa:  # Verificamos si el estado tiene transiciones
            for siguiente, simbolo in nfa[estado]:
                if simbolo == "#" and siguiente not in closure:
                    closure.add(siguiente)
                    stack.append(siguiente)
    
    return closure

def move(nfa, estados, simbolo):
    """ Devuelve el conjunto de estados alcanzables desde `estados` con `simbolo` """
    resultado = set()
    for estado in estados:
        if estado in nfa:
            for siguiente, s in nfa[estado]:
                if s == simbolo:
                    resultado.add(siguiente)
    return resultado

def nfa_to_dfa(nfa, start, end, alphabet):
    """ Convierte un NFA a DFA usando el algoritmo de e-closure """
    dfa = {}
    estados_dfa = {}
    aceptacion_dfa = set()
    
    estado_inicial = frozenset(e_closure(nfa, {start}))
    estados_dfa[estado_inicial] = "A"
    pendientes = [estado_inicial]
    contador = ord("A")  # Para asignar nombres a los estados DFA
    
    while pendientes:
        actual = pendientes.pop(0)
        estado_nombre = estados_dfa[actual]
        dfa[estado_nombre] = []
        
        for simbolo in alphabet:
            mov = move(nfa, actual, simbolo)
            if mov:
                nuevo_estado = frozenset(e_closure(nfa, mov))
                if nuevo_estado not in estados_dfa:
                    contador += 1
                    estados_dfa[nuevo_estado] = chr(contador)
                    pendientes.append(nuevo_estado)
                
                dfa[estado_nombre].append((estados_dfa[nuevo_estado], simbolo))
                
                if end in nuevo_estado:
                    aceptacion_dfa.add(estados_dfa[nuevo_estado])
    
    # Formateo de salida
    print("\nDFA:")
    for estado in sorted(dfa.keys()):
        print(f"{estado} => {dfa[estado]}")
    
    print("Accepting states:", sorted(list(aceptacion_dfa)))
    
    return dfa, "A", sorted(list(aceptacion_dfa))

# *............................... CODIGO ......................................

#alphabet = input("Alphabet: ")
#regEx = input("RegEx: ")
alphabet = "01"
regEx = "(0|1)0(0|1)*"

posExp = shunting_yard(agregar_concatenacion(regEx))

print("\n----RESULTS----")
print("INPUT:")
print(regEx)

nfa, start, end = regEx_to_nfa(posExp)
nfa = bubble_Sort(nfa)

print("\nNFA:")
for i in nfa:
    print(i, "=>", nfa[i])
print("Accepting state: ", end);

nfa_to_dfa(nfa, start, end, alphabet)

# *Refencias ...................................................
# OpenAI. (2025). ChatGP https://chat.openai.com/chat
# DeepSeek. (2025). Into the Unknown. https://chat.deepseek.com/