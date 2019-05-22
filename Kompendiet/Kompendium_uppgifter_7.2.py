from random import randint 

#7.1
# siffra = int(input("välj en siffra: "))
# multiplikator = 1
# räknare = 0
# while räknare < 4:
#     if räknare == 3:
#         svar = input("Fortsätt? ")
#         if svar != "ja":
#             break
#         else: 
#             räknare = 0
#             continue
#     print(siffra*multiplikator)
#     multiplikator+=1
#     räknare+=1

#7.2
talet = randint(0, 99) #slumpar vårat magiska tal
gissning = int(input("gissa ett tal mellan 0-99: ")) #låter användaren välja en int
antalg = 0 #antalet gissningar 
while gissning != talet: #så länge gissningen inte är korrekt
    if gissning < talet: #om gissningen är för låg
        antalg =antalg+1
        gissning =int(input("Too low, try again. New guess: ")) #ny gissning
        
    if gissning > talet: #om gissningen är för hög
        antalg = antalg+1
        gissning  = int(input("Too high, try again. New guess: "))
    
print("grattis, det tog dig endast "+str(antalg)+" försök!") 
#när man gissat rätt kommer man ut ur while loopen och detta medelande skrivs ut