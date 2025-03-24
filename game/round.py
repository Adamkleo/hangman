from game.hangman_art import HangmanArt
import random
from typing import Set


class Round:
    """
    Representa una ronda individual del juego del Ahorcado.
    Maneja el estado de la palabra, intentos, pistas y progreso del jugador.
    """

    MAX_ATTEMPTS = 6
    MAX_HINTS = 1

    def __init__(self, word: str) -> None:
        """
        Inicializa una nueva ronda con la palabra dada.

        Args:
            word (str): La palabra a adivinar en esta ronda.
        """
        self.word: str = word
        self.masked_word: list[str] = ["_"] * len(word)
        self.failed_attempts: int = 0
        self.guessed_letters: Set[str] = set()
        self.failed_letters: Set[str] = set()
        self.is_won: bool = False
        self.hints: int = self.MAX_HINTS

    def play(self) -> None:
        """
        Bucle principal de juego para una sola ronda.
        Pide letras al usuario, gestiona pistas y muestra el estado.
        """
        while self.failed_attempts < self.MAX_ATTEMPTS and "_" in self.masked_word:
            self.display_state()
            guess = self.get_guess()

            if guess == "hint":
                if self.hints > 0:
                    self.hints -= 1
                    self.use_hint()
                else:
                    print("¡No te quedan más pistas!")
                continue

            if guess in self.guessed_letters:
                print("Ya adivinaste esa letra. Intenta con otra.")
                continue

            self.process_guess(guess)

        self.end_round()

    def get_guess(self) -> str:
        """
        Solicita al jugador que introduzca una letra o 'hint'.

        Returns:
            str: Letra adivinada o la palabra 'hint'.
        """
        while True:
            guess = input("Adivina una letra (o escribe 'hint'): ").lower()
            if guess == "hint":
                return "hint"
            if guess.isalpha() and len(guess) == 1:
                return guess
            print("Entrada no válida. Escribe una sola letra o 'hint'.")

    def process_guess(self, guess: str) -> None:
        """
        Procesa la letra introducida por el jugador y actualiza el estado del juego.

        Args:
            guess (str): Letra adivinada.
        """
        self.guessed_letters.add(guess)

        if guess in self.word:
            self.reveal_letter(guess)

            if "_" not in self.masked_word:
                self.is_won = True
        else:
            self.failed_attempts += 1
            self.failed_letters.add(guess)

    def use_hint(self) -> None:
        """
        Utiliza una pista para revelar una letra aún no descubierta.
        """
        unrevealed_indices = [i for i, c in enumerate(self.masked_word) if c == "_"]
        if not unrevealed_indices:
            print("No hay más letras por revelar.")
            return

        unrevealed_letters = list({self.word[i] for i in unrevealed_indices})
        hint_letter = random.choice(unrevealed_letters)
        self.reveal_letter(hint_letter)
        self.guessed_letters.add(hint_letter)
        print(f"¡Pista usada! La letra '{hint_letter}' ha sido revelada.")

        if "_" not in self.masked_word:
            self.is_won = True

    def reveal_letter(self, guess: str) -> None:
        """
        Revela todas las posiciones de la letra adivinada correctamente.

        Args:
            guess (str): Letra adivinada.
        """
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.masked_word[i] = guess

    def display_state(self) -> None:
        """
        Muestra el estado actual del juego: palabra, intentos fallidos, letras fallidas y pistas restantes.
        """
        print(HangmanArt().get_stage(self.failed_attempts))
        print("Palabra: " + " ".join(self.masked_word))
        bar_length = self.MAX_ATTEMPTS
        progress = "█" * self.failed_attempts + "-" * (bar_length - self.failed_attempts)
        print(f"Intentos fallidos: {self.failed_attempts}/{self.MAX_ATTEMPTS} [{progress}]")
        print(f"Letras fallidas: {', '.join(self.failed_letters)}")
        print(f"Pistas restantes: {self.hints}")

    def end_round(self) -> None:
        """
        Lógica para finalizar una ronda, mostrando el resultado final.
        """
        if self.is_won:
            print(f"¡Felicidades! Adivinaste la palabra: {self.word}")
        else:
            print(f"¡Te quedaste sin intentos! La palabra era: {self.word}")
