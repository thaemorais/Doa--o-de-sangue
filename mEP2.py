peso = float(input())
idade = int(input())
if idade >= 16 and idade < 18:
    dda = (input())
bs = (input())
uddi = (input())
pd = (input())
if pd == "N":
    mdud = int(input())
    dnu12m = int(input())
sb = (input())
if sb == "F":
    g = (input())
    a = (input())
    if a == "S":
        mb = int(input())
#DADOS
print(f"Peso: {peso}")
print(f"Idade: {idade}")
if idade >= 16 and idade < 18:
    print(f"Documento de autorizacao: {dda}")
print(f"Boa saude: {bs}")
print(f"Uso de drogas injetaveis: {uddi}")
print(f"Primeira doacao: {pd}")
if pd == "N":
    print(f"Meses desde ultima doacao: {mdud}")
    print(f"Doacoes nos ultimos 12 meses: {dnu12m}")
print(f"Sexo biologico: {sb}")
if sb == "F":
    print(f"Gravidez: {g}")
    print(f"Amamentando: {a}")
    if a == "S":
        print(f"Meses bebe: {mb}")
# RESTRIÇOES
#PESO
if peso < 50.0:
    print("Impedimento: abaixo do peso minimo.")
#IDADE
if idade < 16:
    print("Impedimento: menor de 16 anos.")
if idade >= 16 and idade < 18:    
    if dda == "N":
        print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
if idade > 60 and pd == "S":
    print("Impedimento: maior de 60 anos, primeira doacao.")
if idade > 69:
    print("Impedimento: maior de 69 anos.")
#BOA SAUDE
if bs == "N":
    print("Impedimento: nao esta em boa saude.")
#USO DE DROGAS INJETAVEIS
if uddi == "S":
    print("Impedimento: uso de drogas injetaveis.")
#INTERVALO ENTRE DOACOES
if sb == "M" and pd == "N" and mdud < 2:
    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
if sb == "F" and pd == "N" and mdud < 3:
    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
#DOACOES ANUAIS
if sb == "M" and pd == "N" and dnu12m >= 4:
    print("Impedimento: numero maximo de doacoes anuais foi atingido.")
if sb == "F" and pd == "N" and dnu12m >= 3:
    print("Impedimento: numero maximo de doacoes anuais foi atingido.")
#GRAVIDEZ
if sb == "F" and g == "S":
    print("Impedimento: gravidez.")
#AMAMENTACAO
if sb == "F" and a == "S" and mb < 12:
    print("Impedimento: amamentacao.")
#NENHUM IMPEDIMENTO
if peso >= 50 and bs == "S" and uddi == "N":
    if idade < 18 and dda == "S":
        if sb == "M" and (pd == "S" or (pd == "N" and mdud > 2 and dnu12m < 4)):
            print("Procure um hemocentro.")
        elif sb == "F" and (pd == "S" or (pd == "N" and mdud > 3 and dnu12m < 3)) and g == "N" and (a == "N" or (a == "S" and mb >= 12)):
            print("Procure um hemocentro.")
    elif idade > 60 and idade <= 69 and pd == "N":
        if sb == "M" and mdud > 2 and dnu12m < 4:
            print("Procure um hemocentro.")
        elif sb == "F" and mdud > 3 and dnu12m < 3 and g == "N" and (a == "N" or (a == "S" and mb >= 12)):
            print("Procure um hemocentro.")
    elif idade >= 18 and idade <= 60:
        if sb == "M" and (pd == "S" or (pd == "N" and mdud > 2 and dnu12m < 4)):
            print("Procure um hemocentro.")
        elif sb == "F" and (pd == "S" or (pd == "N" and mdud > 3 and dnu12m < 3)) and g == "N" and (a == "N" or (a == "S" and mb >= 12)):
            print("Procure um hemocentro.")