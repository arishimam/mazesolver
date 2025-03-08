import time
import random
from cell import Cell 


class Maze():
    def __init__(
        self,
        x1,
        y1, 
        num_rows,
        num_cols, 
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None,
    ):
        self.x1 = x1 
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        if seed:
            random.seed(seed)

        self.cells = []
        self.create_cells()
        self.break_entrance_and_exit()
        self.break_walls_r(0,0)

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

    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0,0)

        self.cells[ self.num_rows - 1 ][ self.num_cols - 1 ].has_bottom_wall = False
        self.draw_cell( len(self.cells)-1 , len(self.cells[0])-1 )

    def break_walls_r(self, i, j):
        self.cells[i][j].visited = True

        while True:
            remaining = []

            # check adjacent cells if visited
            # if not visited append to possible directions

            # top
            if i > 0 and not self.cells[i-1][j].visited:
                remaining.append( (i-1,j) )

            # left
            if j > 0 and not self.cells[i][j-1].visited:
                remaining.append( (i,j-1) )

            # bottom
            if i + 1 < self.num_rows and not self.cells[i+1][j].visited:
                remaining.append( (i+1,j) )

            # right
            if j + 1 < self.num_cols and not self.cells[i][j+1].visited:
                remaining.append( (i,j+1) )


            if len(remaining) == 0:
                self.draw_cell(i,j) 
                return

            # pick random direction
            r_direction = random.randrange(len(remaining))
            index = remaining[r_direction]
            
            # knock downwalls between the cells
            if index[0] < i:
                #new cell above
                self.cells[i][j].has_top_wall = False
                self.cells[i-1][j].has_bottom_wall = False

            
            if index[0] > i:
                #new cell below 
                self.cells[i][j].has_bottom_wall = False
                self.cells[i+1][j].has_top_wall = False

            if index[1] > j:
                #new cell right 
                self.cells[i][j].has_right_wall = False
                self.cells[i][j+1].has_left_wall = False

            if index[1] < j:
                #new cell left 
                self.cells[i][j].has_left_wall = False
                self.cells[i][j-1].has_right_wall = False

            # recursive call to new cell
            self.break_walls_r(index[0], index[1])


    def animate(self):
        if self.win == None:
            return

        self.win.redraw()
        time.sleep(0.01)
