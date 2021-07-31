

text_file=open("SampleString.txt", 'r')
content=text_file.readlines()
print(content)

mymap={}

for line in content:
    firstline=line.split(" ")
    for word in firstline:
        mylist = [1]
        if(word in mymap):
            mymap[word]=mymap[word]+1
        else:
            mymap[word]=1


print(mymap)