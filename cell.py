from window import Point, Line
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
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self.win == None: 
            return

        # draw up to 4 lines 
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        left = Line(Point(x1, y1), Point(x1, y2))
        right = Line(Point(x2, y1), Point(x2, y2))
        top = Line(Point(x1, y1), Point(x2, y1))
        bottom = Line(Point(x1, y2), Point(x2, y2))
        
        line_color = ""

        if self.has_left_wall:
            line_color = "black"
        else:
            line_color = "white"
        self.win.draw_line(left, line_color)

        if self.has_right_wall:
            line_color = "black"
        else:
            line_color = "white"
        
        self.win.draw_line(right, line_color)

        if self.has_top_wall:
            line_color = "black"
        else:
            line_color = "white"
        self.win.draw_line(top, line_color)

        if self.has_bottom_wall:
            line_color = "black"
        else:
            line_color = "white"
        self.win.draw_line(bottom, line_color)


    def draw_move(self, to_cell, undo=False):
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

