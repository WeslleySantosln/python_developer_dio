saldo = 1000
extrato = []
num_saque = 0


# --------- menu ---------- #

menu = """
------ M E N U ------ 

    [S] = SAQUE
    [D] = DEPOSITO
    [E] = EXTRATO
    [Q] = SAIR

------ BANCO GT ------


=>

"""

#Metodo para confirmar se valor digitado é numero

def numero_valido(valor):
    
    while True:

            if not isinstance(valor, (int, float)):
                valor = input("Digite um valor valido ou [S] para sair!")
                if valor.upper() == "S":
                    break
                else:
                    continue
            else:
                valor = int(vl_saque)
                saque(vl_saque)
                break  




#Deposito - não deixar depositar valores negativos - constar todos os depositos em extrato

def deposito(valor):
    if valor <= 0 :
        return print("Valor não permitido!")
    else:
        saldo += valor
        extrato.append(f"Deposito realizado no valor de {valor}. Horario: ")  
        print(saldo)  


#saque - só pode no maximo 3 por dia - limite de 500 por saque - usuario com saldo negativo deve ser informado - todos os saques deve ser exibidos em extrato

def saque(valor):
    global num_saque,saldo

    if num_saque == 3:
        return print("Numero de saque excedido")
    elif valor > 500 :
        return print(f"Limite maximo para saque: R$ 500,00. Valor inserido: {valor}")
    elif valor > saldo :
        return print(f"Valor para saque maior que o saldo da conta. Saldo da conta: {saldo}, Valor de saque{valor}.")
    elif valor < 0 :
        return print("Porfavor coloque um numero posito!")
    else:
        saldo -= valor
        num_saque=+ 1
        extrato.append(f"Saque realizado no valor de {valor}. Horario: ")
        return print(f"Seu saldo é: R$ {saldo:.2f}")


#Extrato - listar todos os depositos e saques da conta - exibir no final o saldo da conta - valores deve ser exibido no seguinte formato(R$ 1.500,00)
    
def funcao_extrato():
    print(extrato)
    print(saldo)



while True:
    
    escolha = input(menu).upper()

    if escolha == "S" :

        vl_saque = input("Digite um valor para saque: ")

          
            

    else:    
        break   





     