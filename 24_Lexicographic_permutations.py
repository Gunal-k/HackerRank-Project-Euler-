import math

def nth_lex_permutation(s, n):
    chars = sorted(s)
    n -= 1
    result = ''
    while chars:
        f = math.factorial(len(chars) - 1)
        index = n // f
        if index >= len(chars):
            return "INVALID"
        result += chars.pop(index)
        n %= f
    return result

if __name__ == "__main__":
    s = "abcdefghijklm"
    T = int(input())
    for _ in range(T):
        n = int(input())
        total_perms = math.factorial(len(s))
        if n > total_perms or n < 1:
            print("INVALID")
        else:
            print(nth_lex_permutation(s, n))