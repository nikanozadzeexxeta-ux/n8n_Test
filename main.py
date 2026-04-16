def begruessen_benutzer(name: str) -> str:
    """
    Erstellt eine personalisierte Begrüßungsnachricht auf Deutsch.

    Args:
        name (str): Der Name des zu begrüßenden Benutzers.

    Returns:
        str: Eine Begrüßungsnachricht im Format "Hallo [Name]!".
    """
    return f"Hallo {name}!"

if __name__ == "__main__":
    # Systemnachrichten müssen auf Deutsch sein.
    print("Willkommen zur Benutzerbegrüßungsfunktion.")

    # Aufforderung zur Eingabe des Namens (Systemnachricht)
    benutzername_eingabe = input("Bitte geben Sie Ihren Namen ein: ")

    # Erzeugen der Begrüßungsnachricht
    begruessung = begruessen_benutzer(benutzername_eingabe)

    # Ausgabe der Begrüßungsnachricht (Systemnachricht)
    print(begruessung)

    # Abschlussnachricht (Systemnachricht)
    print("Vielen Dank für die Nutzung. Auf Wiedersehen!")