n = int(input())
a = list(map(int, input().split()))

num_swaps = 0

for i in range(n):
    swaps_this_round = 0
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swaps_this_round += 1
            num_swaps += 1
    if swaps_this_round == 0:
        break

print(f"Array is sorted in {num_swaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")
