num = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão:\n[ 1 ] Converter para BINÁRIO\n[ 2 ] Converter para OCTAL\n[ 3 ] Converter para HEXADECIMAL\n")
op = int(input("Sua opção: "))

binario = format(num, "b")
octal = format(num, "o")
hexa = format(num, "x")

if op == 1:
    print("O número {} em BINÁRIO é: {}".format(num, binario))
elif op == 2:
    print("O número {} em OCTAL é: {}".format(num, octal))
elif op == 3:
    print("O número {} em HEXADECIMAL é: {}".format(num, hexa))
