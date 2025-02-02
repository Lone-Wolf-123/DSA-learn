def nStarTriangle(n: int) -> None:
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")

        for j in range(2 * i + 1):
            print("*", end="")

        for j in range(n - i - 1):
            print(" ", end="")
        print()


def nReverseTrianlge(n: int) -> None:
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(2 * (n - i) - 1):
            print("*", end="")
        for j in range(i):
            print(" ", end="")
        print()


def exapmleEnueration() -> None:
    person = {"name": "John", "age": None}
    person_dict = {k: v for k, v in person.items() if v is not None}
    print(person_dict)  # {'name': 'John'}


def nNumberTriangle(n: int) -> None:
    for i in range(n):
        for j in range(n - i):
            print(j + 1, end="")
        print()


def nZeroOneTriangle(n: int) -> None:
    li = [1, 0]
    counter = 0
    for i in range(n):
        for j in range(i + 1):
            print(li[counter % 2], end=" ")
            counter += 1
        print()


def nAlphabetTriangle(n: int, s: str) -> None:
    s = ord(s)
    for i in range(n):
        for j in range(i + 1):
            print(chr(s + j), end=" ")

        print()


# logic for this is to check min for a cell with it's mirror cell in vertical and horizontal direction
def nNumberBoxSquare(n: int) -> None:
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            top, bottom, left, right = i, 2 * n - 2 - i, j, 2 * n - 2 - j
            print(n - min(min(top, bottom), min(left, right)), end="")
        print()


if __name__ == "__main__":
    n = 3

    # nStarTriangle(n)
    # nReverseTrianlge(n)
    # exapmleEnueration()
    # nNumberTriangle(n)
    # nZeroOneTriangle(n)
    # nAlphabetTriangle(n,"A")
    nNumberBoxSquare(n)
