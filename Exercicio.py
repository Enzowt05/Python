nmercadoria=int(input("Número de mercadorias no estoque"))
estoque=int(0)

for mercadoria in range(1,nmercadoria+1):
    preco=int(input(f"Preço da Mercadoria {mercadoria}:"))
    estoque = estoque + preco

media = estoque/nmercadoria
print(f"Valor total: {estoque}, Quantidade de produtos: {nmercadoria}")
print(f"Média: {media}")