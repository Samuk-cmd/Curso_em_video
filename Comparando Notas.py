n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

cal = (n1+n2)/2

if cal >= 7:
    print(f"Quem tirou {n1} e {n2} tem a média {cal:.1f}")
    print("Aprovado")
elif cal<7 and cal>=5:
    print(f"Quem tirou {n1} e {n2} tem a média {cal:.1f}")
    print("Recuperação")
elif cal<5:
    print(f"Quem tirou {n1} e {n2} tem a média {cal:.1f}")
    print("Reprovado")
