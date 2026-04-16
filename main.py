def greet_user(name: str) -> str:
    """
    Begrüßt den Benutzer mit einem personalisierten Gruß.

    Args:
        name (str): Der Name des Benutzers.

    Returns:
        str: Eine Begrüßungsnachricht.
    """
    return f"Hallo, {name}!"

if __name__ == "__main__":
    # Systemmeldung zum Anfordern des Namens auf Deutsch
    user_name = input("Bitte geben Sie Ihren Namen ein: ")

    # Rufen Sie die Begrüßungsfunktion auf
    greeting = greet_user(user_name)

    # Geben Sie die Begrüßung aus (die bereits "Hallo" auf Deutsch enthält)
    print(greeting)

    # Eine abschließende Systemmeldung auf Deutsch
    print("Vielen Dank für die Nutzung unseres Systems!")