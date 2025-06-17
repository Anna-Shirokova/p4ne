from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('C:\\Users\\am.linnik\\Documents\\Python\\Программирование на Python\\data_analysis_lab.xlsx')

sheet = wb['Data']
colA = sheet['A'][1:]
colC = sheet['C'][1:]
colD = sheet['D'][1:]

def getvalue(x):
    return x.value

list_x = list(map(getvalue, colA))
list_y1 = list(map(getvalue, colC))
list_y2 = list(map(getvalue, colD))

pyplot.plot(list_x,list_y1)
pyplot.plot(list_x,list_y2)
pyplot.show()