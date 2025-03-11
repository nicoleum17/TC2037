def shunting_yard(regEx):
    precedence = {'*': 4, '+': 4, '.': 3, '|': 2, '(': 1}
    output = []
    stack = []

    for i in regEx:
        if i.isalnum():
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

alphabet = input("Alphabet: ")
regEx = input("RegEx: ")
posExp = shunting_yard(regEx)
print("Postfix Expression:", posExp)
nfa, start, end = automata_nfa(posExp)
print("NFA: \n", nfa)
print("Start State:", start)
print("End State:", end)