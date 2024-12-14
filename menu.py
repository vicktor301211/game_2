from tkinter import *




def menu_toggle(canvas):
    global menu_mode
    menu_mode = not menu_mode
    if menu_mode:
        menu_show(canvas)
    else:
        menu_hide(canvas)
def pause_toggle():
    global pause
    pause = not pause


def menu_enter(canvas, player1, player2):
    if menu_current_index == 0:
        game_resume()
    elif menu_current_index == 1:
        game_new(canvas, player1, player2)
    elif menu_current_index == 2:
        game_save()
    elif menu_current_index == 3:
        game_load()
    elif menu_current_index == 4:
        game_exit()
    menu_hide(canvas)
#
#
#
#
#
#
#
def game_new(canvas, player1, player2):
    # menu_toggle()
    x1, y1 = 50, 50
    x2, y2 = x1, y1 + 100 + 100
    canvas.coords(player1, x1, y1, x1 + 100,
                  y1 + 100)
    canvas.coords(player2, x2, y2, x2 + 100,
                  y2 + 100)
    print('Начинаем новую игру')
#
#
#
#
def game_resume():
    print('Возобновляем старую игру')
#
#
def game_save():
    print('Сохраняем игру')
#     # 1
#     x1 =  canvas.coords(player1)[0]
#     x2 =  canvas.coords(player2)[0]
#     data = [x1, x2]
#     with open('save.dat', 'wb') as f:
#         dump(data, f)
#         set_status('Сохранено', color='yellow')
#
#
def game_load():
    print('Загружаем игру')
#     # 2
#     global x1, x2
#     with open('save.dat', 'rb') as f:
#         data = load(f)
#         x1, x2 = data
#         canvas.coords(player1, x1, y1, x1 + player_size,
#                       y1 + player_size)
#         canvas.coords(player2, x2, y2, x2 + player_size,
#                       y2 + player_size)
#         set_status('Загружено', color='yellow')
#
#
def game_exit():
    print('Выходим из игры')
    exit()
#
def menu_show(canvas):
    global menu_mode
    menu_mode = True
    #print('Вижу')
    menu_update(canvas)



def menu_hide(canvas):
    global menu_mode
    menu_mode = False
    #print('Не вижу')
    menu_update(canvas)
#
#
def menu_up(canvas):
    global menu_current_index
    menu_current_index -= 1
    if menu_current_index < 0:
        menu_current_index = 0
    menu_update(canvas)


def menu_down(canvas):
    global menu_current_index
    menu_current_index += 1
    if menu_current_index > len(menu_options) - 1:
        menu_current_index = len(menu_options) - 1
    menu_update(canvas)
#
#
def menu_update(canvas):
    for menu_index in range(len(menu_options_id)):
        element_id = menu_options_id[menu_index]
        if menu_mode:
            canvas.itemconfig(element_id, state='normal')
            if menu_index == menu_current_index:
                canvas.itemconfig(element_id, fill='blue')
            else:
                canvas.itemconfig(element_id, fill='black')
        else:
            canvas.itemconfig(element_id, state='hidden')
def menu_create(canvas):
    offest = 0
    for menu_option in menu_options:
        option_id = canvas.create_text(400, 200 + offest, anchor=CENTER, font=('Arial', '25'), text=menu_option,
                                       fill='black')
        menu_options_id.append(option_id)
        offest += 50
    menu_update(canvas)

menu_mode = True
menu_options = ['Возврат в игру', 'Новая игра', 'Сохранить', 'Загрузить', 'Выход']
menu_current_index = 3
menu_options_id = []
pause = False