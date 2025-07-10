def reverse_number_guessing_game():
    low = 1
    high = 100
    attempts = 0
    print("Think of a number between 1 and 100, and I will try to guess it!")

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it correct, too high, or too low? ").lower()

        if feedback == "correct":
            print(f"Yay! I guessed your number in {attempts} attempts.")
            break
        elif feedback == "too high":
            high = guess - 1
        elif feedback == "too low":
            low = guess + 1
        else:
            print("Please enter: 'correct', 'too high', or 'too low'.")

reverse_number_guessing_game()



