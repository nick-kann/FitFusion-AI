import tkinter as tk
import tkinter.font as tkFont
import os
import json
from tkinter import simpledialog
from tkinter import ttk
import customtkinter as ctk
import situp
import pushup
import jumpingjack
import squat
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

from json_generate import create

from ask_trainer import initialize


class App:
    saveData = ""
    ctk.set_default_color_theme("dark-blue")

    def __init__(self, root):
        # setting title
        root.title("FitFusion AI")
        App._root = root
        # setting window size
        App._width = 880
        App._height = 700
        width = App._width
        height = App._height
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        homeFrame = tk.Frame(root)
        App._homeFrame = homeFrame
        homeFrame["bg"] = "#36393e"
        homeFrame.pack(fill="both", expand=True)

        # SettingsButton = tk.Button(homeFrame)
        # SettingsButton["bg"] = "#6b6b6b"
        # ft = tkFont.Font(family='Arial', size=10)
        # SettingsButton["font"] = ft
        # # SettingsButton["fg"] = "#ffffff"
        # SettingsButton["justify"] = "center"
        # SettingsButton["text"] = "Settings"
        # SettingsButton.place(x=App._width-(600 - 530 + 9),
        #                      y=10, width=50, height=50)
        # SettingsButton["command"] = self.SettingsButton_command

        settingsButton = ctk.CTkButton(
            master=homeFrame, corner_radius=8, width=40, height=40, text="Prefs", font=ctk.CTkFont(family='Arial', size=10), anchor="w", command=self.SettingsButton_command)
        settingsButton.place(
            x=App._width-(600 - 530), y=13)
        # settingsButton.pack()

        options = ['squat', 'situp', 'pushup', 'jumpingjack']

        # create a Combobox widget and add it to the window
        # combo = ttk.Combobox(homeFrame, values=options)
        # combo.place(x=450, y=20, width=30, height=15)
        # combo.pack()
        combo = ctk.CTkComboBox(
            master=homeFrame, values=options, height=15, width=190)
        combo.place(x=350, y=5)

        combo.set(options[0])
        self.__comboDd__ = combo
        # TrainerButton = tk.Button(homeFrame)
        # TrainerButton["bg"] = "#6b6b6b"
        # ft = tkFont.Font(family='Arial', size=10)
        # TrainerButton["font"] = ft
        # # SettingsButton["fg"] = "#ffffff"
        # TrainerButton["justify"] = "center"
        # TrainerButton["text"] = "AI Trainer"
        # TrainerButton.place(x=App._width - 130,
        #                     y=App._height - 85, width=100, height=50)
        # TrainerButton["command"] = self.TrainerButton_command

        TrainerButton = ctk.CTkButton(
            master=homeFrame, text="AI Trainer", width=100, height=50, command=self.TrainerButton_command)
        TrainerButton.place(x=App._width - 125,
                            y=App._height - 60)

        # DropDownButton = tk.Button(homeFrame)
        # DropDownButton["bg"] = "#6b6b6b"
        # ft = tkFont.Font(family='Arial', size=10)
        # DropDownButton["font"] = ft
        # # DropDownButton["fg"] = "#ffffff"
        # DropDownButton["justify"] = "center"
        # DropDownButton["text"] = "Start Rep"
        # DropDownButton.place(x=20, y=10, width=100, height=25)
        # DropDownButton["command"] = self.DropDownButton_command

        DropDownButton = ctk.CTkButton(master=homeFrame, text="Start Counting reps!",
                                       width=175, height=50, command=self.DropDownButton_command, font=ctk.CTkFont(size=14))
        DropDownButton.place(x=20, y=10)

        # GoalLabel = tk.Label(homeFrame)
        # ft = tkFont.Font(family='Arial', size=10)
        # GoalLabel["font"] = ft
        # # GoalLabel["fg"] = "#333333"
        # GoalLabel["justify"] = "center"
        # GoalLabel["text"] = "Goal (# of reps):"
        # GoalLabel.place(x=340, y=30, width=130, height=30)

        GoalLabel = ctk.CTkLabel(
            master=homeFrame, text="Goal (# of reps):", width=130, height=30)
        GoalLabel.place(x=340, y=30)

        # GoalEntry = tk.Entry(homeFrame)
        # ft = tkFont.Font(family='Arial', size=10)
        # GoalEntry["borderwidth"] = "1px"
        # GoalEntry["font"] = ft
        # GoalEntry["justify"] = "center"
        # GoalEntry.insert(0, 10)
        # GoalEntry.place(x=470, y=30, width=70, height=30)

        GoalEntry = ctk.CTkEntry(master=homeFrame, width=70, height=30)
        GoalEntry.place(x=470, y=30)
        GoalEntry.insert(0, 10)

        App._workout_GoalEntry = GoalEntry

        canvas = tk.Canvas(homeFrame)
        canvas.place(x=10, y=70, width=860, height=520)

        AIMessageBoard = tk.Frame(canvas)
        ft = tkFont.Font(family='Arial', size=10)
        # AIMessageBoard["font"] = ft
        # AIMessageBoard["fg"] = "#cec9c3"
        # AIMessageBoard["justify"] = "center"
        # AIMessageBoard["text"] = "AI RECOMANDATION ANALYZATION MEOW"
        # AIMessageBoard.place(x=10, y=70, width=860, height=520)

        canvas.create_window((0, 0), window=AIMessageBoard, anchor=tk.NW)
        scrollbar = tk.Scrollbar(
            homeFrame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

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

        print(weeks[0]['Monday'])
        App._week1_days = weeks[0].keys()
        App._week2_days = weeks[1].keys()
        App._week3_days = weeks[2].keys()
        App._week4_days = weeks[3].keys()

        Week1Label = tk.Label(AIMessageBoard)
        ft = tkFont.Font(family='Arial', size=15, weight="bold")
        Week1Label["font"] = ft
        Week1Label["justify"] = "center"
        Week1Label["text"] = "Week 1"

        Week1Content = tk.Frame(AIMessageBoard)
        App._weekday_1_l = []
        ind = 0
        for weekday in App._week1_days:
            weekday_l = tk.Label(Week1Content)
            ft = tkFont.Font(family='Arial', size=10)
            weekday_l["font"] = ft
            weekday_l["text"] = weekday + ": " + weeks[0][weekday]
            weekday_l["wraplength"] = 250
            weekday_l["justify"] = "left"
            weekday_l.grid(row=ind, column=0, sticky=tk.W, pady=2)
            App._weekday_1_l.append(weekday_l)
            ind += 1

        Week2Label = tk.Label(AIMessageBoard)
        ft = tkFont.Font(family='Arial', size=15, weight="bold")
        Week2Label["font"] = ft
        Week2Label["justify"] = "center"
        Week2Label["text"] = "Week 2"

        Week2Content = tk.Frame(AIMessageBoard)
        App._weekday_2_l = []
        ind = 0
        for weekday in App._week2_days:
            weekday_l = tk.Label(Week2Content)
            ft = tkFont.Font(family='Arial', size=10)
            weekday_l["font"] = ft
            weekday_l["text"] = weekday + ": " + weeks[1][weekday]
            weekday_l["wraplength"] = 250
            weekday_l["justify"] = "left"
            weekday_l.grid(row=ind, column=0, sticky=tk.W, pady=2)
            App._weekday_2_l.append(weekday_l)
            ind += 1

        Week3Label = tk.Label(AIMessageBoard)
        ft = tkFont.Font(family='Arial', size=15, weight="bold")
        Week3Label["font"] = ft
        Week3Label["justify"] = "center"
        Week3Label["text"] = "Week 3"

        Week3Content = tk.Frame(AIMessageBoard)
        App._weekday_3_l = []
        ind = 0
        for weekday in App._week3_days:
            weekday_l = tk.Label(Week3Content)
            ft = tkFont.Font(family='Arial', size=10)
            weekday_l["font"] = ft
            weekday_l["text"] = weekday + ": " + weeks[2][weekday]
            weekday_l["wraplength"] = 250
            weekday_l["justify"] = "left"
            weekday_l.grid(row=ind, column=1, sticky=tk.W, pady=2)
            App._weekday_3_l.append(weekday_l)
            ind += 1

        Week4Label = tk.Label(AIMessageBoard)
        ft = tkFont.Font(family='Arial', size=15, weight="bold")
        Week4Label["font"] = ft
        Week4Label["justify"] = "center"
        Week4Label["text"] = "Week 4"

        Week4Content = tk.Frame(AIMessageBoard)
        App._weekday_4_l = []
        ind = 0
        for weekday in App._week4_days:
            weekday_l = tk.Label(Week4Content)
            ft = tkFont.Font(family='Arial', size=10)
            weekday_l["font"] = ft
            weekday_l["text"] = weekday + ": " + weeks[3][weekday]
            weekday_l["wraplength"] = 250
            weekday_l["justify"] = "left"
            weekday_l.grid(row=ind, column=1, sticky=tk.W, pady=2)
            App._weekday_4_l.append(weekday_l)
            ind += 1

        Week1Label.grid(row=0, column=0, sticky=tk.W, pady=2)
        Week1Content.grid(row=1, column=0, sticky=tk.W, pady=2)
        Week2Label.grid(row=0, column=1, sticky=tk.W, pady=2)
        Week2Content.grid(row=1, column=1, sticky=tk.W, pady=2)
        Week3Label.grid(row=2, column=0, sticky=tk.W, pady=2)
        Week3Content.grid(row=3, column=0, sticky=tk.W, pady=2)
        Week4Label.grid(row=2, column=1, sticky=tk.W, pady=2)
        Week4Content.grid(row=3, column=1, sticky=tk.W, pady=2)

        CurrentWorkoutLabel = tk.Label(homeFrame)
        ft = tkFont.Font(family='Arial', size=10)
        CurrentWorkoutLabel["font"] = ft
        CurrentWorkoutLabel["justify"] = "center"
        CurrentWorkoutLabel["text"] = "label"

        AIMessageBoard.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

    def TrainerButton_command(self):

        BG_GRAY = "#ABB2B9"
        BG_COLOR = "#17202A"
        TEXT_COLOR = "#EAECEE"

        FONT = "Helvetica 14"
        FONT_BOLD = "Helvetica 13 bold"

        trainerFrame = tk.Frame(App._root)
        trainerFrame["bg"] = "#36393e"
        App._homeFrame.pack_forget()
        trainerFrame.pack(fill="both", expand=True)
        App._trainerFrame = trainerFrame

        CloseButton = ctk.CTkButton(
            master=trainerFrame, width=80, height=50, command=self.CloseButtonTrainer_command, text="close")
        CloseButton.place(x=100, y=600)

        label1 = ctk.CTkLabel(master=trainerFrame, fg_color=BG_COLOR,
                              text="Welcome", pady=10, width=20, height=1, corner_radius=9)
        label1.place(x=440 - 70/2, y=20, )

        txt = ctk.CTkTextbox(trainerFrame, fg_color=BG_COLOR,
                             width=670, height=540, pady=2)
        txt.place(x=100, y=60)
        App._txt = txt

        send = ctk.CTkButton(trainerFrame, text="Send", width=50, height=50, fg_color="#000",
                             command=self.send_command)
        send.place(x=100+620, y=600, )

        e = ctk.CTkEntry(trainerFrame, fg_color="#2C3E50",
                         width=540, height=50)
        e.place(x=180, y=600)
        e.focus()
        App._e = e

        scrollbar = Scrollbar(txt)
        scrollbar.place(relheight=1, relx=0.974)

    def send_command(self):
        send = "You -> " + App._e.get()
        App._txt.insert(tk.END, "\n" + send)

        user_q = App._e.get().lower()

        response = initialize(user_q)

        App._e.delete(0, tk.END)

        App._txt.insert(tk.END, "\n" + "Bot -> " + response)

        pass

    def SettingsButton_command(self):

        with open('input.txt', 'r') as f:
            my_dict = {}

            for line in f:

                key, value = line.strip().split(': ')

                my_dict[key] = (int)(value)

        settingsFrame = tk.Frame(App._root)
        settingsFrame["bg"] = "#36393e"
        App._homeFrame.pack_forget()
        settingsFrame.pack(fill="both", expand=True)
        App._settingsFrame = settingsFrame

        labelEntry_x = 20
        weightEntry_x = labelEntry_x + 150
        weight_y = 20
        generalLabelWidth = 150
        generalEntryWidth = 100
        generalHeight = 30

        WeightEntry = ctk.CTkEntry(
            master=settingsFrame, width=generalEntryWidth, height=generalHeight)
        WeightEntry.place(x=weightEntry_x, y=weight_y)

        if(len(my_dict.keys()) == 7):
            WeightEntry.insert(0, my_dict['weight'])

        self._v_weightEntry = WeightEntry


        WeightLabel = ctk.CTkLabel(
            master=settingsFrame, width=generalLabelWidth, height=generalHeight, bg_color="#262626", corner_radius=19, text="Weight (lbs): ")
        WeightLabel.place(x=labelEntry_x, y=weight_y)

        HeightEntry = ctk.CTkEntry(
            master=settingsFrame, width=generalEntryWidth, height=generalHeight)
        HeightEntry.place(x=weightEntry_x, y=weight_y+50)
        if(len(my_dict.keys()) == 7):
            HeightEntry.insert(0, my_dict['height'])
        self._v_heightEntry = HeightEntry

        HeightLabel = ctk.CTkLabel(
            master=settingsFrame, width=generalLabelWidth, height=generalHeight, bg_color="#262626", corner_radius=19, text="Height (ft): ")
        HeightLabel.place(x=labelEntry_x, y=weight_y+50)
        HeightEntry.lift()

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


        GoalLabel = ctk.CTkLabel(
            master=settingsFrame, width=150, height=90, bg_color="#262626", corner_radius=19, text="Goal: ")
        GoalLabel.place(x=labelEntry_x, y=weight_y+110)


        ExpLabel = ctk.CTkLabel(
            master=settingsFrame, width=150, height=90, bg_color="#262626", corner_radius=19, text="Workout experience: ")
        ExpLabel.place(x=labelEntry_x, y=weight_y+220)

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

        TimeEntry = ctk.CTkEntry(
            master=settingsFrame, width=generalEntryWidth, height=generalHeight)
        TimeEntry.place(x=weightEntry_x, y=weight_y+340)
        if(len(my_dict.keys()) == 7):
            TimeEntry.insert(0, my_dict['time_available'])
        self._v_timeEntry = TimeEntry


        TimeLabel = ctk.CTkLabel(
            master=settingsFrame, width=generalLabelWidth, height=generalHeight, bg_color="#262626", corner_radius=19, text="Time per day (hrs): ")
        TimeLabel.place(x=labelEntry_x, y=weight_y+340)
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

        LocationLabel = ctk.CTkLabel(
            master=settingsFrame, width=generalLabelWidth, height=generalHeight*2, bg_color="#262626", corner_radius=19, text="Location: ")
        LocationLabel.place(x=labelEntry_x, y=weight_y+400)

        DaysEntry = ctk.CTkEntry(
            master=settingsFrame, width=generalEntryWidth, height=generalHeight)
        DaysEntry.place(x=weightEntry_x, y=weight_y+490)
        if(len(my_dict.keys()) == 7):
            DaysEntry.insert(0, my_dict['time_available'])
        self._v_daysEntry = DaysEntry

        DaysLabel = ctk.CTkLabel(
            master=settingsFrame, width=generalLabelWidth, height=generalHeight, bg_color="#262626", corner_radius=19, text="Max days per week: ")
        DaysLabel.place(x=labelEntry_x, y=weight_y+490)
        DaysEntry.lift()

        CloseButton = ctk.CTkButton(
            master=settingsFrame, command=self.SaveButton_command, width=100, height=50, text="Close")
        CloseButton.place(
            x=labelEntry_x, y=App._height - 60)

        SaveButton = ctk.CTkButton(
            master=settingsFrame, command=self.SaveButton_command, width=100, height=50, text="Save")
        SaveButton.place(
            x=App._width - (600 - (labelEntry_x + 340 + 130)), y=App._height - 60)

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
        goal = App._workout_GoalEntry.get()
        App._goal_val = goal
        exercise = self.__comboDd__.get()
        match exercise:
            case "situp":
                situp.start(goal)
                App._exercise = 1
                self.ShowResultsPage()
            case "pushup":
                pushup.start(goal)
                App._exercise = 0
                self.ShowResultsPage()
                print("push ups ended")
            case "squat":
                squat.start(goal)
                App._exercise = 3
                self.ShowResultsPage()
            case "jumpingjack":
                jumpingjack.start(goal)
                App._exercise = 2
                self.ShowResultsPage()
            case _:
                pass

    def ShowChoice(self):
        print(self)

    def ShowResultsPage(self):
        resultsFrame = tk.Frame(App._root)
        resultsFrame["bg"] = "#36393e"
        App._homeFrame.pack_forget()
        resultsFrame.pack(fill="both", expand=True)
        App._resultsFrame = resultsFrame

        ResultsLabel = tk.Label(resultsFrame)
        ft = tkFont.Font(family='Times', size=10)
        ResultsLabel["font"] = ft
        # ResultsLabel["fg"] = "#333333"
        ResultsLabel["justify"] = "center"
        ResultsLabel.place(x=440 - 800/2, y=20, width=800, height=560)

        with open('results.json', 'r') as f:
            data = json.load(f)

        results = "N/A"
        t_goal = "N/A"
        if(len(data[App._exercise]) != 0):
            results = data[App._exercise][len(data[App._exercise])-2]
            t_goal = data[App._exercise][len(data[App._exercise])-1]

        GoalHeader = tk.Label(ResultsLabel)
        ft = tkFont.Font(family='Times', size=20, weight="bold")
        GoalHeader["font"] = ft
        GoalHeader["justify"] = "left"
        GoalHeader["anchor"] = "w"
        GoalHeader["text"] = "Goal: " + str(t_goal) + " reps."
        GoalHeader.place(x=20, y=20, width=200, height=30)

        ResultsHeader = tk.Label(ResultsLabel)
        ft = tkFont.Font(family='Times', size=20, weight="bold")
        ResultsHeader["font"] = ft
        ResultsHeader["justify"] = "left"
        ResultsHeader["anchor"] = "w"
        ResultsHeader["wraplength"] = 250
        ResultsHeader["text"] = "Results: " + str(results) + " reps."
        ResultsHeader.place(x=20, y=100, width=200, height=30)

        if results <= 0.8 * t_goal:
            message = "Not quite enough- more work is needed!"
        elif results >= 1.2 * t_goal:
            message = "Nice! You exceeded your goal."
        else:
            message = "Nice! You met your goal."

        messageLabel = tk.Label(resultsFrame)
        ft = tkFont.Font(family='Times', size=10)
        messageLabel["font"] = ft
        messageLabel["justify"] = "center"
        messageLabel.place(x=440 - 800 / 2, y=420, width=700, height=100)

        resultsMessage = tk.Label(messageLabel)
        ft = tkFont.Font(family='Times', size=18, weight="bold")
        resultsMessage["font"] = ft
        resultsMessage["justify"] = "left"
        resultsMessage["anchor"] = "w"
        resultsMessage["text"] = message
        resultsMessage.place(x=20, y=20, width=700, height=120)

        CloseButton = ctk.CTkButton(
            master=resultsFrame, width=80, height=50, command=self.CloseButtonResults_command, text="close")
        CloseButton.place(x=30, y=app._height - 60)

        results_arr = []
        goals_arr = []

        for i in range(0, len(data[App._exercise])):
            if(i % 2 == 0):
                results_arr.append(data[App._exercise][i])
            else:
                goals_arr.append(data[App._exercise][i])
        x_axis = []
        for i in range(0, len(results_arr)):
            x_axis.append(i+1)

        y_axis = []
        for i in range(0, len(results_arr)):
            y_axis.append(results_arr[i]/goals_arr[i]*100)

        exercise_dict = {0: "push-ups", 1: "sit-ups",
                         2: "jumping jacks", 3: "squats"}

        print(y_axis)
        print(x_axis)
        fig, ax = plt.subplots()
        ax.set_ylim(0, max(y_axis))
        ax.set_xlim(0, len(results_arr))
        exercise_dict = {0: "push-ups", 1: "sit-ups",
                         2: "jumping jacks", 3: "squats"}

        plt.scatter(x_axis, y_axis)
        plt.plot(x_axis, y_axis)
        plt.xlabel(f"Workout number")
        plt.ylabel(f"Percent of goal completed")

        plt.grid(True)

        plt.savefig("graph1.png")

        test = ImageTk.PhotoImage(Image.open(
            "graph1.png").resize((450, 400), Image.ANTIALIAS))

        test = ImageTk.PhotoImage(Image.open(
            "graph1.png").resize((450, 400), Image.ANTIALIAS))

        label1 = tk.Label(resultsFrame, image=test)
        label1['bg'] = "#333033"
        label1.image = test

        label1.place(x=350, y=40)

    def CloseButton_command(self):
        App._settingsFrame.pack_forget()
        App._homeFrame.pack(fill="both", expand=True)

    def CloseButtonTrainer_command(self):
        App._trainerFrame.pack_forget()
        App._homeFrame.pack(fill="both", expand=True)

    def CloseButtonResults_command(self):
        App._resultsFrame.pack_forget()
        App._homeFrame.pack(fill="both", expand=True)

    def SaveButton_command(self):
        goal = self._v_goal.get()
        workExp = self._v_workExp.get()
        location = self._v_location.get()
        height = self._v_heightEntry.get()
        weight = self._v_weightEntry.get()
        time = self._v_timeEntry.get()
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

            create()
            
            with open("output.json") as f:
                data = json.load(f)

            # Organize workout plan into list of weeks
            weeks = []
            for week_key in data["workout_plan"]:
                week = {}
                for day_key, workout in data["workout_plan"][week_key].items():
                    week[day_key] = workout
                weeks.append(week)

            ind = 0
            for weekday in App._week1_days:
                weekday_l = App._weekday_1_l[ind]
                weekday_l["text"] = weekday + ": " + weeks[0][weekday]
                ind += 1

            ind = 0
            for weekday in App._week2_days:
                weekday_l = App._weekday_2_l[ind]
                weekday_l["text"] = weekday + ": " + weeks[1][weekday]
                ind += 1

            ind = 0
            for weekday in App._week3_days:
                weekday_l = App._weekday_3_l[ind]
                weekday_l["text"] = weekday + ": " + weeks[2][weekday]
                ind += 1

            ind = 0
            for weekday in App._week4_days:
                weekday_l = App._weekday_4_l[ind]
                weekday_l["text"] = weekday + ": " + weeks[3][weekday]
                ind += 1
            
            self.CloseButton_command()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
