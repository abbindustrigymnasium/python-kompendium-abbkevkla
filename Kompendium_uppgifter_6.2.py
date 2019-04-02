import requests

#6.1
# siffra = int(input("välj ett heltal annars blir jag arg :) "))
# url = "http://77.238.56.27/examples/numinfo/?integer="+str(siffra)
# r = requests.get(url) #vi sätter värdena vi får i en variabel
# response_dictionary = r.json() #vi använder .json för att göra om innehållet till ett läsbart format
# #print(response_dictionary)

# jämt = response_dictionary["even"]
# if jämt == False:
#     a = "inte"
# elif jämt == True:
#     a = ""
# primtal = response_dictionary["prime"]
# if primtal == False:
#     b = "inte"
# elif primtal == True:
#     b = ""
# faktorer = response_dictionary["factors"]
# faktorer2 = ','.join( str(a) for a in faktorer)

# print(str(siffra)+" är "+a+" ett jämt tal. Numret är "+b+" ett primtal. Numrets faktorer är "+faktorer2+".")

#6.2
# print("Stockholm eller Uppsala")
# stad = input("välj en av städerna: ")
# stad = stad.lower()
# url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/"+stad
# r = requests.get(url) #vi sätter värdena vi får i en variabel
# response_dictionary = r.json() #vi använder .json för att göra om innehållet till ett läsbart format
# print("Forecast For "+stad)
# print("*"*75)
# for forecast in response_dictionary["forecasts"]:
#     print(forecast["date"]+"    "+forecast["forecast"])
# print("*"*75)

#6.3
url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" 
r = requests.get(url) #vi sätter värdena vi får i en variabel
response_dictionary = r.json() #vi använder .json för att göra om innehållet till ett läsbart format
for artists in response_dictionary["artists"]: #går igenom alla artister och skriver ut dem
    print(artists["name"])
pick = input("Pick one of the above: ") #låter användaren välja en artist
for artists in response_dictionary["artists"]: #går igenom alla artister igen
    if artists["name"] == pick: #om en namn key stämmer överens med det vi matat in så hämtar vi artistens id
        url = url + artists["id"] #vi lägger till id till url
        t = requests.get(url) #ny request
        response2 = t.json()
        for facts in response2["artist"]: #vi går igenom faktan i API'n
            print(facts+": " + str(response2["artist"][facts])) #vi skriver ut faktans titel och dess innehåll
    else: 
        print("nah boi") #om man har valt något som inte finns skrivs ett medelande ut och loopen bryts
        break