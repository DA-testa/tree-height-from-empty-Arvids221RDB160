#text = input()
#if text == "I":
    #n = int(input())
#else:

n = input()
try:
    n=int(n)
except ValueError:
    n = int(input())
try:
    num = input()
    parents = list(map(int, num.split()))
    root=0
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
except EOFError:
    print("e "+height+1)