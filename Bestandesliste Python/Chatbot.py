print("Bitte wähle deine bevorzugte Sprache, um fortzufahren / Please choose your preferred language to proceed / S'il vous-plait, choisissez vorte langue favorisée pour procéder.")

#Benutzersprache#
user_language = "FR"

#Begrüssungstexte#
begrüssung_Deutsch = "Herzlich Willkommen bei JAROWA, wie können wir Dir helfen?"
begrüssung_Englisch = "Welcome to JAROWA, how can we help you?"
begrüssung_Französich = "Bienvenue à JAROWA, comment pouvons-nous être utiles ?"

if user_language == "DE":
    print(begrüssung_Deutsch)
elif user_language == "FR":
    print("Pardon, actuellement notre Chatbot parle seulement allemand. Veuillez nous contacter par 0848 824 812")
elif user_language == "EN":
    print("Excuse us, the chatbot only is available in German. Please call 0848 824 812 to get help.")


#Chatbot#
print("Worüber würden Sie heute gerne Sprechen?")
print("Zum Beenden der Chatfunktion einfach bye eintippen")
print("")

nutzereingabe = ""
nutzereingabe = input("Ihre Frage / Antwort: ")
print(nutzereingabe)

while nutzereingabe != "bye":
    nutzereingabe = ""
    nutzereingabe = input("Frage / Antwort: ")
    print(nutzereingabe)
print("Einen schönen Tag noch!")

import random
zufallsantworten = ["Oh wirklich?", "Was sie nicht sagen", "Das ist aber gar nicht gut!"]
print("Willkommen beim Chatbot")






