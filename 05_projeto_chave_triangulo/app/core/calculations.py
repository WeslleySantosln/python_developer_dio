import math

# Função para validar se os lados são entre 0 e 57 e nenhum dos lados podem ser iguais
def is_valid_triangle(sides):
    # Verifica se todos os lados estão entre 0 e 57
    valid_range = all(side > 0 and side <= 57 for side in sides)
    
    # Verifica se todos os lados são diferentes
    a, b, c = sides  # Desempacota os lados
    all_different = (a != b) and (a != c) and (b != c)
    
    # Retorna True apenas se ambas as condições forem satisfeitas
    return valid_range and all_different
# Função para encontrar o maior lado do triângulo

def max_side(sides):
    return max(sides)


# Função para calcular o fatorial e elevar ao cubo
def factorial_and_cube(n):

    factorial = math.factorial(n)
    return factorial ** 3