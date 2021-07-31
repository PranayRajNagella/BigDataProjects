

myfile=open("SampleString.txt", 'r')
content=myfile.readlines()
print(content)
mytuple=()
mylist=[]
mymap={}

for line in content:
    firstline=line.split(" ")
    for word in firstline:
        print(f"{word}",1)
        mylist.append(word)

print(mylist)
