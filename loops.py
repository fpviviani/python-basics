for index in range (0, 2): #for dentro do range setado
    print(index)

print("\n")

for name in ['Fábio', 'Tássio', 'Giovana']: #for dentro de uma coleção
    print(name)

print("\n")

for letter in 'Função': #for dentro de uma string
    print(letter)

names = ['Diogo', 'Matheus', 'Ádrian']
index = 0
while index < len(names): #while percorrendo o tamanho da lista
    print(names[index])
    index = index + 1 #index++ não existe em python
