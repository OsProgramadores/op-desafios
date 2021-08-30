package main
import "fmt"
func primos(numero int)bool{
	for  divisor := 2 ;divisor <= numero/ 2; divisor++{
		if  numero % divisor==0{
			return false
}

}
	return numero != 1



}

func main(){
	for i := 1; i < 10000; i++{
		if primos(i){
			fmt.Println(i)

}
}
}
