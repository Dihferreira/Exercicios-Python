vel = float(input('Qual velocidade atual do seu carro? '))
if vel > 80:
    print('Multado! vc excedeu a velocidade permitida de 80km/h')
    multa = (vel-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:print('Tenha um bom dia, Dirija com segurança!')



