idade = 23 
altura = 1.75

nome = "João"

ativo = True


print(f"{nome} tem {idade} anos e {altura} m de altura" )


x = 10 
y = 11

total = x * 11


print(f"{total}")


frutas = ["maça" , "banana", "laranja"]
print("frutas[0]")

frutas.append("uva")
print(frutas)



coordenadas = (10,20)
print (coordenadas[0])

pessoa = {"nome":"João" , "Idade": 23}
print(pessoa["nome"])
pessoa["altura"] = 1.75
print(pessoa)



produtos = produtos = [
    {"nome": "Arroz", "preco": 10.5},
    {"nome": "Feijão", "preco": 8.0},
    {"nome": "Macarrão", "preco": 7.5},
    {"nome": "Óleo", "preco": 12.0},
    {"nome": "Leite", "preco": 5.5}
]



total = 0

for produtos in produtos : 
    total += produtos["preco"]

    print("Preço total " , total)

