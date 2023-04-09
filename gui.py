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
        #SettingsButton["fg"] = "#ffffff"
        SettingsButton["justify"] = "center"
        SettingsButton["text"] = "Settings"
        SettingsButton.place(x=530, y=10, width=50, height=50)
        SettingsButton["command"] = self.SettingsButton_command

        DropDownButton = tk.Button(homeFrame)
        DropDownButton["bg"] = "#6b6b6b"
        ft = tkFont.Font(family='Arial', size=10)
        DropDownButton["font"] = ft
        #DropDownButton["fg"] = "#ffffff"
        DropDownButton["justify"] = "center"
        DropDownButton["text"] = "Button"
        DropDownButton.place(x=20, y=10, width=70, height=25)
        DropDownButton["command"] = self.DropDownButton_command

        AIMessageBoard = tk.Message(homeFrame)
        ft = tkFont.Font(family='Arial', size=10)
        AIMessageBoard["font"] = ft
        #AIMessageBoard["fg"] = "#cec9c3"
        AIMessageBoard["justify"] = "center"
        AIMessageBoard["text"] = "AI RECOMANDATION ANALYZATION MEOW"
        AIMessageBoard.place(x=490, y=70, width=81, height=363)

        CurrentWorkoutLabel = tk.Label(homeFrame)
        ft = tkFont.Font(family='Arial', size=10)
        CurrentWorkoutLabel["font"] = ft
        #CurrentWorkoutLabel["fg"] = "#cec9c3"
        CurrentWorkoutLabel["justify"] = "center"
        CurrentWorkoutLabel["text"] = "label"
        CurrentWorkoutLabel.place(x=20, y=60, width=68, height=363)

    def SettingsButton_command(self):

        settingsFrame = tk.Frame(App._root)
        settingsFrame["bg"] = "#20dfff"
        App._homeFrame.pack_forget()
        settingsFrame.pack(fill="both", expand=True)

        labelEntry_x = 20
        weightEntry_x = labelEntry_x + 150
        weight_y = 20
        generalLabelWidth = 150
        generalEntryWidth = 100
        generalHeight = 30

        WeightEntry=tk.Entry(settingsFrame)
        WeightEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        WeightEntry["font"] = ft
        #WeightEntry["fg"] = "#333333"
        WeightEntry["justify"] = "center"
        WeightEntry.place(x=weightEntry_x,y=weight_y,width=generalEntryWidth,height=generalHeight)

        WeightLabel=tk.Label(settingsFrame)
        ft = tkFont.Font(family='Times',size=10)
        WeightLabel["font"] = ft
        #WeightLabel["fg"] = "#333333"
        WeightLabel["justify"] = "center"
        WeightLabel["text"] = "Weight:"
        WeightLabel.place(x=labelEntry_x,y=weight_y,width=generalLabelWidth,height=generalHeight)

        HeightEntry=tk.Entry(settingsFrame)
        HeightEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        HeightEntry["font"] = ft
        #HeightEntry["fg"] = "#333333"
        HeightEntry["justify"] = "center"
        HeightEntry.place(x=weightEntry_x,y=weight_y + 50,width=100,height=generalHeight)

        HeightLabel=tk.Label(settingsFrame)
        ft = tkFont.Font(family='Times',size=10)
        HeightLabel["font"] = ft
        #HeightLabel["fg"] = "#333333"
        HeightLabel["justify"] = "center"
        HeightLabel["text"] = "Height:"
        HeightLabel.place(x=labelEntry_x,y=weight_y + 50,width=150,height=generalHeight)

        # r_button_options = {1: "cardio",
   	    #  2: "muscle toning",
    	#      3: "ab development",
        #      4: "bicep muscle development",
        #      5: "leg muscle development",
        #      6: "general muscle development"
        # }
        languages = [("cardio", 1),
   	     ("muscle toning", 2),
    	     ("ab development", 3),
             ("bicep muscle development", 4),
             ("leg muscle development", 5),
             ("general muscle development", 6),
        ]
        
        v = tk.IntVar()
        y = weight_y + 110
        ind = 0
        for language, val in languages:
            goal_rb = tk.Radiobutton(settingsFrame, 
                   text=language,
                   padx = 20, 
                   justify='left',
                   anchor='w',
                   variable=v,
                   value=val)
            goal_rb.pack(anchor=tk.W) 
            if(ind<3):  
                goal_rb.place(x=weightEntry_x, y=y, width = 170, height = generalHeight)
            else:
                if(ind==3):
                    y = weight_y + 110
                goal_rb.place(x=weightEntry_x*2, y=y, width = 220, height = generalHeight)
                
            y += generalHeight
            ind += 1
        
        GoalLabel=tk.Label(settingsFrame)
        ft = tkFont.Font(family='Times',size=10)
        GoalLabel["font"] = ft
        #GoalLabel["fg"] = "#333333"
        GoalLabel["justify"] = "center"
        GoalLabel["text"] = "Goal:"
        GoalLabel.place(x=labelEntry_x,y=weight_y + 110,width=150,height=90)

        

        ExpLabel=tk.Label(settingsFrame)
        ft = tkFont.Font(family='Times',size=10)
        ExpLabel["font"] = ft
        #ExpLabel["fg"] = "#333333"
        ExpLabel["justify"] = "center"
        ExpLabel["text"] = "Workout experience:"
        ExpLabel.place(x=labelEntry_x,y=weight_y + 220,width=150,height=90)

        experiences = [("no experience", 1),
   	     ("some experience", 2),
    	     ("extensive experience", 3)
        ]
        
        exp_v = tk.IntVar()
        y = weight_y + 220
        for experience, val in experiences:
            exp_rb = tk.Radiobutton(settingsFrame, 
                   text=experience,
                   padx = 20, 
                   justify='left',
                   anchor='w',
                   variable=exp_v,
                   value=val)
            exp_rb.pack(anchor=tk.W)  
            exp_rb.place(x=weightEntry_x, y=y, width = 190, height = generalHeight)
                
            y += generalHeight
            ind += 1

        TimeEntry=tk.Entry(settingsFrame)
        TimeEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        TimeEntry["font"] = ft
        #TimeEntry["fg"] = "#333333"
        TimeEntry["justify"] = "center"
        TimeEntry.place(x=weightEntry_x,y=weight_y + 340,width=generalEntryWidth,height=generalHeight)

        TimeLabel=tk.Label(settingsFrame)
        ft = tkFont.Font(family='Times',size=10)
        TimeLabel["font"] = ft
        #TimeLabel["fg"] = "#333333"
        TimeLabel["justify"] = "center"
        TimeLabel["text"] = "Time:"
        TimeLabel.place(x=labelEntry_x,y=weight_y + 340,width=generalLabelWidth,height=generalHeight)

        locations = [("gym", 1),
   	     ("home", 2)
        ]
        
        exp_l = tk.IntVar()
        y = weight_y + 400
        for location, val in locations:
            exp_l = tk.Radiobutton(settingsFrame, 
                   text=location,
                   padx = 20, 
                   justify='left',
                   anchor='w',
                   variable=exp_l,
                   value=val)
            exp_l.pack(anchor=tk.W)  
            exp_l.place(x=weightEntry_x, y=y, width = 340, height = generalHeight)
                
            y += generalHeight
            ind += 1

        LocationLabel=tk.Label(settingsFrame)
        ft = tkFont.Font(family='Times',size=10)
        LocationLabel["font"] = ft
        #LocationLabel["fg"] = "#333333"
        LocationLabel["justify"] = "center"
        LocationLabel["text"] = "Location:"
        LocationLabel.place(x=labelEntry_x,y=weight_y + 400,width=generalLabelWidth,height=generalHeight*2)


        print("settings command")

    def select_R_Button(self):
        print(self.opt_)

    def DropDownButton_command(self):
        print("command")
    
    def ShowChoice(self):
        print(self)



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()