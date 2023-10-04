# Boggle_Word_Checker
The find_word function is a Python implementation that checks if a given word can be found on a Boggle board. 
It utilizes a depth-first search (DFS) approach to explore the board for possible paths by using the function find_path
## Function Signature
def find_word(board: List[List[str]], word: str) -> bool:
    """
    Checks if a given word can be found on a Boggle board.

    Args:
        board (List[List[str]]): 2D list representing the Boggle board.
        word (str): The word to be searched for on the board.

    Returns:
        bool: True if the word can be found, False otherwise.
    """
# How It Works
The find_word function takes two arguments: board, a 2D list representing the Boggle board, and word, the word to be searched for.

The function performs a depth-first search (DFS) to explore possible paths on the board, checking if they match the given word.

# Example Usage
testBoard = [
    ["E","A","R","A"],
    ["N","L","E","C"],
    ["I","A","I","S"],
    ["B","Y","O","R"]
]

result = find_word(testBoard, "BINARY")
print(result)  # Output: True
