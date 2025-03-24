import csv
from statistics import mean
import sys

class Hangman:
    def __init__(self, words_path):
        self.words_path = words_path
        self.words = self._load_words()
        
        # Validation: Ensure exactly 30 words**
        if self.get_number_of_words() != 30:
            print("Oops, we can't start the game. Expected 30 words.")
            sys.exit(1)  # Terminates the program safely

        if self.has_duplicates():
            print("Oops, we can't start the game. Duplicate words found.")
            sys.exit(1)

        print("Words are ready, let's go!")  # Success message
    
    def _load_words(self):
        """Loads words from a CSV file safely."""
        words = []
        try:
            with open(self.words_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    for word in row:
                        word = word.strip()
                        if len(word) >= 5:  # Ensure the word is valid
                            words.append(word)
        except FileNotFoundError:
            print(f"Error: File '{self.words_path}' not found.")
            sys.exit(1)  # Stop execution if file is missing
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)
        return words

    def get_number_of_words(self):
        """Returns the number of words loaded."""
        return len(self.words)

    def has_duplicates(self):
        """Checks if there are duplicate words."""
        return len(self.words) != len(set(self.words))

    def calculate_summary(self):
        """Returns a summary of the words dataset."""
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
