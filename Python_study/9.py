from tkinter import *
import random
from tkinter.messagebox import *
root = Tk()
root.title('Крестики Нолики')
root.geometry('300x295+620+180')
games=[]
choice = 0
combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
def new_game():
    global run_game, win, condition, games, button1
    if games!=[]:
        for i in range(3):
            for j in range(3): games[i][j].grid_forget()
        button1.grid_forget()
        games=[]
        return fig()
    run_game = True
    condition = [None] * 9
    win = None
    games = []
    root.columnconfigure(index=2,weight=50)
    for i in range(3):
        row = []
        for j in range(3):
            button = Button(root, text="", width=10, height=5, command=lambda row=i, col=j: click(row, col))
            button.grid(row=i, column=j,sticky='ew')
            row.append(button)
        games.append(row)
    button1 = Button(root,font='9', text="Новая игра", command=new_game)
    button1.grid(row = 3, column=0,columnspan=3, sticky='nswe')
    if choice == 0:bot_move()
def add_x(row, col):
    games[row][col]['text'] = 'X'
    games[row][col]['state'] = 'disabled'
def add_o(row, col):
    games[row][col]['text'] = 'O'
    games[row][col]['state'] = 'disabled'
def click(row, col):
    global choice
    if run_game:
        index = row * 3 + col
        if condition[index] is None:
            if choice == 1:
                condition[index] = 1
                add_x(row, col)
                if winner():
                    end_game()
                else:
                    bot_move()
                    if winner():
                        end_game()
            elif choice == 0:
                condition[index] = 0
                print(condition)
                add_o(row, col)
                if winner():end_game()
                else:
                    bot_move()
                    if winner():end_game()
    else:new_game()
def bot_move():
    index = None
    for i in combinations:
        variants = (([condition[i[0]], condition[i[1]], condition[i[2]]]))
        if variants.count(1-choice) == 2 and variants.count(None) == 1:
            index = i[variants.index(None)]
            break
    if index is None:
        for i in combinations:
            variants = (([condition[i[0]], condition[i[1]], condition[i[2]]]))
            if variants.count(choice) == 2 and variants.count(None) == 1:
                index = i[variants.index(None)]
                break
    if index is None:
        for i in combinations:
            variants = (([condition[i[0]], condition[i[1]], condition[i[2]]]))
            if variants.count(1-choice) == 1 and variants.count(None) == 2:
                index = i[variants.index(None)]
                break
    if index is None:
        if condition[4] is None:
            index = 4
    if index is None:
        empty_indexes = []
        for i in range(0, 9, 2):
            if condition[i] is None:
                empty_indexes.append(i)
        if empty_indexes:
            index = random.choice(empty_indexes)
    if index is None:
        empty_indexes = []
        for index, el in enumerate(condition):
            if el is None:
                empty_indexes.append(index)
        if empty_indexes:
            index = random.choice(empty_indexes)
    condition[index] = 1-choice
    row = index // 3
    col = index % 3
    if choice==0: add_x(row, col)
    else: add_o(row, col)
def winner():
    global win
    variants = []
    for i in combinations:variants.append([condition[i[0]], condition[i[1]], condition[i[2]]])
    if [choice] * 3 in variants:win = 'Ты ПОБЕДИЛ!'
    elif [1-choice] * 3 in variants:win = 'Бот Выиграл'
    elif None not in condition:win = 'Ничья'
    return win
def end_game():
    global run_game,games
    run_game = False
    for row in games:
        for button in row:button['state'] = 'disabled'
    showinfo("Игра окончена", win)
    for i in range(3):
        for j in range(3):games[i][j].grid_forget()
    button1.grid_forget()
    games=[]
    fig()
def choose_x():
    global choice
    choice = 1
    new_game()
def choose_o():
    global choice
    choice = 0
    new_game()
def fig():
    root.columnconfigure(index=0,weight=50)
    root.columnconfigure(index=1,weight=50)
    root.columnconfigure(index=2,weight=0)
    Label(root, text="Выберите фигуру:",font='9').grid(row=0, column=0, columnspan=2)
    Button(root, text="X", font='9', command=choose_x).grid(row = 1, column = 0, sticky='ew',)
    Button(root, text="O", font='9', command=choose_o).grid(row = 1, column = 1, sticky='ew')
fig()
root.mainloop()