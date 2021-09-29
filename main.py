import random as rnd


def endgame():
    end_game = True
    while end_game:
        print("Do you want to try again? Y/N")
        run = input()
        if run == "N":
            end_game = False
            return False
        elif run == "Y":
            end_game = False
            return True
        else:
            print("Invalid input")
            end_game = True


def mad_libs():
    run_feature = True
    while run_feature:
        words = [input("An Adjective: "), input("An Adjective: "), input("A type of Bird: "),
                 input("Room in a House: "), input("A Verb (Past Tense): "), input("A Verb: "),
                 input("A Relative\'s Name: "), input("A Noun: "), input("A Liquid: "),
                 input("A Verb Ending in -ing: "), input("A Part of the Body (Plural): "), input("A Noun (Plural): "),
                 input("A Verb Ending in -ing: "), input("A Noun: ")]
        mad = "it was a {} cold November day. I woke up to the {} smell of {} roasting in the {} downstairs. I {} down the stairs to see if I could help {} the dinner. My mom said, \"See if {} needs a fresh {}.\" So I carried a tray of glasses full of {} into the {} room. When I got there, I couldn't believe my {}! There were {} {} on the {}!".format(
            *words)
        print(mad)
        run_feature = endgame()


def number_guess():
    run_feature = True

    def game(lower_limit, upper_limit):
        run_game = True
        num = rnd.randint(lower_limit, upper_limit)
        print(num)
        while run_game:
            guess = int(input("Guess that number between " + str(lower_limit) + " and " + str(upper_limit) + " : "))
            if guess > num:
                print("lower")
            elif guess < num:
                print("higher")
            elif guess == num:
                print("correct!")
                run_game = False
            else:
                print("invalid input")

    while run_feature:
        print("Choose mode 1. (1-10), 2. (1-100), 3. Custom Range")
        mode = input()
        if mode == "1":
            game(1, 10)
            run_feature = endgame()
        elif mode == "2":
            game(1, 100)
            run_feature = endgame()
        elif mode == "3":
            lower_limit = int(input("input the lower limit: "))
            upper_limit = int(input("input the upper limit: "))
            game(lower_limit, upper_limit)
            run_feature = endgame()
        else:
            print("invalid input")

def hangman():
    run_feature = True
    while run_feature:
        word_list = ["alligator", "charity", "whiteboard", "tongue", "geographic"]
        word = word_list[rnd.randint(0, 5)]
        arr = []
        for x in word:
            arr.append("_")
        current = ""
        while "_" in arr:
            print(current.join(arr))
            guess = input("make a guess: ")
            if guess in word:
                for x, y in enumerate(word):
                    if y == guess:
                        arr[x] = guess


def switcher(choice):
    switch = {
        "1": mad_libs,
        "2": number_guess,
        "3": hangman
    }
    print(switch.get(choice, "Invalid selection"))
    if choice in switch:
        return switch[choice]()
    else:
        print("Invalid")


print(
    "Welcome to my beginner Python Project portfolio. For more information on the projects here please visit: https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/")

choice = input("Please choose a project to try: ")
switcher(choice)
