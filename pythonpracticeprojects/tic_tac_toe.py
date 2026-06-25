def sum(a,b,c):
    return a+b+c
def printBoard(xState, zState):
    # Helper to determine what to print for each cell
    def cell(i):
        if xState[i]: return 'X'
        if zState[i]: return 'O'
        return str(i)

    print(f" {cell(0)} | {cell(1)} | {cell(2)} ")
    print(f"---|---|---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)} ")
    print(f"---|---|---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)} ")
    
def checkWin(xState, zState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]],xState[win[2]])==3:
            print("X won the match")
            return 1
        if sum(zState[win[0]], zState[win[1]],zState[win[2]])==3:
            print("O won the match")
            return 0
        
    return -1
    
if __name__ == '__main__':
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    turn = 1 # 1 for X, 0 for O
    
    print("Welcome to kiku's Tic Tac Toe")
    
    while True:
        printBoard(xState, zState)
        
        if turn == 1: 
            print("X's chance")
            value = int(input("Please enter a value (0-8): "))
            xState[value] = 1
            turn = 0 # Switch turn to O
        else: 
            print("O's chance")
            value = int(input("Please enter a value (0-8): "))
            zState[value] = 1
            turn = 1 # Switch turn to X
            
        print("\n" + "="*20 + "\n") # Visual separator between turns
        cwin = checkWin(xState,zState)
        if cwin!=-1:
            break
    