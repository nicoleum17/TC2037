def shunting_yard(regEx):
    precedence = {'*': 3, '.': 2, '|': 1}
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

def automata_nfa(expR):
    nfa = {}
    estado = 0
    o = 0
    for i in expR:
        if i.isalnum():
            nfa[estado] = [estado + 1 , i]
            o += 1
            estado += 1
        elif i == '|':
            # conectar dos líneas
            nfa[estado] = [[estado - o, '#'], [estado - (2 * o), '#']]
            o = 0
            estado += 1
        elif i == '.':
            print('.')
        elif i == '*':
            # saltos cero o más veces,        concatenar
            nfa[estado] = [[estado + 1 , '#'], [estado - 2, '#']]
            nfa[estado - 1] = [[estado - 2, '#'], [estado + 1, '#']]
            estado += 1

        estado += 1
    return nfa

alphabet = input("Alphabet: ")
regExp = input("RegEx: ")
posExp = shunting_yard(regExp)
print(posExp)
print (automata_nfa(posExp))