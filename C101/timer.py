#Importar el modulo timer
import time 

#define la funcion de conteo
def countdown_timer(seconds):
    while seconds > 0:
        mins = int(seconds / 60)
        secs = int(seconds % 60)
        
        timer = f'{mins}:{secs}'
        print(timer, end='\r')
        time.sleep(1)
        print(timer)
        seconds -= 1
    print("Se acabo el tiempo")

#tiempo del input en segundos
seconds = input("Ingresa el tiempo en segundos ")

#llamar a la funcion countdown_timer 
countdown_timer(int(seconds))
