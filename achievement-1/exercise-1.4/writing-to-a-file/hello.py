hello_file = open('hello.txt', 'w') 
hello_file.write('Hello World!')
hello_file.close()

hello_file = open('hello.txt', 'r') 
print(hello_file.read())