# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 01:50:21 2024

@author: freakadelick
"""

import random
import sys

def main():
    '''Предполагается, что программа генерирует случайные сочетания смешных 
    имен'''
    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill",
             "Bob", 'Bowel Noises', 'Boxelder', "Bud",
             'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield'
             )
    middle = ("'Stink-Bug'", "'Beenie-Weenie'", "'Crab-Head'", "'Hunter'",
              "'Good-Goose'", "'Laptop-Head'", "'Day-Sorrow'",
              "'Kick-Ass'", "'Crying-Boy'", "'Milky-Nail'", "'Monkey-Day'", 
              "'Node-Raper'", "'No-Mad'"
              )
    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 
            'Goodensmith'
            )
    
    while True:
        weights = [1, 59, 67, 100, 100, 34, 48, 98, 93, 27, 60, 11, 28]

        first_name = random.choices(first, weights=weights, k=12)
        middle_name = random.choices(middle, weights=weights, k=12)
        last_name = random.choices(last, weights=weights, k=12)
        united_list = list(zip(first_name, middle_name, last_name))
        random_choice = random.choice(united_list)
        f, m , l = random_choice
        simple_words = [f, m, l]
        ' '.join(map(str, simple_words))
        print("\n\n")
        print(' '.join(str(elem) for elem in simple_words), file=sys.stderr)
        print("\n\n")
        try_again = input('Press "Enter" if you want to play more,'
                          ' or "n" to quit')
        if try_again.lower() == "n":
            break
    print('"Enter" to quit')

    
if __name__ == "__main__":
    main()