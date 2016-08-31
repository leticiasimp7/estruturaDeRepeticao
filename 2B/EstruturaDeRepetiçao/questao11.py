num1=eval(input("Digite o número inicial do intervalo: "))
num2=eval(input("Digite o número final do intervalor:"))
if (num1<num2):
    soma=0
    auxiliar=num1+1
while (auxiliar<num2):
    soma= auxiliar+soma
    auxiliar=auxiliar+1

else:
    print("Cídiho inválido")

print("O valor inicial é: ", num1)
print("O valor final é: ", num2)
print("A soma é: ", soma)

