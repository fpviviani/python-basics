name = input("Digite seu nome:")
hello = "Hello"
msg = hello + ", " + name
#str.upper transforma todas as letras da string em maiúscula 
print(msg.upper())
#str.lower transforma todas as letras da string em minúscula 
print(msg.lower())
#str.capitalize transforma apenas a primeira letra da string em maiúscula 
print(msg.capitalize())
#str.count conta as repetições da string passada como parâmetro dentro de str
print(msg.count("o"))
#in var verifica se a string passada está presente dentro de var, retornando true ou false
print("Hello" in msg)
