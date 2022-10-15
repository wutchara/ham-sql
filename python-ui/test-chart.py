from tkinter import *
import argparse
import sys
import os
import numpy as np
import mysql.connector
import matplotlib.pyplot as plt
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


# Create the parser
my_parser = argparse.ArgumentParser(description='List of parameters')

# Add the arguments
my_parser.add_argument('--phd',
                       type=int,
                       help='the phd value', required=True)
my_parser.add_argument('--hddsn',
                       type=str,
                       help='the hddsn value', required=True)

# Execute the parse_args() method
args = my_parser.parse_args()


def getDisplayColumns():
    return ['avermrval_0', 'avermrval_1']


def exitError(message, code):
    print(message)
    exit(code)


def readFile(fileName):
    try:
        file1 = open(getFilePath() + "/" + fileName, "r+")
        # print("Output of Read function is ")
        # print(file1.read())

        rows = file1.read().split('\n')
        print("Rows count: ", len(rows))
        dataRows = rows[1:]
        print("Data Rows count: ", len(dataRows))
        headerRow = rows[0].split(',')
        print("Header Rows", headerRow)

        # Modify rows
        rows = []
        for i in range(len(dataRows)):
            row = dataRows[i]
            columns = row.split(',')
            rows.append(columns)

        print("Rows", len(rows), rows[0])
        print("Header Index 'avermrval_0'", headerRow.index(
            'avermrval_0'), rows[0][headerRow.index('avermrval_0')])

        result = {}
        headerLen = len(headerRow)
        for i in range(headerLen):
            headerName = headerRow[i]
            column = []

            for val in rows:
                if len(val) == headerLen:
                    column.append(val[i])

            result[headerName] = column
            result['Index'] = range(1, len(column) + 1)

        return result, headerRow
    except:
        exitError("File not found: " + fileName, 2)

# plot function is created for
# plotting the graph in
# tkinter window


def convertToInt(strArr):
    return [int(x) for x in strArr]


def getFileName(args):
    return args.hddsn + "-phd-" + str(args.phd) + ".csv"


def getFilePath():
    return "./data/temp"


def plot(args, chartSize):
    fileName = getFileName(args)
    print("Try to read file: ", fileName)
    result, headers = readFile(fileName)
    displayColumns = getDisplayColumns()

    # the figure that will contain the plot
    figure = Figure(figsize=chartSize,
                    dpi=100)

    # adding the subplot
    plot1 = figure.add_subplot()

    x = result['Index']
    y = []

    for columnName in displayColumns:
        # Convert to number type
        result[columnName] = convertToInt(result[columnName])
        y = y + result[columnName]

    y = np.array(y)

    # plotting the graph
    for columnName in displayColumns:
        plot1.plot(x, result[columnName], label=columnName)

    plot1.legend()
    plot1.set_yticks(np.arange(y.min(), y.max(), 10))
    plot1.set_title(fileName)
    plot1.grid()

    # X = np.arange(0, math.pi*2, 0.05)
    # Y1 = np.sin(X)
    # Y2 = np.cos(X)
    # Y3 = np.tan(X)
    # Y4 = np.tanh(X)
    # figure, axis = plt.subplots(2, 2)

    # # For Sine Function
    # axis[0, 0].plot(X, Y1)
    # axis[0, 0].set_title("Sine Function")

    # # For Cosine Function
    # axis[0, 1].plot(X, Y2)
    # axis[0, 1].set_title("Cosine Function")

    # # For Tangent Function
    # axis[1, 0].plot(X, Y3)
    # axis[1, 0].set_title("Tangent Function")

    # # For Tanh Function
    # axis[1, 1].plot(X, Y4)
    # axis[1, 1].set_title("Tanh Function")

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(figure,
                               master=window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


def databaseConnectionError():
    exitError("Can't connect database, Please make sure your credentials", 3)


def connectDatabase():
    # TODO: move to args
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="db"
        )

        if not mydb.is_connected():
            databaseConnectionError()

        return mydb
    except:
        print("An exception occurred")
        databaseConnectionError()


def writeFile(fileName, contents):
    # create directory
    path = getFilePath()
    if not os.path.exists(path):
        os.makedirs(path)
        print("create new directory successfully")

    myFile = open(path + "/" + fileName, "w")
    myFile.write(contents)
    myFile.close()
    print("create/overwrite new file successfully: " + path + "/" + fileName)


def readDatabaseData(mydb, args):
    columns = ["phd", "subqualifier", "avermrval_0",
               "avermrval_1", "procid", "drivetemp"]

    query = "SELECT {} FROM ccb_ci_rmr WHERE hddsn='{}' AND phd={}".format(
        ",".join(columns), args.hddsn, args.phd)
    print("query:", query)
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    # Generate string file
    strRows = [",".join(columns)]
    for x in myresult:
        strRows.append(",".join(str(v) for v in x))

    writeFile(getFileName(args), "\n".join(strRows))


def validatePHD(args):
    # [0, 17]
    if args.phd not in range(0, 18):
        exitError("PHD out of range", 1)


# the main Tkinter window
window = Tk()

# setting the title
window.title('Krittiya\'s charts')

# dimensions of the main window
window.geometry("900x300")

# TODO: Refresh button
# button that displays the plot
# plot_button = Button(master = window,
#                      command = plot,
#                      height = 2,
#                      width = 10,
#                      text = "Plot")

# place the button
# exit_button = Button(window, text="Exit", command=window.quit)
# exit_button.pack(pady=20)


# print('======sys.argv', sys.argv)
# args = getArguments(sys.argv[1:])
print('args', args)
print('args.phd', args.phd)
print('args.hddsn', args.hddsn)
validatePHD(args)

myDatabaseConnection = connectDatabase()
readDatabaseData(myDatabaseConnection, args)

# in main window
# plot_button.pack()
plot(args, (300, 100))

# run the gui
window.mainloop()
exitError(".............................Finished.............................", 0)
