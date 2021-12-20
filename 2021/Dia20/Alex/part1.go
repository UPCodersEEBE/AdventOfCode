package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func main() {
	// this will be useful later
	algo_steps := 2
	input_size := 100 // for this specific input, could be taken from the file but who cares
	padding := algo_steps + 1
	row_size := padding*2 + input_size
	grid_size := row_size * row_size

	file, err := os.Open("input.dat")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	// Save first line to rules
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	enhancement_algo := string(scanner.Text()[:])
	var rules []int
	for i := 0; i < len(enhancement_algo); i++ {
		if enhancement_algo[i] == '.' {
			rules = append(rules, 0)
		} else {
			rules = append(rules, 1)
		}
	}

	// skip one line per input shape
	scanner.Scan()

	// Convert to array of int
	grid := make([]int, grid_size)
	row := 0
	for scanner.Scan() {
		text := string(scanner.Text()[:])
		for i := 0; i < len(text); i++ {
			// some magic indexing, it works
			index := (row_size+1)*padding + row*row_size + i
			if text[i] == '.' {
				grid[index] = 0
			} else {
				grid[index] = 1
			}
		}
		row++
	}

	// loop through all points and do the magic
	for a := 0; a < algo_steps; a++ {
		new_grid := make([]int, grid_size)
		for i := 0; i < grid_size; i++ {
			isBorder := i < row_size || i > (row_size-1)*row_size || i%row_size == 0 || i%row_size == row_size-1
			array := ""
			if isBorder {
				// fuck it
				// Negating border since on infinite space all points are negated
				// with input algorithm (not with the example lol)
				new_grid[i] = int(math.Abs(float64(grid[i] - 1)))
			} else {
				for j := -1; j < 2; j++ {
					for k := -1; k < 2; k++ {
						array += strconv.Itoa(grid[i+k+j*row_size])
					}
				}
				array_dec, err := strconv.ParseInt(array, 2, 64)
				if err != nil {
					panic(err)
				}

				new_grid[i] = rules[array_dec]
			}
		}
		grid = new_grid
	}

	// Count ones
	tot := 0
	for i := 0; i < grid_size; i++ {
		tot += grid[i]
	}

	fmt.Println(tot)
}
