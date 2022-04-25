from labs.lab12 import algorithms
from graphics import Rectangle, Point

# this is a mess, but just run the file.


def main():
    print("Testing is_in_binary algorithm:")
    print()
    lst = [-6, -5, -4, 9, 999, 1000, 1010, 2000]
    print("sorted list values:", lst)
    bool_1 = algorithms.is_in_binary(1010, lst)
    bool_2 = algorithms.is_in_binary(2000, lst)
    bool_3 = algorithms.is_in_binary(-6, lst)
    bool_4 = algorithms.is_in_binary(-1, lst)
    print("1010 in list:", bool_1)
    print("2000 in list:", bool_2)
    print("-6 in list:", bool_3)
    print("-1 in list:", bool_4)
    print()
    print()

    print("Testing selection_sort algorithm:")
    print()
    unsorted_lst = [999,  7, 88, 27, 38, 39, 901, 221, 704576, -1, -2, -3, -4, -5, 1, 2, 3, 4]
    print("list before sort:", unsorted_lst)
    new_lst = algorithms.selection_sort(unsorted_lst)
    print("sorted list:", new_lst)
    print()
    print()

    print("Testing rect_sort algorithm:")
    print()
    # worst case scenario. random points, out of order p1 and p2
    origin = Point(0, 0)
    rect_1 = Rectangle(origin, Point(20, 30))
    rect_2 = Rectangle(origin, Point(200, 300))
    rect_3 = Rectangle(origin, Point(50, 10))
    rect_4 = Rectangle(Point(200, 200), Point(250, 275))
    rectangles = [rect_1, rect_2, rect_3, rect_4]
    unsorted_areas = []
    for rect in rectangles:
        unsorted_areas.append(algorithms.calc_area(rect))

    print("unsorted rectangles:")
    for rect in rectangles:
        print(rect)
    print()

    print("corresponding unsorted areas:")
    for area in unsorted_areas:
        print(area)
    print()

    sorted_rectangles = algorithms.rect_sort(rectangles)
    sorted_areas = []
    for rect in sorted_rectangles:
        sorted_areas.append(algorithms.calc_area(rect))

    print("sorted rectangles:")
    for rect in sorted_rectangles:
        print(rect)
    print()

    print("corresponding sorted areas:")
    for area in sorted_areas:
        print(area)
    print()


if __name__ == '__main__':
    main()
