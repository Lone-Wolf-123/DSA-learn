import math


def countDigits(n: int) -> None:
    count = 0
    # while n > 0:
    #     n //= 10
    #     count += 1

    count = math.log10(n) + 1

    print(int(count))


def reverseNumber(n: int) -> None:
    # nstr = reversed(str(n))
    # for n in nstr:
    # 	if n == "0":
    # 		continue
    # 	print(n,end="")

    rev = 0

    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n //= 10

    print(rev)


def checkForPalindrome(n: int) -> bool:
    li = []
    p1, p2 = 0, -1
    while n > 0:
        li.append(n // 10)
        n //= 10
        p2 += 1

    for i in li[: int(len(li)) // 2]:
        if i != li[p1]:
            return False
        p2 -= 1

    print()
    return True


def GCD_brute(n1: int, n2: int) -> None:
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == n2 % i == 0:
            gcd = i

    print(gcd)


count: int = 0


def GCD_Euclidian(n1: int, n2: int) -> int:
    global count
    count += 1
    print(count)
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1

    else:
        maxNo = max(n1, n2)
        minNo = min(n1, n2)
        return GCD_Euclidian(maxNo % minNo, minNo)


def Armstrong_Number(n: int) -> bool:
    lenOfNumber = len(str(n))
    ans = 0
    for i in str(n):
        print(i)
        ans += int(i) ** lenOfNumber

    return ans.__eq__(n)


if __name__ == "__main__":
    n = 23432

    # countDigits(n)
    # reverseNumber(n)
    # ans = checkForPalindrome(n)
    # GCD_brute(20,16)
    # ans = GCD_Euclidian(2000, 12413560)
    ans = Armstrong_Number(200)
    print(f"{ans} : ans ")
