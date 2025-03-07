from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")

        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)

        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def close(self):
        self.running = False


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.p1 = point1 
        self.p2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )

class Cell():
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None

        self.win = window

    def draw(self, x1, y1, x2, y2):
        if self.win == None: 
            return

        # draw up to 4 lines 
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        if self.has_left_wall:
            l1 = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(l1, "black")
        if self.has_right_wall:
            l1 = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(l1, "black")
        if self.has_top_wall:
            l1 = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(l1, "black")
        if self.has_bottom_wall:
            l1 = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(l1, "black")

    def draw_move(self, to_cell, undo=False):
        if self.win == None: 
            return
        # draw line to each cells center
        # we likely don't have to worry about legality of the move if we only 
        # perform this action on adjacent cells
        # therefore lets get the center of self and the center of to_cell
        # and simply create a line from those 2 points

        self_x = self.x1 + ((self.x2 - self.x1)// 2)
        self_y = self.y1 + ( (self.y2 - self.y1) // 2)
        self_point = Point(self_x, self_y)


        to_x = to_cell.x1 + ( (to_cell.x2 - to_cell.x1) // 2 )
        to_y = to_cell.y1 + (( to_cell.y2 - to_cell.y1) // 2 )
        to_point = Point(to_x, to_y)

        l = Line(self_point, to_point)

        if not undo:
            self.win.draw_line(l, "red")
        else:
            self.win.draw_line(l, "gray")

