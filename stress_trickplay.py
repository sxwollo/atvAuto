# Import Tkinter for GUI
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

# Import necessary tools for time pause and date
import time
import datetime
import threading

# Import the ADB_Action_Script.py
# This have all the core function to control the TV
from daaf.ADB_Action_Scipt import ActionScript

# Import the RC keys and App PKGs
# This is a supporting tools for ActionScript
# It has a list of RC key code and App PKGs
from daaf.RC_Code import SonyRCKey
from daaf.AppList import AppList
import daaf.Power_Tools as pt
from daaf.atvAuto import atvAuto


class TestScript(atvAuto):

    def __init__(self, tkRoot):
        """ Initialize the UI and then Set Title Header"""
        # Update the string "Template" to your desired Title
        super().__init__(tkRoot, "STB Trickplay")

        # this is in minutes
        self.playback_time = 1
        # set loopCount default value
        self.loopCount.set(50000)

    def testCaseInfo(self):
        """ 
        Set the test case info
        This is the one that shows on the left side of the screen
        Each call of the 'makeInstructionLabel' is one line
        """
        self.makeInstructionLabel("Rewind Content for 3 seconds")
        self.makeInstructionLabel("Play Content for 30 seconds")
        self.makeInstructionLabel("Fast Forward Content for 3 seconds")

    def runThis(self):
        """
        Below is where you assemble test cases
        """
        self.press_rw(3)
        self.press_play(30)
        self.press_ff(3)



# Start the script
root = Tk()
TestScript(root).startApp()