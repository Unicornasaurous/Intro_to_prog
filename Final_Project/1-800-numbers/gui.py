from tkinter import *
from tkinter import colorchooser
from stringtools import StrTools as tools
from phoneword import converter, inv_converter, map
import json

#Open the config file and convert it to a python dict
fileobj = open("config.json", "r")
config = json.load(fileobj)
fileobj.close()

#lists to store widget objects for configuration
accent_color_group = []
background_color_group = []
button_color_group = []

dict_of_groups = {"accent": accent_color_group,
                  "background": background_color_group,
                  "button": button_color_group}



class App(Tk):
    """The main window of the app -- inherits from Tk() class 
    from module tkinter"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #App configuration
        accent_color_group.append(self)
        self.config(bg=config["Accent Color"])
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.title("Phone Word Converter")
        #self.minsize(self.winfo_screenwidth(), self.winfo_screenheight())

        #Create widgets
        self.tab_bar = TabBar(self, 
                              highlightthickness=0,
                              name="thing")
        self.live_converter = LiveConvert(self)
        self.converter = Converter(self)
        self.settings = Settings(self)

        #Place widgets in grid
        self.tab_bar.grid(column=0, row=0, sticky="nw")
        self.settings.grid(column=0, row=1, sticky="wens")
        self.live_converter.grid(column=0, row=1, sticky="wens")
        self.converter.grid(column=0, row=1, sticky="wens")
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.converter.tkraise()

        self.allocate_children()
    
    def allocate_children(self):
        """Method iterates through the various
        widget objects within the app and logicaly
        determines which group to append them to for 
        color scheme configuration. Note: This solution
        is a bit convoluted, and there is probably a better 
        way to go about this."""
        for child in self.winfo_children()[1:]:
            background_color_group.append(child)
            for childschild in child.winfo_children():
                if "label" in str(childschild) \
                    and "conversion" not in str(childschild) or\
                        "checkbutton" in str(childschild):
                    accent_color_group.append(childschild)
                elif "button" in str(childschild) and\
                    "checkbutton" not in str(childschild):
                    button_color_group.append(childschild)
                elif "canvas" in str(childschild):
                    accent_color_group.append(childschild)
                elif "frame" in str(childschild):
                    background_color_group.append(childschild)
                else:
                    pass
        for child in self.tab_bar.winfo_children():
            if str(child) != ".thing.!button3":
                accent_color_group.append(child)
            else:
                background_color_group.append(child)
        for child in self.converter.keyboard.winfo_children():
            for childschild in child.winfo_children():
                button_color_group.append(childschild)
        for child in self.converter.keypad.winfo_children():
            button_color_group.append(child)
        for child in self.settings.color_scheme_parent.winfo_children():
            if "label" in str(child):
                accent_color_group.append(child)


class TabBar(Frame):
    """Tab bar widget for changing between app tabs"""
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        #Create widgets
        self.reg_convert_butt = Button(self, text="Converter", bd=0,
                                       bg=config["Background Color"], 
                                       command=lambda:self.reg_convert(master), 
                                       highlightthickness=0, 
                                       height=2,
                                       font=("Arial", 12))
        self.live_convert_butt = Button(self, text="Live Converter", bd=0, 
                                        command=lambda:self.live_convert(master),
                                        highlightthickness=0, 
                                        height=2,
                                        bg=config["Accent Color"],
                                        font=("Arial", 12))
        self.settings_butt = Button(self, text="Settings", bd=0, 
                                        command=lambda:self.settings(master),
                                        highlightthickness=0, 
                                        height=2,
                                        bg=config["Accent Color"],
                                        font=("Arial", 12))

        #Place widgets in grid
        self.reg_convert_butt.grid(column=0, row=0)
        self.live_convert_butt.grid(column=1, row=0)
        self.settings_butt.grid(column=2, row=0)


    def reg_convert(self, master):
        """Changes tab colors appropriately and raises 
        the Converter widget to the top of the stack"""
        self.live_convert_butt.config(bg=config["Accent Color"])
        self.reg_convert_butt.config(bg=config["Background Color"])
        self.settings_butt.config(bg=config["Accent Color"])
        master.converter.tkraise()


    def live_convert(self, master):
        """Changes tab colors appropriately and raises 
        the LiveConvert widgetto the top of the stack"""
        self.reg_convert_butt.config(bg=config["Accent Color"])
        self.live_convert_butt.config(bg=config["Background Color"])
        self.settings_butt.config(bg=config["Accent Color"])
        master.live_converter.tkraise()

    def settings(self, master):
        self.reg_convert_butt.config(bg=config["Accent Color"])
        self.live_convert_butt.config(bg=config["Accent Color"])
        self.settings_butt.config(bg=config["Background Color"])
        master.settings.tkraise()

class Settings(Frame):
    """This is the settings widget. It currently allows you to
    change the color scheme of the enitre app"""
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        #Widget configuration
        self.config(bg=config["Background Color"])
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        #Settings variables
        self.chosen_accent = StringVar(self, config["Accent Color"])
        self.chosen_background = StringVar(self, config["Background Color"])
        self.chosen_buttoncolor = StringVar(self, config["Button Color"])
        
        #Create parent Frames
        self.color_scheme_parent = Frame(self, 
                                    highlightthickness=2, 
                                    highlightbackground=config["Accent Color"],
                                    bg=config["Background Color"])
        self.color_scheme_parent.columnconfigure(1, weight=1)
        self.color_scheme_parent.config(padx=15, pady=15)

        #Create widgets
        self.color_scheme_label = Label(self,
                                   text="Color Scheme",
                                   bg=config["Accent Color"],
                                   font=("Arial", 12))
        self.accent_color_label = Label(self.color_scheme_parent,
                                   text="Accent Color:",
                                   bg=config["Accent Color"],
                                   font=("Arial", 12))
        self.accent_color_butt = Button(self.color_scheme_parent,
                                   width=2,
                                   height=2,
                                   bg=config["Accent Color"],
                                   command=self.choose_accent,
                                   highlightbackground="black")
        self.background_color_label = Label(self.color_scheme_parent,
                                       text="Background Color:",
                                       bg=config["Accent Color"],
                                       font=("Arial", 12))
        self.background_color_butt = Button(self.color_scheme_parent,
                                   width=2,
                                   height=2,
                                   bg=config["Background Color"],
                                   command=self.choose_background,
                                   highlightbackground="black")
        self.button_color_label = Label(self.color_scheme_parent,
                                       text="Button Color:",
                                       bg=config["Accent Color"],
                                       font=("Arial", 12))
        self.button_color_butt = Button(self.color_scheme_parent,
                                   width=2,
                                   height=2,
                                   bg=config["Button Color"],
                                   command=self.choose_buttoncolor,
                                   highlightbackground="black")
        self.apply_butt = Button(self,
                                 text="Apply",
                                 command=self.apply_settings,
                                 font=("Arial", 12),
                                 bg=config["Button Color"],
                                 highlightthickness=0)
        self.default_butt = Button(self,
                                 text="Reset to default",
                                 command=self.apply_settings,
                                 font=("Arial", 12),
                                 bg=config["Button Color"],
                                 highlightthickness=0)       
        #Place widgets in the grid
        self.color_scheme_parent.grid(column=1, row=1, sticky="wens")
        self.color_scheme_label.grid(column=1, row=0, sticky="s")
        self.accent_color_label.grid(column=0, row=0, sticky="w")
        self.accent_color_butt.grid(column=1, row=0, sticky="w")
        self.background_color_label.grid(column=0, row=1, sticky="w")
        self.background_color_butt.grid(column=1, row=1, sticky="w")
        self.button_color_label.grid(column=0, row=2, sticky="w")
        self.button_color_butt.grid(column=1, row=2, sticky="w")
        self.apply_butt.grid(column=1, row=2)
        self.default_butt.grid(column=1, row=2, sticky="e")
        


    def apply_settings(self):
        file = open("config.json", "w")
        config["Accent Color"] = self.chosen_accent.get()
        config["Background Color"] = self.chosen_background.get()
        config["Button Color"] = self.chosen_buttoncolor.get()
        json_config = json.dumps(config, indent=1)
        file.write(json_config)
        file.close()
        for group in dict_of_groups:
            for widget in dict_of_groups[group]:
                if group == "accent":
                    widget.config(bg=config["Accent Color"])
                elif group == "background":
                    widget.config(bg=config["Background Color"],
                                  highlightbackground=config["Accent Color"])
                elif group == "button":
                    widget.config(bg=config["Button Color"])

    def choose_accent(self):
        chosen_color = colorchooser.askcolor()[1]
        if chosen_color != None:
            self.chosen_accent.set(chosen_color)
            self.accent_color_butt.config(bg=chosen_color)
        else:
            pass

    def choose_background(self):
        chosen_color = colorchooser.askcolor()[1]
        if chosen_color != None:
            self.chosen_background.set(chosen_color)
            self.background_color_butt.config(bg=chosen_color)
        else:
            pass

    def choose_buttoncolor(self):
        chosen_color = colorchooser.askcolor()[1]
        if chosen_color != None:
            self.chosen_buttoncolor.set(chosen_color)
            self.button_color_butt.config(bg=chosen_color)
        else:
            pass


class LiveConvert(Frame):
    """Widget converts phoneword to phonenumber as
    characters are entered, hence the name 
    'LiveConvert'"""
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        #Widget configuration
        self.config(bg=config["Background Color"])
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)

        #Create widgets
        self.entry_label = Label(self, text="Enter Phoneword", bg=config["Accent Color"],
                            font=("Arial", 15))
        self.phoneword_entry_box = Entry(self, font=("Arial", 50))
        self.conversion_label = Label(self, text="Conversion", bg=config["Accent Color"],
                                 font=("Arial", 15))
        self.conversion = Label(self, bg="white", 
                                font=("Arial", 50), 
                                anchor="w",
                                name="conversion")
        self.copy_button = Button(self, 
                                  text="Copy", 
                                  font=("Arial", 20),
                                  command=lambda: self.copy_to_clip(master),
                                  bg=config["Button Color"],
                                  highlightthickness=0)
        
        #Create appropriate bindings
        self.phoneword_entry_box.bind("<KeyPress>", self.key_convert)
        self.phoneword_entry_box.bind("<KeyPress-BackSpace>", self.backspace)

        #Place widgets in grid
        self.entry_label.grid(column=1, row=0, sticky="s")
        self.phoneword_entry_box.grid(column=1, row=1, sticky="sew")
        self.conversion_label.grid(column=1, row=2)
        self.conversion.grid(column=1, row=3, sticky="new")
        self.copy_button.grid(column=1, row=3, sticky="ne")

    def key_convert(self, event):
        """Takes each key value entered and
        converts it, placing it in the conversion label"""
        converted_num = converter(event.char)
        self.conversion.config(text=self.conversion["text"] + converted_num)
    
    def backspace(self, event):
        """When backspace detected, deletes the most recent
        converted key value"""
        self.conversion.config(text=tools.char_remove(
                                     self.conversion["text"], -1))

    def copy_to_clip(self, master):
        """Copies the contents of the conversion to the 
        user's clipboard. It then shows an app message, which fades 
        after some time"""
        self.clipboard_clear()
        self.clipboard_append(self.conversion["text"])
        master.copy_message = AppMessage(master, 
                                text="Copied to clipboard!",
                                font=30,
                                bg=config["Accent Color"])
        self.after(500, master.copy_message.message_fadeout)


class Converter(Frame):
    """Widget for converting and inversely converting
    phoneword to phone number and phonenumber to phoneword
    respectively."""
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        #Widget configuration
        self.config(bg=config["Background Color"])
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=5)
        self.columnconfigure(3, weight=10)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=5)
        self.rowconfigure(5, weight=8)

        #Tkinter variables
        self.text = StringVar()
        self.check_value = IntVar()
        self.is_flipped = BooleanVar(self, False)

        #Create widgets
        self.enter_label = Label(self, text="Enter Phoneword", bg=config["Accent Color"],
                                 font=("Arial", 15))
        self.conversion_entry = Entry(self, font=("Arial", 25),
                                      textvariable=self.text,
                                      justify=CENTER)
        self.flip_img_canvas = Canvas(self, width=50, height=50, 
                                      bg=config["Accent Color"], highlightthickness=1,
                                      highlightbackground="black",
                                      relief=RAISED,
                                      bd=1
                                      )
        self.conversion_label = Label(self, bg=config["Accent Color"], text="Phonenumber:",
                                      font=("Arial", 15))
        self.conversion = Label(self, bg="white", font=("Arial", 25),
                                name="conversion")
        self.copy_button = Button(self, text="Copy", 
                                  command=lambda:self.copy_to_clip(master),
                                  font=("Arial", 12),
                                  bg=config["Button Color"],
                                  highlightthickness=0)
        self.keypad = Keypad(self, highlightthickness=0,)
        self.enter_button = Button(self, text="Enter", font=("Arial", 18),
                                   width=10, command=self.convert,
                                   bg=config["Button Color"],
                                   highlightthickness=0)
        self.check_button = Checkbutton(self,
                                        text="Display full conversions\
                                        of phonenumber to phoneword",
                                        bg=config["Accent Color"],
                                        highlightthickness=0,
                                        font=("Arial", 13),
                                        wraplength=300,
                                        variable=self.check_value,
                                        command=self.inv_convert)
        self.keyboard = Keyboard(self, highlightcolor="white", 
                                 highlightthickness=0)

        #Create image object(s)
        self.flip_image = PhotoImage(file="assets/flip-resized.png")
        self.flip_img_canvas.create_image((26,26), image=self.flip_image)

        #Create appropriate bindings
        self.flip_img_canvas.bind("<Button-1>", self.flip)
        self.flip_img_canvas.bind("<ButtonRelease-1>", self.flip_release)

        #Place widgets in grid
        self.enter_label.grid(column=1, row=0, sticky="s")
        self.conversion_entry.grid(column=1, row=1, sticky="wens")
        self.flip_img_canvas.grid(column=2, row=1, rowspan=3)
        self.conversion_label.grid(column=1, row=2, sticky="s")
        self.conversion.grid(column=1, row=3, sticky="wens")
        self.copy_button.grid(column=1, row=3, sticky="nes")
        self.keypad.grid(column=3, row=0, rowspan=6, sticky="wens")
        self.enter_button.grid(column=1, row=4, sticky="s")
        self.keyboard.grid(column=1, row=5, sticky="wes")
    
    def convert(self):
        """Converts phoneword in the Entry widget to 
        phonenumber, which is displayed in its appropriate label"""
        text_to_convert = self.conversion_entry.get()
        self.conversion.config(text=converter(text_to_convert))
    
    def inv_convert(self):
        """Converts number in the Entry widget to 
        phoneword, which is displayed in its appropriate label
        -- Note that there are two options. The first, when
        the checkbox is not checked, shows a randomly chosen
        letter out of the appropriate conversion to use in the 
        phoneword. The other, when the checkbox is checked, displays
        all possible letters that each respective number could be in the
        form of '(...)'"""
        text_to_convert = self.conversion_entry.get()
        if self.check_value.get() == 0:
            self.conversion.config(text=inv_converter(text_to_convert))
        else:
            self.conversion.config(text=inv_converter(text_to_convert, full=True))

    def flip(self, event):
        """Method inverts the conversion"""
        self.flip_img_canvas.config(relief=SUNKEN)
        if self.is_flipped.get():
            self.is_flipped.set(False)
            self.enter_label.config(text="Enter Phoneword")
            self.conversion_label.config(text="Phonenumber:")
            self.enter_button.config(command=self.convert)
            self.check_button.grid_remove()
            self.convert()
        else:
            self.is_flipped.set(True)
            self.enter_label.config(text="Enter Phonenumber")
            self.conversion_label.config(text="Phoneword:")
            self.enter_button.config(command=self.inv_convert)
            self.check_button.grid(column=1, row=4, sticky="e")
            self.inv_convert()
        
    def flip_release(self, event):
        """Changes the border of the flip button when released"""
        self.flip_img_canvas.config(relief=RAISED)
    
    def copy_to_clip(self, master):
        """Copies the contents of the conversion to the 
        user's clipboard. It then shows an app message, which fades 
        after some time"""
        self.clipboard_clear()
        self.clipboard_append(self.conversion["text"])
        master.copy_message = AppMessage(master, 
                                text="Copied to clipboard!",
                                font=30,
                                bg=config["Accent Color"])
        self.after(500, master.copy_message.message_fadeout)

    
class Keypad(Frame):
    """This is a tkinter widget class. It is a 
    3 by 4 number keypad"""
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        #Widget configuration
        background_color_group.append(self)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        #Constants
        self.buttonheight = 3
        self.buttonwidth = 5
        self.font = ("Arial", 20)

        #Creates the buttons programatically and 
        #stores them in a nested dictionary based on 
        #row and column
        number_grid_dict = {}
        counter=0
        for row in range(4):
            number_grid_dict[row] = {}
            for column in range(3):
                counter+=1
                if row==3 and column==0:
                    number_grid_dict[row][column] = Button(self, 
                                                           text="*", 
                                                           padx=0, 
                                                           pady=0, 
                                                           font=self.font, 
                                                           height=self.buttonheight, 
                                                           width=self.buttonwidth,
                                                           bg=config["Button Color"],
                                                           highlightthickness=0)
                    number_grid_dict[row][column].bind("<Button-1>", 
                                                       lambda event:self.keypress(event, master))
                elif row==3 and column==1:
                    number_grid_dict[row][column] = Button(self, 
                                                           text="0", 
                                                           padx=0, 
                                                           pady=0, 
                                                           font=self.font, 
                                                           height=self.buttonheight, 
                                                           width=self.buttonwidth,
                                                           bg=config["Button Color"],
                                                           highlightthickness=0)
                    number_grid_dict[row][column].bind("<Button-1>",
                                                       lambda event:self.keypress(event, master))
                elif row==3 and column==2:
                    number_grid_dict[row][column] = Button(self, 
                                                           text="#", 
                                                           padx=0, 
                                                           pady=0, 
                                                           font=self.font, 
                                                           height=self.buttonheight,
                                                           width=self.buttonwidth,
                                                           bg=config["Button Color"],
                                                           highlightthickness=0)
                    number_grid_dict[row][column].bind("<Button-1>", 
                                                       lambda event:self.keypress(event, master))
                else:
                    number_grid_dict[row][column] = Button(self, 
                                                           text=str(counter), 
                                                           padx=0, 
                                                           pady=0, 
                                                           font=self.font, 
                                                           height=self.buttonheight, 
                                                           width=self.buttonwidth,
                                                           bg=config["Button Color"],
                                                           highlightthickness=0)
                    number_grid_dict[row][column].bind("<Button-1>", 
                                                       lambda event:self.keypress(event, master))
        
        #Places the buttons in the grid
        for row in number_grid_dict:
            for column in number_grid_dict[row]:
                number_grid_dict[row][column].grid(row=row, 
                                                   column=column, 
                                                   sticky="wens")
    
    def keypress(self, event, master):
        """What happens when you press a button"""
        button_value = event.widget["text"]
        master.text.set(master.text.get() + button_value)
        

class Keyboard(Frame):
    """A keyboard widget -- dynamic resizing of buttons
    not available yet"""
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        #Widget configuration
        background_color_group.append(self)
        self.config(bg=config["Background Color"])
        self.columnconfigure(0, weight=1)
        for row in range(3):
            self.rowconfigure(row, weight=1)

        #Constants
        self.buttonheight = 4
        self.buttonwidth = 5
        self.font = ("Arial", 22)
        
        #The keys of the keyboard
        keyboard_def = ("q","w","e","r","t","y","u","i","o","p","Del","a","s",
                        "d","f","g","h","j","k","l","z","x","c","v","b","n","m")
        
        #Dictionary to store the button objects
        keyboard_dict = {0:{},
                         1:{},
                         2:{}}

        #Lines of the keyboard
        line0 = Frame(self, highlightthickness=0)
        line1 = Frame(self, highlightthickness=0)
        line2 = Frame(self, highlightthickness=0)

        #Creates and places the buttons programmatically
        index=-1
        for letter in keyboard_def[:11]:
            index+=1
            keyboard_dict[0][letter] = Button(line0, text=letter, padx=0,
                                              pady=0,
                                              highlightthickness=0, 
                                              height=self.buttonheight,
                                              width=self.buttonwidth,
                                              font=self.font,
                                              bg=config["Button Color"])
            keyboard_dict[0][letter].bind("<Button-1>", lambda event:self.keypress(event, master))
            keyboard_dict[0][letter].grid(column=index, row=0)
        index=-1
        for letter in keyboard_def[11:20]:
            index+=1
            keyboard_dict[1][letter] = Button(line1, text=letter, padx=0, 
                                              pady=0,
                                              highlightthickness=0, 
                                              height=self.buttonheight, 
                                              width=self.buttonwidth,
                                              font=self.font,
                                              bg=config["Button Color"])
            keyboard_dict[1][letter].bind("<Button-1>", lambda event:self.keypress(event, master))
            keyboard_dict[1][letter].grid(column=index, row=0)
        index=-1
        for letter in keyboard_def[20:]:
            index+=1
            keyboard_dict[2][letter] = Button(line2, text=letter, padx=0, 
                                              pady=0,
                                              highlightthickness=0, 
                                              height=self.buttonheight, 
                                              width=self.buttonwidth,
                                              font=self.font,
                                              bg=config["Button Color"])
            keyboard_dict[2][letter].bind("<Button-1>", lambda event:self.keypress(event, master))
            keyboard_dict[2][letter].grid(column=index, row=0)

        line0.pack()
        line1.pack()
        line2.pack()
    
    def keypress(self, event, master):
        button_value = event.widget["text"]
        if button_value == "Del":
            self.backspace(master)
        else:
            master.text.set(master.text.get() + button_value)
    
    def backspace(self, master):
        master.text.set(tools.char_remove(master.text.get(), -1))
    

class AppMessage(Toplevel):
    """This toplevel window is used as an app message.
    It overlays a message window over top of the main app"""
    def __init__(self, master=None, text="", font=0, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        #Window configuration
        self.overrideredirect(True)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        #Create widget(s)
        self.message = Label(self, 
                             text=text, 
                             font=("Arial", font),
                             bg=kwargs["bg"])
        self.message.grid(column=0, row=0)

        #Updates the window to register its size attributes
        self.update_idletasks()

        #Accesses size attributes of window and its parent
        #and places window in the middle of its parent
        x = master.winfo_x()
        y = master.winfo_y()
        middle_x = master.winfo_width()/2 - self.winfo_width()/2
        middle_y = master.winfo_height()/2 - self.winfo_height()/2
        self.geometry("+%d+%d" %(x+middle_x,y+middle_y))
        self.transient(master)

    def message_fadeout(self, interval=50):
        """Method creates a fade out effect"""
        alpha = self.attributes("-alpha")
        if alpha > 0:
            alpha -= .1
            self.attributes("-alpha", alpha)
            self.after(interval, self.message_fadeout)
        else:
            self.destroy()
        

app = App()
app.mainloop()