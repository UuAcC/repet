f = open('27_A.txt')
n = int(f.readline())
nums = list(map(int, f.readlines()[:n]))
m, ms = float('inf'), 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        s = sum(nums[i:j + 1])
        if s % 89 == 0 and s > ms:
            ms, m = s, j - i + 1
        if s % 89 == 0 and s == ms:
            m = min(m, j - i + 1)
print(m)
