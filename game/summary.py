from typing import List
from game.round import Round

class GameSummary:
    """
    Representa el resumen final de una partida del juego.
    Contiene estadísticas, palabras jugadas y una medalla según el rendimiento.
    """

    def __init__(self, player_name: str, rounds: List[Round]) -> None:
        """
        Inicializa el resumen del juego.

        Args:
            player_name (str): Nombre del jugador.
            rounds (List[Round]): Lista de rondas jugadas.
        """
        self.player_name = player_name
        self.rounds = rounds

    def success_rate(self) -> float:
        """
        Calcula la tasa de éxito del jugador -- Porcentaje de rondas ganadas (entre 0 y 1).
        """

        return sum(1 for r in self.rounds if r.is_won) / len(self.rounds)

    def total_attempts(self) -> int:
        """
        Calcula el número total de intentos (letras adivinadas) en todas las rondas -- Número total de intentos.
        """
        return sum(r.failed_attempts + len(r.guessed_letters) - r.failed_attempts for r in self.rounds)

    def medal(self) -> str:
        """
        Determina la medalla otorgada al jugador según su puntuación.
        """
        score = sum(1 for r in self.rounds if r.is_won)
        if score == 3:
            return "Excelente"
        elif score == 2:
            return "Muy bien"
        elif score == 1:
            return "Hay que mejorar"
        else:
            return "Sigue practicando"

    def summary_text(self) -> str:
        """
        Genera un texto con el resumen completo de la partida.

        Returns:
            str: Texto con estadísticas del juego.
        """
        words = [r.word for r in self.rounds]
        summary = [
            f"Jugador: {self.player_name}",
            f"Palabras: {', '.join(words)}",
            f"Aciertos: {sum(1 for r in self.rounds if r.is_won)}/3",
            f"Intentos totales: {self.total_attempts()}",
            f"Tasa de éxito: {self.success_rate() * 100:.0f}%",
            f"Medalla: {self.medal()}"
        ]
        return "\n".join(summary)
