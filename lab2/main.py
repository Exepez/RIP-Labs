from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle("синего", 6, 8)
    c = Circle("зеленого", 10)
    s = Square("желтого", 7)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()