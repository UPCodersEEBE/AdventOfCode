package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("input.dat")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var tot int
	var ones []int
	a := 0

	for scanner.Scan() {
		text := string(scanner.Text()[:])
		if a == 0 {
			tot = len(text)
			ones = make([]int, tot)
		}
		for i := 0; i < tot; i++ {
			ones[i] += int(text[i]) - 48
		}
		a += 1
	}

	gamma := ""
	epsilon := ""
	for i := 0; i < tot; i++ {
		if ones[i] > (a / 2) {
			gamma += "1"
			epsilon += "0"
		} else {
			gamma += "0"
			epsilon += "1"
		}
	}

	gamma_dec, err := strconv.ParseInt(gamma, 2, 64)
	epsilon_dec, err := strconv.ParseInt(epsilon, 2, 64)
	if err != nil {
		panic(err)
	}

	fmt.Println(gamma_dec * epsilon_dec)
}
