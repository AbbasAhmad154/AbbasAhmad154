print("hello, nothing")

a = 5.5
print(type (a))

#List
list1 = [1,2,3]
list2 = ["a", "b"]
print(list1, list2)

#Tuple
tuple_1 = (1,2,3)
print(tuple_1)

#Set
set1 = {1,2,3}
print(set1)

#Dictionary

student1 = { "name" : "Abbas Ahmad",
"Father name" : "Siraj Muhammad",
"age" : 22,
"married" : True,
"CGPA" : 3.5,
'Friends' : ["a", "b"],
"Address" : {
    "village" : "Showwand",
    "tehsil" : "Razzar",
    "District" : "Swabi"}
}
print(student1)
print(student1["Address"]["village"])

str_1 = ("5")
print(type(str_1))

a = 15
b = 45
print(a+b)
print(b-a)
print(a*b)
print(a/b)

str1 = "hello, this is"
str2 = "corvit"
str3 = str1 + str2
print(str3)

str4 = "This is Mardan"
print(str4)
str4[ :4]

list5 = [1,2]
list5.append(6)
print (list5)

list5.insert(3,8)
print(list5)

list6 = [1,2,3,4,5];
list6.pop(3)
print(list6)


color = ["red", "blue" , "white", "green"]
print(color)
fav1 = color[0]
fav2 = color[1]
print(fav1,fav2)


numbers= (1,2,3,4)
print(numbers)
fav1 = numbers[0]
fav2 = numbers[1]
print(fav1,fav2)


#Conditional Statements

#1
x = 5
y = 5
if x == y :
    print(x, "is equal to", y)

#2
a = 50
b = 60
if a>b:
    print("a is greater than b")    
else:
    print("b is greater than a")

#3
x = 3

if x == 0 :
    print(x, 'is equal to 0')    
elif x == 1 :
    print(x, 'is equal to 1')    
elif x == 2 :
    print(x, 'is equal to 2')    
else:
    print(x, 'is not equal to 0, 1, 2')
       
#4
#a = input ("Enter a number : ")
#a = int(a)
#print(a)

#5
a=2
b=3
if a==2:
    print(a)
elif b==3:
    print(b)
else:
    print("Sorry")
    
#6
"""age=int(input('Age: '))
if age>=18:
    education=int(input('Education: '))
    if education>=16:
        print("Yes you are allowed")
    else:
        print("Please improve your education")
else:
    print('You are under 18')"""
    
    
#for loop
"""list_a = [1,5,3,4]
for i in list_a:
    print(i)
    print(i+2)
    print(i*3)       
    print(i**2)"""

str1 = 'Python'
for a in str1:Are you currently interested in making a purchase? I have a variety of designs available in my catalog. If you'd like, I can share the link with you.
    print(a)
    
for i in range(5,100,10):
    print(i)
    
dist = {
'name': 'Abbas Ahmad',
'class_no': 17,
"village": "Showwand"
}
for k in dist:
   #print(k)
   #print(dist[k])
    print(k, ":", dist[k])
    
#While loop
count=0
while count<10:
    print(count)
    if count==7:
        break
    count += 1
    
#Function
def intro():
    print("Welcome to function topic")
intro()

