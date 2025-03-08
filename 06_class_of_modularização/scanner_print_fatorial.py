#Código inicial para a aula de modularização
#Faça uma função que imprime o resultado fatorial de um numero inteiro.

def calc_and_print(n):
    if n < 0:
        print("Fatorial não definido para números negativos.")
        return
    elif n == 0:
        print(1)
        return
    
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i

    print(fatorial)


vlr = int(input("Digite um valor para calcular o fatorial: "))
calc_and_print(vlr)



