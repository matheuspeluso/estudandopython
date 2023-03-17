a = "A"

b = "B"

c = 1.1

string = "a = {} b = {} c= {:.2f}" # no c eu posso formatar com as casas decimais ou deixar em branco e não formartar
formato = string.format(a, b , c)
print (formato)


string2 = "a = {2:.2f} b = {0} c= {1}" #perceba que agora eu que setei os indices para que fosse chamado
formato2 = string2.format(a, b , c)
print(formato2)

string3 = "a = {nome1} b = {nome2} c= {nome3:.2f}" 
formato3 = string3.format(nome1 = a, nome2 =  b , nome3 = c) #tb posso colocar um nome para ele ! lembrandi que tudo que vem dps de um parametro 
#nomeado tb precisa ser nomeado
print (formato3)

#quando uma função ta dentro do 