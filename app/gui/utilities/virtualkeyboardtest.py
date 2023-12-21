# keyboard_utils.py
import subprocess

def open_keyboard(widget, width=480, height=200):
    command = ['matchbox-keyboard']
    widget.virtual_keyboard = subprocess.Popen(command)
