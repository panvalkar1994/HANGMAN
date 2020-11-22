import random

# The Hangman: Trailer
# trailer = """
# H A N G M A N
# The game will be available soon.
# """
# print(trailer)

# version 0.0 :fixed answer
# title = 'H A N G M A N'
# print(title)
# guess = str(input('Guess the word: '))
# answer = 'python'
# if guess.upper() == answer.upper():
#     print('You survived!')
# else:
#     print('You lost!')

# version 1.0 : random answer from list
# words=['python', 'java', 'kotlin', 'javascript']
# title = 'H A N G M A N'
# print(title)
# guess = str(input('Guess the word: '))
# answer = random.choice(words)
# if guess.upper() == answer.upper():
#     print('You survived!')
# else:
#     print('You lost!')

# version 2.0 : random answer from list with first three letters hint

# words=['python', 'java', 'kotlin', 'javascript']
# title = 'H A N G M A N'
# print(title)
# answer = random.choice(words)
# hint = ''
# for i in range(len(answer)):
#     if i<3:
#         hint += answer[i]
#     else:
#         hint += '-'
# print(f'Guess the word {hint}: ',end='')
# guess = str(input())
# if guess.upper() == answer.upper():
#     print('You survived!')
# else:
#     print('You lost!')


# version 3.0 : iterative letter guessing with 8 guesses.
# def main():
#     words = ['python', 'java', 'kotlin', 'javascript']
#     answer = random.choice(words)
#     display = '-' * 20
#     title = 'H A N G M A N'
#     print(title)
#     print()
#
#     max_tries = 8
#     tries = 0
#     while tries < max_tries:
#         print(display)
#         letter = str(input('Input a letter: '))
#         if letter in answer:
#             dis_chars = list(display)
#             dis_chars[answer.find(letter)] = letter
#             display = "".join(dis_chars)
#         else:
#             pass
#         print()
#         tries += 1
#
#     final_message = """
#     Thanks for playing!
#     We'll see how well you did in the next stage
#     """
#
#     print(final_message)


# version 4.0 : reduce lives with each wrong attempt


# def main():
#     words = ['python', 'java', 'kotlin', 'javascript']
#     answer = random.choice(words)
#     display = '-' * len(answer)
#     title = 'H A N G M A N'
#     print(title)
#     lives = 8
#     while lives > 0:
#         print()
#         print(display)
#         print('Input a letter:', end=' ')
#         letter = str(input())
#         if letter in answer:
#             if letter in display:
#                 print('No improvements')
#                 lives -= 1
#             else:
#                 dis_chars = list(display)
#                 for i in range(len(answer)):
#                     if letter == answer[i]:
#                         dis_chars[i] = letter
#                 display = "".join(dis_chars)
#         else:
#             print("That letter doesn't appear in the word")
#             lives -= 1
#
#     if display == answer:
#         # print()
#         print("You guessed the word!")
#         print("You survived!")
#     else:
#         # print()
#         print("You lost!")


# version 5.0 : improvements - repeated attempt will not reduce attempts, lower case letter input is mandatory


# def main():
#     words = ['python', 'java', 'kotlin', 'javascript']
#     answer = random.choice(words)
#     display = '-' * len(answer)
#     title = 'H A N G M A N'
#     print(title)
#     lives = 8
#     guess = []
#     while lives > 0:
#         print()
#         print(display)
#         print('Input a letter:', end=' ')
#         letter = str(input())
#         if len(letter) != 1:
#             print("You should input a single letter")
#             continue
#         elif not letter.islower():
#             print("Please enter a lowercase English letter")
#             continue
#         elif (letter in display) or (letter in guess):
#             print("You've already guessed this letter")
#             continue
#         elif letter in answer:
#             dis_chars = list(display)
#             for i in range(len(answer)):
#                 if letter == answer[i]:
#                     dis_chars[i] = letter
#             display = "".join(dis_chars)
#
#         else:
#             print("That letter doesn't appear in the word")
#             lives -= 1
#         guess.append(letter)
#
#     if display == answer:
#         # print()
#         print("You guessed the word!")
#         print("You survived!")
#     else:
#         # print()
#         print("You lost!")

# version 6.0 : improvements - menu added to choosing to play or quit


def main():
    words = ['python', 'java', 'kotlin', 'javascript']
    answer = random.choice(words)
    display = '-' * len(answer)
    title = 'H A N G M A N'
    print(title)
    # Menu
    while True:
        print('Type "play" to play the game, "exit" to quit: ', end='')
        action = str(input())
        if action == 'play':
            break
        elif action == 'exit':
            exit(0)
        else:
            continue
    lives = 8
    guess = []
    while lives > 0:
        print()
        print(display)
        print('Input a letter:', end=' ')
        letter = str(input())
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        elif not letter.islower():
            print("Please enter a lowercase English letter")
            continue
        elif (letter in display) or (letter in guess):
            print("You've already guessed this letter")
            continue
        elif letter in answer:
            dis_chars = list(display)
            for i in range(len(answer)):
                if letter == answer[i]:
                    dis_chars[i] = letter
            display = "".join(dis_chars)

        else:
            print("That letter doesn't appear in the word")
            lives -= 1
        guess.append(letter)

    if display == answer:
        # print()
        print("You guessed the word!")
        print("You survived!")
    else:
        # print()
        print("You lost!")


if __name__ == '__main__':
    main()
