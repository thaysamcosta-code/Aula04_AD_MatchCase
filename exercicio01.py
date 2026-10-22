print("Resultado 2026 - Alunos")
nome = input("nome completo do aluno: ").title()
nota01 = float(input("nota prova 1: ").replace(",","."))
nota02 = float(input("nota prova 2: ").replace(",","."))
nota03 = float(input("nota prova 3: ").replace(",","."))
soma = nota01 + nota02 + nota03
resultado = soma/3
print("\n")
if(resultado >= 7):
    situacao = "aprovado"
elif(resultado >= 5):
    situacao = "recuperação"
else:
    situacao = "reprovado"  

"""
    if(resultado >= 7):
    print(f"{resultado} aprovado")
elif(resultado >= 5):
    print(f"{resultado} Recuperação") 
else:
    print(f"{resultado} Reprovado")  
"""

print(f"Nome do Aluno: {nome}")
print(f"Prova 01: {nota01:.2f}".replace(".",","))
print(f"Prova 02: {nota02:.2f}".replace(".",","))
print(f"Prova 03: {nota03:.2f}".replace(".",","))
print(f"Média 2026: {resultado:.2f}".replace(".",","))
print(f"Resultado Final: {situacao.upper()}")

