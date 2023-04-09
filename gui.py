import tkinter as tk
import tkinter.font as tkFont
import os
import json
from tkinter import simpledialog


class App:
    saveData = ""

    def __init__(self, root):
        # setting title
        root.title("undefined")
        App._root = root
        # setting window size
        width = 600
        height = 700
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
        # SettingsButton["fg"] = "#ffffff"
        SettingsButton["justify"] = "center"
        SettingsButton["text"] = "Settings"
        SettingsButton.place(x=530, y=10, width=50, height=50)
        SettingsButton["command"] = self.SettingsButton_command

        TrainerButton = tk.Button(homeFrame)
        TrainerButton["bg"] = "#6b6b6b"
        ft = tkFont.Font(family='Arial', size=10)
        TrainerButton["font"] = ft
        # SettingsButton["fg"] = "#ffffff"
        TrainerButton["justify"] = "center"
        TrainerButton["text"] = "AI Trainer"
        TrainerButton.place(x=480, y=600, width=100, height=50)
        TrainerButton["command"] = self.TrainerButton_command

        DropDownButton = tk.Button(homeFrame)
        DropDownButton["bg"] = "#6b6b6b"
        ft = tkFont.Font(family='Arial', size=10)
        DropDownButton["font"] = ft
        # DropDownButton["fg"] = "#ffffff"
        DropDownButton["justify"] = "center"
        DropDownButton["text"] = "Button"
        DropDownButton.place(x=20, y=10, width=70, height=25)
        DropDownButton["command"] = self.DropDownButton_command

        AIMessageBoard = tk.Frame(homeFrame)
        ft = tkFont.Font(family='Arial', size=10)
        # AIMessageBoard["font"] = ft
        # AIMessageBoard["fg"] = "#cec9c3"
        # AIMessageBoard["justify"] = "center"
        # AIMessageBoard["text"] = "AI RECOMANDATION ANALYZATION MEOW"
        AIMessageBoard.place(x=310, y=70, width=260, height=500)

        # Load data from JSON file
        with open("output.json") as f:
            data = json.load(f)

        # Organize workout plan into list of weeks
        weeks = []
        for week_key in data["workout_plan"]:
            week = {}
            for day_key, workout in data["workout_plan"][week_key].items():
                week[day_key] = workout
            weeks.append(week)

        # Print the weeks and their workout plans
        #for i, week in enumerate(weeks):
            #print(f"Week {i+1}:")
            #for day, workout in week.items():
                #print(f"\t{day}: {workout}")
                

        print(weeks[0]['Monday'])
        week1_days = weeks[0].keys()

        Week1Label = tk.Label(AIMessageBoard)
        ft = tkFont.Font(family='Arial', size=15, weight="bold")
        Week1Label["font"] = ft
        Week1Label["justify"] = "center"
        Week1Label["text"] = "Week 1"
        Week1Label.pack(fill="both", expand=True)

        if 'Monday' in week1_days:
            Week1Monday= tk.Label(AIMessageBoard)
            ft = tkFont.Font(family='Arial', size=10)
            Week1Monday["font"] = ft
            Week1Monday["text"] = weeks[0]['Monday']
            Week1Monday["wraplength"] = 100
            Week1Monday["justify"] = "center"
            Week1Monday.pack(fill="both", expand=True)


        Week2Label = tk.Label(AIMessageBoard)
        ft = tkFont.Font(family='Arial', size=15, weight="bold")
        Week2Label["font"] = ft
        Week2Label["justify"] = "center"
        Week2Label["text"] = "Week 2"
        Week2Label.pack(fill="both", expand=True)

        Week3Label = tk.Label(AIMessageBoard)
        ft = tkFont.Font(family='Arial', size=15, weight="bold")
        Week3Label["font"] = ft
        Week3Label["justify"] = "center"
        Week3Label["text"] = "Week 3"
        Week3Label.pack(fill="both", expand=True)

        Week4Label = tk.Label(AIMessageBoard)
        ft = tkFont.Font(family='Arial', size=15, weight="bold")
        Week4Label["font"] = ft
        Week4Label["justify"] = "center"
        Week4Label["text"] = "Week 4"
        Week4Label.pack(fill="both", expand=True)

        CurrentWorkoutLabel = tk.Label(homeFrame)
        ft = tkFont.Font(family='Arial', size=10)
        CurrentWorkoutLabel["font"] = ft
        # CurrentWorkoutLabel["fg"] = "#cec9c3"
        CurrentWorkoutLabel["justify"] = "center"
        CurrentWorkoutLabel["text"] = "label"
        CurrentWorkoutLabel.place(x=20, y=60, width=68, height=363)

    def TrainerButton_command(self):
        pass



    def SettingsButton_command(self):

        with open('input.txt', 'r') as f:
            # Initialize an empty dictionary
            my_dict = {}

            # Iterate over each line in the file
            for line in f:
                # Split the line into key and value pairs

                key, value = line.strip().split(': ')

                # Add the key-value pair to the dictionary
                my_dict[key] = (int)(value)

        settingsFrame = tk.Frame(App._root)
        settingsFrame["bg"] = "#20dfff"
        App._homeFrame.pack_forget()
        settingsFrame.pack(fill="both", expand=True)
        App._settingsFrame = settingsFrame

        labelEntry_x = 20
        weightEntry_x = labelEntry_x + 150
        weight_y = 20
        generalLabelWidth = 150
        generalEntryWidth = 100
        generalHeight = 30

        WeightEntry = tk.Entry(settingsFrame)
        WeightEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        WeightEntry["font"] = ft
        # WeightEntry["fg"] = "#333333"
        WeightEntry["justify"] = "center"
        WeightEntry.place(x=weightEntry_x, y=weight_y,
                          width=generalEntryWidth, height=generalHeight)
        if(len(my_dict.keys()) == 7):
            WeightEntry.insert(0, my_dict['weight'])

        self._v_weightEntry = WeightEntry

        WeightLabel = tk.Label(settingsFrame)
        ft = tkFont.Font(family='Times', size=10)
        WeightLabel["font"] = ft
        # WeightLabel["fg"] = "#333333"
        WeightLabel["justify"] = "center"
        WeightLabel["text"] = "Weight:"
        WeightLabel.place(x=labelEntry_x, y=weight_y,
                          width=generalLabelWidth, height=generalHeight)
        WeightEntry.lift()
        WeightEntry.focus()

        HeightEntry = tk.Entry(settingsFrame)
        HeightEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        HeightEntry["font"] = ft
        # HeightEntry["fg"] = "#333333"
        HeightEntry["justify"] = "center"
        HeightEntry.place(x=weightEntry_x, y=weight_y + 50,
                          width=100, height=generalHeight)
        if(len(my_dict.keys()) == 7):
            HeightEntry.insert(0, my_dict['height'])
        self._v_heightEntry = HeightEntry

        HeightLabel = tk.Label(settingsFrame)
        ft = tkFont.Font(family='Times', size=10)
        HeightLabel["font"] = ft
        # HeightLabel["fg"] = "#333333"
        HeightLabel["justify"] = "center"
        HeightLabel["text"] = "Height:"
        HeightLabel.place(x=labelEntry_x, y=weight_y + 50,
                          width=150, height=generalHeight)
        HeightEntry.lift()

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

        self._v_goal = tk.IntVar()
        y = weight_y + 110
        goal_rbuttons = [0, 0, 0, 0, 0, 0]
        ind = 0
        for language, val in languages:
            goal_rb = tk.Radiobutton(settingsFrame,
                                     text=language,
                                     padx=20,
                                     justify='left',
                                     anchor='w',
                                     variable=self._v_goal,
                                     value=val)
            goal_rb.pack(anchor=tk.W)
            goal_rbuttons[ind] = goal_rb
            if(ind < 3):
                goal_rb.place(x=weightEntry_x, y=y,
                              width=170, height=generalHeight)
            else:
                if(ind == 3):
                    y = weight_y + 110
                goal_rb.place(x=weightEntry_x*2, y=y,
                              width=220, height=generalHeight)

            y += generalHeight
            ind += 1
        if(len(my_dict.keys()) == 7):
            goal_rbuttons[my_dict['goal']-1].select()

        GoalLabel = tk.Label(settingsFrame)
        ft = tkFont.Font(family='Times', size=10)
        GoalLabel["font"] = ft
        # GoalLabel["fg"] = "#333333"
        GoalLabel["justify"] = "center"
        GoalLabel["text"] = "Goal:"
        GoalLabel.place(x=labelEntry_x, y=weight_y + 110, width=150, height=90)

        ExpLabel = tk.Label(settingsFrame)
        ft = tkFont.Font(family='Times', size=10)
        ExpLabel["font"] = ft
        # ExpLabel["fg"] = "#333333"
        ExpLabel["justify"] = "center"
        ExpLabel["text"] = "Workout experience:"
        ExpLabel.place(x=labelEntry_x, y=weight_y + 220, width=150, height=90)

        experiences = [("no experience", 1),
                       ("some experience", 2),
                       ("extensive experience", 3)
                       ]
        # WORKOUT EXPERIENCE

        self._v_workExp = tk.IntVar()
        y = weight_y + 220
        exp_rbuttons = [0, 0, 0]
        ind = 0
        for experience, val in experiences:
            exp_rb = tk.Radiobutton(settingsFrame,
                                    text=experience,
                                    padx=20,
                                    justify='left',
                                    anchor='w',
                                    variable=self._v_workExp,
                                    value=val)
            exp_rb.pack(anchor=tk.W)
            exp_rb.place(x=weightEntry_x, y=y, width=190, height=generalHeight)
            exp_rbuttons[ind] = exp_rb
            y += generalHeight
            ind += 1
        if(len(my_dict.keys()) == 7):
            exp_rbuttons[my_dict['experience']-1].select()

        TimeEntry = tk.Entry(settingsFrame)
        TimeEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        TimeEntry["font"] = ft
        # TimeEntry["fg"] = "#333333"
        TimeEntry["justify"] = "center"
        TimeEntry.place(x=weightEntry_x, y=weight_y + 340,
                        width=generalEntryWidth, height=generalHeight)
        if(len(my_dict.keys()) == 7):
            TimeEntry.insert(0, my_dict['time_available'])
        self._v_timeEntry = TimeEntry

        TimeLabel = tk.Label(settingsFrame)
        ft = tkFont.Font(family='Times', size=10)
        TimeLabel["font"] = ft
        # TimeLabel["fg"] = "#333333"
        TimeLabel["justify"] = "center"
        TimeLabel["text"] = "Time:"
        TimeLabel.place(x=labelEntry_x, y=weight_y + 340,
                        width=generalLabelWidth, height=generalHeight)

        locations = [("gym", 1),
                     ("home", 2)
                     ]

        # LOCATION
        self._v_location = tk.IntVar()
        y = weight_y + 400
        location_rbuttons = [0, 0]
        ind = 0
        for location, val in locations:
            l_rb = tk.Radiobutton(settingsFrame,
                                  text=location,
                                  padx=20,
                                  justify='left',
                                  anchor='w',
                                  variable=self._v_location,
                                  value=val)
            l_rb.pack(anchor=tk.W)
            l_rb.place(x=weightEntry_x, y=y, width=340, height=generalHeight)
            location_rbuttons[ind] = l_rb
            y += generalHeight
            ind += 1
        if(len(my_dict.keys()) == 7):
            location_rbuttons[my_dict['location']-1].select()

        LocationLabel = tk.Label(settingsFrame)
        ft = tkFont.Font(family='Times', size=10)
        LocationLabel["font"] = ft
        # LocationLabel["fg"] = "#333333"
        LocationLabel["justify"] = "center"
        LocationLabel["text"] = "Location:"
        LocationLabel.place(x=labelEntry_x, y=weight_y + 400,
                            width=generalLabelWidth, height=generalHeight*2)

        DaysEntry = tk.Entry(settingsFrame)
        DaysEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        DaysEntry["font"] = ft
        # DaysEntry["fg"] = "#333333"
        DaysEntry["justify"] = "center"
        DaysEntry.place(x=weightEntry_x, y=weight_y + 490,
                        width=generalEntryWidth, height=generalHeight)
        if(len(my_dict.keys()) == 7):
            DaysEntry.insert(0, my_dict['time_available'])
        self._v_daysEntry = DaysEntry

        DaysLabel = tk.Label(settingsFrame)
        ft = tkFont.Font(family='Times', size=10)
        DaysLabel["font"] = ft
        # DaysLabel["fg"] = "#333333"
        DaysLabel["justify"] = "center"
        DaysLabel["text"] = "Days per week:"
        DaysLabel.place(x=labelEntry_x, y=weight_y + 490,
                        width=generalLabelWidth, height=generalHeight)
        DaysEntry.lift()

        CloseButton = tk.Button(settingsFrame)
        CloseButton["bg"] = "#6b6b6b"
        ft = tkFont.Font(family='Arial', size=10)
        CloseButton["font"] = ft
        # CloseButton["fg"] = "#ffffff"
        CloseButton["justify"] = "center"
        CloseButton["text"] = "close"
        CloseButton.place(x=labelEntry_x, y=weight_y +
                          550, width=80, height=50)
        CloseButton["command"] = self.CloseButton_command

        SaveButton = tk.Button(settingsFrame)
        SaveButton["bg"] = "#6b6b6b"
        ft = tkFont.Font(family='Arial', size=10)
        SaveButton["font"] = ft
        # SaveButton["fg"] = "#ffffff"
        SaveButton["justify"] = "center"
        SaveButton["text"] = "save"
        SaveButton.place(x=labelEntry_x + 340 + 140,
                         y=weight_y + 550, width=80, height=50)
        SaveButton["command"] = self.SaveButton_command

        WeightEntry.lift()
        HeightEntry.lift()
        TimeEntry.lift()
        DaysEntry.lift()

        print("settings command")
        # intializing values from file
        try:
            with open("input.json", "r") as f:
                if os.path.getsize("input.json") > 0:
                    for line in f:
                        print(line)
        except Exception:
            pass

    def select_R_Button(self):
        print(self.opt_)

    def DropDownButton_command(self):
        print("command")

    def ShowChoice(self):
        print(self)

    def CloseButton_command(self):
        App._settingsFrame.pack_forget()
        App._homeFrame.pack(fill="both", expand=True)

    def SaveButton_command(self):
        # print(self._v_goal.get())
        goal = self._v_goal.get()
        # print(self._v_workExp.get())
        workExp = self._v_workExp.get()
        # print(self._v_location.get())
        location = self._v_location.get()
        # print(self._v_heightEntry.get())
        height = self._v_heightEntry.get()
        # print(self._v_weightEntry.get())
        weight = self._v_weightEntry.get()
        # print(self._v_timeEntry.get())
        time = self._v_timeEntry.get()
        # print(self._v_daysEntry.get())
        days = self._v_daysEntry.get()
        if weight == "" or height == "" or time == "" or workExp == 0 or location == 0 or weight == 0 or days == "":
            print("not valid do not submit try again")
        else:
            f = open("input.txt", 'w')
            # f.write("goal", )

            """f.write("{")
            f.write("\"weight\": " + str(weight) + ",")
            f.write("\"height\": " + str(height) + ",")
            f.write("\"goal\": " + str(goal)+ ",")
            f.write("\"experience\": " + str(workExp)+ ",")
            f.write("\"time_available\": " + str(time)+ ",")
            f.write("\"location\": " + str(location)+ ",")
            f.write("\"days_per_week\": " + str(days))
            f.write("}")
            f.write(" ")
            f.close()"""
            f.write("weight: " + str(weight) + "\n")
            f.write("height: " + str(height) + "\n")
            f.write("goal: " + str(goal) + "\n")
            f.write("experience: " + str(workExp) + "\n")
            f.write("time_available: " + str(time) + "\n")
            f.write("location: " + str(location) + "\n")
            f.write("days_per_week: " + str(days) + "\n")
            f.close()

            self.CloseButton_command()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
