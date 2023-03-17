nome  = "Matheus"
altura = 1.61
valor_da_bmw = 100050.4
peso = 69 
imc = peso / (altura ** 2)

print (nome , " tem ", altura , "de altura,")
print ("pesa " , peso, "quilos e seu IMC é ")
print (imc)

# "f-strings" -- formatação
linha_1 = f"{nome} tem {altura:.2f} de altura" # {altura:.2f} o .2f se trata de quantas casas decimais  // poderia por também uma virgula exemplo abaixo
texto_teste = f"Uma BMW custa em media {valor_da_bmw:,.2f}"
linha_2 = f"pesa {peso} quilos e seu IMC é : {imc:.3f}"


print (linha_1)
print (linha_2)
print()
print(texto_teste)

