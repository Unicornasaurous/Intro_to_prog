from tkinter import *
#root class
root = Tk()
#app title
root.title("Rectangle Compare")
#window size
root.geometry("800x800")

#Dictates how large the rectangles can appear visually
#Works best at sizes between 200-300
MAX_RECT_SIZE = 300

#Creates title label
title = Label(root, text="Rectangle Compare\nBy TJ", font=20)

#Places title
title.grid(column=1, row=0, pady=50)
#Creating canvases for rectangles
rectangle1 = Canvas(root, height=MAX_RECT_SIZE, width=MAX_RECT_SIZE)
rectangle2 = Canvas(root, height=MAX_RECT_SIZE, width=MAX_RECT_SIZE)
#Placing canvases in root via grid style
rectangle1.grid(column=0, row=1, padx="10", pady="25")
rectangle2.grid(column=2, row=1, padx="10", pady="25")
#creates labels for entries
rectangle_label1 = Label(root, text="Rectangle 1")
rectangle_label2 = Label(root, text="Rectangle 2")
#places rectangle labels about entries
rectangle_label1.grid(column=0, row=2)
rectangle_label2.grid(column=2, row=2)
#creates entry widgets for rectangles
width1 = Entry(root)
width1.insert(0, "width")
width1.bind("<FocusIn>", lambda args: width1.delete(0, END))
height1 = Entry(root)
height1.insert(0, "height")
height1.bind("<FocusIn>", lambda args: height1.delete(0, END))
width2 = Entry(root)
width2.insert(0, "width")
width2.bind("<FocusIn>", lambda args: width2.delete(0, END))
height2 = Entry(root)
height2.insert(0, "height")
height2.bind("<FocusIn>", lambda args: height2.delete(0, END))
#places entries below canvases
width1.grid(column=0, row=3)
height1.grid(column=0, row=4)
width2.grid(column=2, row=3)
height2.grid(column=2, row=4)

#Creates the rectangles based on what the user enters
#Scales the rectangles down in order to fit within the app and be comparable to each other
def createRectangles():
    #Deletes all the items within the two canvases(rectangle1 and rectangle2)
    rectangle1.delete("all")
    rectangle2.delete("all")
    #Aquires the data from the Entry widgets width1-2 and height1-2
    try:
        w1 = float(width1.get()) 
        h1 = float(height1.get())
    except ValueError:
        rectangle1.create_text(MAX_RECT_SIZE/2, MAX_RECT_SIZE-15, text="Hint: Try entering a number")
    try:
        w2 = float(width2.get())
        h2 = float(height2.get())
    except ValueError:
        rectangle2.create_text(MAX_RECT_SIZE/2, MAX_RECT_SIZE-15, text="Hint: Try entering a number")
    #calculates the area of both rectangles
    try:    
        area1 = w1 * h1
        area2 = w2 * h2
        #list of sides
        dimensionList = [w1, h1, w2, h2]
        #Logic behind visual indication of bigger rectangle
        if area1 > area2:
            color1 = "blue"
            color2 = "black"
            thickness1 = 4
            thickness2 = 1
            rectangle1.create_text(MAX_RECT_SIZE/2, MAX_RECT_SIZE-285, text="This one is bigger!")
        elif area1 == area2:
            color1 = "purple"
            color2 = "purple"
            thickness1 = 4
            thickness2 = 4
            rectangle1.create_text(MAX_RECT_SIZE/2, MAX_RECT_SIZE-285, text="They are equal!")
            rectangle2.create_text(MAX_RECT_SIZE/2, MAX_RECT_SIZE-285, text="They are equal!")
        else:
            color1 = "black"
            color2 = "blue"
            thickness1 = 1
            thickness2 = 4
            rectangle2.create_text(MAX_RECT_SIZE/2, MAX_RECT_SIZE-285, text="This one is bigger!")
        #double for loop determines largest side out of all sides within dimensionList
        #for each number in the list, it compares that number to each other number.
        #Each time said number is found to be either larger or equal to another number,
        #1 is added to the counter for that iterance. If the counter is found to be equivalent to the number of
        #numbers in the list, then that number is assigned to biggestSide
        #Note that the >= operator is used in case two largest numbers are equal
        for i in dimensionList:
            counter = 0
            for p in dimensionList:
                if i >= p:
                    counter += 1
                else: 
                    pass
                if counter == len(dimensionList):
                    biggestSide = i
                else:
                    pass
        #For each side in dimensionList, the side 'side' is scaled down 
        #and limited by MAX_RECT_SIZE - 130 and then reassigned to its 
        #index in dimensionList
        index = -1
        for side in dimensionList:
            index += 1
            dimensionList[index] = (MAX_RECT_SIZE - 130) * (side / biggestSide)
        #determines the coordinates for the rectangles from the scaled down sides
        # and assigns them to their own variable 
        # Example: x1_r1 is the first x coordinate of the first rectangle
        x1_r1 = (MAX_RECT_SIZE / 2) - (dimensionList[0] / 2)
        y1_r1 = (MAX_RECT_SIZE / 2) + (dimensionList[1] / 2)
        x2_r1 = (MAX_RECT_SIZE / 2) + (dimensionList[0] / 2)
        y2_r1 = (MAX_RECT_SIZE / 2) - (dimensionList[1] / 2)
        x1_r2 = (MAX_RECT_SIZE / 2) - (dimensionList[2] / 2)
        y1_r2 = (MAX_RECT_SIZE / 2) + (dimensionList[3] / 2)
        x2_r2 = (MAX_RECT_SIZE / 2) + (dimensionList[2] / 2)
        y2_r2 = (MAX_RECT_SIZE / 2) - (dimensionList[3] / 2)
        #creates rectangles along with all the related labels
        rectangle1.create_rectangle(x1_r1, y1_r1, x2_r1, y2_r1, outline=color1, width = thickness1)
        rectangle2.create_rectangle(x1_r2, y1_r2, x2_r2, y2_r2, outline=color2, width = thickness2)
        rectangle1.create_line(MAX_RECT_SIZE/2, MAX_RECT_SIZE/2, MAX_RECT_SIZE-50, int(MAX_RECT_SIZE*0.533))
        rectangle2.create_line(MAX_RECT_SIZE/2, MAX_RECT_SIZE/2, 50, int(MAX_RECT_SIZE*0.533))
        rectangle1.create_text(MAX_RECT_SIZE-30, int(MAX_RECT_SIZE*0.566), text=area1)
        rectangle2.create_text(30, int(MAX_RECT_SIZE*0.566), text=area2)
        rectangle1.create_text(x1_r1 + (dimensionList[0] / 2), y1_r1 + 20, text=w1)
        rectangle1.create_text(x1_r1 - 30, y1_r1 - (dimensionList[1] / 2), text=h1)
        rectangle2.create_text(x1_r2 + (dimensionList[2] / 2), y1_r2 + 20, text=w2)
        rectangle2.create_text(x2_r2 + 30, y2_r2 + (dimensionList[3] / 2), text=h2)
    except UnboundLocalError:
        pass

#creates button for submitting widths and heights
submitbtn = Button(root, text="Submit", command=createRectangles, font=15)
#places submit button
submitbtn.grid(column=1, row=5, pady=50)
#initiates main loop for tkinter framework
root.mainloop()