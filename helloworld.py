# print('hello world from python')

#---------------------------------------------------------------

#Crie uma variável chamada Saldo e atribua o 
# valor de 950,60. Em seguida, pergunte ao usuário 
# quanto dinheiro ele deseja sacar e armazene a 
# resposta em uma variável chamada Saque. Subtraia 
# o valor de saque do valor de saldo e imprima a 
# mensagem "Seu novo saldo é {saldo}"

# saldo = 1000.454545
# print(f"Seu saldo eh:  {saldo: .2f}")
# saque = float(input("quanto deseja sacar?"))
# print(f"Voce esta sacando:  {saque}")
# novoSaldo = saldo - saque
# print(f"Seu novo saldo eh de {novoSaldo: .2f}")

#---------------------------------------------------------------

#Faça um programa que crie uma lista com 5 
# frutas e permita que o usuário digite o nome 
# da fruta. Se for uma fruta repetida, 
# deverá ser desconsiderada.

# solucao 1
# frutas = ["banana", "maca", "uva", 'pera', 'kiwi']
# userFruta = input("Digite uma fruta")
# userFruta = userFruta.lower()
# if userFruta in frutas: 
#     input("fruta repetida, escolha outra") 
# else:
#     frutas.append(userFruta) 
# print(frutas)

# solucao 2
# comprarFrutas = ["banana", "maca", "uva", 'pera', 'kiwi']
# userFruta = input("Digite 1 fruta que falta comprar no mercado")
# userFruta = userFruta.lower()
# comprarFrutas.append(userFruta)
# newList = set(comprarFrutas)
# print(comprarFrutas)
# print(newList)

#---------------------------------------------------------------
#usuario digitar 5 nomes separados por virgula e develver uma lista de strings

# frase = input("type 5 names separated by ,")
# newf = frase.split(",")
# print(newf)

#---------------------------------------------------------------
# lista com 5 numeros inteiros

# mlist = []
# while len(mlist) < 5:
#     userInput = input("digite um numero inteiro")
#     mlist.append(userInput)
#     print(mlist)

#aqui eu poderia ainda ter tratado o erro se o usuario digitar 
#qqr coisa que seja diferente de um numero inteiro

#---------------------------------------------------------------

# IMC

# peso = float(input("digite seu peso em kg"))
# altura = float(input("digite sua altura em metros"))
# imc = peso / (altura ** 2)
# if imc < 18.5:
    # print(f"seu imc é: {imc} e você está abaixo do peso")
#   elif imc < 25:
#     print(f"seu imc é: {imc} e você está com peso normal")
#   elif imc < 30:
#     print(f"seu imc é: {imc} e você está com sobrepeso")
#   elif imc < 35:
#     print(f"seu imc é: {imc} e você está com obesidade")

#---------------------------------------------------------------

# x = 3

# if x % 2 == 0: 
#     print("par") 
# else: 
#     print("impar")

#---------------------------------------------------------------

# senha = input("digite uma senha de 4 digitos")
# senhaCorreta = 1234

# while senha != senhaCorreta :
#     senha = input("digite uma senha de 4 digitos") 
# else: 
#     print('senha')

#---------------------------------------------------------------
# solicite ao usuario para digitar uma frase e em seguida exiba cada frase e o numero de caracteres.

# frase = input("digite uma frase") 
# print(frase.split())
# print(len(frase))

#---------------------------------------------------------------
# dado um valor n calcula o fatorial de n
# de
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# # Example usage:
# number = 5
# print("Factorial of", number, "is", factorial(number))


#---------------------------------------------------------------
# dicionario, loop mostrar os valores

# dic = {"um": 1, "dois": "dois", "tres": 3}
# for i in dic:
#     print(i)    

#---------------------------------------------------------------