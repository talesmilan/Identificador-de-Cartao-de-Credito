# Pedir ao usuário o número do cartão
numero = input("Qual o número do cartão? ")

# Número de digitos do cartão
digitos = len(numero)

# Variavel soma = a soma dos números necessários para o calculo do algoritimo de Luhn
soma = 0

# Variavel resultados = também é uma variavel que faz parte dos calculos
resultados = []

# Variavel que irá conter os digitos do cartão de crédito
digito = []

# Converte os números do cartão que estão em string para inteiros
m = 0
while m < digitos:
    digito.append(int(numero[m]))
    m += 1

# Multiplica por dois os digitos do cartão necessários para o calculo
i = 2
j = 0
while i <= digitos:
    resultados.append(digito[digitos - i] * 2)

    # Se o resultado da multiplicação for igual ou maior que 10, separa os números e depois faz a soma deles
    if resultados[j] >= 10:
        resultados[j] = (resultados[j] % 10) + int(((resultados[j] / 10) % 10))

    # Soma todos os resultados dos digitos multiplicado por 2
    soma += resultados[j]

    # Incrimenta números a variaveis do loop
    i += 2
    j += 1

# Adiciona a soma dos digitos que não foram multiplicados por 2, seguindo o calculo do algoritimo de Luhn
n = 1
while n <= digitos:
    soma += digito[digitos - n]
    n += 2

# Se o numero digitado for maior que 16 ou menor que 13 imprime invalido
if digitos > 16 or digitos < 13:
    print("INVALID")

# Verifica se o ultimo digito da soma do calculo do algoritimo de Luhn é diferente de 0 e se for imprime cartão invalido
elif soma %10 != 0:
    print("INVALID")

# Verefica se o cartão tem 15 digitos e se começa com 3
elif digitos == 15 and digito[0] == 3:

    # Verefica se o segundo digito é 4 ou 7 e se for imprime cartão Amex
    if digito[1] == 4 or digito[1] == 7:
        print("AMEX")
    else:
        print("INVALID")

# Verifica se o cartão tem 16 digitos
elif digitos == 16:

    # Verifica se o primeiro digito do cartão é 5
    if digito[0] == 5:

        # Verifica se o segundo digito do cartão é maior que 0 e menor que 6 e se for imprime Mastercard
        if digito[1] > 0 and digito[1] < 6:
            print("MASTERCARD")
        else:
            print("INVALID")

    # Verifica se o primeiro digito do cartão é igual a 4 e se for imprime Visa
    elif digito[0] == 4:
        print("VISA")
    else:
        print("INVALID")

# Verifica se o cartão tem 13 digitos e se o primeiro digito é 4 e se for imprime Visa
elif digitos == 13 and digito[0] == 4:
    print("VISA")
else:
    print("INVALID")
