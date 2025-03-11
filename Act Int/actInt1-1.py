
# .............................. FUNCIONES ....................................

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
def automata_nfa(regEx):
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
def bubbleSort(nfa):
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

# ............................... CODIGO ......................................

alphabet = input("Alphabet: ")
regEx = input("RegEx: ")
posExp = shunting_yard(regEx)

print("----RESULTS----")
print("INPUT:")
print(regEx)

nfa, start, end = automata_nfa(posExp)
print("NFA: \n", nfa)
print("Accepting state: ", end)
nfa = bubbleSort(nfa)

for i in nfa:
    print(i, "=>", nfa[i])