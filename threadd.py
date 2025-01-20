import time
import threading

def square(numbers):
    print("Square ")
    for i in numbers : 
        time.sleep(0.2)
        print("square " , i*i )

def cube(numbers):
    print("Cube")
    for i in numbers: 
        time.sleep(0.2)
        print("cube ", i*i*i)

arr =  [2,4,15,20]

t = time.time()

t1 = threading.Thread(target = square, args=(arr,))
t2 = threading.Thread(target= cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()


print("time taken ", time.time()-t)


