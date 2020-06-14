# coding: utf-8
"""This file contains the functions used in the Pendu game"""

import pickle
import gamedata
import random
import os

def get_playername():
    os.system("clear")
    playername = input("*** Bienvenue ! Tu t'apprêtes à jouer au Pendu ! *** \n\nComment t'appelles-tu ? ")
    playername.capitalize()
    if not playername.isalnum():
        print("Ce nom est invalide.")
        get_playername()
    return playername

def choose_word():
    chosen_word = random.choice(gamedata.words_list)
    return chosen_word.upper()

def get_letter():
    input_letter = input("Donne-moi une lettre : ")
    input_letter = input_letter.upper()
    if not input_letter.isalpha() or len(input_letter) > 1:
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

def get_scores():
    if os.path.exists(gamedata.scores_filename):
        with open(gamedata.scores_filename, "rb") as score_file:
            my_deplicker = pickle.Unpickler(score_file)
            scores = my_deplicker.load()
    else:
        scores = {}
    return scores

def save_scores(scores):
    with open(gamedata.scores_filename, "wb") as score_file:
        my_pickler = pickle.Pickler(score_file)
        my_pickler.dump(scores)