import random
attempt = 0 
print("======== Guess the number =======")
while True:
    number = int(input("Choose a number(0 to 5): "))
    secret_key = random.randint(0,5)
    if number==secret_key:
        attempt=attempt+1
        if(attempt==1):
            print("Correct guess")
            print("You guessed the number in 1 attempts.")
            decision = input("You want to continue? yes or no? ")
            if(decision == "yes"):
                attempt = 0
                continue
            else:
                break

        else:
            print("Correct guess")
            decision = input("You want to continue? yes or no? ")
            if(decision == "yes"):
                attempt = 0
                continue
            else:
                break
    else:
        print("Not matching! Its: ",secret_key)
        decision = input("You want to continue? yes or no? ")
        if(decision == "yes"):
            attempt = attempt + 1
            continue
        else:
            break

print("===== Game Over =====")