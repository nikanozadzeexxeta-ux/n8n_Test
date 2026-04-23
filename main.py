def greet_user_in_german():
    """
    Begrüßt den Benutzer auf Deutsch, nachdem der Name abgefragt wurde.
    Alle Systemmeldungen sind in deutscher Sprache.
    """
    # Systemmeldung zur Abfrage des Namens (Deutsch)
    user_name = input("Bitte geben Sie Ihren Namen ein: ")

    # Begrüßungstext (Deutsch)
    greeting_message = f"Hallo, {user_name}!"

    # Ausgabe der Begrüßung (Deutsch)
    print(greeting_message)

if __name__ == "__main__":
    greet_user_in_german()