import random
number= random.randint(1,100)

def give_extra_hints(number, user):
    hints = []

    # Even or Odd
    if number % 2 == 0:
        hints.append("Hint: The number is EVEN.")
    else:
        hints.append("Hint: The number is ODD.")

    # Divisibility
    if number % 3 == 0:
        hints.append("Hint: The number is divisible by 3.")
    elif number % 5 == 0:
        hints.append("Hint: The number is divisible by 5.")
    else:
        hints.append("Hint: The number is not divisible by 3 or 5.")

    # Close guess?
    if abs(number - user) <= 2:
        hints.append("You're very close! 🔥")

    return hints

for i in range(5):
    user=int(input("Guess the number (1-100) : "))

    if user==number:
        print(f"Hurray! You guessed the number right, it's {number} .")
        break
    else:
        if user < number:
                print("Too low! Try a higher number.")
        else:
                print("Too high! Try a lower number.")

        extra_hints = give_extra_hints(number, user)
        for hint in extra_hints:
                print("➤", hint)
        print()
else:
        print(f"\n❌ Out of attempts! The correct number was {number}.\n")

if user!= number:
    print(f"Sorry , you've used all attempts. The number was {number} .")