#List_remove_append
input_list=['SAS', 'R', 'PYTHON', 'SPSS']
input_list.remove("SPSS")
input_list.append('SPARK')
print(input_list)

#String to List Conversion
input_str = 'I love Data Science & Python'
result_list=input_str.split("&")
print(result_list)

#List to String Conversion
list=['Pythons syntax is easy to learn', 'Pythons syntax is very clear']
text_char=" & "
print(text_char.join(list));

#Nested List
input_list = [['SAS','R'],['Tableau','SQL'],['Python','Java']]
print(input_list[2][0])

#It’s the time to disco
t = ("disco", 12, 4.5)
print(t[0][2])

#String Formatting
nametext=str(input())
print(nametext.lower().replace(" ","_"))

#String Palindrome
mystring=str(input())
copyofString=mystring
print(mystring[::-1])
if(mystring==copyofString):
    print(1)
else:
    print(0)

#ReverseWords
mysentence=str(input())
words=mysentence.split(" ")
finalsentence=""

for word in words:
    finalsentence=finalsentence+word[::-1]+' '

print(finalsentence)




