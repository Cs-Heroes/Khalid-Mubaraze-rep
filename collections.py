# collections in python are basically container data types ,normaly lists,sets,tuples,dictionary.
#list -> store multiple items in single variable it is ordered ,changeable,allow duplicate
from copy import copy
import this


mylist=['apple',3,'cherry']
print(mylist)
for i in mylist:
    print(i)
print(len(mylist))
print(type(mylist))
#list constructor
newlist=list(('ahmad','khan','khalid'))
print(newlist)
# access the item of list by index
print(mylist[2])
#negative mean -1 to last item -2 second last item
print(mylist[-1])
# range of indexex (2: from 2 untel end   , :3 from first to 3)
print(mylist[1:2])
#check if item exist in list
if 'apple' in mylist:
    print('yes the apple is exist in the list')

#insert items in list
mylist.insert(3,'khalidahmad')
print(mylist[3])

mylist.append('khalid')#append
print(mylist)


mylist.extend('khan') #extend
print(mylist)

#remove item from list
thislist=['apple','banana','cherry']
thislist.remove('banana')
print(thislist)


thislist.pop(1)  # remove specific index if we dont specify the index pop remove the last one
print(thislist)

del thislist[0] #also use del

# clear is use to empty the list
thislist.clear()
#loop in the list
listt=['khan','ahmad','khalid']
for i in listt:
    print(i)

#also in range
for i in range(len(listt)):
    print(listt[i])

#sorting list  accending
listt.append('jamal')
listt.sort()

print(listt)


num=[10,100,20,2,88]
num.sort()
print(num)

#decending sort
num.sort(reverse=True)
print(num)


#copy the list
mynewlist=num.copy()
print(mynewlist)

#joing list 

list3=num+mynewlist
print(list3)


#also we use the extend
num.extend(mynewlist)
print(num)


#----------------Tuple in python--------------
mytuple=('apple','banana','cherry')
print(mytuple)
 #tuple object
newtuple=tuple(('apple',))#one item tuple
print(newtuple)
print(type(newtuple))

#access the tuple items  note:tuple are unchangeanble and immutable
print(mytuple[2])
#if we want to change the tuple we should convert it to list
x=('apple','banana')
y=list(x)
y[1]='cherry'
x=tuple(y)
print(x)
#if we want to add ,remove item or append the tuple we should convert it to list after that change 
#the del delete the tuple completly
# thistuple=('khan','ahmad')
# del thistuple
# print(thistuple)

#join tuple
tuple1=('ahmad',)
tuple2=('khalid',)# (,)mean that the tuple has one item if we remove , it true a error
tuple3=tuple1+tuple2
print(tuple3)

#multiply the tuple
mytup=tuple1*3
print(mytup)
# tuple methods are count () and index()


#----------sets in python-----------------

myset={'apple','banana'}  # set is unordered,unchangable,dublicate not allowed
print(myset)
print(type(myset))
print('banana' in myset)

#add item in set
myset.add('orange')
print(myset)
#add item from one set to other
set1={'ahmad','khan'}
set2={'khallid','ali'}
set1.update(set2) # we can add every collection in set by apdate
print(set1)
lists=['ahmad','khan','jan']
set1.update(lists)
print(set1)
#remove set item
set1.remove('ali')# if the item to remove dose not exist it raise an error

set1.discard('khalid')# it not raise error when not exist

set1.pop()
print(set1)

set1.clear()
print(set1)# clear all items

del set1 #delete set completly

#join sets union
setone={'khan','jan'}
settwo={'ahmad','jan'}
set3=setone.union(settwo)
print(set3)
#set intersection common item
setone.intersection(settwo)
print(setone)

#-----------------dictionaries----------------------
mydic={'khalid':32, 'ahmad':33, 'khan':'jan'}
print(mydic)

print(mydic['ahmad'])
x=mydic.get('khalid')
print(x)
#get keys
x=mydic.keys()
print(x)
#get values
x=mydic.values()
print(x)
#change values in dic
thisdic={
    'year':1990,
    'model':'mustang',
}
thisdic['year']=2022
print(thisdic)
#also update
thisdic.update({'year':2021})
print(thisdic)

#add item to dic
thisdic['color']='red'
print(thisdic)


thisdic.update({'age':21})
print(thisdic)

#remove dic item
thisdic.pop('age')
print(thisdic)

thisdic.popitem()#it removes the last one
print(thisdic)

del thisdic['model']
#it also remove the dic complitly
print(thisdic)


thisdic.update({'model': 'benz', 'number':3})
for x in thisdic:# print the keys
    print(x)

#for valuse
for x in thisdic:
    print(thisdic[x])

#also
for x in thisdic.values():
    print(x)

for x,y in thisdic.items():#print both key and value
    print(x,y)

#copy dic
mydict=copy(thisdic)
print(mydict)

newdic=dict(thisdic)
print(newdic)

#nested dic
myfamily={
    'child1':{
       'name':'khalid',
       'year':30
    },
    'child2':{
        'name':'ahmad',
        'year':32
    }
}
print(myfamily)












































































































#tuple  which is ordered , unchangeable, allow dublicate
# set is unordered, unchangeable,no dublicate
#dictionary  ordered,changeable,no dublicate





