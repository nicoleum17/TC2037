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
        if i != '|':
            o += 1
        if i.isalnum():
            nfa[estado] = [estado + 1 , i]
            estado += 1
        elif i == '|':
            print('|')
        elif i == '.':
            print('.')
        elif i == '*':
            # ... o más veces
            nfa[estado] = [estado - o, '#']
            nfa[estado] = [estado - (2 * o), '#']
            nfa[estado + 1] = [estado , '#']
            # cero ...
            nfa[estado + 2] = [estado, '#']
            nfa[estado + 1] = [estado + 3, '#']
            nfa[estado + 2] = [estado + 3, '#']
            o = 0
            estado += 3
        estado += 1
    return nfa

alphabet = input("Alphabet: ")
regExp = input("RegEx: ")
posExp = shunting_yard(regExp)
print(posExp)
print (automata_nfa(posExp))