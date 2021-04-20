package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

func power(base float64, expo float64) (float64, float64, float64) {
	var power_of float64
	power_of = math.Pow(base, expo)
	return base, expo, power_of
}

func main() {
	now := time.Now()
	fmt.Println(now)
	n := 2548
	fmt.Printf("%X\n", n)

	//rune   Ex: var aRune rune = 'Z'. type rune = int32. Arune represent a Unicode code point. "U+X"
	//string   Ex : “management office”, “room 265”, `raw text`... implicitly encoded using UTF-8.
	//uint, uint8, uint16, uint32, uint64   Ex : 2445, 676, 0, 1,...
	//int, int8, int16, int32, int64   Ex : -1245, 65, 78,...
	//bool   Ex : true, false
	//float32, float64   Ex : 12.67
	//Go initialize the variable value to the default value of the type
	//var <name[, name2...]> [<type>] [= <expresion_list>]
	var password string
	fmt.Println(password)
	var roomNumber, floorNumber int
	fmt.Println(roomNumber, floorNumber)
	var occupancy = 12
	fmt.Println(occupancy)
	//Short variable declaration (only inside functions)
	roomNumber2, floorNumber2 := 154, 3
	fmt.Println(roomNumber2, floorNumber2)
	// Constants
	const version string = "1.3.1" // Typed constant
	const version2 = "1.3.2"       // Untyped constant
	fmt.Print(version + "\n")

	hotelName := "The Gopher Hotel"
	fmt.Println("Hotel " + hotelName)
	rand.Seed(time.Now().UTC().UnixNano())
	println(rand.Intn(100))

	// Operator	Signification
	// ==,    !=,    >,    >=,    <,    <=
	if version <= version2 {
		fmt.Print("True\n")
	} else {
		fmt.Println(false)
	}

	var f, g, h = power(12, 2)
	fmt.Printf("%0.2f %.0f %.2f", f, g, h)

}