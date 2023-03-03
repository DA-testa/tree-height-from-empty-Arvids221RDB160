import os

# Define a function to read input from the keyboard or a file
def read_input():
    # Ask the user whether they want to input from the keyboard or a file
    source = input("Enter 'I' to input from keyboard or 'F' to input from a file: ")
    
    if source.upper() == 'I':
        # Read input from the keyboard
        n = int(input().strip())
        parents = list(map(int, input().strip().split()))
    elif source.upper() == 'F':
        # Read input from a file
        filename = input("Enter the file name (without the .txt extension): ")
        # Check that the file name doesn't contain the letter 'a'
        if 'a' in filename.lower():
            print("File name contains the letter 'a'. Please choose a different name.")
            return None
        try:
            with open(os.path.join('folder', f"{filename}.txt"), 'r') as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
        except FileNotFoundError:
            print("File not found. Please check the file name and try again.")
            return None
    else:
        # Invalid input
        print("Invalid input. Please enter 'K' or 'F' to choose input source.")
        return None
    
    # Check that the input is valid
    if len(parents) != n:
        print("Invalid input. Number of parent nodes does not match the number of nodes.")
        return None
    
    return n, parents


# Define a function to compute the height of the tree
def compute_tree_height(n, parents):
    # Create a dictionary to store the children of each node
    children = {i: [] for i in range(n)}
    for i in range(n):
        if parents[i] != -1:
            children[parents[i]].append(i)
    
    # Define a recursive function to compute the height of a node
    def compute_height(node):
        if not children[node]:
            # Leaf node
            return 0
        else:
            # Compute the height of each child and take the maximum
            return 1 + max(compute_height(child) for child in children[node])
    
    # Compute the height of the root node
    return compute_height(parents.index(-1))


# Main program
input_data = read_input()
if input_data is not None:
    n, parents = input_data
    tree_height = compute_tree_height(n, parents)
    print(tree_height+1)
    