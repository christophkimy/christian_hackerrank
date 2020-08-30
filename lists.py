#https://www.hackerrank.com/challenges/python-lists/submissions/code/175776562

if __name__ == '__main__':
    N = int(input())

    a = []
    for i in range(N):
        S = input().split(" ")
        if S[0] == "insert":
            a.insert(int(S[1]), int(S[2]))
        elif S[0] == "print":
            print(a)
        elif S[0] == "remove":
            a.remove(int(S[1]))
        elif S[0] == "append":
            a.append(int(S[1]))
        elif S[0] == "sort":
            a.sort()
        elif S[0] == "pop":
            a.pop()
        elif S[0] == "reverse":
            a.reverse()


    


