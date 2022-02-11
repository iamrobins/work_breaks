import tkinter as tk
from tkinter.font import BOLD

class GUI:

    """
    Initiallizing an empty window, and minutes to minus one.
    """
    def __init__(self) -> None:

        # creating a window
        self.window = tk.Tk()
        # window properties: title, size, icon
        self.window.title("Work Breaks")
        self.window.iconbitmap('images/logo.png')
        self.window.geometry("410x140")
        self.window.configure(bg='#e6ccff')
        self.window.resizable(width=False, height=False)

        self.gui_font = 'arial'
        self.background_color = '#e6ccff'
        self.button_color = '#ffe6ff'
        self.button_color_hover = '#b3b3ff'
        
        self.minutes = -1

        self.repeat = -1

    def create_input_gui(self) -> None:       
        """ 
        Gets user's input from the textbox. The input is accepted if it is a positive number  
        greater than zero. Providing this input the graphic window, gets destroyed.
        """
        def get_input():
            try:
                self.minutes = int(user_input.get("1.0","end"))
                if (self.minutes > 0):
                    self.window.destroy()
                else:
                    invalid_input_message = tk.Label(self.window, text="please provide a valid number", 
                                                    bg=self.background_color, fg='red',font=(self.gui_font, 15))
                    invalid_input_message.grid(row=4, column=2)
            except:
                invalid_input_message = tk.Label(self.window, text="please provide a valid number",
                                                bg=self.background_color, fg='red', font=(self.gui_font, 15))
                invalid_input_message.grid(row=4, column=2)

        """
        Adds color to the button on hover
        """
        def on_enter(e):
            button['background'] = self.button_color_hover

        def on_leave(e):
            button['background'] = self.button_color

        # widgets
        # message
        label = tk.Label(self.window, text=' Enter your break preference in minutes', 
                        bg=self.background_color, font=(self.gui_font, 17))
        label.grid(row=0, column=1, columnspan=3)

        # text box to get the user's input
        user_input = tk.Text(self.window, height=1, width=15)
        user_input.grid(row=2, column=2, padx=10, pady=10)

        # submit button
        button = tk.Button(self.window, height=1, width=10, text="sumbit", command=get_input,
                            bg=self.button_color, font=((self.gui_font, 10, BOLD)))
        button.grid(row=3, column=2)

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

        self.window.mainloop()

    def create_continue_gui(self):
        """
        Gets user's input, for whether they want to keep receiving 
        notifications, or change the prefered time, from gui window
        """
        #Define a function to update the entry widget
        def yes_button_pressed():
            self.repeat = 1
            self.window.destroy()

        def no_button_pressed():
            self.repeat = 0
            self.window.destroy()

        def change_minutes():
            self.repeat = 2
            self.window.destroy()

        # button bind actions style
        def yes_on_enter(e):
            yes_button['background'] = self.button_color_hover

        def yes_on_leave(e):
            yes_button['background'] = self.button_color

        def no_on_enter(e):
            no_button['background'] = self.button_color_hover

        def no_on_leave(e):
            no_button['background'] = self.button_color

        def change_on_enter(e):
            change_minutes_button['background'] = self.button_color_hover

        def change_on_leave(e):
            change_minutes_button['background'] = self.button_color
        
        # widgets
        label = tk.Label(self.window, text=' Do you want to continue?', 
                        bg=self.background_color, font=(self.gui_font, 17), padx=1, pady=1)
        label.pack()

        yes_button = tk.Button(self.window, height=1, width=20, text="CONTINUE", command= yes_button_pressed,
                                bg=self.button_color, font=((self.gui_font, 10, BOLD)))
        yes_button.pack()

        no_button = tk.Button(self.window, height=1, width=20, text="EXIT", command= no_button_pressed,
                                bg=self.button_color, font=((self.gui_font, 10, BOLD)))
        no_button.pack()

        empty_label = tk.Label(self.window, text=" ", bg=self.background_color)
        empty_label.pack()

        change_minutes_button = tk.Button(self.window, height=1, width=20, text="CHANGE BRAKE", 
                                            command= change_minutes, bg=self.button_color, 
                                            font=((self.gui_font, 10, BOLD)))
        change_minutes_button.pack()

        # button binds
        yes_button.bind("<Enter>", yes_on_enter)
        yes_button.bind("<Leave>", yes_on_leave)
        no_button.bind("<Enter>", no_on_enter)
        no_button.bind("<Leave>", no_on_leave)
        change_minutes_button.bind("<Enter>", change_on_enter)
        change_minutes_button.bind("<Leave>", change_on_leave)

        self.window.mainloop()
