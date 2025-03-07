from window import Window, Point, Line, Cell
from maze import Maze


def main():
    window = Window(800, 600)
    # c1 = Cell(window)
    # c1.has_right_wall = False
    # c1.draw(50, 50, 100, 100)

    # c2 = Cell(window)
    # c2.has_left_wall = False
    # c2.has_bottom_wall = False
    # c2.draw(100, 50, 150, 100)

    # c1.draw_move(c2, False)

    # c3 = Cell(window)
    # c3.has_right_wall = False
    # c3.has_top_wall = False
    # c3.draw(100, 100, 150, 150)
    # c2.draw_move(c3, False)

    maze = Maze(50, 50, 14, 10, 50, 50, window)  
    maze.create_cells()


    window.wait_for_close()

if __name__ == '__main__':
    main()
