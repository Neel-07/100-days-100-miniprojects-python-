import os

def generate_tree(dir_path, indent=''):
    print(indent + os.path.basename(dir_path) + '/')
    indent += '    '
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            generate_tree(item_path, indent)
        else:
            print(indent + item)

if __name__ == "__main__":
    path = input("Enter the directory path: ")
    generate_tree(path)
