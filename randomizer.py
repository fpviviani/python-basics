import random

base = input("Digite o piso do randomizador:")
roof = input("Digite o teto do randomizador:")
print(random.randrange(int(base), int(roof)))