#File Handling
import os, sys

fn = input("Enter File Name here : ")

if os.path.isfile(fn):
    f = open(fn, '+a')
    #for single string
    
    #ip = input("Enter data to be entered here : ") 
    #f.write(ip)
    
    #for multiple strings
    print('Enter text (end with #) here : ')
    ip = ''
    while ip != '#':
        ip = input()
        if(ip != '#'):
            f.write(ip+"\n")

    print("\nFile Contents :\n")
    f = open(fn, 'r')
    op = f.read()
    print(op)

    l = w = c = 0
    for i in f:
        ln = i.split()
        print(i)

        l += 1        #no. of lines
        print('No. of Lines :', l)
        
        w += len(ln)  #no. of words
        print('No. of Words :', w)
        
        c +=len(i)    #no. of characters
        print('No. of Character :', c)
        
    f.close()
    
else:
    print(fn,"does not exists!")
    sys.exit()
