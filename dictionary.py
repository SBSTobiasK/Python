woerterbuch = {
"Haus": "house",
"Baum": "tree",
"Auto": "car",
"Katze": "cat",
"Hund": "dog",
"Mensch": "human",
"Tisch": "table",
"Stuhl": "chair",
"Buch": "book",
"Schule": "school"
}

user_vokabel = " "
while user_vokabel != "":
  user_vokabel = input("Bitte geben sie eine Vokabel ein: ")
  for key, value in zip(woerterbuch.keys(), woerterbuch.values()):
    if user_vokabel == key:
        print(user_vokabel, "bedeutet in Englisch:", woerterbuch[key])
    elif user_vokabel == value:
        print(user_vokabel, "bedeutet in Deutsch:", key)
