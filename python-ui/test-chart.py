from tkinter import *
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


def getDisplayColumns():
    return ['avermrval_0', 'avermrval_1']


def readFile(fileName):
    file1 = open("./data/" + fileName, "r+")
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
        result['Index'] = range(1, len(column) + 1)  # TODO:

    return result, headerRow

# plot function is created for
# plotting the graph in
# tkinter window


def convertToInt(strArr):
    return [int(x) for x in strArr]


def plot():
    result, headers = readFile("8LGSRWNN-phd-0.csv")
    displayColumns = getDisplayColumns()

    # the figure that will contain the plot
    fig = Figure(figsize=(100, 100),
                 dpi=100)

    # adding the subplot
    plot1 = fig.add_subplot()

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

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
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


# the main Tkinter window
window = Tk()

# setting the title
window.title('Plotting in Tkinter')

# dimensions of the main window
window.geometry("500x500")

# button that displays the plot
# plot_button = Button(master = window,
#                      command = plot,
#                      height = 2,
#                      width = 10,
#                      text = "Plot")

# place the button
# in main window
# plot_button.pack()
plot()

# run the gui
window.mainloop()
