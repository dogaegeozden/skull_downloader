# This Python file uses the following encoding: utf-8

# LIBRARIES/MODULES
from pathlib import Path
from pytube import YouTube
from os import path, rename, system
from sys import argv
from logging import basicConfig, DEBUG, debug, disable, CRITICAL
from webbrowser import open as wbopen
from threading import Thread

# PySide2 Modules
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog

# Graphical User Interfaces
from guis.main_window_ui import Ui_MainWindow
from guis.credits_win_ui import Ui_CreditsDialog

# Resources
import resources_rc

# Doing the basic configuration for the debugging feature
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Diabling the debugging feature. Hint: Comment out the line to enable debugging.
# disable(CRITICAL)

# GLOBAL VARIABLES
# Creating a variable called base_dir which leads to the current working directory.
base_dir = path.dirname(__file__)


def download_the_media(format_choice, url):
    """A function which downloads media from youtube."""

    # Sending notification to let the user know that the application is trying to connect to the server
    system(f'notify-send -i "/opt/skull_downloader/icons/skull_downloader_logo.jpg" -t 300 "Trying to download the media. This might take some time!"')
    
    # Configuring the url
    yt = YouTube(f'{url}')
    
    # Trying to execute the code which is located inside the try block
    try:
        # Checking if the format_choice is equal to Video
        if format_choice == "Video":

            # Creating a variable called destination which is leading to user's Videos folder
            destination = str(Path(Path.home(), "Videos"))

            # Filtering and downloading the media
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=destination)

        # Checking if the format_choice is equal to Audio
        elif format_choice == "Audio":

            # Creating a variable called destination which is leading to user's Music folder
            destination = str(Path(Path.home(), "Music"))

            # Extracting only the audio
            video = yt.streams.filter(only_audio=True).first()

            # Downloading the media
            out_file = video.download(output_path=destination)

            # Saving the file
            base, ext = path.splitext(out_file)

            # Creating a new file name
            new_file = base + '.mp3'

            # Renaming the file
            rename(out_file, new_file)

        # Creating a message to display in a notification
        message = f'{yt.title} is downloaded to {destination}'
    
    # Instructing the computer about what to do if it faces with an error
    except:
        # Creating a message to display in a notification
        message = "Couldn't connect to the server"

    # Sending notification to let the user know where media is downloaded to
    system(f'notify-send -i "/opt/skull_downloader/icons/skull_downloader_logo.jpg" -t 300 "{message}"')

# Creating a dialog class called CreditsDialog
class CreditsDialog(QDialog, Ui_CreditsDialog):

    def __init__(self, *args, **kwargs):
        """An init function which makes the window self contained""" 

        # Calling super function with init
        super().__init__(*args, **kwargs)

        # Loading the GUI
        self.setupUi(self)

# Creating a MainWindow class
class MainWindow(QMainWindow, Ui_MainWindow):

    # Initializing the main window to make it self contained.
    def __init__(self, *args, **kwargs):
        """An init function which makes the window self contained""" 

        # Calling super function with init
        super().__init__(*args, **kwargs)

        # Loading the GUI
        self.setupUi(self)

        # Connecting the download_button with the download_media_from_youtube function in a way that the function will going to trigger with a press signal
        self.download_button.pressed.connect(self.download_media_from_youtube)

        # Connecting the credits_action_button with the show_credits_dialog function in a way that the function will going to trigger with a trigger signal
        self.credits_action_button.triggered.connect(self.show_credits_dialog)

        # Connecting the help_page_action_button with the open_the_help_page function in a way that the function will going to trigger with a trigger signal
        self.help_page_action_button.triggered.connect(self.open_the_help_page)

    def open_the_help_page(self):
        """A function which opens the help page in the default browser"""

        # Opening the help page in the default browser
        wbopen('https://github.com/dogaegeozden/skull_downloader#readme')

    def show_credits_dialog(self):
        """A function which shows the credits dialog window"""

        # Creating a dialog object using CreditsDialog class
        dialog = CreditsDialog()

        # Opening the dialog window
        dialog.exec_()
    
    def download_media_from_youtube(self):
        """A function which downloads media from youtube"""

        # Creating a variable called url from the url_line_edit widget's text
        url = self.url_line_edit.text()

        # Creating a variable called format_choice from the media_format_choice_combo_box widget's current text
        format_choice = self.media_format_choice_combo_box.currentText()
        
        # Printing the url and the format_choice in debug mode.
        debug(f'URL = {url}')

        # Printing the media format choice in debug mode
        debug(f'Format Choice = {format_choice}')

        # Create thread called download_thread. Hint: Threading is important for concurrency.
        download_thread = Thread(target=download_the_media, args=(format_choice,url))

        # Starting the thread
        download_thread.start()


# Evaluate if the source is being run on its own or being imported somewhere else. With this conditional in place, your code can not be imported somewhere else.
if __name__ == '__main__':

    # Creating an app object from QApplication
    app = QApplication(argv)

    # Creating a main_win object from MainWindow class
    main_win = MainWindow()

    # Showing the main_win
    main_win.show()

    # Executing the app
    app.exec_()