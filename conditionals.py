escolha = 0
name = ""
while(escolha != 2):
    print("\nEscolha uma opção: \n1 - Oi\n2 - Tchau\n3 - Nome")
    escolha = int(input("Digite a opção referente a sua escolha: " ))
    if(escolha == 1):
        if (name == ""):
            print("E aí")
        else:
            print("E aí, " + name)
    # elif tem a função de elseif
    elif(escolha == 2):
        if (name == ""):
            print("Falou")
        else:
            print("Falou, " + name)
    elif(escolha == 3):
        name = input("Digite seu name: ")

