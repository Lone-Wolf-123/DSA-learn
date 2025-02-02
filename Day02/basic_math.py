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


def Divisiors_Of_Number(n: int) -> list:
    li = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            li.add(i)
            li.add(n // i)
    li.add(n)
    return li


def CheckForPrime(n: int) -> bool:
    """if 0 < n < 3:
        return True

    for i in range(2, n // 2):
        if n % i == 0:
            return False

    return True"""

    count = 0

    iterations = int(math.sqrt(n))

    for i in range(1, iterations):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1

    if count == 2:
        return True

    return False


def ArrayReversal(arr: list) -> list:
    ans = []

    for i in arr[::-1]:
        ans.append(i)
    return ans


def isPalindrome01(s: str) -> bool:
    s = "".join([c for c in s if c.isalpha()])
    s = s.lower()
    if s[0].isalpha():
        pass

    print(s)
    p1, p2 = 0, len(s) - 1
    while p1 < p2:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1

    return True


def isPalindrome02(s: str) -> bool:
    p1, p2 = 0, len(s) - 1

    while p1 < p2:
        if not s[p1].isalpha():
            p1 += 1
        elif not s[p2].isalpha():
            p2 -= 1
        elif s[p1].lower() == s[p2].lower():
            p1 += 1
            p2 -= 1
        else:
            return False

    return True

def fib(n: int) -> int:
    if n < 1:
        return n
    return fib(n-1) + fib(n-2)


def calFib(n : int, sum : int) -> int:
    if n == 0:
        return sum

    print(sum + n)
    print(n-1)

    return calFib(n-1, sum + n)


def freq_count(n: list) -> int:
    occurance = {}
    max_occuance = n[0]
    min_occurance = n[0]

    for ele in n:
        if ele in occurance:
            occurance[ele] += 1
        else:
            occurance[ele] = 1

        if occurance[min_occurance] >= occurance[ele]:
            min_occurance = ele
        elif occurance[max_occuance] < occurance[ele]:
            max_occuance = ele

    print(max_occuance , occurance[max_occuance] , ' :: ', min_occurance , occurance[min_occurance]       )

def selection_sort(n:list) -> list:
    for i in range(len(n)):
        least = i
        for j in range(i,len(n)):
            if n[j] < n[least]:
                least = j
        n[i], n[least] = n[least], n[i]

    return n


def bubble_sort(n : list) -> list:
    for i in range(len(n)-1,-1):
        for j in range(0, i):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n


def merge_sort(arr, le, r):
    if le >= r:
        return

    m = (le+r)//2
    merge_sort(arr, le, m)
    merge_sort(arr, m+1, r)

    merge(arr, le, m, r)

def merge(arr, l1, m, r):
    nl, nr = l1, m+1
    temp = []

    while nl <= m and nr <= r:

        if arr[nl] <= arr[nr]:
            temp.append(arr[nl])
            nl += 1

        else:
            temp.append(arr[nr])
            nr += 1

    while nl <= m:
        temp.append(arr[nl])
        nl += 1

    while nr <= r:
        temp.append(arr[nr])
        nr += 1

    print(temp)

    for i in range(l1,r+1):
        arr[i] = temp[i-l1]


if __name__ == "__main__":
    n = [41, 9, 9, 48, 11, 2, 11, 12, 28, 10, 15, 4, 16, 48]
    # n = ''.join(int(n.split()))
    ''' local funcs
    countDigits(n)
    reverseNumber(n)
    ans = checkForPalindrome(n)
    GCD_brute(20,16)
    ans = GCD_Euclidian(2000, 12413560)
    ans = Armstrong_Number(200)
    ans = Divisiors_Of_Number(n)
    ans = CheckForPrime(n)
    ans = ArrayReversal([1, 2 ,3 ,4])
    ans = isPalindrome01(n)
    ans = isPalindrome02(n)
    ans = fib(2)
    ans = freq_count(n)
    ans = selection_sort(n)
    ans = bubble_sort(n)
    '''

    ans = merge_sort(n, 0, len(n)-1)
    print(f"Result : {ans}")
