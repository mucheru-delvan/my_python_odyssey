credentials = {
    "user1": "password1"
}

max_attempts = 3
attempts = 0

print("You have 3 attempts!")

while attempts < max_attempts:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    attempts += 1

    if username in credentials and credentials[username] == password:
        print(f"Welcome {username}!")
        break
    else:
        remaining = max_attempts - attempts
        print("Invalid username or password, try again!")
        if remaining > 0:
            print(f"You have {remaining} attempts remaining.\n")

if attempts == max_attempts:
    print("You are locked out!")
