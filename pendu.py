# coding: utf-8
"""This file contains the main loop of the Pendu game"""

import fonctions
import gamedata
import os

playername = ""

def main():  
    all_scores = fonctions.get_scores() # Retrieve all_scores from saved file
    playername = fonctions.get_playername() # Ask player for her name

    # Main loop: as long as the player wants to keep playing, the game will suggest a new word
    continue_game = True
    while continue_game:
        guess_word = fonctions.choose_word()
        rounds_left = gamedata.rounds # Get number of rounds from gamedata
        found_word = []
        found_letters = []
        print("\nOk {}. Tu as déjà {} points !".format(playername, all_scores.get(playername, 0)))
        print("\nLe nouveau mot à trouver contient {} lettres".format(len(guess_word)))
        
        # As long as player did not find the entire word and still has chances, ask for a letter
        while found_word != guess_word and rounds_left > 0:
            print("\nIl te reste {} chances.".format(rounds_left))
            input_letter = fonctions.get_letter() 
            
            if input_letter in found_letters:
                print("Tu as déjà proposé cette lettre")
            else:
                found_letters.append(input_letter) # Add the letter to the list of the already found letters
                found_word = fonctions.update_found_word(input_letter, guess_word, found_letters) # Build the found word with the found letters
            
            print("Ton mot : {}".format(found_word))
            rounds_left -= 1

        # If the player has found the right word, update score
        if found_word == guess_word:

            if all_scores.get(playername, False): # If player is in the save file, update the score with additional points
                all_scores[playername] += rounds_left
            else:
                all_scores = {playername: rounds_left} # If player is not in the save file, create the item in dict
            
            fonctions.save_scores(all_scores)
            print("\nFélicitations, tu as trouvé le mot !!! \nTu marques {} points.".format(rounds_left)) 
            print("Nouveau score = ", all_scores[playername])

        elif rounds_left == 0: # If the player has no more chances
            print("PENDU ! Le mot était : {}".format(guess_word))

        # Ask player for a new game
        if input("Nouvelle partie (O/N) ? ").upper() == "N":
            continue_game = False
        
        os.system("clear")

if __name__ == "__main__":
    main()