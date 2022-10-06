import sys
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    input_data = sys.stdin.readline().split()
    data.append((int(input_data[0]), input_data[1]))
    
data = sorted(data, key = lambda age: age[0])
for i in data:
    print(i[0], i[1])
