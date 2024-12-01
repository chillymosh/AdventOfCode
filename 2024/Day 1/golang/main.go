package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	data, err := os.ReadFile("../input.txt")
	if err != nil {
		panic(err)
	}

	var left, right []int
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")
	for _, line := range lines {
		parts := strings.Fields(line)
		l, _ := strconv.Atoi(parts[0])
		r, _ := strconv.Atoi(parts[1])
		left = append(left, l)
		right = append(right, r)
	}

	sort.Ints(left)
	sort.Ints(right)

	p1 := 0
	for i := 0; i < len(left); i++ {
		diff := left[i] - right[i]
		if diff < 0 {
			diff = -diff
		}
		p1 += diff
	}
	fmt.Println(p1)

	rightCount := make(map[int]int)
	for _, r := range right {
		rightCount[r]++
	}

	p2 := 0
	for _, l := range left {
		p2 += l * rightCount[l]
	}
	fmt.Println(p2)
}
