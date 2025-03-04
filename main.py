from window import Window, Line


def main():
    window = Window(800, 600)
    line1 = Line(0,0,400,400)
    window.draw_line(line1, "black")
    window.wait_for_close()

if __name__ == '__main__':
    main()
