from window import Window, Point, Line, Cell


def main():
    window = Window(800, 600)
    c = Cell(window)
    #l = Line(Point(50,50), Point(400,400))
    #window.draw_line(l, "black")
    c.draw(50, 50, 100, 100)
    c.draw(100, 100, 150, 150)
    c.draw(100, 50, 150, 100)
    c.has_right_wall = False
    c.has_bottom_wall = False
    c.draw(150, 50, 200, 100) 
    window.wait_for_close()

if __name__ == '__main__':
    main()
