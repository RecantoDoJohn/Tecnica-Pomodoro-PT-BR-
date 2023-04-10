from time import sleep
import winsound

continua = True
pontos = 0


print('{:=^30}'.format(' Metodo pomodoro '))
sleep(2) 
task = input("oq tu vai fazer fi? ")

while continua == True:

    print('começando (25min)...')
    sleep(1500)
    pontos += 1
    print(f'marca numero {pontos}')
    winsound.PlaySound('alarm-clock-01.wav', winsound.SND_FILENAME)

    if pontos == 4:
        print('pausa longa (30min)...')
        pontos = 0
        sleep(1800)
    else:
        print('pausa curta (5min)...')
        sleep(300)
    vontade = input('quer continuar? ')
    if vontade in 'Ssim':
        continua = True
    else: 
        continua = False
print('adeus...')
