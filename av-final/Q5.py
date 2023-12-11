pc = 0#contcontador de números pares

for i in range(5):#loop para inserir os números
    numero = int(input("insira um número."))
    if numero % 2 == 0:#verifica se o número é par
        pc += 1
#EXIBE QUANTOS NÚMEROS PARES FORAM INSERIDOS
print(f"quantidade de números pares é de {pc}.")