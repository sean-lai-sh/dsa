def print_triangle(n):
    if not isinstance(n, int):
        raise TypeError("Invalid Input")
    if n <= 0:
        print("")
    if n == 1:
        print("*")
    else:
        print_triangle(n - 1)
        print("*" * n)


def print_oposite_triangles(n):
    if not isinstance(n, int):
        raise TypeError("Invalid Input")
    if n <= 0:
        print("")
    elif n == 1:
        print("*")
    else:
        print("*" * n)
        print_oposite_triangles(n - 1)


def print_ruler(n):
    if not isinstance(n, int) or n < 0:
        raise Exception("Invalid Input")
    if n == 0:
        print("")
    if n == 1:
        print("-")
    else:
        print_ruler(n - 1)
        print("-" * n)
        print_ruler(n - 1)
