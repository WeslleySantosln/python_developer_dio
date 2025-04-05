# app/key_generator.py
import datetime
import random
import string
from app.core.calculations import factorial_and_cube, is_valid_triangle, max_side

def generate_key(sides):
    """Gera uma chave baseada nos lados fornecidos"""
    # Valida os lados fornecidos
    if not is_valid_triangle(sides):
        raise ValueError("Os valores devem ser de 0 a 57 e todos os lados devem ser diferentes")

    # Encontra o maior lado do triângulo
    max_value = max_side(sides)

    # Calcula o fatorial do maior valor e eleva ao cubo
    result = factorial_and_cube(max_value)

    # Formata o timestamp atual
    timestamp = datetime.datetime.now().strftime("%d%m%y%H%M%S")

    # Gera um número aleatório para a chave
    random_number = random.randint(1000000, 9999999)

    # Monta a chave final
    semifinal = f"{result}{timestamp}{random_number}"

    a = 255 - len(semifinal)

    # Define o tamanho da string
    tamanho = a

    # Gera uma string com 255 letras aleatórias (maiúsculas e minúsculas)
    letras_aleatorias = ''.join(random.choices(string.ascii_letters, k=tamanho))

    # Exibe o resultado
    print(f"String gerada ({len(letras_aleatorias)} caracteres):")
    print(letras_aleatorias)

    return semifinal + letras_aleatorias



if __name__ == "__main__":
   i = [1,2,3]
   x = generate_key(i)
   print(f"tamanho:{len(x)} o numero gerado: {x}")

   y = [1,2,57]
   t = generate_key(y)
   print(f"tamanho:{len(t)} o numero gerado: {t}")
   

