from window import Window, Point, Line, Cell


def main():
    window = Window(800, 600)
    c = Cell(True, True, True, True, 50, 50, 100, 100, window)
    #l = Line(Point(50,50), Point(400,400))
    #window.draw_line(l, "black")
    c.draw()
    window.wait_for_close()

if __name__ == '__main__':
    main()
