# https://www.hackerrank.com/challenges/polar-coordinates/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import cmath

z = complex(input().strip())

print(cmath.polar(z)[0])
print(cmath.polar(z)[1])
