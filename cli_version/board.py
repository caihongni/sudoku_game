class SudokuBoard:
    def __init__(self,size=9):
        self.size=size
        self.board=[[0]*size for _ in range(size)]
    def set_cell(self,row,col,value):
        #設置單元格值
        self.board[row][col]=value
       

    def get_cell(self,row,col):
        return self.board[row][col]
    
    def is_valid(self,row,col,value):
        #檢查在(row,col)處填入value是否符合數獨規則
        for i in range(9):
            if self.board[row][i]==value or self.board[i][col]==value:
                return False
            box_row,box_col=3*(row//3),3*(col//3)
            for i in range(box_row,box_row+3):
                for j in range(box_col,box_col+3):
                   if self.board[i][j]==value:
                       return False
        return True
    def find_empty_cell(self):
        #找九宮格上是否有空位
        for i in range(9):
            for j in range(9):
                if self.board[i][j]==0:
                    return i,j
        return False
    def is_solved(self):
        #檢查當前九宮格是否滿足數獨規則且全部填滿
        empty=self.find_empty_cell()
        if empty:
            return False

        for i in range(9):
            if not self._is_unit_valid(self.board[i]):
                return False
            column=[self.board[j][i] for j in range(9)]
            if not self._is_unit_valid(column):
                return False
            box_row=3*(i // 3)
            box_col=3*(i % 3)
            box=[self.board[r][c] for c in range(box_col,box_col+3) for r in range(box_row,box_row+3)]
            if not self._is_unit_valid(box):
                return False
        return True
    def _is_unit_valid(self,unit):
        #檢查一個單元是否包含1-9各一次
        return set(unit)==set(range(1,10))
    def clear(self):
        #清空九宮格
        self.board=[[0]*self.size for _ in range(self.size)]