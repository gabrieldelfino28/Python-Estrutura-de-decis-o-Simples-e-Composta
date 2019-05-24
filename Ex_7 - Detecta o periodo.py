print("Diga-nos de qual periodo você pertence")
periodo = input("M para matutino, V para Vespertino ou N para Norturno: ")

if (periodo == "M") :
    print("Bom Dia!")
elif (periodo == "V") :
    print("Boa Tarde!")
elif (periodo == "N") :
    print("Boa Noite!")

else :
    print ("Valor Inválido")
