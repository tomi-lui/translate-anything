from tkinter import *
import pyautogui


class Application():
    """
    This is a class for the GUI for screen snipping text.

    Attributes:
        master (Tk()): Required to start the tkinter GUI.
    """

    def __init__(self, master) -> None:

        self.master = master
        self.master.geometry("350x300+500+300")

        # nav bar frame
        self.nav_bar = Frame(self.master, height=20, width=50)
        self.nav_bar.rowconfigure(0, minsize=50, weight=1)
        self.master.columnconfigure([0, 1, 2], minsize=50, weight=1)
        self.nav_bar.pack(side=TOP)

        # textbox frame
        self.textframe = Frame(self.master, height=600, width=500)
        self.textframe.pack()

        # button snip
        self.btn_snip = Button(self.nav_bar, text="Snip",
                               command=self.select_ROI)
        self.btn_snip.grid(row=0, column=0, sticky="nsew")

        # option translate from
        self.curr_lang_from = StringVar(master)
        self.curr_lang_from.set("en")
        self.btn_translate_from = OptionMenu(
            self.nav_bar, self.curr_lang_from, "en")
        self.btn_translate_from.grid(row=0, column=1, sticky="nsew")

        # option translate to
        self.curr_lang_to = StringVar(master)
        self.curr_lang_to.set("cn")
        self.btn_translate_to = OptionMenu(
            self.nav_bar, self.curr_lang_to, "en", "jp")
        self.btn_translate_to.grid(row=0, column=2, sticky="nsew")

        # textbox
        self.textbox = Text(self.textframe)
        placeholder = "中文"
        self.textbox.insert(END, placeholder)
        self.textbox.pack()

        # set ROI_window ( allow user to select region of interest )
        self.ROI_window = Toplevel()
        self.ROI_window.attributes("-alpha", .8)

        # create ROI_frame, master -> ROI_window
        self.ROI_frame = Frame(self.ROI_window, background="#8698b0")
        self.ROI_frame.pack(fill=BOTH, expand=YES)

        # hide ROI_window for now
        self.ROI_window.withdraw()

    def select_ROI(self):

        print("selectROI clicked")

        # create ROI_canvas
        self.ROI_canvas = Canvas(self.ROI_frame, cursor="cross", bg="#696969")
        self.ROI_canvas.pack(fill=BOTH, expand=YES)

        # set ROI_window attributes
        self.ROI_window.attributes('-fullscreen', True)
        self.ROI_window.attributes('-alpha', .2)
        self.ROI_window.attributes("-topmost", True)

        self.ROI_window.lift()

        # withdraw master
        self.master.withdraw()  # hide master

        # display ROI_canvas
        self.ROI_window.deiconify()  # show roi_canvas

        # bind buttons
        self.ROI_canvas.bind("<Button>", self.on_left_click)
        self.ROI_canvas.bind("<Motion>", self.on_mouse_drag)
        self.ROI_canvas.bind("<ButtonRelease>", self.on_mouse_release)

    def on_left_click(self, a):
        print("left mouse button clicked!")

    def on_mouse_drag(self, a):
        print("mouse dragging")

    def on_mouse_release(self, a):
        print("Mouse released")

        self.ROI_canvas.destroy()
        self.ROI_window.withdraw()
        self.master.deiconify()

    def snip(self, left, top, width, height):
        """
        The method to take a screenshot given an area.
        Parameters:
            left (int): The left position.
            top (int): The top position.
            width (int): The width.
            height (int): The height.
        """
        im = pyautogui.screenshot(region=(left, top, width, height))
        im.save(".capture.png")

    def exitScreenshotMode(self):
        """ Method to exit the selecting mode. """
        self.screenCanvas.destroy()
        self.master_screen.withdraw()
        self.master.deiconify()

    def exit_application(self):
        """ Method to end the application. """
        self.master.quit()


def main():
    root = Tk()
    app = Application(root)
    root.mainloop()


if __name__ == "__main__":
    main()
