from time import sleep

nome = input("Digite o seu nome completo: ")
sleep(1)
print("\nAnalisando seu nome...\n")
sleep(1)
print(f"Seu nome em maiúsculas é: {nome.upper()}")
print(f"Seu nome em minúsculas é: {nome.lower()}")

nome = "".join(nome.split())

print(f"O seu nome ao todo tem {len(nome)} letras.")