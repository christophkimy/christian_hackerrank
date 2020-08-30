#https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x ** 3

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []

    fibo = [0,1]
    if n <= 2:
        return fibo[:n]

    for x in range(2, n):
        fibo.append(fibo[x-2] + fibo[x-1])

    return fibo

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
