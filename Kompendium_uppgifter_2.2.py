#2.1
# citat="datatyper har inbyggda metoder"
# citat2=citat.title()
# print(citat2)

#2.2
# talet = float(input("skriv ett float-tal: ")) 
# print(talet)
# talet2 = int(talet) #gör om talet till int, vilken tvingar det att avrundas
# print(talet2)

#2.3
# print("hello boi")
# namn=input("Vad är ditt förnamn? ")
# efternam=input("Vad är ditt namn efter namnet? ")
# print("Ayy lamo du heter " + namn +" " + efternam+"!")

#2.4
# ålder = int(input("Hur många år du vara? "))
# kvartillmyndig = 18-ålder
# if kvartillmyndig <=0: #gör en if-sats för att se om personen redan är 18 eller över
#     print("du är redan myndig")
# else:
#     print("det är "+str(kvartillmyndig)+" år kvar till du är myndig!")

#2.5
Vanlig2=2*int(input("Hur många vill ha två vanliga korvar?"))
Vanlig3=3*int(input("Hur många vill ha tre vanliga korvar?"))
Vegan2=2*int(input("Hur många vill ha två veganska korvar?"))
Vegang3=3*int(input("Hur många vill ha tre veganska korvar?"))
Vanlig_korv= Vanlig2+Vanlig3
Vegan_korv= Vegan2+Vegang3
Antal_paket1= Vanlig_korv/8
Antal_paket2= Vegan_korv/4
Antal_elever=Vanlig2/2+Vanlig3/3+Vegan2/2+Vegang3/3
print(str(Antal_paket1) + " paket vanlig korv behöver köpas in")
print(str(Antal_paket2)+" paket vegansk korv behöver köpas in")
print(str(Antal_elever)+" stycken drickor behöver köpas in")
#Man skulle kunna avrunda men risken är att det gör att talet blir för litet om det avrundas neråt, därför skippade jag det