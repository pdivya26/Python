import array as arr

l = []
while(1):
    n = int(input("Enter no. of elements here : \n"))

    for i in range(n):
        e = int(input("Enter element here : "))
        l.append(e)

    a = arr.array('i', l)

    k = int(input("Enter element to find here : "))

    def search(k):
        c = 0
        for i in a:
            if(i == k):
                print("Element found at index :",c)
                break
            c += 1
        else:
                print("Element not found")   
    search(k)
