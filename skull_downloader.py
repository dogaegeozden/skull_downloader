# LIBRARIES
# Python Modules
from pathlib import Path
from pytube import YouTube
from os import path, rename
from sys import argv
from logging import basicConfig, DEBUG, debug, disable, CRITICAL
from webbrowser import open as wbopen

# PySide2 Libraries
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog

# Graphical User Interfaces
from user_interfaces.main_window_ui import Ui_MainWindow
from user_interfaces.credits_win_ui import Ui_CreditsDialog

# Resources
import resources_rc

# Doing the basic configuration for the debugging feature
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Diabling the debugging feature. Hint: Comment out the line to enable debugging.
disable(CRITICAL)

# GLOBAL VARIABLES

# Creating a variable called base_dir which leads to the current working directory.
base_dir = path.dirname(__file__)

def main():
    """The function which runs the entire script"""
    app = QApplication(argv)
    main_win = MainWindow()
    main_win.show()
    app.exec_()

# Creating a dialog class called CreditsDialog
class CreditsDialog(QDialog, Ui_CreditsDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loading the GUI
        self.setupUi(self)


# Creating a MainWindow class
class MainWindow(QMainWindow, Ui_MainWindow):
    # Initializing the main window to make it self contained.
    def __init__(self, *args, **kwargs):
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
        wbopen('https://github.com/dogaegeozden/skull_downloader#readme')

    def show_credits_dialog(self):
        """A function which shows the credits dialog window"""
        dialog = CreditsDialog()
        dialog.exec_()
    
    def download_media_from_youtube(self):
        """A function which downloads media from youtube"""
        # Creating a variable called url from the url_line_edit widget's text
        url = self.url_line_edit.text()
        # Creating a variable called format_choice from the media_format_choice_combo_box widget's current text
        format_choice = self.media_format_choice_combo_box.currentText()
        
        # Printing the url and the format_choice in debug mode.
        debug(f'URL = {url}')
        debug(f'Format Choice = {format_choice}')

        # Trying to execute the block inside the try block
        try:
            # Checking if the format_choice is equal to Video
            if format_choice == "Video":
                # Creating a variable called destination which is leading to user's Videos folder
                destination = str(Path(Path.home(), "Videos"))
                # Downloading the video
                yt = YouTube(f'{url}')
                yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=destination)
                # Setting the info_label widget's text
                self.info_label.setText(f'{yt.title} is downloaded to {destination}')
            
            # Checking if the format_choice is equal to Audio
            elif format_choice == "Audio":
                # Creating a variable called destination which is leading to user's Music folder
                destination = str(Path(Path.home(), "Music"))
                # Downloading the audio
                yt = YouTube(f'{url}')
                # Extracting only the audio
                video = yt.streams.filter(only_audio=True).first()
                # Downloading
                out_file = video.download(output_path=destination)
                # Saving the file
                base, ext = path.splitext(out_file)
                # Creating a new file name
                new_file = base + '.mp3'
                # Renaming the file
                rename(out_file, new_file)
                # Setting the info_label widget's text
                self.info_label.setText(f'{yt.title} is downloaded to {destination}')


        except Exception as error_string:
            error_string = str(error_string)
            self.info_label.setText(f'{error_string}')
            self.info_label.setStyleSheet(u"#info_label {color: red;}")

# Evaluate if the source is being run on its own or being imported somewhere else. With this conditional in place, your code can not be imported somewhere else.
if __name__ == '__main__':
    main()