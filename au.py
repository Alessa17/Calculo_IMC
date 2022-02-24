def bemvindo():
    print(''' Seja bem vindo(a) ao calculo de IMC!
    ''')

    print("Digite a altura como no exemplo a seguir: 1.63")
    print("Digite o peso como no exemplo a seguir: 70.2")
    print(                                           
    )
    altura= float(input('Digite a sua altura: '))
    peso= float(input('Digite o seu  peso: '))

    imc= peso/(altura*altura)
    print("O seu IMC é: %.2f" %imc)

    if imc <= 16:
	    print("Magreza extrema")
        
    elif imc <= 18.5 and imc <= 24.9:
        print("Resultado: Abaixo do peso") 

    elif imc <= 24.99: 
        print("Resultado: Peso ideal")

    elif imc <= 29.99:    
        print("Resultado: Acima do peso")
    
    elif imc <= 34.99:
        print("Resultado: Obesidade Grau I")

    elif imc <= 39.9:
        print("Resultado: Obesidade Grau II - Severa")

    elif imc >= 40:
        print("Obesidade Grau III - Mórbida")
        
bemvindo()


