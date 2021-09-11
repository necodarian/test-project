def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    if b == 0:
        return None
    else:
        return a / b


def mul(a, b):
    return a * b


if __name__ == "__main__":
    print(f"addition of {3} and {5} is equal to {add(3, 5)}")
