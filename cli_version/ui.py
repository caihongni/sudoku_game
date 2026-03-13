

def print_board(grid):
    """打印帶分隔符的棋盤"""
    
    for i in range(9):
        if i % 3==0 and i!=0:
            print("-"*21)
        for j in range(9):
            if j % 3 ==0 and j!=0:
                print("|",end=" ")
            val=grid[i][j]
            if val==0:
                print(".",end=" ")
            else:
                print(val,end=" ")
        print()
    print()
                      
                  
def get_user_input():
    """接收用戶輸入的坐標和數字，選擇難度"""
    while True:
        try:
            row=int(input("請輸入0-8,row="))
            col=int(input("請輸入0-8,col="))
            val=int(input("請輸入1-9的數字："))
            if row>8 or row<0 or col>8 or col<0 or val>9 or val<1:
                raise Exception("輸入的數字不滿足條件")
        except ValueError as e:
            print ("異常提示：請輸入一個有效數字")
        except Exception as e:
            print(f'異常提示：{e}')
        else:
            break
    return row,col,val

def cli_loop(board):
    get_inputs=[]
    next_step='0'
    
    while not board.is_solved():
        print_board(board.board)
        row,col,val=get_user_input()
       
        if board.board[row][col]==0 and board.is_valid(row,col,val):
            board.set_cell(row,col,val)
            get_inputs.append((row,col))
        else:
            next_step=input(f'{(row,col)}位置填充無效,是否要刪除其他位置的填充，是請按1，否則按其他任意鍵:')
            
            while next_step=='1':
                r=int(input('要刪除的行的位置(0-8):'))
                c=int(input('要刪除的列的位置(0-8):'))
                if (r,c) in get_inputs:
                    board.board[r][c]=0
                    next_step=input("是否繼續刪除其他位置的填充，是請按1，否則請按其他任意鍵:")
                else:
                    next_step=input(f'{(r,c)}位置的元素不可刪除,是否繼續刪除請按1，否則按任意鍵退出:')
                    if next_step !='1':
                        break
    print("恭喜，你完成了數獨")