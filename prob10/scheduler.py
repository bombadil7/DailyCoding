# Problem 10
#This problem was asked by Apple.

#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import time
import threading

def schedule(f, n, *args):
    time.sleep(n)
    f(args)

def func(args=""):
    print("Function called", end="")
    for arg in args:
        print(arg, end=" ")
    print()

def main():
    time_sleep = 3
    thread = threading.Thread(target=schedule, args=(func, time_sleep, ". Good Job!", ))
    thread.start()
    print("Hi")

if __name__ == "__main__":
    main()