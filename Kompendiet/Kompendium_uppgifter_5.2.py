# #5.1
# Matches=[]
# Antalpers=0
# Kön=input("Ditt kön: ")
# Hår=input("Din hårfärg: ")
# ögon=input("Din ögonfärg: ")

# Daniel_Radcliffe =["man", "brun", "brun", "Daniel Radcliffe"] 
# Rupert_Grint =["man", "röd", "blå", "Rupert Grint"] 
# Emma_Watson =["kvinna", "brun", "brun", "Emma Watson"] 
# Selena_Gomez =["kvinna", "brun", "brun", "Selena Gomez"]
# Jeff_Loomis =["man", "blond", "blå", "Jeff Loomis"]
# Elmo =["man", "röd", "blå", "Elmo"] 
# Kändisar = [Daniel_Radcliffe, Rupert_Grint, Emma_Watson, Selena_Gomez, Jeff_Loomis, Elmo]
# Kändisar2 = " "


# for pers in Kändisar:
#     if Kön == pers[0]:
#         if Hår == pers[1]:
#             if ögon == pers[2]:
#                 Kändisar2 = Kändisar2+ pers[3] + ", "
                
# if Kändisar2 == " ":    
#     print("Du är unik")
# else:
#     print("Egenskaperna matchar med:"+Kändisar2)

# #5.2
# namn = input("Ange ditt namn: ")
# ålder = int(input("Ange din ålder: "))
# sömnbehov = [14,13,12,11.5,11,11,10.5,10,10,10,9.5,9,9,9,9,8.5]
# if ålder<17:
#     sovtimmar = sömnbehov[ålder-1]
# else:
#     sovtimmar = 8
# print("Hej "+namn+", enligt några smarta personer borde folk i din ålder ("+str(ålder)+" år) sova minst "+str(sovtimmar)+" timmar per natt.")

#5.3
land = input("Välj ett land: ")
land = land.capitalize()
Norden=["Danmark", "Finland", "Island", "Norge", "Sverige"]
GB=["England", "Nordirland", "Skottland", "Wales"]
if land in Norden:
    print("ditt land ligger i norden")
elif land in GB:
    print("ditt land ligger i Storbritanien")
else:
    print("rackarns, ditt land finns inte")