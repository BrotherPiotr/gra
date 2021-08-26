import random

narzedzia = ["kamien","papier","nozyczki"]






zwyciestwo_komp = True
punkty_komp = 0
while zwyciestwo_komp == True:
    wybor_komp = narzedzia[random.randint(0,2)]
    wybor_gracz = ""
    while wybor_gracz!= "kamien" and wybor_gracz != "papier" and  wybor_gracz != "nozyczki":    
        wybor_gracz = input("kamien, papier, nozyczki:")
    print(wybor_komp)
    if wybor_gracz == wybor_komp:
            print("remis")
            punkty_komp = punkty_komp +1
    elif wybor_gracz == "kamien" and wybor_komp == "papier" or wybor_gracz == "papier" and wybor_komp == "nozyczki" or wybor_gracz == "nozyczki" and wybor_komp == "kamien":
        print("Gracz W plecy") 
        punkty_komp = punkty_komp +1
        print("punkty komputera " + str(punkty_komp))
    else: 
        print("Gracz Do przodu") 
        zwyciestwo_komp = False 
        print("wygrales za "+str(punkty_komp +1)+" razem")   