package main

/* Problem 10
 * This problem was asked by Apple.

 * Implement a job scheduler which takes in a
 * function f and an integer n, and calls f after
 * n milliseconds
 */
import (
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup
var wg1 sync.WaitGroup

func main() {
	fmt.Println("Hello")
	wg.Add(1)
	go scheduler(myfunc, 800)

	wg.Wait()
	fmt.Println("All tasks finished")
}

func myfunc() {
	defer wg1.Done()
	fmt.Println("Function started")
}

func scheduler(f func(), n int) {
	defer wg.Done()

	fmt.Println("Scheduler started")
	wg1.Add(1)

	time.Sleep(time.Duration(n) * time.Millisecond)
	go f()
	wg1.Wait()
	fmt.Println("Scheduler finished")
}
