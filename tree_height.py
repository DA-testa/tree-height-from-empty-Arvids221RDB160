import sys
import threading

def compute_height(n, parents):
    # izveido koku
    child1 = [[] for _ in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            child1[parent].append(i)

    def compute_depth(node):
        if not child1[node]:
            return 1
        max_depth = 0
        for child2 in child1[node]:
            depth = compute_depth(child2)
            max_depth = max(max_depth, depth)
        return max_depth + 1

    return compute_depth(root)

def main():
    input_type = input("Input type")
    if 'I' in input_type:
        temp = int(input())
        temp2 = list(map(int, input().split()))
        height = compute_height(temp, temp2)
        print(height)
    elif 'F' in input_type:
        filename = input()
        with open("test/" + filename, 'r') as file:
            temp = int(file.readline())
            temp2 = list(map(int, file.readline().split()))
            height = compute_height(temp, temp2)
            print(height+1)
    else:
        print("Invalid")
        exit()
    