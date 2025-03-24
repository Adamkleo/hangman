# Hangman Game Project

A command-line implementation of the Hangman Game to practice applications of SOLID principles. This project includes core game logic, round tracking, player statistics, logging, and summary generation. It also features a basic `statistics.ipynb` notebook for analyzing gameplay data.

## Features

- Three-round hangman game sessions
- Letter guessing with masked words
- One hint allowed per round
- ASCII-based hangman art
- Per-round and full-game logging
- Summary generation with performance medals
- Word list validation (exactly 30 words, no duplicates)
- Game summaries saved to text files
- CSV logs for games and rounds

## Project Structure

```
.
├── game/
│   ├── ession.py       # Game session manager
│   ├── round.py              # Logic for a single round
│   ├── summary.py       # Summary and performance stats
│   ├── hangman.py            # Word loading and validation
│   ├── hangman_art.py        # ASCII art for hangman stages
│   ├── logger.py        # CSV logging for games and rounds
│   └── utils.py              # CSV writing utility
├── statistics.ipynb          # Notebook for data analysis
├── words.csv                 # CSV file with 30 valid words
├── games.csv                 # Output log: summary per game
├── rounds_in_games.csv       # Output log: per-round data
├── README.md                 # Project documentation
```

## Requirements

- Python 3.13+

## Installation and Running Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/AdamKleo/hangman-game.git
   cd hangman-game
   ```

2. **Create a virtual environment** 
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the game**  
   Make sure `words.csv` exists and contains at least 30 valid words (5+ characters each). Then run your main script or the provided `main.py`:
   ```bash
   python main.py
   ```

## Statistics  
   Open `statistics.ipynb` in Jupyter Notebook or any compatible environment to explore basic gameplay data.


## License

This project is licensed for educational and personal use.





