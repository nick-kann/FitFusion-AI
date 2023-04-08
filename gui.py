import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        App._root = root
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        homeFrame = tk.Frame(root)
        App._homeFrame = homeFrame
        homeFrame["bg"] = "#00ffff"
        homeFrame.pack(fill="both", expand=True)

        SettingsButton = tk.Button(homeFrame)
        SettingsButton["bg"] = "#6b6b6b"
        ft = tkFont.Font(family='Arial', size=10)
        SettingsButton["font"] = ft
        SettingsButton["fg"] = "#ffffff"
        SettingsButton["justify"] = "center"
        SettingsButton["text"] = "Settings"
        SettingsButton.place(x=530, y=10, width=50, height=50)
        SettingsButton["command"] = self.SettingsButton_command

        DropDownButton = tk.Button(homeFrame)
        DropDownButton["bg"] = "#6b6b6b"
        ft = tkFont.Font(family='Arial', size=10)
        DropDownButton["font"] = ft
        DropDownButton["fg"] = "#ffffff"
        DropDownButton["justify"] = "center"
        DropDownButton["text"] = "Button"
        DropDownButton.place(x=20, y=10, width=70, height=25)
        DropDownButton["command"] = self.DropDownButton_command

        AIMessageBoard = tk.Message(homeFrame)
        ft = tkFont.Font(family='Arial', size=10)
        AIMessageBoard["font"] = ft
        AIMessageBoard["fg"] = "#cec9c3"
        AIMessageBoard["justify"] = "center"
        AIMessageBoard["text"] = "AI RECOMANDATION ANALYZATION MEOW"
        AIMessageBoard.place(x=490, y=70, width=81, height=363)

        CurrentWorkoutLabel = tk.Label(homeFrame)
        ft = tkFont.Font(family='Arial', size=10)
        CurrentWorkoutLabel["font"] = ft
        CurrentWorkoutLabel["fg"] = "#cec9c3"
        CurrentWorkoutLabel["justify"] = "center"
        CurrentWorkoutLabel["text"] = "label"
        CurrentWorkoutLabel.place(x=20, y=60, width=68, height=363)

    def SettingsButton_command(self):
        settingsFrame = tk.Frame(App._root)
        settingsFrame["bg"] = "#20dfff"
        App._homeFrame.pack_forget()
        settingsFrame.pack(fill="both", expand=True)

        print("settings command")

    def DropDownButton_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
