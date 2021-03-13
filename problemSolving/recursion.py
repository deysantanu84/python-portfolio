def bar(x, y):
    print("INSIDE BAR: x=%d\ty=%d" % (x, y))
    if y == 0:
        return 0
    result = x + bar(x, y - 1)
    print("BAR RESULT: %d" % result)
    return result


def foo(x, y):
    print("INSIDE FOO: x=%d\ty=%d" % (x, y))
    if y == 0:
        return 1
    result = bar(x, foo(x, y-1))
    print("FOO RESULT: %d" % result)
    return result


if __name__ == '__main__':
    print(foo(3, 5))
