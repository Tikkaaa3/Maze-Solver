from tkinter import BOTH, Canvas, Tk


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("My Tkinter Window")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, line.point1, line.point2, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, point1, point2, fill_color="black"):
        canvas.create_line(
            point1.x, point1.y, point2.x, point2.y, fill=fill_color, width=2
        )
