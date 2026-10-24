n = int(input("Enter the number of integers: "))

nums = []

for i in range(n):
    nums.append(int(input()))

exist = [0] * (n + 1)

for i in range(n):
    x = nums[i]

    if 1 <= x <= n:
        exist[x] = 1

for i in range(1, n + 1):
    if exist[i] == 0:
        print(i)
        exit()

print(n + 1)