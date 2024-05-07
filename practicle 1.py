size = int(input("Enter size of Hash Table : "))
array1 = [None] * size
array2 = [None] * size

def insert_LinearProbing(data):
    count = 0
    i = 0
    while count < size:
        value = (data + i) % size
        if array1[value] is None:
            array1[value] = data
            display_LinearProbing()
            print("Number of comparisons : ", count+1)
            return
        i += 1
        count += 1
    print("Hash table is full. Unable to insert.")

def insert_QuadraticProbing(data):
    count = 0
    i = 0
    while count < size:
        value = (data + i*i) % size
        if array2[value] is None:
            array2[value] = data
            display_QuadraticProbing()
            print("Number of comparisons : ", count+1)
            return
        i += 1
        count += 1
    print("Hash table is full. Unable to insert.")

def display_LinearProbing():
    print("Linear Probing: ")
    print(array1)

def display_QuadraticProbing():
    print("Quadratic Probing : ")
    print(array2)

def search1(data):
    count = 0
    i = 0
    while count < size:
        value = (data + i) % size
        if array1[value] == data:
            print("Telephone Number Found ")
            print("Number of Comparisons in Linear Probing are : ", count+1)
            return
        elif array1[value] is None:
            break
        i += 1
        count += 1
    print("Opps, Element Not Present")
    print("Number of Comparisons : ", count+1)

def search2(data):
    count = 0
    i = 0
    while count < size:
        value = (data + i*i) % size
        if array2[value] == data:
            print("Telephone number found ")
            print("Number of comparisons in Quadratic Probing are : ", count+1)
            return
        elif array2[value] is None:
            break
        i += 1
        count += 1
    print("No such Element Found")
    print("Number of comparisons : ", count+1)

while True:
    print("1. Insert    2. Search")
    choice = int(input("Enter Choice : "))
    if choice == 1:
        data1 = int(input("Enter Telephone Number : "))
        print("\n")
        insert_LinearProbing(data1)
        insert_QuadraticProbing(data1)
        print("\n")
    elif choice == 2:
        data1 = int(input("Enter Telephone Number : "))
        print("\n")
        search1(data1)
        search2(data1)
        print("\n")
