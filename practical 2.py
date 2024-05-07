class Set:
    def __init__(self, init_elements_count):
        self._s = []
        for i in range(init_elements_count):
            e = int(input("Enter Element {}: ".format(i + 1)))
            self.add(e)

    def get_set(self):
        return self._s

    def __str__(self):
        string = "\n{ "
        for i in range(len(self.get_set())):
            string = string + str(self.get_set()[i])
            if i != len(self.get_set()) - 1:
                string = string + " , "
        string = string + " }\n"
        return string

    def __len__(self):
        return len(self._s)

    def __contains__(self, e):
        return e in self._s

    def is_empty(self):
        return len(self._s) == 0

    def add(self, e):
        if e not in self:
            self._s.append(e)

    def remove(self, e):
        if e in self.get_set():
            self.get_set().remove(e)
        else:
            print("\nElement is not found")

    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.is_subset_of(setB)

    def is_subset_of(self, setB):
        for e in setB.get_set():
            if e not in self.get_set():
                return False
        return True

    def union(self, setB):
        new_set = self
        for e in setB:
            if e not in self.get_set():
                new_set.add(e)
        return new_set

    def intersect(self, setB):
        new_set = Set(0)
        for i in range(len(self.get_set())):
            for j in range(len(setB.get_set())):
                if self.get_set()[i] == setB.get_set()[j]:
                    new_set.add(self.get_set()[i])
        return new_set

    def difference(self, setB):
        new_set = Set(0)
        for e in self.get_set():
            if e not in setB.get_set():
                new_set.add(e)
        return new_set

    def __iter__(self):
        return iter(self._s)


def create_set():
    n = int(input("Enter number of Elements in set: "))
    s = Set(n)
    return s


choice = 0
print("Create Set A")
s1 = create_set()
print(str(s1))

while choice != 9:
    print("|-------------------|")
    print("| Menu              |")
    print("| 1. Add            |")
    print("| 2. Remove         |")
    print("| 3. Contains       |")
    print("| 4. Size           |")
    print("| 5. Intersection   |")
    print("| 6. Union          |")
    print("| 7. Difference     |")
    print("| 8. Subset         |")
    print("| 9. Exit           |")
    print("|-------------------|")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        e = int(input("Enter Number to Add: "))
        s1.add(e)
        print(str(s1))
    elif choice == 2:
        e = int(input("Enter Number to Remove: "))
        s1.remove(e)
        print(str(s1))
    elif choice == 3:
        e = int(input("Enter Number to Search: "))
        if e in s1:
            print("Number Present in Set")
        else:
            print("Number is not Present in Set")
        print(str(s1))
    elif choice == 4:
        print("Set Contains {} elements".format(len(s1)))
        print(str(s1))
    elif choice == 5:
        print("Create a Set B for doing Intersection Operation")
        s2 = create_set()
        s3 = s1.intersect(s2)
        print("Set A = " + str(s1))
        print("Set B = " + str(s2))
        print("Intersection = " + str(s3))
    elif choice == 6:
        print("Create a Set B for doing Union Operation")
        s2 = create_set()
        s3 = s1.union(s2)
        print("Set A = " + str(s1))
        print("Set B = " + str(s2))
        print("Union = " + str(s3))
    elif choice == 7:
        print("Create a Set B for calculating Set Difference")
        s2 = create_set()
        s3 = s1.difference(s2)
        print("Set A = " + str(s1))
        print("Set B = " + str(s2))
        print("Difference = " + str(s3))
    elif choice == 8:
        print("Create a Set B for checking Subset or not")
        s2 = create_set()
        is_subset = s1.is_subset_of(s2)
        print("Set A = " + str(s1))
        print("Set B = " + str(s2))
        if is_subset:
            print("Set B is the Subset of Set A")
        else:
            print("Set B is not a Subset of Set A")
    elif choice == 9:
        break
    else:
        print("\nPlease enter valid Choice between 1 to 8")