import keyboard


def key_down(key):
    if keyboard.is_pressed(key):
        print(key)
        return True
    else:
        return False
