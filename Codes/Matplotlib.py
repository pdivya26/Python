import matplotlib.pyplot as plt
import numpy as np

def line():
    w = np.linspace(0, 10, 100)
    x = np.sin(w)
    y = np.cos(w)
    plt.plot(w, x)
    plt.plot(w, y)
    plt.title('Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

def bar():
    x = ['A', 'B', 'C', 'D', 'E']
    y = [75, 90, 85, 63, 98]
    plt.bar(x, y)
    plt.title('Bar Plot')
    plt.xlabel('Students')
    plt.ylabel('Marks')
    plt.show()

def scatter():
    x = [64, 45, 52, 82, 70, 60, 76, 48]
    y = [170, 153, 160, 183, 166, 172, 168, 158]
    plt.scatter(x, y)
    plt.title('Scatter Plot')
    plt.xlabel('Weight (kg)')
    plt.ylabel('Height (cm)')
    plt.show()

def pie():
    p = [20, 30, 40, 10]
    l = ['Savings', 'EMIs', 'Essentials', 'Luxury']
    plt.pie(p, labels=l, autopct='%d%%')
    plt.title('Pie Chart')
    plt.axis('equal')
    plt.show()


while True:
    print("\nChoose a Plot :")
    print("1. Line Plot")
    print("2. Bar Plot")
    print("3. Scatter Plot")
    print("4. Pie Chart")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        line()
    elif choice == '2':
        bar()
    elif choice == '3':
        scatter()
    elif choice == '4':
        pie()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")
