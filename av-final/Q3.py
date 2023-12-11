senha = int(input("insira sua senha"))#recebe a senha

while senha != 2002:#emquanto a senha for diferente de 2002 ele pede que a senha seja inserida novamente
    print("senha invalida")
    senha = int(input("insira a senha"))
else:
    print('senha válida.')