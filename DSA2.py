def create set(): 
my set (l 
choice 
while(choicelOl 'y ) 
print('lXn Enter the number: ") 
num int(input()) 
my set. append(num) 
print('lXn Do you want to enter more number?(y/n)") 
choice input(); 
return my set 
def Add Element(A,num): 
print(llXn Enter the position at which you want to insert the element: 
pos int(input()) 
for i in range(len(A)): 
if(i— —pos): 
AZ Al:posl + Inuml + Alpos:l 
print(A) 
def Remove Element(A,num): 
count—O 
for i in range(len(A)): 
if(AIil —num): 
count: count + 1 
if(count» 1): 
pos —A. index(num) 
new A Al:posl+Alpos+ 
print(new A) 
else: 
print(llelement not found in array") 
def Union Function(setA, setB): 
C i for i in setA + 
print(IlUnion set: Il,C) 
def Intersection Function(setA, setB): 