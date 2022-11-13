package main

import "fmt"
import "math"

func main() {
	for i := 1; i <= 10000; i++ {
		var primo bool = true;
		var raizQuadrada int = int(math.Floor(math.Sqrt(float64(i))));
		for j := 2; j <= raizQuadrada; j++ {
			if (i % j == 0) {
				primo = false;
				break;
			}
		}
		if (primo) {
			fmt.Println(i);
		}
	}
}
