import webbrowser

url = "https://github.com/RajParsaniya"
box = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def main():
    print('\n\n-----------------------------------------------------------------------')
    print('| Options                 | Use                                       |')
    print('-----------------------------------------------------------------------')
    print('| (1) Start New Game      | To start a new game.                      |')
    print('| (2) About Developer     | To see information about the developer    |')
    print('| (3) Game Rule           | To Know rules of the game.                |')
    print('| (4) Exit                | To Quit/Exit the game.                    |')
    print('-----------------------------------------------------------------------\n')

    entered_choice = input('Enter your choice : ')

    if entered_choice == '1':
        player = 1
        status = -1

        while status == -1:
            board()

            if player % 2 == 1:
                player = 1
            else:
                player = 2

            print('\n-> Player', player)
            choice = int(input('-> Enter a number : '))

            if player == 1:
                mark = 'X'
            else:
                mark = 'O'

            if choice == 1 and box[1] == 1:
                box[1] = mark
            elif choice == 2 and box[2] == 2:
                box[2] = mark
            elif choice == 3 and box[3] == 3:
                box[3] = mark
            elif choice == 4 and box[4] == 4:
                box[4] = mark
            elif choice == 5 and box[5] == 5:
                box[5] = mark
            elif choice == 6 and box[6] == 6:
                box[6] = mark
            elif choice == 7 and box[7] == 7:
                box[7] = mark
            elif choice == 8 and box[8] == 8:
                box[8] = mark
            elif choice == 9 and box[9] == 9:
                box[9] = mark
            elif choice == 0:
                exit()
            else:
                print('\n\n Only 0 to 9 Digits Are Allowed !!!')
                player -= 1

            status = game_status()
            player += 1

        print('\n\n-------------------------')
        print('|      GAME RESULT      |')
        print('-------------------------\n')

        if status == 1:
            print('-> Player', player - 1, 'Win\n')
            result()
        else:
            print('-> Game Is Draw\n')

    elif entered_choice == '2':
        about()

    elif entered_choice == '3':
        rule()

    elif entered_choice == '4':
        quit_game()

    else:
        main()


def game_status():
    if box[1] == box[2] and box[2] == box[3]:
        return 1
    elif box[4] == box[5] and box[5] == box[6]:
        return 1
    elif box[7] == box[8] and box[8] == box[9]:
        return 1
    elif box[1] == box[4] and box[4] == box[7]:
        return 1
    elif box[2] == box[5] and box[5] == box[8]:
        return 1
    elif box[3] == box[6] and box[6] == box[9]:
        return 1
    elif box[1] == box[5] and box[5] == box[9]:
        return 1
    elif box[3] == box[5] and box[5] == box[7]:
        return 1
    elif box[1] != 1 and box[2] != 2 and box[3] != 3 and box[4] != 4 and box[5] != 5 and box[6] != 6 and box[7] != 7 and \
            box[8] != 8 and box[9] != 9:
        return 0
    else:
        return -1


def board():
    print('\n\n--------------------------------')
    print('|      Tic Tac Toe - Game      |')
    print('--------------------------------\n\n')
    print('-> Player 1 symbol is X ')
    print('-> Player 2 symbol is O ')
    print('-> Press 0 to exit')
    print()

    print('     |     |     ')
    print(' ', box[1], ' | ', box[2], ' |  ', box[3])

    print('_____|_____|_____')
    print('     |     |     ')

    print(' ', box[4], ' | ', box[5], ' |  ', box[6])

    print('_____|_____|_____')
    print('     |     |     ')

    print(' ', box[7], ' | ', box[8], ' |  ', box[9])

    print('     |     |     ')


def result():
    print('     |     |     ')
    print(' ', box[1], ' | ', box[2], ' |  ', box[3])

    print('_____|_____|_____')
    print('     |     |     ')

    print(' ', box[4], ' | ', box[5], ' |  ', box[6])

    print('_____|_____|_____')
    print('     |     |     ')

    print(' ', box[7], ' | ', box[8], ' |  ', box[9])

    print('     |     |     \n\n')

    key_press = input('\n-> Do you want to continue (Y/N) : ')

    if key_press == 'Y' or key_press == 'y':
        main()
    else:
        quit_game()


def rule():
    print('\n\n---------------------------')
    print('|        Game Rule        |')
    print('---------------------------\n')
    print('-> It seems you have some Trouble while play game, no worry i will help you. ')
    print('-> In Tic-Tac-Toe you have to make a straight line out of 3-O or 3-X ')
    print('-> For example: ')
    print("\n\t X | O | X \n\t ---------- \n\t X | X | O \n\t ----------\n\t X | O | O ")
    main()


def about():
    print('\n\n---------------------------------')
    print('|        About Developer        |')
    print('---------------------------------\n')
    print('-> Design By Raj Parsaniya')

    key_press = input('-> Do you want to explore more projects (Y/N) : ')

    if key_press == 'Y' or key_press == 'y':
        webbrowser.open_new_tab(url)
    else:
        main()


def quit_game():
    exit()


main()
