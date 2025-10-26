lista = [1,2,3,3,3,4,5,6,7]

print("Tamanho da lista :  %d" % len(lista))

lista.append(8)

print(lista)

lista.pop()
print(lista)

lista.pop(0)
print(lista)

lista.remove(2)
print(lista)

lista.insert(0,1)
print(lista)

print(lista.count(3))

print(lista.index(1))

lista.clear()
print(lista)