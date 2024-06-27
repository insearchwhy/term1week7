def check_password():
    user_password = "AstroNur19"

    while input("please enter your password: ") != user_password:
        print("Access denied! Incorrect password")

    print("Access granted!")
