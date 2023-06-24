val = float(input("Qual o valor da casa? R$"))
sal = float(input("Qual o salário do comprador? R$"))
anos = int(input("Em quantos anos vai pagar? "))

cal = anos*12
cal2 = val/cal
cal3 = (30/100)*sal

print(f"Para pagar uma casa de R${val} em {anos} anos a prestação será de R${cal2:.2f} ")

if cal2<cal3:
    print("Empréstimo CONCEDIDO")
else:
    print("Empréstimo NEGADO")
