
# *..........................Actividad Integradora 1...........................
#   Convertir una expresión regular a DFA
# 
#   By: Joanna Nicole Uriostegui Magaña
#       A01711853
#       14/03/25

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
            # 1. Un paréntesis de cierre es seguido por un paréntesis de apertura o un símbolo
            # 2. Un símbolo es seguido por otro símbolo o un paréntesis de apertura
            # 3. Un operador de cierre (*, +, ?) es seguido por un símbolo o un paréntesis de apertura
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

# ? Automata_Nfa ..............................................................
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


# ? Cerrando el clousure de epsilon ...............................................
#   Cerramos el clousure de epsilon para el NFA.
#   @param {str} nfa: el automata NFA
#   @return {str} el NFA con el clousure de epsilon cerrado.
# ? ...........................................................................
def e_closure(nfa, start, end):
    conjunto = set()
    transiciones = list(nfa[start])  #! Para no modificarla
    aceptacion = False

    conjunto.add(start)

    while transiciones: 
        # Sacamos solo un estado
        siguiente_estado, simbolo = transiciones.pop(0)  
        
        while simbolo == "#":  # Mientras el valor sea epsilon
            if(siguiente_estado == end): aceptacion = True

            # Sacamos el siguiente estado
            conjunto.add(siguiente_estado) 
            
            # Ver si hay más transcisiones
            if siguiente_estado in nfa:
                transiciones.extend(nfa[siguiente_estado])
            
            if not transiciones:  # Salir del while
                break

            siguiente_estado, simbolo = transiciones.pop(0)  # Siguiente

    return conjunto, aceptacion

    

# ? NFA a DFA ...............................................................
#   Convierte el NFA a DFA
#   @param {str} nfa: el automata NFA
#   @return {str} el automata DFA
# ? ...........................................................................

def nfa_to_dfa(nfa, start, end, alphabet):
    # Diccionario del DFA
    dfa = {}

    conjuntos = {}
    aceptacion_edo = set()
    conjunto = set()
    transiciones = list(nfa[start])  #! Para no modificarla

    conjunto, aceptacion_edo = e_clousure(nfa, start, end)
    print(conjunto, aceptacion_edo)
    
    for valor in alphabet:
        nuevo_conjunto = set()
        for estado in conjunto :
            for siguiente_estado, simbolo in nfa[estado]:
                if valor == simbolo:
                    nuevo_conjunto.add(siguiente_estado)
        print(nuevo_conjunto)
        for i in nuevo_conjunto:
            conjunto, aceptacion_edo = e_clousure(nfa, i, end)
            print(conjunto, aceptacion_edo)

        

# *............................... CODIGO ......................................

alphabet = input("Alphabet: ")
regEx = input("RegEx: ")
posExp = shunting_yard(agregar_concatenacion(regEx))

print("\n----RESULTS----")
print("INPUT:")
print(regEx)

nfa, start, end = regEx_to_nfa(posExp)
nfa = bubble_Sort(nfa)

print("\nNFA:")
for i in nfa:
    print(i, "=>", nfa[i])
print("Accepting state: ", end, "\n");

parcials = nfa_to_dfa(nfa, start, end, alphabet)

print("DFA: \n", parcials)