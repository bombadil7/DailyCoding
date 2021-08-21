package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
)

const (
	filename = "tree.dat"
)

type node struct {
	val   string
	left  *node
	right *node
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func read_tree(f *os.File) (t []string, err error) {
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)

	var tokens []string

	for scanner.Scan() {
		tokens = append(tokens, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading input: ", err)
	}

	return tokens, err
}

func create_tree(tokens []string) (n *node, t []string) {
	if tokens[0] == "@" {
		return nil, tokens[1:]
	}

	new_node := &node{tokens[0],
		nil,
		nil}
	left, new_token := create_tree(tokens[1:])
	right, new_token := create_tree(new_token)

	new_node.left = left
	new_node.right = right

	return new_node, new_token
}

func print_tree_inorder(t *node) {
	if t == nil {
		return
	}

	if t.left != nil {
		print_tree_inorder(t.left)
	}

	fmt.Println(t.val)

	if t.right != nil {
		print_tree_inorder(t.right)
	}
}

func evaluate_tree(n *node) (f float64, err error) {
	if n.left == nil {
		return strconv.ParseFloat(n.val, 32)
	}

	left, err := evaluate_tree(n.left)
	check(err)
	right, err := evaluate_tree(n.right)
	check(err)

	switch n.val {
	case "+":
		return left + right, nil
	case "-":
		return left - right, nil
	case "*":
		return left * right, nil
	case "/":
		return left / right, nil
	default:
		return 0, errors.New("Invalid operation")
	}
}

func main() {
	f, err := os.Open(filename)
	check(err)

	tokens, err := read_tree(f)
	check(err)

	fmt.Println("Tree in file: ")
	for _, t := range tokens {
		fmt.Println(t)
	}

	tree, _ := create_tree(tokens)
	fmt.Println("Generated tree: ")
	print_tree_inorder(tree)

	val, err := evaluate_tree(tree)
	check(err)
	fmt.Printf("Calcualted value is %f\n", val)

}
