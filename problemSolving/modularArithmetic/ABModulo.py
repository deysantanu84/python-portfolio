# Given two integers A and B, find the greatest possible positive M, such that A % M = B % M.
# 1 <= A, B <= 10^9
# A != B
def modulo(A, B):
    high = max(A, B)
    low = min(A, B)
    for i in range(high - low, 0, -1):
        if A % i == B % i:
            return i


print(modulo(1, 2))  # 1
print(modulo(5, 10))  # 5
print(modulo(106978, 4487506))  # 4380528
print(modulo(8093192, 337391))  # 7755801
print(modulo(6795772, 4741741))  # 2054031
