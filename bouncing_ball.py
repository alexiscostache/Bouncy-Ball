# Screen resolution is 1300x900
# When you are in the leaderboard menu press Esc to close it
# Press epace to pause and unpause the game
# Shift-Up is the first cheatcode and Alt-Down the second
# Tab is the boss key
from tkinter import *
from random import randint as rand
from time import sleep
import json

settingCHANGE = 0


def createCanvas():
    global canvas
    canvas = Canvas(window, width=1300, height=900, bg="black")
    canvas.pack()


def image():
    Bk = PhotoImage(file="excel.gif")
    canvas.create_image(0, 0, image=Bk, anchor=NW)
# the function which creates the image for the bosskey


def close(event):
    canvas.destroy()


def delete_image(event):
    global x, y
    canvas.delete(img)
    x = x_ball
    y = y_ball
    window.bind('<Tab>', bosskey)


def bosskey(event):
    global img, x, y
    canvas.Bk = PhotoImage(file="excel.gif")
    img = canvas.create_image(0, 0, image=canvas.Bk, anchor=NW)
    x = 0
    y = 0
    window.bind('<Tab>', delete_image)


def keys(event):
    if event.char == left_movement and pos3[0] > 0:
        x_pole = -8
        y_pole = 0
        canvas.move(pole, x_pole, y_pole)
    if event.char == right_movement and pos3[2] < 1300:
        x_pole = 8
        y_pole = 0
        canvas.move(pole, x_pole, y_pole)
# function to move from the keys


def move_left(event):
    x_pole = -8
    y_pole = 0
    canvas.move(pole, x_pole, y_pole)


def move_right(event):
    x_pole = 8
    y_pole = 0
    canvas.move(pole, x_pole, y_pole)


def empty(event):
    pass


def change_settings_movement():
    global left_movement, right_movement, settingCHANGE
    left_movement = left.get()
    right_movement = right.get()
    settingCHANGE = 1
    canvas5.destroy()


def reset_settings():
    global settingCHANGE
    settingCHANGE = 0
    canvas5.destroy()


def change_settings():
    global left, right, canvas5
    canvas5 = Canvas(canvas2, width=1300, height=900, bg="black")
    canvas5.pack()
    canvas5.create_text(640, 200,
                        text="Please enter the key to move left the pole:",
                        fill="red", font=('Times New Roman', 18))
    left = Entry(canvas5)
    left.place(x=490, y=250)
    canvas5.create_text(640, 350,
                        text="Please enter the key to move right the pole:",
                        fill="red", font=('Times New Roman', 18))
    right = Entry(canvas5)
    right.place(x=490, y=400)
    btn8 = Button(canvas5, width=10, height=2, text='Save Settings',
                  command=lambda: change_settings_movement(), background='red')
    btn8.place(x=550, y=450)
    btn9 = Button(canvas5, width=10, height=2, text='Reset Settings',
                  command=lambda: reset_settings(), background='red')
    btn9.place(x=550, y=550)


def pause(event):
    global canvas2, x, y
    x = 0
    y = 0
    canvas2 = Canvas(canvas, width=1300, height=900, bg="black")
    canvas2.pack()
    window.bind('<space>', resume_game)
    canvas2.create_text(680, 150, text="You paused the game!",
                        fill="red",
                        font=('Times New Roman', 24, 'bold'))
    btn5 = Button(canvas2, text="Save Game", width=20, height=3,
                  command=lambda: save_game(), background="red")
    btn6 = Button(canvas2, text="Change Settings", width=20, height=3,
                  command=lambda: change_settings(), background="red")
    btn7 = Button(canvas2, text="Quit Game", width=20, height=3,
                  command=lambda: quit_canvases(), background="red")
    btn5.place(x=500, y=250)
    btn6.place(x=500, y=400)
    btn7.place(x=500, y=550)


def quit_canvases():
    canvas2.destroy()
    canvas.destroy()


def save_game():
    saved_data = {}
    saved_data['cur_score'] = current_score
    saved_data['speed'] = {'x_speed': x_ball, 'y_speed': y_ball}
    saved_data['mainballcoords'] = pos
    saved_data['polecoords'] = pos3
    saved_data['name'] = saved_name
    pos_balls = []
    saved_data['ballscoords'] = []
    saved_data['bc'] = []
    i = 0
    while(i < len(balls)):
        pos_balls.append(canvas.coords(balls[i]))
        saved_data['ballscoords'].append(pos_balls[i])
        saved_data['bc'].append(balls_colour[i])
        i += 1
    with open('data.json', 'w') as f:
        json.dump(saved_data, f)


def resume_game(event):
    global x, y
    x = x_ball
    y = y_ball
    window.bind('<space>', pause)
    canvas2.destroy()


def enter(event):
    canvas.destroy()
# function that goes back to main menu


def cheatcode1(event):
    global canvas3, current_score
    canvas3 = Canvas(canvas, width=1300, height=900, bg="black")
    canvas3.pack()
    canvas3.create_oval(600, 250, 626, 276, fill='#39ff14')
    canvas3.create_rectangle(545, 770, 795, 820, fill='#3EF1FA')
    canvas3.create_text(1150, 850, text="Score: 96",
                        fill="white",
                        font=('Times New Roman', 20, 'italic'))
    canvas3.create_text(650, 450, text="Congratulations! You won!!!",
                        fill="red",
                        font=('Times New Roman', 24, 'bold'))
    current_score = 96
    leaderboard_data[saved_name] = current_score
    with open('leaderboard.json', 'w') as file:
        json.dump(leaderboard_data, file)
    canvas3.create_text(650, 550, text="Press enter to go to main menu",
                        fill="red",
                        font=('Times New Roman', 18, 'bold'))
    loop = False
    window.bind('<Return>', enter)


def cheatcode2(event):
    global pos3
    pos3[2] += 10
    canvas.coords(pole, pos3)
# cheatcode which enlarges the pole by 10 to its right


def get_name():
    global saved_name
    saved_name = player_name.get()
    leader = {}
    file = open('leaderboard.json')
    leader = json.load(file)
    if saved_name in leader:
        canvas4.create_text(640, 500, text="Please enter another name!",
                            fill="red", font=('Times New Roman', 18))
    else:
        new_game()
# function which gets the name of the player
# if there exists an old user with the same name,
# the user is prompted to enter another name


def name_input():
    global player_name, canvas4
    canvas4 = Canvas(window, width=1300, height=900, bg='black')
    canvas4.pack()
    canvas4.create_text(640, 200, text="Please enter your name:",
                        fill="red",
                        font=('Times New Roman', 22, 'italic'))
    player_name = Entry(canvas4)
    player_name.place(x=490, y=300)
    btn6 = Button(canvas4, width=10, height=2, text='Start Game',
                  command=lambda: get_name(), background='red')
    btn6.place(x=550, y=350)


def new_game():
    global pole, main_ball, x, y, x_ball, y_ball, current_score
    global pos, pos3, balls, balls_colour
    canvas4.destroy()
    createCanvas()
    score = canvas.create_text(1150, 850, text="Score: 0",
                               fill="white",
                               font=('Times New Roman', 20, 'italic'))
    balls = []
    balls_colour = []
    current_score = 0
    colour = ["red", "blue", "green", "orange", "white",
              "purple", "pink", "brown"]
    y = 5
    for i in range(4):
        x = 5
        for j in range(24):
            fill_ball = rand(0, 7)
            xy = (x, y, x+34, y+34)
            x += 54
            balls.append(canvas.create_oval(xy, fill=colour[fill_ball]))
            balls_colour.append(colour[fill_ball])
        y += 54
# this code creates the balls at the top of the screen
    x = 2.5
    y = 2.5
    x_ball = x
    y_ball = y
    main_ball = canvas.create_oval(600, 250, 626, 276, fill='#39ff14')
    pole = canvas.create_rectangle(545, 770, 795, 820, fill='#3EF1FA')
    window.bind('<space>', pause)
    window.bind('<Tab>', bosskey)
    window.bind('<Shift-Up>', cheatcode1)
    window.bind('<Alt-Down>', cheatcode2)
    loop = True
    while loop is True:
        window.bind('<Return>', empty)
        pos = canvas.coords(main_ball)
        if current_score == 96:
            loop = False
            canvas.create_text(650, 450, text="Congratulations! You won!!!",
                               fill="red",
                               font=('Times New Roman', 24, 'bold'))
            canvas.create_text(650, 550, text="Press enter to go to main menu",
                               fill="red",
                               font=('Times New Roman', 18, 'bold'))
            window.bind('<Return>', enter)
            leaderboard_data[saved_name] = 96
            with open('leaderboard.json', 'w') as file:
                json.dump(leaderboard_data, file)
        if pos[3] >= 900:
            loop = False
            canvas.create_text(650, 450, text="Game Over", fill="red",
                               font=('Times New Roman', 24, 'bold'))
            canvas.create_text(650, 550, text="Press enter to go to main menu",
                               fill="red",
                               font=('Times New Roman', 18, 'bold'))
            window.bind('<Return>', enter)
            leaderboard_data[saved_name] = current_score
            with open('leaderboard.json', 'w') as file:
                json.dump(leaderboard_data, file)
        if pos[1] < 0:
            y = -y
            y_ball = y
        if pos[2] > 1300 or pos[0] < 0:
            x = -x
            x_ball = x
        i = 0
        while(i < len(balls)):
            pos2 = canvas.coords(balls[i])
            if(pos[0] < pos2[2] and pos[2] > pos2[0] and
               pos[1] < pos2[3] and pos[3] > pos2[1]):
                y = -y
                y_ball = y
                canvas.delete(balls[i])
                balls.remove(balls[i])
                del balls_colour[i]
                current_score += 1
                canvas.itemconfig(score, text="Score: " + str(current_score))
            i += 1
        pos3 = canvas.coords(pole)
        if(settingCHANGE == 1):
            window.bind('<Left>', empty)
            window.bind('<Right>', empty)
            if loop is False:
                window.bind('<Key>', empty)
            else:
                if(pos3[0] > 0 and pos3[2] < 1300):
                    window.bind('<Key>', keys)
        elif loop is False:
            window.bind('<Left>', empty)
            window.bind('<Right>', empty)
        else:
            window.bind('<Key>', empty)
            if(pos3[0] > 0 and pos3[2] < 1300):
                window.bind('<Left>', move_left)
                window.bind('<Right>', move_right)
            elif(pos3[0] <= 0):
                window.bind('<Left>', empty)
            elif(pos3[2] >= 1300):
                window.bind('<Right>', empty)
# collision detection
        if(pos3[0] < pos[2] and pos3[2] > pos[0] and
           pos3[1] < pos[3] and pos3[3] > pos[1]):
            if(x > 0 and x < 4):
                x += 0.5
            elif x < 0 and x > -4:
                x -= 0.5
            if(y > 0 and y < 4):
                y += 0.5
            elif y < 0 and y > -4:
                y -= 0.5
            y = -y
            y_ball = y
# increases speed of the ball when the ball which moves hits the pole
        canvas.move(main_ball, x, y)
        sleep(0.012)
        window.update()
# the function which starts a new game


def load_game():
    global pole, main_ball, x, y, x_ball, y_ball
    global current_score, pos, pos3, balls, balls_colour
    createCanvas()
    f = open('data.json')
    saved_data = json.load(f)
    current_score = saved_data['cur_score']
    saved_name = saved_data['name']
    score = canvas.create_text(1150, 850, text="Score: " + str(current_score),
                               fill="white",
                               font=('Times New Roman', 20, 'italic'))
    pos = saved_data['mainballcoords']
    pos3 = saved_data['polecoords']
    main_ball = canvas.create_oval(pos, fill='#39ff14')
    pole = canvas.create_rectangle(pos3, fill='#3EF1FA')
    balls = []
    balls_colour = []
    i = 0
    while(i < len(saved_data['bc'])):
        balls.append(canvas.create_oval(saved_data['ballscoords'][i],
                     fill=saved_data['bc'][i]))
        balls_colour.append(saved_data['bc'][i])
        i += 1
# this code loads the balls at the top of the screen
    x = saved_data['speed']['x_speed']
    y = saved_data['speed']['y_speed']
    window.bind('<space>', pause)
    window.bind('<Tab>', bosskey)
    window.bind('<Shift-Up>', cheatcode1)
    window.bind('<Alt-Down>', cheatcode2)
    loop = True
    while loop is True:
        window.bind('<Return>', empty)
        pos = canvas.coords(main_ball)
        if current_score == 96:
            loop = False
            canvas.create_text(650, 450, text="Congratulations! You won!!!",
                               fill="red",
                               font=('Times New Roman', 24, 'bold'))
            canvas.create_text(650, 550, text="Press enter to go to main menu",
                               fill="red",
                               font=('Times New Roman', 18, 'bold'))
            window.bind('<Return>', enter)
            leaderboard_data[saved_name] = 96
            with open('leaderboard.json', 'w') as file:
                json.dump(leaderboard_data, file)
        if pos[3] >= 900:
            loop = False
            canvas.create_text(650, 450, text="Game Over",
                               fill="red",
                               font=('Times New Roman', 24, 'bold'))
            canvas.create_text(650, 550, font=('Times New Roman', 18, 'bold'),
                               fill="red",
                               text="Press enter to go to main menu")
            window.bind('<Return>', enter)
            leaderboard_data[saved_name] = current_score
            with open('leaderboard.json', 'w') as file:
                json.dump(leaderboard_data, file)
        if pos[1] < 0:
            y = -y
            y_ball = y
        if pos[2] > 1300 or pos[0] < 0:
            x = -x
            x_ball = x
        i = 0
        while(i < len(balls)):
            pos2 = canvas.coords(balls[i])
            if(pos[0] < pos2[2] and pos[2] > pos2[0] and
               pos[1] < pos2[3] and pos[3] > pos2[1]):
                y = -y
                y_ball = y
                canvas.delete(balls[i])
                balls.remove(balls[i])
                del balls_colour[i]
                current_score += 1
                canvas.itemconfig(score, text="Score: " + str(current_score))
            i += 1
        pos3 = canvas.coords(pole)
        if(settingCHANGE == 1):
            window.bind('<Left>', empty)
            window.bind('<Right>', empty)
            if loop is False:
                window.bind('<Key>', empty)
            else:
                if(pos3[0] > 0 and pos3[2] < 1300):
                    window.bind('<Key>', keys)
        elif loop is False:
            window.bind('<Left>', empty)
            window.bind('<Right>', empty)
        else:
            if(pos3[0] > 0 and pos3[2] < 1300):
                window.bind('<Left>', move_left)
                window.bind('<Right>', move_right)
            elif(pos3[0] <= 0):
                window.bind('<Left>', empty)
            elif(pos3[2] >= 1300):
                window.bind('<Right>', empty)
# collision detection
        if(pos3[0] < pos[2] and pos3[2] > pos[0] and
           pos3[1] < pos[3] and pos3[3] > pos[1]):
            if(x > 0 and x < 4):
                x += 0.5
            elif x < 0 and x > -4:
                x -= 0.5
            if(y > 0 and y < 4):
                y += 0.5
            elif y < 0 and y > -4:
                y -= 0.5
            y = -y
            y_ball = y
# increases speed of the ball when the ball which moves hits the pole
        canvas.move(main_ball, x, y)
        sleep(0.012)
        window.update()
# this function loads the previous saved game


def leaderboard():
    createCanvas()
    window.bind('<Escape>', close)
    file = open('leaderboard.json')
    leaderboard_output = json.load(file)
    sort_leaderboard = sorted(leaderboard_output.items(),
                              key=lambda z: z[1], reverse=True)
    hei = 500
    wid = 650
    canvas.img1 = PhotoImage(file="gold.png")
    canvas.create_image(650, 250, image=canvas.img1)
    canvas.img2 = PhotoImage(file="silver.png")
    canvas.create_image(150, 300, image=canvas.img2)
    canvas.img3 = PhotoImage(file="bronze.png")
    canvas.create_image(1100, 300, image=canvas.img3)
    canvas.create_text(wid, 50, text="Leaderboard",
                       fill="red", font=('Times New Roman', 24, 'bold'))
    canvas.create_text(650, 350, text=str(sort_leaderboard[0][0]) + ": " +
                       str(sort_leaderboard[0][1]),
                       fill="red", font=('Times New Roman', 21, 'italic'))
    canvas.create_text(150, 400, text=str(sort_leaderboard[1][0]) + ": " +
                       str(sort_leaderboard[1][1]),
                       fill="red", font=('Times New Roman', 21, 'italic'))
    canvas.create_text(1100, 400, text=str(sort_leaderboard[2][0]) + ": " +
                       str(sort_leaderboard[2][1]),
                       fill="red", font=('Times New Roman', 21, 'italic'))
    for i in range(3, 10):
        canvas.create_text(wid, hei, text=str(i+1) + ". " +
                           str(sort_leaderboard[i][0]) + ": " +
                           str(sort_leaderboard[i][1]),
                           fill="red", font=('Times New Roman', 18))
        hei += 50


window = Tk()
window.title("Bouncy Ball")
window.geometry("1300x900")
window.configure(bg="black")
leaderboard_data = {}
file = open('leaderboard.json')
leaderboard_data = json.load(file)
title = Label(window, text="Bouncy Ball",
              font=('Times New Roman', 30, 'bold'), bg="black", fg="red")
title.place(x=470, y=50)
gameimage1 = PhotoImage(file='game.png')
label_image1 = Label(window, image=gameimage1)
label_image1.place(x=30, y=320)
gameimage2 = PhotoImage(file='game2.png')
label_image2 = Label(window, image=gameimage2)
label_image2.place(x=916, y=320)
btn1 = Button(window, text="New Game", width=20,
              height=3, command=lambda: name_input(), background="red")
btn2 = Button(window, text="Resume Game", width=20,
              height=3, command=lambda: load_game(), background="red")
btn3 = Button(window, text="Leaderboard", width=20,
              height=3, command=lambda: leaderboard(), background="red")
btn4 = Button(window, text="Quit", width=20,
              height=3, command=quit, background="red")
btn1.place(x=500, y=200)
btn2.place(x=500, y=350)
btn3.place(x=500, y=500)
btn4.place(x=500, y=650)
window.mainloop()
