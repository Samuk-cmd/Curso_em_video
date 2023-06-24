ano = int(input("Digite o seu ano de nascimento: "))

cal = 2023-ano
ano2 = 18-cal
ano3 = cal-18

if cal == 18:
    print(f"Quem nasceu em {ano} tem {cal} anos em 2023")
    print("Você tem que se alistar IMEDIATAMENTE!")
elif cal<18:
    print(f"Quem nasceu em {ano} tem {cal} anos em 2023")
    print(f"Ainda faltam {ano2} anos para o alistamento!")
    print(f"Seu alistamento será em {2023+ano2}")
elif cal>18:
    print(f"Quem nasceu em {ano} tem {cal} anos em 2023")
    print(f"Você já deveria ter se alistado há {ano3} anos")
    print(f"Seu alistamento foi em {2023-ano3}")