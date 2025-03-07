import time
from window import Cell 


class Maze():
    def __init__(
        self,
        x1,
        y1, 
        num_rows,
        num_cols, 
        cell_size_x,
        cell_size_y,
        win = None
    ):
        self.x1 = x1 
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self.cells = []
        self.create_cells()

    def create_cells(self):
        for i in range(self.num_rows):
            col = []
            for j in range (self.num_cols):
                c = Cell(self.win)
                col.append(c) 
            self.cells.append(col)


        # call draw_cells on cells 
        for i in range(self.num_rows):
            for j in range (self.num_cols):
                self.draw_cell(i,j)

    def draw_cell(self, i, j):
        x1 = self.x1 + self.cell_size_x * i
        y1 = self.y1 + self.cell_size_y * j

        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        # how to draw each cell
        self.cells[i][j].draw(x1, y1, x2, y2)
        self.animate()



    def animate(self):
        if self.win == None:
            return

        self.win.redraw()
        time.sleep(0.01)
