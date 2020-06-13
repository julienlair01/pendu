# coding: utf-8

"""This file contains the functions used in the Pendu game"""

# manage user input
# check if letter matches
# display
# update and save score

import pickle
import donnees
import random

def get_playername():
    print("\nBienvenue ! Tu t\'apprêtes à jouer au Pendu !")
    playername = input("Comment t'appelles-tu ? ")
    playername.capitalize()
    if not playername.isalnum():
        print("Ce nom est invalide.")
        get_playername()
    return playername

def choose_word():
    chosen_word = random.choice(donnees.words_list)
    return chosen_word.upper()

def get_letter():
    input_letter = input("Donne-moi une lettre : ")
    input_letter = input_letter.upper()
    if not input_letter.isalpha():
        print("Merci d'entrer une lettre valide.")
        get_letter()
    return input_letter

def update_found_word(input_letter, guess_word, found_letters):
    found_word = ""
    for letter in guess_word:
        if letter in found_letters:
            found_word += letter
        else:
            found_word += "*"
    return found_word

def update_player_score(playername, score):
    
    return score  

def get_score(username):
    try:
    # Try to load scores data from file
        with open("scores",mode = "rb") as scores_file:
            my_depickler = pickle.Unpickler(scores_file)
            user_score = my_depickler.load()
    
    except FileNotFoundError:
        print("fichier non trouvé")
        return 0

    except EOFError:
        print("pas de données dans le fichier")
        return 0

#        try: 
 #       except:
   #         "Une erreur est survenue"

def save_score():
    # If the file does not exist, create it
    # except FileNotFoundError:
    #     print("fichier non trouvé")
    #     with open("scores",mode = "wb") as scores_file2:
    #         pass
    #     return -1
    pass