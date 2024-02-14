
def create_set():
    my_set = []
    choice = 'y'
    while(choice[0]=='y'):
        print("\n Enter the number: ")
        num = int(input())
        my_set.append(num)
        print("\n Do you want to enter more number?(y/n)")
        choice = input();
    return my_set

def Add_Element(A,num):
    print("\n Enter the position at which you want to insert the element: ") 
    pos = int(input())
    for i in range(len(A)):
        if(i== pos):
            A=A[:pos]+[num]+A[pos:]
    print(A)

def Remove_Element(A,num):
    count=0
    for i in range(len(A)):
        if(A[i]==num):
            count=count+1
    if(count >= 1):
        pos=A.index(num)
        new_A=A[:pos]+A[pos+1:]
        print(new_A)
    else:
        print("element not found in array")

def Union_Function(setA1, setB):
    C = list({i: i for i in setA1 + setB}.values()) 
    print("Union set: ",C)

def Intersection_Function(setA1, setB):
    C = [i for i in setA1 if i in setB] 
    print("Intersection set: ",C)

def Difference_Function(setA1, setB):
    C = [element for element in setA1 if element not in setB]   
    print("Difference set:",C)

def Contains_Element(A,num):
    found=False
    for i in range(len(A)):
        if(A[i]==num):
            found=True
            break
        else:
            found=False
    return found

def Size_of_Set(A):
    count=0
    for i in range(len(A)):
        count = count + 1
    return count

def Subset_Function(A1,B):
    status=False
    if(all(i in A1 for i in B)):
        status=True
    if(status):
        print("\n Yes, Subset exists")
    else:
        print("\n No, Subset does not exist")

#driver code
A = {}
print("\n Create set A")
A=create_set()
print("A = ",A)
while(True):
    print("Main Menu")
    print("1.Add an element to the set")
    print("2.Remove an element from the set") 
    print("3.Memebership of element")
    print("4.Size of Set")
    print("5.Union") 
    print("6.Intersection")
    print("7.Difference") 
    print("8.Check Subset") 
    print("9.Exit")
    print("Enter your choice") 
    choice = int(input())

    if choice == 1:
        print("A = ",A)
        print("Enter the element to be added in the set: ")
        num = int(input()) 
        Add_Element(A,num)

    elif choice == 2:
        print("A = ",A)
        print("Enter the element to be removed from the set: ")
        num = int(input())
        print(A)
        Remove_Element(A,num)

    elif choice == 3:
        print("A",A)
        print("Enter the element to be searched from the set: ") 
        num = int(input())
        if(Contains_Element(A,num)):
            print("\n The element is present in the set")
        else:
            print("\n The element is not present in the set")

    elif choice == 4:
        print("A = ",A)
        print("\n The size of the set is: ",Size_of_Set(A))

    elif choice == 5:
        A1 = {}
        print("\n Create set A")
        A1=create_set()
        B = {}
        print("\n Create set B")
        B = create_set()
        print("A = ",A1)
        print("B = ",B)
        Union_Function(A1,B)
        

    elif choice == 6:
        A1 = {}
        print("\n Create set A")
        A1=create_set()
        B = {}
        print("\n Create set B")
        B = create_set()
        print("A = ",A1)
        print("B = ",B)
        Intersection_Function(A1,B)

    elif choice == 7:
        A1 = {}
        print("\n Create set A")
        A1=create_set()
        B = {}
        print("\n Create set B")
        B = create_set()
        print("A = ",A1)
        print("B = ",B)
        Difference_Function(A1,B)
        
    elif choice==8:
        A1 = {}
        print("\n Create set A")
        A1=create_set()
        B = {}
        print("\n Create set B")
        B = create_set()
        print("A = ",A1)
        print("B = ",B)
        Subset_Function(A1,B)
    
    else:
        print("Exitting")
        break
