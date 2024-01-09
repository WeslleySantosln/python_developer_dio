# --------- TIPOS DE DADOS ----------- #
print("# --------- TIPOS DE DADOS ----------- #")

print(11 +20 + 1000)
print(1.5 + 1 + 0.5)
print(True)
print(False)
print("Python")

int()
float()
bool()
bool()
str()

# --------- DIR E HELP ----------- #
print("# --------- DIR E HELP ----------- #")
import math

#dir(1)
#help(math)

# --------- VARIAVEIS E CONSTANTES ----------- #
print("# --------- VARIAVEIS E CONSTANTES ----------- #")

NOME = "Weslley"
idade = 29

print("Meu nome é: " + NOME, ",Tenho ", idade, "anos.")


# --------- TIPOS DE CONVENÇÕES ----------- #
print("# --------- TIPOS DE CONVENÇÕES ----------- #")

fl = idade / 2

print(fl)

fl = idade // 2

print(fl)

st = str(f"String: {fl}")

print(st)

print(int(112.211223))

str = "10.10"

fl = idade / float(str)

print(fl)


# --------- INPUT E OUTPUT  ----------- #
print("# --------- INPUT E OUTPUT  ----------- #")

nome = input("informe seu nome: ")
idade = input("informe sua idade: ")

print(nome, idade)
print(nome, idade, end=". . . \n")
print(nome, idade, sep=" * ")