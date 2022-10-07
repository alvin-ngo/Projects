
#from tkinter import N


fin = open('word.txt')

include = []
exclude = []

inc_0 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
inc_1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
inc_2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
inc_3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
inc_4 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
exc_0 = []
exc_1 = []
exc_2 = []
exc_3 = []
exc_4 = []

def list_include(): 
    incl_add = None
    while incl_add != '.':
        incl_add = input(f"valid letters: ")
        include.append(incl_add.strip())
    del include[len(include)-1]      
    return include


def list_exclude(): 
    excl_add = None
    while excl_add != '.':
        excl_add = input(f"invalid letters: ")
        exclude.append(excl_add.strip())
    del exclude[len(exclude)-1]
    return exclude


def index_input():
    print("Add valid indexed positions")
    index = int(input(f"Position?: "))
    letter = input(f"Letter?: ")
    if index == 1:
        inc_0.clear()
        inc_0.append(letter.strip())
    elif index == 2:
        inc_1.clear()
        inc_1.append(letter.strip())
    elif index == 3:
        inc_2.clear()
        inc_2.append(letter.strip())
    elif index == 4:
        inc_3.clear()
        inc_3.append(letter.strip())
    elif index == 5:
        inc_4.clear()
        inc_4.append(letter.strip())


def index_input_invalid():
    print("Add invalid indexed positions")
    index = int(input(f"Position?: "))
    letter = input(f"Letter?: ")
    if index == 1:
        exc_0.append(letter.strip())
    elif index == 2:
        exc_1.append(letter.strip())
    elif index == 3:
        exc_2.append(letter.strip())
    elif index == 4:
        exc_3.append(letter.strip())
    elif index == 5:
        exc_4.append(letter.strip())


def wordle(inc, exc):
    fin.seek(0) #loops fin back to the beginning of the word list
    for line in fin:
        word = line.strip() 
        if (
            all(words in word for words in inc) 
            and all(words not in word for words in exc)
            and len(word) == 5
            and word[0] not in exc_0
            and word[1] not in exc_1
            and word[2] not in exc_2
            and word[3] not in exc_3
            and word[4] not in exc_4
            and word[0] in inc_0
            and word[1] in inc_1
            and word[2] in inc_2
            and word[3] in inc_3
            and word[4] in inc_4
            ):
                print(word)

def main():
    print("Enter valid or invalid letters. Type '.' once complete \nEnter '+' or '-' to set valid or invalid positions")
    while True:
        status  = input(f"Continue? y/n: ")
        if status == 'y':
            wordle(list_include(), list_exclude())
        elif status == '+':
            index_input()
        elif status == '-':
            index_input_invalid()
        elif status == 'n':
            return False
main()