# Import Tkinter for GUI
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import time
import datetime
import threading
# Import the ADB_Action_Script.py it must be on the same folder
from daaf.ADB_Action_Scipt import ActionScript
# Import the RC keys and App PKGs for easy scripting
from daaf.RC_Code import SonyRCKey
from daaf.AppList import AppList


class SampleTkinterLoop:

    def __init__(self, tkRoot):
        # create an instance of the class for ATV Automation
        self.tv = ActionScript()
        self.rc = SonyRCKey()
        self.app = AppList()

        # Initialize tkRoot as the Tk() instance
        self.tkRoot = tkRoot
        self.tkRoot.title("Major Apps Playback")  # Change title for each test
        self.tkRoot.iconbitmap("img/bot_icon.ico")
        self.tkRoot.geometry("1200x480")

        # Create frame for header and test area
        self.headerFrame = ttk.Frame(self.tkRoot)
        self.headerFrame.pack(fill=X)

        self.sideCanvas = Canvas(self.tkRoot)
        self.sideCanvas.pack(fill=BOTH, side=LEFT)

        self.sideFrame = ttk.Frame(self.sideCanvas)
        self.sideFrame.pack(fill=BOTH, side=LEFT)

        self.testCanvas = Canvas(self.tkRoot)
        self.testCanvas.pack(fill=BOTH, side=LEFT, expand=True)

        self.scrollbar = Scrollbar(self.tkRoot, command=self.testCanvas.yview)
        self.scrollbar.pack(fill=Y, side=RIGHT, expand=False)

        self.testFrame = ttk.Frame(self.testCanvas)
        self.testFrame.pack(fill=BOTH, side=LEFT, expand=True)

        # configure canvas and scrollbar
        self.testCanvas.configure(yscrollcommand=self.scrollbar.set)
        # put frame in canvas
        self.sideCanvas.create_window(
            (0, 0), window=self.sideFrame, anchor='nw', width=400)

        self.testCanvas.create_window(
            (0, 0), window=self.testFrame, anchor='nw', width=800)

        # Create a custom font
        self.mainFont = tkFont.Font(
            family="Helvetica", size=14, weight=tkFont.NORMAL)
        self.sideFont = tkFont.Font(
            family="Helvetica", size=14, weight=tkFont.NORMAL)
        self.buttonFont = tkFont.Font(
            family="Helvetica", size=10, weight=tkFont.BOLD)
        self.boldFont = tkFont.Font(
            family="Helvetica", size=14, weight=tkFont.BOLD)

        # Initialize flags for background of the labels and loop count
        self.bgCounter = 0
        self.loopCount = IntVar()
        self.loopCount.set(5)
        self.stopLoop = False

        # Initialize button so we can access it on any functions
        self.btnStart = Button()
        self.btnStop = Button()
        self.txtLoop = Entry()
        self.labelLoop = Label()
        self.LabelLists = []
        self.tsFormat = '%Y-%m-%d, %I:%M:%S %p'
        self.playback_time = 60

    def on_configure(self, event):
        # update scrollregion after starting 'mainloop'
        # then move scrollbar on the bottom
        self.testCanvas.configure(scrollregion=self.testCanvas.bbox('all'))
        self.testCanvas.yview_moveto(1)

    def off_configure(self, event):
        # update scrollregion after starting 'mainloop'
        # then move scrollbar on the topmost
        self.testCanvas.configure(scrollregion=self.testCanvas.bbox('all'))
        self.testCanvas.yview_moveto(0)

    def update_scrollbar(self):
        # call on_configure everytime canvas and frame change size
        self.testCanvas.bind('<Configure>', self.on_configure)
        self.testFrame.bind('<Configure>', self.on_configure)

    def reset_scrollbar(self):
        # call off_configure everytime canvas and frame change size
        self.testCanvas.bind('<Configure>', self.off_configure)
        self.testFrame.bind('<Configure>', self.off_configure)

    def bgChooser(self):
        """Background for labels"""
        if (self.bgCounter % 2) == 0:
            return str("#fff")
        return str("#e8ecf2")

    def resetLabels(self):
        """ Reset labels """
        for label in self.LabelLists:
            label.destroy()
        self.tkRoot.update()

    def startApp(self):
        # Create Label for loop count
        self.labelLoop = Label(
            self.headerFrame, text=f'Enter Loop count: ',
            font=self.mainFont)
        self.labelLoop.pack(fill=X, side=LEFT)
        # Create Textbox for loop count
        self.txtLoop = Entry(self.headerFrame, font=self.mainFont,
                             textvariable=self.loopCount)
        self.txtLoop.pack(fill=X, side=LEFT)
        # Create start button
        self.btnStart = Button(self.headerFrame, text="Start Test",
                               font=self.buttonFont, command=self.start_loop, padx=55)
        self.btnStart.pack(fill=X, side=LEFT)
        # Create stop button
        self.btnStop = Button(self.headerFrame, text="Stop Test",
                              font=self.buttonFont, command=self.stopIt, padx=55)
        self.btnStop.pack(fill=X, side=LEFT)
        self.btnStop.config(state="disabled")
        # Instruction Pane ----------------
        sideLabel = Label(
            self.sideFrame, text=f'Test Case:',
            font=self.sideFont)
        sideLabel.pack(fill=X)
        # intruction below
        Label(self.sideFrame, text=f'Launch Netflix then playback for 1 hour',
              font=self.sideFont, anchor='w').pack(fill=X, padx=10)
        Label(self.sideFrame, text=f'Launch Amazon then playback for 1 hour',
              font=self.sideFont, anchor='w').pack(fill=X, padx=10)
        Label(self.sideFrame, text=f'Launch Hulu then playback for 1 hour',
              font=self.sideFont, anchor='w').pack(fill=X, padx=10)
        Label(self.sideFrame, text=f'Launch Vudu then playback for 1 hour',
              font=self.sideFont, anchor='w').pack(fill=X, padx=10)
        Label(self.sideFrame, text=f'Launch YouTube then playback for 1 hour',
              font=self.sideFont, anchor='w').pack(fill=X, padx=10)
        # allow window to catch up
        self.tkRoot.update()
        self.tkRoot.mainloop()


# Function Template --------------------------------------------------------------------

    def sample_testcase(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Sample test case running',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

# Create test case inside a function --------------------------------------------------

    def launch_netflix(self):
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launching Netflix',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)

            # Automation Script below --------------------

            self.tv.press_rc_key(self.rc.HOME)
            self.tv.clear_launch_app(
            self.app.NETFLIX_PKG, self.app.NETFLIX_ACT)
            self.tv.wait_in_second(10)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def select_netflix_content(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Selecting content for playback',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------

            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(2)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(2)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def playback_netflix(self, pt):
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Playback Netflix',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)

            # Automation Script below --------------------
            # playback time
            self.tv.wait_in_minute(pt)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def launch_amazon(self):
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launching Amazon',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)

            # Automation Script below --------------------

            self.tv.press_rc_key(self.rc.HOME)
            self.tv.clear_launch_app(self.app.AMAZON_PKG, self.app.AMAZON_ACT)
            self.tv.wait_in_second(10)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def select_amazon_content(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Selecting content for playback',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------

            self.tv.press_rc_key(self.rc.DOWN)
            self.tv.wait_in_second(2)
            self.tv.press_rc_key(self.rc.DOWN)
            self.tv.wait_in_second(2)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(2)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(2)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def playback_amazon(self, pt):
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Playback Amazon',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)

            # Automation Script below --------------------
            # playback time
            self.tv.wait_in_minute(pt)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def launch_hulu(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launching Hulu',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------

            self.tv.press_rc_key(self.rc.HOME)
            self.tv.wait_in_second(1)
            self.tv.clear_launch_app(self.app.HULU_PKG, self.app.HULU_ACT)
            self.tv.wait_in_second(10)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def select_hulu_content(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Selecting content for playback',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------

            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(1)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def playback_hulu(self, pt):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Playback Hulu',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------

            self.tv.wait_in_minute(pt)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def launch_vudu(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launching Vudu',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------

            self.tv.press_rc_key(self.rc.HOME)
            self.tv.wait_in_second(1)
            self.tv.clear_launch_app(self.app.VUDU_PKG, self.app.VUDU_ACT)
            self.tv.wait_in_second(10)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def select_vudu_content(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Selecting content for playback',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------
            
            self.tv.press_rc_key(self.rc.RIGHT)
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.RIGHT)
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.DOWN)
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(1)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def playback_vudu(self, pt):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Playback Vudu',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------

            self.tv.wait_in_minute(pt)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def launch_youtube(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launching YouTube',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------

            self.tv.press_rc_key(self.rc.HOME)
            self.tv.wait_in_second(1)
            self.tv.force_stop_app(self.app.YOUTUBE_PKG)
            self.tv.wait_in_second(1)
            self.tv.launch_app(self.app.YOUTUBE_PKG)
            self.tv.wait_in_second(10)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def select_youtube_content(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Selecting content for playback',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------

            self.tv.press_rc_key(self.rc.RIGHT)
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(1)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def playback_youtube(self, pt):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Playback YouTube',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------

            self.tv.wait_in_minute(pt)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

# End of test case inside a function --------------------------------------------------

    def stopIt(self):
        # stop main loop
        self.loopCount.set(1)
        self.stopLoop = True
        # disable stop button
        self.btnStop.config(state="disabled")
        # let user know
        x = Label(
            self.testFrame, text=f'Stopping test..',
            background=self.bgChooser(),
            foreground="#a5120d",
            font=self.boldFont)
        x.pack(fill=X)
        self.LabelLists.append(x)

    def start_loop(self):
        self.stopLoop = False
        self.watch_loop()

    def watch_loop(self):
        def repeatIt():
            # reset UI and flag before starting loop
            self.resetLabels()
            # enable stop button
            self.btnStop.config(state="normal")
            # disable button while loop is running
            self.btnStart.config(state="disabled")
            self.txtLoop.config(state="disabled")
            self.labelLoop.config(text="Remaining Loop:  ")

            while self.loopCount.get() > 0:
                # move scrollbar to bottom
                self.testCanvas.yview_moveto(0)
                # assemble test case below ---------------------------------------

                self.launch_netflix()
                self.select_netflix_content()
                self.playback_netflix(self.playback_time)

                self.launch_amazon()
                self.select_amazon_content()
                self.playback_amazon(self.playback_time)

                self.launch_hulu()
                self.select_hulu_content()
                self.playback_hulu(self.playback_time)

                self.launch_vudu()
                self.select_vudu_content()
                self.playback_vudu(self.playback_time)

                self.launch_youtube()
                self.select_youtube_content()
                self.playback_youtube(self.playback_time)

                # Below are just to reset the UI ---------------------------------
                # update and reset testFrame after all function run
                self.resetLabels()
                self.reset_scrollbar()
                self.tkRoot.update()

                # pause before restarting loop
                self.loopCount.set(self.loopCount.get()-1)
                time.sleep(1)

            # disable stop button
            self.btnStop.config(state="disabled")
            # re-enable button after loop is done
            self.btnStart.config(state="normal")
            self.txtLoop.config(state="normal")
            self.labelLoop.config(text="Enter Loop count: ")
            self.testCanvas.yview_moveto(0)
            # Let user know the script is done
            if not self.stopLoop:
                # loop did not stopped
                x = Label(
                    self.testFrame, text=f'Test is done!',
                    background=self.bgChooser(),
                    foreground="#a5120d",
                    font=self.boldFont)
                x.pack(fill=X)
            else:
                x = Label(
                    self.testFrame, text=f'Test stopped!',
                    background=self.bgChooser(),
                    foreground="#a5120d",
                    font=self.boldFont)
                x.pack(fill=X)
            self.btnStart.config(state="normal")
            self.txtLoop.config(state="normal")
            self.labelLoop.config(text="Enter Loop count: ")
            self.testCanvas.yview_moveto(0)
            self.loopCount.set(5)
            self.LabelLists.append(x)
        thread = threading.Thread(target=repeatIt)
        thread.start()


root = Tk()
LoopTest = SampleTkinterLoop(root)
LoopTest.startApp()