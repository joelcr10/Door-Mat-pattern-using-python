n, m = map(int, input("Enter row and colum: ").split())
SingleDot = "."
BinaryDot = ".."
line = "|"
dash = "-"

inc = 3
welcome = "WELCOME"
index = 0

li = []

for i in range(int(n/2)+1):
    numberOfDash = (m-inc)/2
    starting = numberOfDash+1
    numberOfLine = (2*i)+1
    string = ""
    for j in range(m):
        if int(n/2)==i:
            centerDash = (m-7)/2
            if(j<centerDash or j>=centerDash+7):
                string = string+dash
            else:
                string = string+welcome[index]
                index = index+1
        else:
            if j<numberOfDash or j>=numberOfDash+inc:
                string = string+dash
            elif j==numberOfDash or j==numberOfDash+inc-1:
                string = string+SingleDot
            else:
                if j == starting:
                    string = string+line
                    starting = starting+3
                else:
                    string = string+SingleDot
    inc = inc+6
    li.append(string)

    print(string)


for i in range(1,int(n/2)+1):
    print(li[int(n/2)-i])
