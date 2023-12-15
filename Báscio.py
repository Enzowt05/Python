n1=input("Coloque o primeiro número")
n2=input("Coloque o segundo número")
n1=float(n1)
n2=float(n2)
n3 = n1 + n2

if n3%2==0:
    print(f'Soma Par: {n3}')
else:
    print(f'Soma Ímpar {n3:.2f}')