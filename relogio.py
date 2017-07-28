import tkinter
from time import strftime
rel = tkinter.Label()
rel['font'] = "Helvetica 120 bold"
rel['text'] = '15:56:49'
def tic():
	rel['text'] = strftime('%H:%M:%S')
def tac():
	tic():
	rel.after(1000, tac)
tac()