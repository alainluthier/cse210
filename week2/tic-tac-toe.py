def main():
    player = nextPlayer("o")
    matrix = createMatrix()
    while not (aWinner(matrix) or aDraw(matrix)):
        displayMatrix(matrix)
        move(player,matrix)
        player = nextPlayer(player)
    displayMatrix(matrix)
    print("Good game. Thanks for playing!")
    
def nextPlayer(player):
    if (player=="o"):
        return "x"
    else:
        return "o"
def createMatrix():
    matrix=['1','2','3','4','5','6','7','8','9']
    return matrix

def aWinner(m):
    return (m[0]==m[1]==m[2] or 
    m[3]==m[4]==m[5] or 
    m[6]==m[7]==m[8] or 
    m[0]==m[3]==m[6] or 
    m[1]==m[4]==m[7] or 
    m[2]==m[5]==m[8] or 
    m[0]==m[4]==m[8] or 
    m[2]==m[4]==m[6])
    return False
def aDraw(m):
    for i in range(9):
        if (m[i] != "x" and m[i] != "o"):
            return False
    return True
def displayMatrix(m):
    text ="""
    %s|%s|%s
    -+-+-
    %s|%s|%s
    -+-+-
    %s|%s|%s
    """ % (m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7],m[8]) 
    print(text)
def move(player,matrix):
    index = int(input(player+"'s turn to choose a square (1-9): "))
    matrix[index-1]=player

if __name__ == "__main__":
    main()