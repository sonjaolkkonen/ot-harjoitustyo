from ui.ui import Ui

class Sudoku:
    """Luokka, joka käynnistää ohjelman.
    """
    def __init__(self):
        """Luokan konstruktori, joka aloittaa uuden pelin"
        """
        Ui()

if __name__ == "__main__":
    sudoku = Sudoku()
