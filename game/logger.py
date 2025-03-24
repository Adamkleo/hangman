import uuid
from datetime import datetime
from game.utils import append_to_csv
from typing import List


class GameLogger:
    """
    Registra información sobre las partidas y rondas jugadas,
    guardando los datos en archivos CSV para análisis o persistencia.
    """

    def log_game(self, player_name: str, rounds: List['Round']) -> None:
        """
        Registra una partida completa y sus rondas en archivos CSV.

        Args:
            player_name (str): Nombre del jugador.
            rounds (List[Round]): Lista de rondas jugadas.
        """
        game_id = str(uuid.uuid4())
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        score = sum(1 for r in rounds if r.is_won)

        # Registrar datos generales de la partida en games.csv
        append_to_csv(
            'games.csv',
            {
                'game_id': game_id,
                'username': player_name,
                'start_date': start_time,
                'end_date': end_time,
                'final_score': score
            },
            ['game_id', 'username', 'start_date', 'end_date', 'final_score']
        )

        # Registrar los datos de cada ronda en rounds_in_games.csv
        for rnd in rounds:
            round_id = str(uuid.uuid4())
            attempts = rnd.failed_attempts + \
                len(rnd.guessed_letters -
                    {rnd.word[i] for i, c in enumerate(rnd.masked_word) if c == "_"})

            append_to_csv(
                'rounds_in_games.csv',
                {
                    'game_id': game_id,
                    'word': rnd.word,
                    'username': player_name,
                    'round_id': round_id,
                    'user_attempts': attempts,
                    'victory': rnd.is_won
                },
                ['game_id', 'word', 'username', 'round_id', 'user_attempts', 'victory']
            )
