idade = int(input("Digite sua idade: "))
esporte = int(input("Escolha seu esporte: 1 - Natação / 2 - Corrida / 3 - Ciclismo: "))

match esporte: 
    case 1: 
        if idade < 10: 
            print("Categoria Mirim")
        elif idade <= 14: 
            print("Categoria Infantil")
        else:
            print("Categoria Juvenil") 
    case 2:
        if idade < 16: 
            print("Categoria Junior")
        else:
            print("Categoria Adulto")            
    case 3: 
        if idade >= 18:
            print("Categoria profissional")
        else: 
            print("Categoria Amador") 
    case _:
        print("Opção inválida")                                       