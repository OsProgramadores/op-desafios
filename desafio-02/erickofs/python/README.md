# Sieve of Eratosthenes Set

This is a Python program that uses the Sieve of Eratosthenes algorithm to generate prime numbers up to a specified limit. It also allows the user to specify the number of prime numbers to be displayed.

## Getting Started

To use this program, you will need to have Python installed on your computer. If you do not have Python installed, you can download it from the official website: https://www.python.org/downloads/

## Functionality

This program can calculate prime numbers from 1 to 1.000.000 (including) and only accepts numerical values/null as inputs. 

The __main__.py script is the entry point of the application. It calls the Sieve of Eratosthenes calculation procedures on module soecalc.py. 

The sieve_of_eratosthenes_set function takes the following steps:

1. Read the input values: the upper limit for calculating prime numbers and the number of prime numbers to display.
2. Initialize an empty set called primelist to store the prime numbers.
3. Add all numbers from 2 to the specified limit to the primelist set.
4. Iterate over the numbers in the primelist set and eliminate the multiples of each prime number.
5. Return the prime numbers from the primelist set, up to the specified number of prime numbers to display.
6. The function is then called within a for loop to print the generated prime numbers.

Below you can check program behavior based on the input:

### Errors

If user's input isn't accepted, error messages will be returned depending on the input:

- If limit/display range input is negative, returns error message: "Please enter a positive number." and circles back to user's input.
- If limit/display range input is greater than 1.000.000, rturns message: "The limit is too high. Please enter a number less than 1000000." and circles back to user's input.
- If limit/display range input is a string that can't be converted to a number, returns error message: "Invalid input. Please enter a valid number." and circles back to user's input.

### Non-integer acceptable inputs & 0 case

If user's input is a decimal or zero, program will behave as follows:

- If limit/display range input is zero, limit is set to 100 and display all prime numbers from 1 to it.
- If limit/display range input is null, limit is set to 100 and display all prime numbers from 1 to it.
- If limit/display range input is decimal, converts to closest integer and performs calculations. If convertion result is zero, follows input zero behavior.

## Running the Program

After you have installed Python, you can run the program by executing the following command in your terminal:

```
python __main__.py
```
The program will prompt you to enter the calculation limit and the number of prime numbers to be displayed. If you want to display all prime numbers, simply enter 0 for the second input.

For example:

```
Enter the calculation limit: 100
Enter the number of prime numbers to be displayed (0 = all): 0
```

This will display all prime numbers up to 100.

## Output
The output of the program will be the prime numbers up to the specified limit, printed one per line.

For example:

```
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
```

This output represents all prime numbers up to 100.