n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))

if (n1 > n2 > n3) :
    print("O primeiro valor é maior que todos e o terceiro é o menor")
if (n1 > n3 > n2) :
    print("O primeiro valor é maior que todos e o segundo é o menor")

if (n2 > n3 > n1) :
    print("O segundo valor é maior que todos e o menor é o primeiro")
if (n2 > n1 > n3) :
    print("O segundo valor é maior que todos e o menor é o terceiro")

if (n3 > n2 > n1) :
    print("O terceiro valor é maior que todos e o menor é o primeiro")
if (n3 > n1 > n2) :
    print("O terceiro valor é maior que todos e o menor é o segundo")
