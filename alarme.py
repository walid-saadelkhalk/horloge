import time

def alarme(horloge: list):
    tuple_alarm = (8, 30, 0)
    sonnerie = list(tuple_alarm)
    if sonnerie == horloge:
        print("Réveillez-vous, le temps file plus vite qu'on ne le croit!")  

   



def pause(horloge: list):
    tuple_pause = (10, 0, 0)
    pause = list(tuple_pause)
    if pause == horloge:
        print("Il est temps d'arreter le temps!")
        time.sleep(10)