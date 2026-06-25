def sum(a,b,c):
    return a+b+c
def board(xState, zState):
    def cell(i):
        if xState[i]:
            return "X"
        if zState[i]:
            return "O"
        return str(i)

    print(f"{cell(0)}|{cell(1)}|{cell(2)}")
    print(f"-|-|-")
    print(f"{cell(3)}|{cell(4)}|{cell(5)}")
    print(f"-|-|-")
    print(f"{cell(6)}|{cell(7)}|{cell(8)}")
    
def winBoard(xState,zState):
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
    xState = [0,0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0,0]
    turn = 1
    while True:
        board(xState, zState)
        if turn == 1:
            print(f"X's chance")
            value = int(input("Enter the value"))
            xState[value] =1
            turn = 0
        else:
            print(f"O's chance")
            value = int(input("Enter the value"))
            zState[value] =1
            turn = 1
        cwin = winBoard(xState,zState)
        if cwin !=-1:
            print("It's a draw")
            break
