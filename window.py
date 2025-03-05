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
    def __init__(self, left, right, top, bottom, x1, y1, x2, y2, window):
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom 

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.win = window

    def draw(self):
        # draw up to 4 lines 
        if self.has_left_wall:
            l1 = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(l1, "black")
        if self.has_right_wall:
            l1 = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(l1, "black")
        if self.has_top_wall:
            l1 = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(l1, "black")
        if self.has_bottom_wall:
            l1 = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(l1, "black")

