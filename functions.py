def string_letters(string): #função que retorna as letras de uma string qualquer
    for letter in string: 
        print(letter)
    
escolha = 0
while(escolha != 2):
    print("\nEscolha uma opção: \n1 - Inputar string\n2 - Parar")
    escolha = int(input("Digite a opção referente a sua escolha: " ))
    if(escolha == 1):
        string = input("\nDigite uma frase ou palavra: ")
        string_letters(string) #chamando a função, passsando como parametro as strings inputadas
    elif(escolha == 2):
        print("Falou")
