import sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for x in sys.stdin.readlines():
        print_hi(x.rstrip())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
