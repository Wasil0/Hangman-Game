print('Welcome to the HANGMAN!!!')
#initialization
import random
#~slection of word
words = open('words.txt').read()
available_words = words.split()
selected_word = random.choice(available_words)

user_id = 'admin'
password = '12345'

def loop(x): #for printing of list
    for i in range(len(x)):
        print(x[i],end='')

def start(): #first interface
    while True:
        user_type = int(input('How do you want to continue?\nEnter 1 to continue as administritor\nEnter 2 to continue as player\n'))
        if user_type == 1 or user_type == 2:
            break
        else:
            print('Invalid input')
    if user_type == 1:
        while True:
            admin_id = input('user id:\n')
            id_password = input('password:\n')
            if admin_id == user_id and password == id_password:
                admin_interface()
                break
            else:
                print('wrong user id or password\naccess denied')
                start()
    if user_type == 2:
        start_hangman()



def admin_interface():
    def option1():
        print('Type the word you want to add: ')
        word_to_add = input()
        f = open('words.txt', 'a+')
        f.write(word_to_add + ' ')
        f.close()
    def option2():
        print('The scores have been reseted.')
        f = open('scores.txt','w')
        f.close()
    while True:
        print('Enter 1 to add a word\nEnter 2 to reset scores\nEnter 3 to exit\n')
        options = int(input())
        if options in [1,2,3]:
            break
        else:
            print('Invalid input')
    if options == 1:
        option1()
        admin_interface()
    if options == 2:
        option2()
        admin_interface()
    if options == 3:
        start()



def start_hangman():
    player_name = input('Enter your name:\n')
    warnings_ = 3
    guesses = 6
    word = ['_ ' for _ in selected_word]
    word_ = list(selected_word)
    alphs = list('abcdefghijklmnopqrstuvwxyz')
    vowels = 'aeiou'
    consonents = 'bcdfghjklmnpqrstvwxyz'
    guessed_letters = []
    #code for game round
    print(f'Your word is {len(selected_word)} letters long.')
    while True:
        print(f'You now have {warnings_} warnings and {guesses} guesses.')
        print('Available letters are ', end='')
        for i in range(len(alphs)):
            print(alphs[i], end='')
        print()
        x = input('Guess a letter: ')
        letter = x.lower()
        if letter in guessed_letters:
            warnings_-=1
            print('Sorry! You have already guessed this letter.')
            loop(word)
            print()
            print('--------------------------')
        elif letter in selected_word:
            for i,j in enumerate(selected_word):
                if j == letter:
                    word[i] = j
            guessed_letters.append(letter)
            alphs.remove(letter)
            print('Good Guess')
            loop(word)
            print()
            print('--------------------------')
        elif letter not in selected_word:
            if letter in vowels:
                guesses-=2
                print('Sorry! Wrong guess.')
                loop(word)
                print()
                print('--------------------------')
            elif letter in consonents:
                guesses-=1
                print('Sorry! Wrong guess.')
                loop(word)
                print()
                print('--------------------------')
            else:
                warnings_-=1
                print('Invalid Input')
                loop(word)
                print()
                print('--------------------------')
        if warnings_<0:
            guesses-=1
            warnings_ = 0
        if word==word_:
            score = guesses*len(guessed_letters)
            print('Congratulations! You won the game.')
            print(f'Your total score is {score}')
            f = open('scores.txt', 'a+')
            f.seek(0)
            s = f.read()
            player_scores = s.split()

            previous_score = 'xxxx=00'
            for player_score in player_scores:

                if player_name == player_score[:-3]:
                    if int(player_score[-2:]) >= score:
                        print(f'Your previous score was {player_score[-2:]}')
                        previous_score = player_score
                    else:
                        print(f'Great! You have set a high score for your self which is {score}.')
                        previous_score = player_score
            print(previous_score)
            if player_name not in s:
                f.write(player_name + '=' + str(score) + ' ')
                f.close()
            if player_name in s:
                if int(previous_score[-2:]) < score:
                    player_scores.append(previous_score[:-2] + str(score))
                    player_scores.remove(previous_score)
                    f1 = open('scores.txt', 'w')
                    for e in player_scores:
                        f.write(e + ' ')
                    f1.close()
            break
        elif guesses==0:
            print('Ooops! You ran out of guesses.')
            print(f'The word was {selected_word}')
            break

start()