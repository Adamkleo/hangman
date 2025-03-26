import csv, sys, time

from typing import List
from statistics import mean


class Hangman:
    """
    Clase que gestiona la carga y validación de palabras para el juego del Ahorcado.
    """

    def __init__(self, words_path: str) -> None:
        """
        Inicializa la instancia cargando las palabras desde el archivo CSV.

        Args:
            words_path (str): Ruta al archivo CSV que contiene las palabras.
        """
        self.words_path = words_path
        self.words: List[str] = self._load_words()
        
        # Validación: asegurarse de que haya mas de 30 palabras
        if self.get_number_of_words() < 30:
            print("Ups, no podemos comenzar el juego. Se esperaban al menos 30 palabras.")
            sys.exit(1)  # Finaliza el programa de forma segura

        # Validación: detectar palabras duplicadas
        if self.has_duplicates():
            print("Ups, no podemos comenzar el juego. Se encontraron palabras duplicadas.")
            sys.exit(1)

        self._loading_animation()
        print("Las palabras estan listas para jugar!")

    def _load_words(self) -> List[str]:
        """
        Carga las palabras desde un archivo CSV de forma segura.

        Returns:
            List[str]: Lista de palabras válidas (mínimo 5 caracteres).
        """
        words: List[str] = []
        try:
            with open(self.words_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    for word in row:
                        word = word.strip()
                        if len(word) >= 5:
                            words.append(word)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{self.words_path}'.")
            sys.exit(1)
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            sys.exit(1)
        return words

    def get_number_of_words(self) -> int:
        """
        Devuelve el número total de palabras cargadas.

        Returns:
            int: Cantidad de palabras.
        """
        return len(self.words)

    def has_duplicates(self) -> bool:
        """
        Verifica si hay palabras duplicadas.

        Returns:
            bool: True si hay duplicados, False en caso contrario.
        """
        return len(self.words) != len(set(self.words))

    def calculate_summary(self) -> dict:
        """
        Calcula un resumen de las palabras cargadas.

        Returns:
            dict: Diccionario con estadísticas de las palabras.
        """
        if not self.words:
            return {
                "number_of_words": 0,
                "duplicates": False,
                "average_word_length": None,
                "longest_word": None,
                "shortest_word": None
            }
        
        word_lengths = [len(word) for word in self.words]
        return {
            "number_of_words": self.get_number_of_words(),
            "duplicates": self.has_duplicates(),
            "average_word_length": round(mean(word_lengths), 2),
            "longest_word": max(self.words, key=len),
            "shortest_word": min(self.words, key=len)
        }


    def _loading_animation(self) -> None:
        """
        Loading animation.
        """
        print("Cargando Palabras: ", end="", flush=True)
        bar_length = 10
        for i in range(1, bar_length + 1):
            progress = "█" * i + "-" * (bar_length - i)
            print(f"\rCargando Palabras:  [{progress}]", end="", flush=True)
            time.sleep(0.3)
        print()  



