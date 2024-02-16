import sys

def deafault():
    print('hello')

def cat():
    print('meow')
def main():
    if sys.argv[1]=='cat':
        cat()
    else:
        default()

if __name__=='__main__':
    main()
