import time
from alarme import alarme, pause

def afficher_heure():
    debut_h = int(input("Heure de départ (00-23) : "))
    debut_m = int(input("Minute de départ (00-59) : "))
    debut_s = int(input("Seconde de départ (00-59) : "))

    choix_format = input("Choisissez le format de l'heure (12 ou 24) : ")

    if 0 <= debut_h < 24 and 0 <= debut_m < 60 and 0 <= debut_s < 60:
        while True:
            for h in range(debut_h, 24):
                for m in range(debut_m, 60):
                    for s in range(debut_s, 60):
                        time.sleep(1)

                        if s == 59:
                            if m == 59:
                                if h == 23:
                                    debut_h = 0
                                else:
                                    debut_h += 1
                                debut_m = 0
                            else:
                                debut_m += 1
                            debut_s = 0
                        else:
                            debut_s += 1

                        if choix_format == "12":
                            heure_format = h % 12
                            
                            if heure_format == 0:
                                heure_format = 12
                            am_pm = "AM" if h < 12 else "PM"
                            horloge_tuple = (heure_format, m, s, am_pm)
                        
                        elif choix_format == "24":
                            heure_format = h
                            am_pm = ""
                            horloge_tuple = (h, m, s, am_pm)
                        
                        else:
                            print("Format d'heure non valide. Veuillez choisir 12 ou 24.")
                            return None

                        defilement_liste = [heure_format, m, s]
                        print(str(defilement_liste[0]).zfill(2), ":", str(defilement_liste[1]).zfill(2), ":", str(defilement_liste[2]).zfill(2), am_pm, end="\r")
                        
                        if am_pm == "PM":
                            continue
                        alarme(defilement_liste)     
                        pause(defilement_liste)

            
                    
afficher_heure()


