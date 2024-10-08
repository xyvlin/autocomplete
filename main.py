#user interface 
from word import Node
from tree import *

def menu():
    print("\nChoose an option:")
    print("1. Add new word ")
    print("2. Search for a word")
    print("3. Autocomplete")
    print("4. display all words")
    print("5. exit the system")

def ask():
    while True:
        try:
            n = int(input("> "))
            assert(1<=n<=5)
            break
        except:
            print("error. please input a valid choice")
    return n

print("AUTOCOMPLETE SYSTEM")
start = None
while True:
    menu()
    choice = ask()
    if choice==1:
        s = input("Enter the new word or a list of words separated by space: ")
        l = s.split(" ")
        for w in l:
            start = insert(start,w)
        print(l,"has been added to the system.")
    elif choice==2:
        result = search(start,input("Enter the word: "))
        if result:
            print(result.word,"is in the system")
        else:
            print("this word is not in the system")
    elif choice==3:
        pre = input("Enter the prefix: ")
        print(traversal(start,pre))
    elif choice==4:
        print(traversal(start))
    else:
        break

"""
Welcome to the Autocomplete System!
Choose an option:
1. Insert a word
2. Search for a word
3. Autocomplete a word
4. Exit

> 1
Enter a word to insert: banana
Word "banana" has been inserted.

> 1
Enter a word to insert: apple
Word "apple" has been inserted.

> 3
Enter a prefix: app
Suggestions: ['apple', 'application', 'apply']

"""