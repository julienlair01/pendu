# coding: utf-8

import fonctions
import donnees

def main():
    all_scores = fonctions.get_scores()
    playername = fonctions.get_playername()

    continue_game = True
    while continue_game:
        # guess_word = fonctions.choose_word()
        guess_word = "TOTO"
        rounds_left = donnees.rounds
        found_word = []
        found_letters = []

        print("\nOk {}. Tu as déjà {} points !".format(playername, all_scores.get(playername, 0)))
        print("\nLe nouveau mot à trouver contient {} lettres".format(len(guess_word)))

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
            if all_scores.get(playername, False):     
                all_scores[playername] += rounds_left
            else:
                all_scores = {playername: rounds_left}

            fonctions.save_scores(all_scores)
            print("\nFélicitations, tu as trouvé le mot !!! \nTu marques {} points.".format(rounds_left)) 
            print("Nouveau score = ", all_scores[playername])
        elif rounds_left == 0:
            print("PENDU ! Le mot était : {}".format(guess_word))

        if input("Nouvelle partie (O/N) ? ").upper() == "N":
            continue_game = False
        

if __name__ == "__main__":
    main()