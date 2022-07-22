# use open function to read content of a file!
# f = open('/home/cyberboyayush/Documents/Python/Practise/Chapter 9/sample.txt', 'r')
with open('/home/cyberboyayush/Documents/Python/Practise/Chapter 9/sample.txt') as f:
    # data = f.read() # read full file
    data = f.read(5) #read only file letters in file
    print(data)