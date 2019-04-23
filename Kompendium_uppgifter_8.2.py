import web #vi importerar två moduler som vi själva gjort, nämligen web.py och ui.py
import ui
import os #Används av ui.py för att rensa terminalen
import requests #låter oss anropa och få info från APIer

#8.1
# Distans = input("Ange distans: ") #Måste anges med siffra först och enhet sedan med ett mellanrum, t.ex 22 km eller 5 miles
# Distans.title()
# Distans = Distans.split() #delar upp distans så att vi kan kolla sträckan och enheten för sig

# def km_to_miles(distance):  #En funktion som gör om km till miles genom att dividera distansen med 1.609 
#     convert = int(distance)/1.609
#     print(distance,"km motsvarar",convert,"miles") #skriver ut resultatet
# def miles_to_km(distance):  #En funktion som funkar åt andra hållet, miles till km. Utöver det gör den samma som den innan
#     convert = int(distance)*1.609
#     print(distance,"miles motsvarar",convert,"km")

# if Distans[1] == "km": #Om användaren angav i km så kör vi passande funktion
#     km_to_miles(Distans[0])
# elif Distans[1] == "miles": #om användaren angav i miles så kör den passande funktion
#     miles_to_km(Distans[0])
# else:
#     print("Naej rackarns nu vart de knas hörru") #Om svaret är varken km eller miles så får man ett felmeddelande

#8.2
#se web.py

#8.3
#se ui.py

#8.4
shutdown = False #variabeln som stänger av/sätter på vår UI
url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
#så länge vi inte stänger ner programmet så kommer det att loopa runt i while-loopen,
#vilket låter oss hoppa fram och tillbaka mellan de olika sidorna
while shutdown == False: 
    ui.clear() #rensar terminalen ifall den inte redan är rensad
    ui.line() #en linje, ----
    ui.header("ARTIST DATABASE") #Rubrik
    ui.line()
    ui.echo("Welcome to the world of")
    ui.echo("Music!")
    ui.line()
    ui.echo("L | List artists")
    ui.echo("V | View artist profile")
    ui.echo("E | Exit application")
    ui.line()
    userinput = ui.prompt("Selection")
    

    if userinput == "L":
        ui.clear()
        ui.line()
        ui.header("ARTIST DATABASE")
        ui.line()

        artists = web.get(url) #gör en request för att hämta alla tillgängliga artister
        for i in artists["artists"]: #en for loop för att snabbt och enkelt kunna rada upp alla artister
            ui.echo(i["name"])

        ui.line(True) #Om line är True så skriver vi ut ****
        ui.echo("L | Back to startpage")
        ui.echo("V | View artist profile")
        ui.echo("E | Exit application")
        ui.line()
        userinput = ui.prompt("Selection")

    if userinput == "V":
        ui.clear()
        ui.line()
        ui.header("ARTIST DATABASE")
        ui.line()
        pick = ui.prompt("Artist Name")
        artists = web.get(url) #ny request
        for i in artists["artists"]: #går igenom alla artister igen
            if i["name"] == pick: #om en namn key stämmer överens med det vi matat in så hämtar vi artistens id
                url2 = url + i["id"] #vi lägger till id till url
                facts = web.get(url2) #gör en ny request
        ui.line(True)
        ui.header(facts["artist"]["name"]) #använder den nya infon
        ui.line(True)
        ui.echo("Members:      " + str(facts["artist"]["members"]))
        ui.echo("Genres:       " + str(facts["artist"]["genres"]))
        ui.echo("Years active: " + str(facts["artist"]["years_active"]))
        ui.line()
        ui.echo("L | List artists")
        ui.echo("V | Back to startpage")
        ui.echo("E | Exit application")
        ui.line()
        userinput = ui.prompt("Selection")

        
    if userinput == "E":
        ui.clear()
        shutdown = True #Får oss att hoppa ur loopen, vilket leder till att programmet avslutas
 