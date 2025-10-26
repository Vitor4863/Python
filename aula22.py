tupla_num = (1,2,3,4)
print(tupla_num)


#tupla_num[0] = 2

print(tupla_num.count(1))
print(tupla_num.index(2))
print(len(tupla_num))


tupla_conv = list(tupla_num)


tupla_conv.append(5)
print("O elemento 5 adicionado : %s" % (tupla_conv))

tupla_conv.pop()

print("Elemento 5 removido : %s" % tupla_conv)