#https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':

    list = []
    grade = []

    for i in range(int(input())):
        name = input()
        score = float(input())

        list.append([name,score])
        grade.append(score)

    list.sort()
    low_score = sorted(set(grade))[1]

    for i in list:
        name = i[0]
        score = i[1]
        if score == low_score:
            print(name)
        
