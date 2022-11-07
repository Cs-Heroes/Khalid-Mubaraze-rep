from threading import Thread
from time import sleep

class test:
    def __init__(self,array):
        self.array=array

    
    def sum(self,array):
        res=0
        for i in array:
            res=res+i
            sleep(1)
        print(res)
    def sort(self,array):
        for i in range(0,len(array)):
            for j in range(i+1,len(array)):
                if array[i]>array[j]:
                    temp=array[i]
                    array[i]=array[j]
                    array[j]=temp
        sleep(1)
        print(array)



arr=[100,2,1,6,4,9,3,8,7]
obj=test(arr)

t1=Thread(target=obj.sum,args=(arr,))
sleep(1)
t2=Thread(target=obj.sort,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print('end of program')
        