def find_word(board, word):
    def find_path(i, j, word):
        if not word:
            return True
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[0]:
            temp, board[i][j] = board[i][j], "@"
            found = (find_path(i+1, j, word[1:]) or find_path(i-1, j, word[1:]) or
                 find_path(i, j+1, word[1:]) or find_path(i, j-1, word[1:]) or
                 find_path(i+1, j+1, word[1:]) or find_path(i+1, j-1, word[1:]) or
                 find_path(i-1, j+1, word[1:]) or find_path(i-1, j-1, word[1:]))
            board[i][j] = temp
            return found
        return False

    return any(find_path(i, j, word) for i in range(len(board)) for j in range(len(board[0])))

# Example usage:
testBoard = [
    ["E","A","R","A"],
    ["N","L","E","C"],
    ["I","A","I","S"],
    ["B","Y","O","R"]
]

 

print(find_word(testBoard, "C"))  # True
print(find_word(testBoard, "EAR"))  # True
print(find_word(testBoard, "EARS"))  # False
print(find_word(testBoard, "BAILER"))  # True
print(find_word(testBoard, "RSCAREIOYBAILNEA"))  # True
print(find_word(testBoard, "CEREAL"))  # False
print(find_word(testBoard, "ROBES"))  # False
