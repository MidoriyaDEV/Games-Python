import time
import sys
from random import randint

def animacao_jokenpo(intervalo=0.5):
    mensagens = [
        "JO",
        "KEN",
        "PO!!!"
    ]
    
    for mensagem in mensagens:
        sys.stdout.write(f'\r{mensagem}')  #Escreve na mesma linha
        sys.stdout.flush()  #Força a escrita no terminal
        time.sleep(intervalo)  #Pausa entre atualizações

#Inicializa a escolha do computador
Computador = randint(1, 3)
itens = ('PEDRA', 'PAPEL', 'TESOURA')

print('''SUAS OPÇÕES
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

#Pede a escolha do jogador
Jogador = int(input('Qual é a sua jogada? '))

#Executa a animação
sys.stdout.write('\r')  # Limpa a linha para iniciar a animação
animacao_jokenpo()

#Exibe os resultados após a animação
print('\rO computador escolheu {}'.format(itens[Computador-1]))
print('-=-'*10)
print('Jogador jogou {}'.format(itens[Jogador-1]))
print('-=-'*10)
if Computador == Jogador:
    print('EMPATE')
elif (Computador == 1 and Jogador == 3) or (Computador == 2 and Jogador == 1) or (Computador == 3 and Jogador == 2):
    print('COMPUTADOR VENCE')
else:
    print('JOGADOR VENCE')
