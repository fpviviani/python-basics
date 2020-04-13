from datetime import datetime, timedelta

today = datetime.now()
print("Data de hoje:" + str(today))

# timedelta é usado para definir um período de tempo
two_days = timedelta(days = 2)
one_day = timedelta(days = 1)
print("Antes-de-ontem foi: " + str(today - two_days))
print("Amanhã será: " + str(today + one_day))

birth = input("Digite sua data de nascimento (dd/mm/yyyy): " )
# strptime transforma string em datetime na formatação desejada
birthdate = datetime.strptime(birth, '%d/%m/%Y')
print("Sua data de nascimento é: " + str(birthdate))
# strftime transforma datetime em string na formatação desejada
birthdate_day = birthdate.strftime("%A")
print("Seu nascimento caiu em uma: " + birthdate_day)