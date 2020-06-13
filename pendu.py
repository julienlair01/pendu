# coding: utf-8

import fonctions
import donnees

def main():
    guess_word = fonctions.choose_word()
    rounds_left = donnees.rounds

    print("Le mot à trouver contient {} lettres".format(len(guess_word)))

    found_word = []
    found_letters = []

    # As long as the player still has chances and the found word does not match the word to guess

    while found_word != guess_word and rounds_left > 0:
        print("\nIl te reste {} chances.".format(rounds_left))

        input_letter = fonctions.get_letter() 
        if input_letter in found_letters:
            print("Tu as déjà trouvé la lettre", input_letter)
        else:
            # Add the letter to the list of the already found letters
            found_letters.append(input_letter)

            # Build the found word with the found letters
            found_word = fonctions.update_found_word(input_letter, guess_word, found_letters)
      
        print("Ton mot : {}".format(found_word))
        rounds_left -= 1

    # If the player has found the right word, congratulates her!
    
    if found_word == guess_word:
        player_total_score = fonctions.update_player_score("Julien", rounds_left)
        print("\nFélicitations, tu as trouvé le mot !!! \n\
                Tu marques {} points.\n\
                Tu as maintenant {} points.".format(rounds_left, player_total_score))

    elif rounds_left == 0:
        print("PENDU ! Le mot était : {}".format(guess_word))

        


    # playername = fonctions.get_name()
    # user_score = fonctions.get_score(playername)
    # print("Tu as", user_score, "points.")
    # current_points = 0
    # fonctions.save_score(user_score + current_points)

if __name__ == "__main__":
    main()