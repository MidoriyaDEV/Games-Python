    from time import sleep
    from random import randint
    computador = randint(0, 9) #faz o computador pensar
    print('-=-'*20)
    print('   \033[35mVou pensar em um número entre 0 e 9. Tente adivinhar...\033[m       ')
    print('-=-'*20)
    jogador = int(input(' Em qual número eu pensei?')) # Jogador tenta adivinhar
    print('\033[35mPROCESSANDO...\033[m')
    sleep(4)
    if jogador == computador:
        print('PARÁBENSM VOCÊ ACERTOU!!!')
    else:
        print('EBA eu ganhei! eu pensei no número {}, e não no {}, boa sorte na proxima vez...'.format(computador, jogador))

    #Escreva um programa que faça o computador “pensar” em um número
    #inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
    # foi o número escolhido pelo computador. O programa deverá escrever
    # na tela se o usuário venceu ou perdeu.