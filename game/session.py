from game.summary import GameSummary
from game.hangman import Hangman
from game.logger import GameLogger
from game.round import Round
from typing import List, Set
import random


class GameSession:
    """
    Gestiona una sesión completa del juego.
    Incluyendo múltiples rondas, cálculo de puntuación y generación de resumen.
    """

    def __init__(self, hangman: Hangman, logger: GameLogger) -> None:
        """
        Inicializa una nueva sesión del juego.
        """

        self.hangman = hangman # Clase del Juego
        self.logger = logger # Clase del logger de la partida
        self.player_name: str | None = None
        self.rounds: List[Round] = [] # Rondas del juego
        self.used_words: Set[str] = set() # Palabras usadas

    def start(self) -> None:
        """
        Inicia una nueva sesión del juego. Pide el nombre del jugador,
        ejecuta tres rondas del ahorcado y finaliza el juego.
        """
        self.player_name = input("Ingresa tu nombre: ")
        print(f"¡Bienvenido/a, {self.player_name}! Empecemos.")

        # Jugar 3 rondas
        for _ in range(3):
            word = self.get_random_word()
            round_instance = Round(word)
            self.rounds.append(round_instance)
            round_instance.play()

        # Finalizar el juego
        self.end_game()

    def end_game(self) -> None:
        """
        Finaliza la sesión actual. Registra la sesión, muestra el resumen,
        lo guarda en un archivo y muestra la puntuación final.
        """

        self.logger.log_game(self.player_name, self.rounds)

        # Generar y mostrar resumen
        summary = GameSummary(self.player_name, self.rounds)
        print("\n===== Resumen de la partida =====")
        print(summary.summary_text())

        # Guardar resumen en archivo
        self.save_summary_file(summary)

        # Mostrar puntuación final
        print(f"\nJuego terminado, {self.player_name}. Tu puntuación: {self.get_score()}/3.")

    def get_score(self) -> int:
        """
        Calcula la puntuación del jugador según las rondas ganadas.

        Returns:
            int: Número de rondas ganadas.
        """
        return sum(1 for r in self.rounds if r.is_won)

    def get_random_word(self) -> str:
        """
        Selecciona una palabra aleatoria de la lista disponible y asegura
        que no se repita.

        Returns:
            str: Una palabra para usar en la ronda actual.
        """

        word = random.choice(self.hangman.words)
        self.hangman.words.remove(word)
        self.used_words.add(word)
        return word

    def save_summary_file(self, summary_obj: GameSummary) -> None:
        """
        Guarda el resumen del juego en un archivo de texto con el nombre del jugador.

        Args:
            summary_obj (GameSummary): Instancia del resumen del juego.
        """
        filename = f"{self.player_name}_resumen.txt"
        with open(filename, "w") as file:
            file.write(summary_obj.summary_text())
