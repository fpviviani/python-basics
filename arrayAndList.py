from array import array

names_list = [] #isso é uma list, só armazena strings
names_list.append("Fábio")
names_list.append("Matheus")
names_list.insert(0, "Diogo") #insert insere antes do índice (pode ser usado em lista ou array)
print("List sendo impressa: \n")
print(names_list) #lista não pode ser concatenada em um mesmo print


numbers_array = array('b') #isso é um array, só armazena valores do tipo passado em sua criação. No exemplo: int
numbers_array.append(1)
numbers_array.append(2)
print("\nArray sendo impresso: \n")
print(numbers_array)
print(len(numbers_array)) #len conta a quantidade de indices (pode ser usado em lista ou array)

full_name = {'nome': 'Fábio'} #isso é um dicíonario. basicamente uma lista com string na chave
full_name['sobrenome'] = 'Piovani'
print("\n")
print(full_name)
print(full_name['sobrenome'])