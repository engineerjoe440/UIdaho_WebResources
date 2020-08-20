"""
AcSELerator RTAC (SEL-5033) Software Screen-Shot Capturing Tool
---------------------------------------------------------------

This tool can be used to programatically capture screen shots of the
AcSELerator RTAC software so that it can be documented for presentations.

"""


# Import Required Packages
from PIL import ImageGrab
import win32gui, win32con
import time


# Define Function to Find Particular Application Window
def find_app_handle(app_name):
    # Enumerate Windows
    toplist, winlist = [], []
    # Define Function to Enumerate Windows
    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
    win32gui.EnumWindows(enum_cb, toplist)
    acrtacWindow = [(hwnd, title) for hwnd, title in winlist if app_name.lower() in title.lower()]
    # just grab the hwnd for first window matching the requested name
    acrtacWindow = acrtacWindow[0]
    hwnd = acrtacWindow[0]
    return(hwnd)

# Define Function to Call Forground and Take Screenshot
def foreground_screenshot(hwnd, filename=''):
    win32gui.SetForegroundWindow(hwnd)
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    bbox = win32gui.GetWindowRect(hwnd)
    # # Correct Sizing
    # bbox = [int(i*3/2 - 15) if i > 0 else 0 for i in bbox]
    time.sleep(0.1)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.1)
    img = ImageGrab.grab(bbox)
    if filename == '':
        img.show()
    else:
        if not (filename.endswith('.png') or filename.endswith('.jpg')):
            filename = filename + '.png'
        img.save(filename)


# Define Function to Show Application and Save Screenshot
def show_and_screenshot( app_name, filename ):
    # Find Application Handle
    app_handle = find_app_handle(app_name)
    # Capture Image
    foreground_screenshot(app_handle, filename)


# Main Script Entry Point
if __name__ == '__main__':
    # Capture Image of AcSELerator RTAC
    show_and_screenshot('AcSELerator RTAC', 'images/acRTAC_screenshot.png')