import tkinter as tk
from tkinter import messagebox

from board import SudokuBoard
from generator import generate_full_solution, generate_puzzle, remove_cells

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("数独游戏")
        self.root.resizable(False, False)

        # 游戏状态
        self.puzzle = None          # 当前谜题盘面（二维列表，0表示空格）
        self.solution = None        # 完整解（用于检查或提示）
        self.cells = []             # 存储所有 Entry 控件的二维列表

        # 创建界面
        self.difficulty = tk.StringVar(value='medium')  # 默认简单
        
        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        # 顶部框架（可选计时器）
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)
         # 难度标签
        tk.Label(top_frame, text="难度：").pack(side='left', padx=5)

        # 三个单选按钮，绑定到 self.difficulty
        tk.Radiobutton(top_frame, text="简单", variable=self.difficulty,value='easy',command=self.new_game).pack(side='left')
        tk.Radiobutton(top_frame, text="中等", variable=self.difficulty,value='medium',command=self.new_game).pack(side='left')
        tk.Radiobutton(top_frame, text="困难", variable=self.difficulty,value='hard',command=self.new_game).pack(side='left')

        # 中间棋盘框架
        board_frame = tk.Frame(self.root, bg='#2e5e4e')
        board_frame.pack()

        # 创建 9x9 的格子
        for i in range(9):
            row_entries = []
            for j in range(9):
                # 区分宫格边界（粗线）
                if i % 3 == 0 and j % 3 == 0:
                    border = {'bd': 2, 'relief': 'ridge'}
                else:
                    border = {'bd': 1, 'relief': 'solid'}

                entry = tk.Entry(board_frame, width=2, font=('Arial', 18),
                                 justify='center', **border)
                entry.grid(row=i, column=j, padx=1, pady=1, ipady=5)

                # 绑定事件
                entry.bind('<KeyRelease>', self.on_key_release)
                entry.bind('<FocusIn>', self.on_focus_in)

                row_entries.append(entry)
            self.cells.append(row_entries)

        # 底部按钮框架
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="新游戏", command=self.new_game,
                  width=8).pack(side='left', padx=5)
        tk.Button(button_frame, text="检查", command=self.check_answer,
                  width=8).pack(side='left', padx=5)
        tk.Button(button_frame, text="提示", command=self.give_hint,
                  width=8).pack(side='left', padx=5)
        tk.Button(button_frame, text="重置", command=self.reset_puzzle,
                  width=8).pack(side='left', padx=5)
    

    def new_game(self):
        # 获取当前难度
        diff = self.difficulty.get()  
        holes = remove_cells(diff)
        # 生成完整解
        full_board = SudokuBoard()      # 假设你有一个 SudokuBoard 类
        full_board = generate_full_solution(full_board)
        #self.solution = full_board.board  # 保存完整解

        # 根据难度挖洞
        
        puzzle_board = generate_puzzle(full_board, holes)
        self.solution = full_board.board

        self.puzzle = puzzle_board       # 保存谜题盘面
        self.update_board()              # 更新 UI

    def update_board(self):
        for i in range(9):
            for j in range(9):
                val = self.puzzle[i][j]
                self.cells[i][j].delete(0, tk.END)
                if val != 0:
                    self.cells[i][j].insert(0, str(val))
                    # 预置数字设为只读或特殊颜色
                    self.cells[i][j].config(state='readonly', 
                                         readonlybackground='#f0f0f0')
                else:
                    self.cells[i][j].config(state='normal', bg='lightblue')
    def on_key_release(self, event):
        entry = event.widget
        content = entry.get()
        if content and content.isdigit():
            if content not in '123456789':
                entry.delete(0, tk.END)
            else:
                # 自动跳转到下一个格子（可选）
                entry.tk_focusNext().focus()
        else:
            entry.delete(0, tk.END)

    def on_focus_in(self, event):
        # 聚焦时清空内容以便输入（如果是空格）
        entry = event.widget
        if entry.get() == '0' or entry.get() == '':
           entry.delete(0, tk.END)

    def check_answer(self):
        # 收集当前用户输入
        user_board = [[0]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = self.cells[i][j].get()
                if val.isdigit():
                    user_board[i][j] = int(val)
                else:
                    user_board[i][j] = 0

        # 与完整解比较
        correct = True
        for i in range(9):
            for j in range(9):
                if user_board[i][j] != self.solution[i][j]:
                    correct = False
                    # 高亮错误格子（例如红色背景）
                    self.cells[i][j].config(bg='#ffcccc')
                else:
                    self.cells[i][j].config(bg='white')

        if correct:
            messagebox.showinfo("恭喜", "答案正确！")
        else:
            messagebox.showinfo("提示", "答案有误，红色格子需修正。")

    def give_hint(self):
        # 找到第一个空格或错误格，填入正确答案
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].get() != str(self.solution[i][j]):
                    self.cells[i][j].delete(0, tk.END)
                    self.cells[i][j].insert(0, str(self.solution[i][j]))
                    return
        messagebox.showinfo("提示", "所有格子都已正确！")
    def reset_puzzle(self):
        # 恢复初始谜题盘面
        self.update_board()
        # 清除所有背景色
        for i in range(9):
            for j in range(9):
                self.cells[i][j].config(bg='white')

if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()