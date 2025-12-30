dict={}
def add_word():
    n=int(input("How many word you want to enter ? :"))
    for _ in range(n):
        word=input("Enter Word :")
        meaning=input(f"Enter Meaning Of {word} :")
        dict[word]=meaning
def search_word():
    word=input("Enter Word :")
    print()
    if word in dict:
        print(f"{word}->{dict[word]}")
    else:
        print("Word Is Not Exist In Dictionary")
def update_word():
    word=input("Enter Word :")
    meaning=input(f"Enter Meaning of {word} :")
    dict[word]=meaning
def delete_word():
    word=input("Enter Word :")
    if word in dict:
        del dict[word]
    else:
        print("Word Does Not Exist")
def display():
    for k,v in dict.items():
        print(f"{k}->{v}")
def exit():
    print("Thank You")
while True:
    print("\nSimple Dictionary App\n")
    print("1. Add Word")
    print("2. Search Word")
    print("3. Update Word")
    print("4. Delete Word")
    print("5. Display All Word")
    print("6. Exit")
    print()
    
    fun_num=int(input("Enter Number :"))
    print()
    
    if fun_num==1:
            add_word()
    elif fun_num==2:
            search_word()
    elif fun_num==3:
            update_word()
    elif fun_num==4:
            delete_word()
    elif fun_num==5:
            display()
    elif fun_num==6:
            exit()
            break




