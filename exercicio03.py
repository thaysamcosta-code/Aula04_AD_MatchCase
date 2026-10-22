num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
op = input("Escolha uma opção: + , - , x , /: ")

match op: 
    case "+": 
        soma = num1 + num2
        print(f"A soma de {num1} com {num2} é {soma}")
    case "-":
        subt = num1 - num2
        print(f"A subtração de {num1} com {num2} é {subt}")    
    case "x":
        multi = num1 * num2
        print(f"A multiplicação de {num1} com {num2} é {multi}")    
    case "/":
        divi = num1 / num2
        print(f"A divisão de {num1} com {num2} é {divi}")
    case _:    
        print("Opção inválida")