nome = input('Digite seu nome\n')
i = True
texto = "Digite sua idade\n"
while i == True:
    try:
       idade =   input(texto)
       idade = int(idade)
       i = False
    except:
        i = True
        texto = "Digite uma idade válida:  valor {} não é permitido\n".format(idade)

peso  =  input('Peso\n')

print("Olá {} , idade {} , Peso {}".format(nome,idade,peso))