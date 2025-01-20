import tkinter as tk
from tkinter import messagebox


dictionaries = {
    "French": {
        "thank you": "merci",
        "please": "s'il vous plaît",
        "yes": "oui",
        "no": "non",
        "water": "eau",
        "food": "nourriture",
        "house": "maison",
        "book": "livre",
        "man": "homme",
        "woman": "femme",
        "chair": "chaise",
        "bag": "sac",
        "walk": "marcher",
        "sit": "asseoir",
        "leg": "jambe",
        "shoe": "chaussure",
        "talk": "parler",
        "sleep": "dormir",
        "right": "droite",
        "left": "gauche",
        "boy": "garçon",
        "pencil": "crayon",
    },

    "Igala": {
        "thank you": "anẹ",
        "please": "ẹ biko",
        "yes": "ẹẹ",
        "no": "ọda",
        "water": "ama",
        "food": "nra",
        "house": "ụla",
        "book": "akwụkwọ",
        "man": "ọmẹ",
        "woman": "ọb’iyọ",
        "Head": "Oji",
        "Hand": "Ówó",
        "Forehead": "Ógba Oji",
        "Blood": "Ebié",
        "Breath": "Imi",
        "four": "Őnáńá",
        "bench": "Èkpé",
    },
}

def search_word():
    selected_dictionary = dictionary_var.get()
    word = entry.get().strip().lower()  # Get user input, trim spaces, and convert to lowercase
    meaning = dictionaries.get(selected_dictionary, {}).get(word)

    if meaning:
        result_label.config(text=f"Meaning: {meaning}")
    else:
        result_label.config(text="")
        messagebox.showinfo(
            "Not Found",
            f"The word '{word}' is not in the {selected_dictionary} dictionary.",
        )


root = tk.Tk()
root.title("Multi-Language Dictionary")
welcome_label = tk.Label(root, text="Welcome to our Dictionary", padx=200, pady=100, bg='blue', fg="white", font='Arial 16')
welcome_label.pack()
root.geometry("600x600")


title_label = tk.Label(root, text="Please select a Language")
title_label.pack(pady=10)


dictionary_var = tk.StringVar(value="French")
dictionary_menu = tk.OptionMenu(root, dictionary_var, *dictionaries.keys())
dictionary_menu.pack()


word_label = tk.Label(root, text="Enter a word:")
word_label.pack()

entry = tk.Entry(root)
entry.pack()


search_button = tk.Button(root, text="Search", command=search_word, pady=10, padx=10)
search_button.pack(pady=10)


result_label = tk.Label(root, text="Meaning will appear here.")
result_label.pack(pady=20)


root.mainloop()
