from threading import*
from time import sleep
class hello:
    def say(self):
        for i in range(5):
            print('hello')
            sleep(1)

class hi:
    def jan(self):
        for i in range(5):
            print('Hi')
            sleep(1)
obj1=hello()
obj2=hi()
t1=Thread(target=obj1.say,args=())
t2=Thread(target=obj2.jan,args=())
# t1=hello()
# t2=hi()

t1.start()
sleep(0.2)
t2.start()


# there it work better but sometime it print hellohi or hihello at same time
#that is mean collesion that the both tread are going to cpu at same time for preventing this we use a sleep between statring two tread

t1.join()
t2.join()
print('bye')
# there we have three threads 1 main thread , thread 1 and thread 2 there the main is printing between two other threads 
#if we want to first do other threads and in the final we do the main thread we use join
