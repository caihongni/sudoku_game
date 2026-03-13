from board import SudokuBoard
import random

def generate_full_solution(board):
   
    def backtrack(cell_index=0):
        if cell_index==81:
            return True
        row=cell_index // 9
        col=cell_index % 9
        if board.board[row][col] != 0:
            return backtrack(cell_index + 1)
        nums=list(range(1,10))
        random.shuffle(nums)
        for num in nums:
            if board.is_valid(row,col,num):
                board.board[row][col]=num
                
                if backtrack(cell_index+1):
                    return True
                board.board[row][col]=0
        return False
    backtrack()
    return board
def has_unique_solution(board):
    grid=[row[:] for row in board]
    solutions_count=0

    def solve():
        nonlocal solutions_count
        for i in range(9):
            for j in range(9):
                if grid[i][j]==0:
                    for num in range(1,10):
                        if is_valid(grid,i,j,num):
                            grid[i][j]=num
                            solve()
                            if solutions_count>=2:
                                return
                            grid[i][j]=0
                    return 
        solutions_count+=1
        if solutions_count>=2:
            return
    solve()
    return solutions_count==1

def is_valid(board,row,col,num):
    for i in range(9):
        if board[row][i]==num or board[i][col]==num:
            return False
    box_row,box_col=3*(row//3),3*(col//3)
    for i in range(box_row,box_row+3):
        for j in range(box_col,box_col+3):
            if board[i][j]==num:
                return False
    return True
def remove_cells(difficulty):
    match difficulty:
        case 'easy':
            holes=random.randint(30,35)
        case 'medium':
            holes=random.randint(40,45)
        case 'hard':
            holes=random.randint(50,55)
    return holes
def generate_puzzle(full_board,holes,max_attempts=50):

    original_full = full_board
    for attempt in range(max_attempts):
        if attempt == 0:
            board_copy = [row[:] for row in original_full.board]
            puzzle = board_copy
        else:
            new_board = SudokuBoard()  # 假设有空棋盘
            new_board = generate_full_solution(new_board)  # 填充
            full_board.board=[row[:] for row in new_board.board]
            puzzle = [row[:] for row in new_board.board]

    
    cells=[(i,j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    removed=0
    for i,j in cells:
        if removed>=holes:
            break
        backup=puzzle[i][j]
        puzzle[i][j]=0
        #檢查唯一性
        if not has_unique_solution(puzzle):
            #如果唯一性被破壞，恢復該格子
            puzzle[i][j]=backup
        else:
             removed+=1
        if removed == holes:
            return puzzle
            
    return puzzle
