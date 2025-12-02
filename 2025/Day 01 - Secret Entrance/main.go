package main

import (
	"bufio"
	"container/ring"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func main() {

	// exampleInputRaw := `L68
	// L30
	// R48
	// L5
	// R60
	// L55
	// L1
	// L99
	// R14
	// L82
	// 	`
	// lines := strings.Split(strings.TrimSpace(exampleInputRaw), "\n")
	lines, err := readLines("input.txt")

	if err != nil {
		panic("Canot read input data...")
	}

	r := ring.New(100)
	n := r.Len()

	for i := 0; i < n; i++ {
		r.Value = i
		r = r.Next()
	}

	counter := 0
	currPos := 50
	r = r.Move(currPos)
	v := r.Value.(int)

	for i := range len(lines) {
		line := strings.TrimSpace(string(lines[i]))

		// get direction and move
		direction := string([]rune(line)[0])
		moveStr := line[1:]
		move, err := strconv.Atoi(moveStr)
		if err != nil {
			fmt.Printf("Error converting distance '%s' to int: %v. Skipping line.\n", moveStr, err)
			continue
		}

		// make negative if moving left
		if direction == "L" {
			move = -(move)
		}

		// move ring
		r = r.Move(move)
		v = r.Value.(int)

		// count if 0
		if v == 0 {
			counter += 1
		}
	}

	fmt.Println(counter)
}
