package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	tot := 12
	o2 := ""
	co2 := ""
	var numbers []string

	file, err := os.Open("input.dat")
	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		numbers = append(numbers, scanner.Text())
	}

	for i := 0; i < tot; i++ {
		ones_o2 := 0
		ones_co2 := 0
		count_o2 := 0
		count_co2 := 0
		for j := 0; j < len(numbers); j++ {
			text := numbers[j]

			if text[0:i] == o2 {
				count_o2 += 1
				ones_o2 += int(text[i]) - 48
			}
			if text[0:i] == co2 {
				count_co2 += 1
				ones_co2 += int(text[i]) - 48
			}

		}

		if ones_o2*2 >= count_o2 {
			o2 += "1"
		} else {
			o2 += "0"
		}
		if count_co2 == 1 {
			co2 += strconv.FormatInt(int64(ones_co2), 10)
		} else {
			if ones_co2*2 < count_co2 {
				co2 += "1"
			} else {
				co2 += "0"

			}
		}
	}
	o2_dec, err := strconv.ParseInt(o2, 2, 64)
	co2_dec, err := strconv.ParseInt(co2, 2, 64)
	if err != nil {
		panic(err)
	}

	fmt.Println(o2_dec * co2_dec)
}
