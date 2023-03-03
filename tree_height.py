#text = input()
#if text == "I":
    #n = int(input())
#else:
try:
    n = int(input())
except: 
    n = int(input())
parents = list(map(int, input().split()))

tree = [[] for _ in range(n)]
for child, parent in enumerate(parents):
    if parent == -1:
        root = child
    else:
        tree[parent].append(child)

stack = [(root, 0)]  # (node, depth)
depths = [0] * n
while stack:
    node, depth = stack.pop()
    depths[node] = depth
    for child in tree[node]:
        stack.append((child, depth+1))

height = max(depths)
print(height+1)