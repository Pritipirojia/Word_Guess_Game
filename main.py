import random
import pandas as pd

# Read the CSV file into a DataFrame
mov_data = pd.read_csv('Data/IMDB-Movie-Dataset(2023-1951).csv')

win = 0
end = 'False'

while end == 'False':

    random_num = random.randint(0, len(mov_data['id']) - 1)

    # Hints = ['YearOfRelease', 'Genre', 'Cast1', 'Cast2', 'Director', 'Overview']
    Hints = mov_data.loc[random_num]

    hints_taken = 0

    random_movie = mov_data.loc[random.randint(0, len(mov_data['id']) - 1), 'movie_name'].lower()

    print(random_movie)

    print(mov_data.loc[random_num, 'cast'])

    guessedWord = ['_'] * len(random_movie)

    for i in range(0, len(random_movie)):

        # Changing the ith character
        # to '_' if it's not a space.
        if random_movie[i] == ' ':
            guessedWord[i] = ' '

    attempts = 10

    while attempts > 0:
        print('\nCurrent word: ' + ' '.join(guessedWord))

        guess = input('Guess a letter: ').lower()

        if guess in random_movie:
            for i in range(len(random_movie)):
                if random_movie[i] == guess:
                    print (guessedWord[i])
                    guessedWord[i] = guess
            print('Great guess!')

        else:
            attempts -= 1
            print('Wrong guess! Attempts left: ' + str(attempts))
            if 7 > attempts > 0:
                hint_req = input ('Do you want a HINT (y/n)?')
                if hint_req == 'y':
                    print(Hints[hints_taken])
                    hints_taken += 1

        if '_' not in guessedWord:
            print('\nCongratulations!! You guessed the word: ' + random_movie)
            attempts = -1
            win += 1
            print('No. of games won:' + str(win))
            continue_game = input('Do you want to continue the game (y/n):')
            if continue_game == 'n':
                end = 'True'
            break

    while attempts > 0:

        print('\nCurrent word: ' + ' '.join(guessedWord))

        guess = input('Guess a letter: ').lower()

        if guess in random_movie:
            for i in range(len(random_movie)):
                if random_movie[i] == guess:
                    guessedWord[i] = guess
            print('Great guess!')
        else:
            attempts -= 1
            print('Wrong guess! Attempts left: ' + str(attempts))
            if 7 > attempts > 0:
                hint_req = input ('Do you want a HINT (y/n)?')
                if hint_req == 'y':
                    print(Hints[hints_taken])
                    hints_taken += hints_taken


        if '_' not in guessedWord:
            print('\nCongratulations!! You guessed the word: ' + random_movie)
            win += 1
            print('No. of games won:' + str(win))
            continue_game = input('Do you want to continue the game (y/n):')
            if continue_game == 'n':
                end = 'True'
            break

        else:
            print('\nYou\'ve run out of attempts! The word was: ' + random_movie)
            continue_game = input('Do you want to continue the game (y/n):')
            if continue_game == 'n':
                end = 'True'
