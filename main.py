from board import SudokuBoard
import generator,ui
def main():
    #初始化九宮格
    board=SudokuBoard()
    difficulty=input("請選擇等級模式：'easy' or 'medium' or 'hard' ")
    holes=generator.remove_cells(difficulty)
    full_board=generator.generate_full_solution(board)
    puzzle=generator.generate_puzzle(full_board,holes)
    copy_puzzle=SudokuBoard()
    copy_puzzle.board=puzzle
    ui.cli_loop(copy_puzzle)

if __name__=='__main__':
    main()

