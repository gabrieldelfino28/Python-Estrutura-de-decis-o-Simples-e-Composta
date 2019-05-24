n1 = float(input("Infome o valor da primeira nota: "))
n2 = float(input("Informe o valor da segunda nota: "))

total = (n1 + n2)/2

if (total == 10) :
    print("Aprovado com Distinção")

elif (total > 7 and total < 10) :
    print("Aprovado")

else :
    print("Reprovado")


