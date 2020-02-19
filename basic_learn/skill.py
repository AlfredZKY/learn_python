
from __future__ import print_function


def any_all():
    x = [True, False, True]
    if any(x):
        print("At leadst one True")

    if all(x):
        print("Not one False")

    if any(x) or not all(x):
        print("At least ont True and one False")


def my_zip():
    keys = ['a', 'b', 'c', 'd']
    vals = [1, 2, 3, 4]
    zips = zip(keys, vals)
    for key, val in zips:
        print(key, val)


if __name__ == '__main__':
    any_all()
    print("hello world")
    my_zip()
