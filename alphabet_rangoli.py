#https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    # your code goes here

    n = size
    alpha = list(map(chr,range(97,123)))

    x = alpha[n-1::-1] + alpha[1:n]
    width = len('-'.join(x))

    for i in range(1,n):
        print('-'.join(alpha[n-1:n-i:-1] + alpha[n-i:n]).center(width,'-'))

    for i in range(n,0,-1):
        print('-'.join(alpha[n-1:n-i:-1] + alpha[n-i:n]).center(width,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
