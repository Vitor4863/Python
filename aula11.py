nome  = input('Qual seu nome?')
idade = int(input('qual sua idade?'))
altura = float(input('Qual é sua altura ?'))
peso = float(input("Qual é seu peso?"))

imc = peso / (altura * altura)

print('o IMC = ', imc)
print("Muito abaixo do peso " , imc < 17)
print("Abaxo do peso normal " , imc >= 17 and imc < 18.5)
print("Peso dentro do normal" , imc >= 18.5 and imc < 25.0)
print("Acima do peso normal ", imc >= 25 and imc < 30)
print('Muito acima do peso :' , imc >= 30)
