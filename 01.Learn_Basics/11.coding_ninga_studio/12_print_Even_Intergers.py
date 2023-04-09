def generateEvenNumbers(n: int) -> list:
    # Create an empty list

    ans = []
    for i in range(n + 1):
        if (i % 2 == 0):
            ans.append(i)

    return ans

