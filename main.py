def greet_user():
    """
    ეკითხება მომხმარებელს სახელს და შემდეგ ესალმება მას ქართულად.
    """
    user_name = input("გთხოვთ, შეიყვანოთ თქვენი სახელი: ")
    print(f"გამარჯობა, {user_name}!")

if __name__ == "__main__":
    greet_user()