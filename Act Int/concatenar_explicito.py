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

# Ejemplos de uso
exp1 = "(a|b)*abb"
exp2 = "(a|b)+aba*"
exp3 = "(0|1)0(0|1)*"
exp4 = "1*(01)*(01)+"
print(agregar_concatenacion(exp1))  # (a|b)*.a.b.b
print(agregar_concatenacion(exp2))  # (a|b)+.a.b.a*
print(agregar_concatenacion(exp3))  
print(agregar_concatenacion(exp4)) 

# (a|b)*.a.b.b
# (a|b)+.a.b.a*
# (0|1).0.(0|1)*
# 1*(0.1)*(0.1)+
# 1*.(0.1)*.(0.1)+