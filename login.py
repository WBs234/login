import os
import time

os.system("clear")

class bcolors:
    s = '\033[92m' #GREEN
    Cadastrastrado com sucesso = '\033[93m' #YELLOW
    n = '\033[91m' #RED
print(' _  _  _ ______       _______ _______  ______ _____  _____  _______')
time.sleep(0.3)

print(' |  |  | |_____]      |______ |       |_____/   |   |_____]    |   ')
time.sleep(0.3)

print(' |__|__| |_____]      ______| |_____  |    \_ __|__ |          |  \n')
time.sleep(1.0)

login = input("Login:")

print ()
time.sleep(1.0)

print("Seu nome é: " + login)

input("certo? digite [s ou n]: ")
time.sleep(1.0)

print("\n\n")
print("Cadastrado com sucesso\n")
os.system ("clear")
print(f"Olá, bem vindo {login} ao meu teste de divisão")
print(" ")
num1=float(input(" digite o primeiro numero:"))
num2=float(input("digite o segundo numero:"))
divisao= num1/num2
print(" ")
print("resultado é ", divisao)
