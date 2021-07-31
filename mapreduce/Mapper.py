

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

mynewlist=[1]
for word in mylist:
    if word in mymap:
        print(f"inside the if {word}")
        mymap[word]=mymap[word].append(2)
    else:
        mymap[word]=mynewlist
       # print(mymap)

print(mymap)


