def exist(board, word):
    def dfs(board, word, i, j, index):
        if index == len(word):
            return True

        if (i<0 or i== len(board)) or (j<0 or j==len(board)) or (board[i][j] != word[index]):
            return False

        temp, board[i][j] = board[i][j], "/"

        found=(dfs(board,word,i+1,j,index+1) or dfs(board,word,i-1,j,index+1) or dfs(board,word,i,j+1,index+1) or dfs(board,word,i,j-1,index+1))

        board[i][j]=temp
        return found

    for i in range(len(board)):
        for j in range(len(board[0])):
            if(dfs(board,word,i,j,0)):
                return True
    return False


board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]

print(exist(board, "ABCCED"))  # Output: True
print(exist(board, "SEE"))     # Output: True
print(exist(board, "ABCB"))



