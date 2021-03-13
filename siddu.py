def fun(d,n):
    s = 0
    a = sorted(d.values())
    # print(a)
    # for i in sorted(d.values()):
    #   print(i)
    #  s+=i
    # print(s)
    min1 = 99999999
    i = 0
    j = 3
    while (i <= (len(a) - 3) and j < len(a)):
        if (abs(a[i] - a[j]) <= min1):
            l = []
            min1 = abs(a[i] - a[j])
            p = i
            q = j
        i += 1
        j += 1
    # print(a[p:q+1])
    res = {}
    for i in d.keys():
        if d[i] in a[p:q + 1]:
            res[i] = d[i]
    print(str(res), min1)
    # s="Here the goodies that are selected for distribution are:"+"\n"+str(res)+"\n"+"And the diffrenece between the chossen goodie with highest price and the lowest price is"+str(min1)
    # print(s)
    x=[]
    x.append(res)
    x.append(min1)
    return x

def display(d,diff):
    s = "The goodies selected for distribution are:" + "\n" + "\n"
    for i in d:
        s += i + ": " + str(d[i]) + "\n"
    s += "\n" + "And the difference between the chosen goodie with highest price and the lowest price is " +str(diff)
    f=open("sample_output.txt","w")
    f.write(s)
    f.close()


myfile = open("sample_input.txt","r") #Opening file
a1=myfile.readline()
n=int(a1[21]) #Number of emloyees
a1=myfile.readline()
a1=myfile.readline()
a1=myfile.readline()

d={} #Extracting input values from file to dictionary
for i in range(10):
    a1=myfile.readline()
    a=a1.split(": ")
    d[a[0]]=int(a[1])
x=fun(d,n)
d=x[0]
diff=x[1]
display(d,diff)
