import tkinter
import customtkinter
import os
import ctypes

# Set DPI awareness
ctypes.windll.shcore.SetProcessDpiAwareness(1)


# Set appearance mode and default color theme
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


# Colors for matching tkinter and customtkinter
DARK_GREY = "#3b3b3b"
LIGHT_GREY = "#5c5d5f"
BACKGROUND_COLOR = "#242424"
SECTION_COLOR = "#2b2b2b"


# Create Main window
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.toplevel = None

        
        # Configure window
        self.title("NFO Maker")
        self.geometry("1370x420")
        self.minsize(1370, 420)
        self.maxsize(1370, 420)


        # Configure grid
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)


        # Making frame for the movie labels and entry boxes
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, columnspan=8, rowspan=4, padx=(20, 15), pady=(15, 15), sticky="nsew")


        # Change window name
        def change_window_name():
            if self.radio_var.get() == 0:
                change_logo_label('Movie')
                remove_episode_field()
            elif self.radio_var.get() == 1:
                change_logo_label('TV Show')
                remove_episode_field()
            elif self.radio_var.get() == 2:
                change_logo_label('Episode')
                add_episode_field()


        # Change logo label
        def change_logo_label(name):
            self.title(name)
            self.logo_label.grid_forget()
            self.logo_label = customtkinter.CTkLabel(self.radiobutton_frame, text=name, font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=15, sticky="n")
        
        
        # Add episode field and multiple episode toggle
        def add_episode_field():
            self.first_episode = customtkinter.CTkLabel(self.radiobutton_frame, text = "Episode: ")
            self.first_episode.grid(row=5, column=0, padx=(53, 5), pady=5, sticky="w")
            self.season_box = customtkinter.CTkEntry(self.radiobutton_frame, width=40, placeholder_text='S')
            self.season_box.grid(row=5, column=0, padx=(30, 5), pady=5)
            self.first_episode_box = customtkinter.CTkEntry(self.radiobutton_frame, width=40, placeholder_text='Ep')
            self.first_episode_box.grid(row=5, column=0, padx=(0, 30), pady=5, sticky="e")
            self.multiple_episodes_var = tkinter.IntVar(value=0)
            self.multiple_episodes = tkinter.Checkbutton(self.radiobutton_frame, text="Multiple Episodes", background=SECTION_COLOR,
                                                        fg='white', activebackground=SECTION_COLOR, activeforeground='white',
                                                        selectcolor=BACKGROUND_COLOR, variable=self.multiple_episodes_var,
                                                        command=toggle_multiple_episodes)
            self.multiple_episodes.grid(row=6, column=0, padx=10, pady=5, sticky="n")
        
        
        # Remove the episode fields when triggered
        def remove_episode_field():
            try:
                self.first_episode.grid_forget()
                self.season_box.grid_forget()
                self.first_episode_box.grid_forget()
                if self.multiple_episodes_var.get():
                    self.last_episode.grid_forget()
                    self.last_episode_box.grid_forget()
                self.multiple_episodes.grid_forget()
            except AttributeError:
                pass
        
        
        # Switch between single and multiple episodes
        def toggle_multiple_episodes():
            if self.multiple_episodes_var.get():
                self.last_episode = customtkinter.CTkLabel(self.radiobutton_frame, text = "Last Episode: ")
                self.last_episode.grid(row=7, column=0, padx=(25, 0), pady=5, sticky="w")
                self.last_episode_box = customtkinter.CTkEntry(self.radiobutton_frame, width=40, placeholder_text='Ep')
                self.last_episode_box.grid(row=7, column=0, padx= (0, 30), pady=5, sticky="e")
                self.first_episode.grid_forget()
                self.first_episode = customtkinter.CTkLabel(self.radiobutton_frame, text = "First Episode: ")
                self.first_episode.grid(row=5, column=0, padx=(25, 0), pady=5, sticky="w")
            else:
                self.last_episode.grid_forget()
                self.last_episode_box.grid_forget()
                self.first_episode.grid_forget()
                self.first_episode = customtkinter.CTkLabel(self.radiobutton_frame, text = "Episode: ")
                self.first_episode.grid(row=5, column=0, padx=(53, 5), pady=5, sticky="w")


        # Radiobuttons for choosing Movie, TV Show or Episode
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=0, rowspan=9, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.radiobutton_frame.grid_rowconfigure(9, weight=1)
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Movie, TV Show or Episode:")
        self.label_radio_group.grid(row=1, column=0, columnspan=1, padx=40, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0, text='Movie', command=change_window_name)
        self.radio_button_1.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1, text='TV Show', command=change_window_name)
        self.radio_button_2.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2, text='Episode', command=change_window_name)
        self.radio_button_3.grid(row=4, column=0, pady=10, padx=20, sticky="n")


        # Starting Main Label
        self.logo_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Movie", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=15, sticky="n")


        # All movie labels
        self.title_name = customtkinter.CTkLabel(self.main_frame, text = "Title:")
        self.uniqueid_type = customtkinter.CTkLabel(self.main_frame, text = "ID Type:")
        self.uniqueid = customtkinter.CTkLabel(self.main_frame, text = "Unique ID:")
        self.country = customtkinter.CTkLabel(self.main_frame, text = "Country:")
        self.credits = customtkinter.CTkLabel(self.main_frame, text = "Credits:")
        self.director = customtkinter.CTkLabel(self.main_frame, text = "Director:")
        self.premiered = customtkinter.CTkLabel(self.main_frame, text = "Premiered:")
        self.studio = customtkinter.CTkLabel(self.main_frame, text = "Studio:")
        self.genres = customtkinter.CTkLabel(self.main_frame, text = "Genres:")
        self.tags = customtkinter.CTkLabel(self.main_frame, text = "Tags:")
        self.actors = customtkinter.CTkLabel(self.main_frame, text = "Actors:")
        self.plot = customtkinter.CTkLabel(self.main_frame, text = "Plot:")


        # All entry boxes
        self.title_name_box = customtkinter.CTkEntry(self.main_frame, placeholder_text='Title', width=180)
        self.uniqueid_type_box = customtkinter.CTkEntry(self.main_frame, placeholder_text='IMDB/TVDB/etc.', width=180)
        self.uniqueid_box = customtkinter.CTkEntry(self.main_frame, placeholder_text='Unique ID', width=180)
        self.country_box = customtkinter.CTkEntry(self.main_frame, placeholder_text='Country', width=160)
        self.credits_box = customtkinter.CTkEntry(self.main_frame, placeholder_text='Credits', width=180)
        self.director_box = customtkinter.CTkEntry(self.main_frame, placeholder_text='Director', width=180)
        self.premiered_box = customtkinter.CTkEntry(self.main_frame, placeholder_text='YYYY-MM-DD', width=180)
        self.studio_box = customtkinter.CTkEntry(self.main_frame, placeholder_text='Studio', width=160)


        # Textbox for the plot
        self.plot_box = customtkinter.CTkTextbox(self.main_frame, width = 180, fg_color=DARK_GREY)


        # Making Frames to use as backgrounds for the listboxes as they do not have a inner padding option
        self.genre_frame = customtkinter.CTkFrame(self.main_frame, fg_color=DARK_GREY)
        self.genre_frame.grid(row=2, column=2)
        self.tag_frame = customtkinter.CTkFrame(self.main_frame, fg_color=DARK_GREY)
        self.tag_frame.grid(row=2, column=4)
        self.actor_frame = customtkinter.CTkFrame(self.main_frame, fg_color=DARK_GREY)
        self.actor_frame.grid(row=2, column=6)


        # All listboxes for easy overview of actors, genres and tags
        self.genre_box = tkinter.Listbox(self.main_frame, height=12, width=30)
        self.tag_box = tkinter.Listbox(self.main_frame, height=12, width=30)
        self.actor_box = tkinter.Listbox(self.main_frame, height=12, width=30)


        # Configuring the listboxes to look like the other entry boxes
        self.actor_box.configure(background=DARK_GREY, foreground='white', selectbackground=BACKGROUND_COLOR,
                                selectforeground='white', border=0, highlightthickness=0, activestyle='none')
        self.genre_box.configure(background=DARK_GREY, foreground='white', selectbackground=BACKGROUND_COLOR,
                                selectforeground='white', border=0, highlightthickness=0, activestyle='none')
        self.tag_box.configure(background=DARK_GREY, foreground='white', selectbackground=BACKGROUND_COLOR,
                                selectforeground='white', border=0, highlightthickness=0, activestyle='none')


        # Placing text in the textboxes
        self.plot_box.insert(0.0, 'Plot')


        # Placing all the labels and entry boxes in the grid
        self.title_name.grid(row = 0, column = 1, sticky = 'E', pady = 2, padx = (20, 5))
        self.title_name_box.grid(row = 0, column = 2, pady = (10, 10), padx = (10, 0), sticky = "W")

        self.uniqueid_type.grid(row = 0, column = 3, sticky = 'E', pady = 2, padx = (20, 5))
        self.uniqueid_type_box.grid(row = 0, column = 4, pady = (10, 10), padx = (10, 0), sticky = "W")

        self.uniqueid.grid(row = 0, column = 5, sticky = 'E', pady = 2, padx = (20, 5))
        self.uniqueid_box.grid(row = 0, column = 6, pady = (10, 10), padx = (10, 0), sticky = "W")

        self.country.grid(row = 0, column = 7, sticky = 'E', pady = 2, padx = (20, 5))
        self.country_box.grid(row = 0, column = 8, pady = (10, 10), padx = (10, 0), sticky = "W")

        self.credits.grid(row = 1, column = 1, sticky = 'E', pady = 2, padx = (20, 5))
        self.credits_box.grid(row = 1, column = 2, pady = (10, 15), padx = (10, 0), sticky = "W")

        self.director.grid(row = 1, column = 3, sticky = 'E', pady = 2, padx = (20, 5))
        self.director_box.grid(row = 1, column = 4, pady = (10, 15), padx = (10, 0), sticky = "W")

        self.premiered.grid(row = 1, column = 5, sticky = 'E', pady = 2, padx = (20, 5))
        self.premiered_box.grid(row = 1, column = 6, pady = (10, 15), padx = (10, 0), sticky = "W")

        self.studio.grid(row = 1, column = 7, sticky = 'E', pady = 2, padx = (20, 5))
        self.studio_box.grid(row = 1, column = 8, pady = (10, 15), padx = (10, 0), sticky = "W")


        # Placing all the labels and listboxes in the grid
        self.genres.grid(row = 2, column = 1, sticky = 'SE', pady = 2, padx =(0, 10))
        self.genre_box.grid(row = 2, column = 2, pady = 2)

        self.tags.grid(row = 2, column = 3, sticky = 'SE', pady = 2, padx = (0, 10))
        self.tag_box.grid(row = 2, column = 4, pady = 2)

        self.actors.grid(row = 2, column = 5, sticky = 'SE', pady = 2, padx = (0, 10))
        self.actor_box.grid(row = 2, column = 6, pady = 2)


        # Placing label and textbox for Plot in the grid
        self.plot.grid(row = 2, column = 7, sticky = 'SE', pady = 2, padx = 10)
        self.plot_box.grid(row = 2, column = 8, padx = 0, sticky = "W", )


        # Test to see if user entered data correctly
        def collect_data(self):
            if (self.title_name_box.get() == ""):
                tkinter.messagebox.showerror("Error", "Please enter a title")
                return
            elif (self.uniqueid_type_box.get() == ""):
                tkinter.messagebox.showerror("Error", "Please enter an ID Type")
                return
            elif (self.uniqueid_box.get() == ""):
                tkinter.messagebox.showerror("Error", "Please enter a unique ID")
                return
            elif self.radio_var.get() == 2:
                if not self.season_box.get():
                    tkinter.messagebox.showerror("Error", "Please enter a season number")
                    return
                elif not self.first_episode_box.get():
                    tkinter.messagebox.showerror("Error", "Please enter an episode number")
                    return
                elif not self.season_box.get().isnumeric():
                    tkinter.messagebox.showerror("Error", "Please enter a valid season number")
                    return
                elif not self.first_episode_box.get().isnumeric():
                    tkinter.messagebox.showerror("Error", "Please enter a valid episode number")
                    return
                elif self.multiple_episodes_var.get():
                    if not self.last_episode_box.get():
                        tkinter.messagebox.showerror("Error", "Please enter the last episode number")
                        return
                    elif not self.last_episode_box.get().isnumeric():
                        tkinter.messagebox.showerror("Error", "Please enter a valid last episode number")
                        return
                    elif self.first_episode_box.get() > self.last_episode_box.get():
                        tkinter.messagebox.showerror("Error", "The last episode can not be before the first episode")
                        return
                    elif self.first_episode_box.get() == self.last_episode_box.get():
                        tkinter.messagebox.showerror("Error", "Please use the single episode option if there is only one episode")
                        return
            
            if tkinter.messagebox.askyesno("Confirm", "Are you done entering the data?"):
                
                
                # Collecting the data from the entry boxes
                title_data = self.title_name_box.get()
                uniqueid_type_data = self.uniqueid_type_box.get()
                uniqueid_data = self.uniqueid_box.get()
                country_data = self.country_box.get()
                credits_data = self.credits_box.get()
                director_data = self.director_box.get()
                premiered_data = self.premiered_box.get()
                studio_data = self.studio_box.get()
                genre_data = self.genre_box.get(0, "end")
                tag_data = self.tag_box.get(0, "end")
                actor_data = self.actor_box.get(0, "end")
                plot_data = self.plot_box.get(0.0, "end-1c")
                if self.radio_var.get() == 2:
                    season_data = int(self.season_box.get())
                    first_episode_data = int(self.first_episode_box.get())
                    if self.multiple_episodes_var.get():
                        last_episode_data = int(self.last_episode_box.get())
                
                
                # Creating the text for the file
                while True:
                    if self.radio_var.get() == 0:
                        file_text = """<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n<movie>\n"""
                    elif self.radio_var.get() == 1:
                        file_text = """<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n<tvshow>\n"""
                    elif self.radio_var.get() == 2:
                        file_text = """<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n<episodedetails>\n"""
                    file_text += f"\t<title>{title_data}</title>\n"
                    if self.radio_var.get() == 2:
                        file_text += f"\t<season>{season_data}</season>\n"
                        file_text += f"\t<episode>{first_episode_data}</episode>\n"
                    if plot_data not in ["", "Plot"]:
                        file_text += f"\t<plot>{plot_data}</plot>\n"
                    file_text += f"\t<uniqueid type=\"{uniqueid_type_data}\"default=\"true\">{uniqueid_data}</uniqueid>\n"
                    for genre in genre_data:
                        file_text += f"\t<genre>{genre}</genre>\n"
                    for tag in tag_data:
                        file_text += f"\t<tag>{tag}</tag>\n"
                    if country_data:
                        file_text += f"\t<country>{country_data}</country>\n"
                    if credits_data:
                        file_text += f"\t<credits>{credits_data}</credits>\n"
                    if director_data:
                        file_text += f"\t<director>{director_data}</director>\n"
                    if premiered_data:
                        file_text += f"\t<premiered>{premiered_data}</premiered>\n"
                    if studio_data:
                        file_text += f"\t<studio>{studio_data}</studio>\n"
                    for i in range(0, len(actor_data), 3):
                        file_text += f"\t<actor>\n"
                        file_text += f"\t\t<name>{actor_data[i][6:]}</name>\n"
                        file_text += f"\t\t<role>{actor_data[i + 1][6:]}</role>\n"
                        if actor_data[i + 2] != "Thumbnail: ":
                            file_text += f"\t\t<thumb>{actor_data[i + 2][11:]}</thumb>\n"
                        file_text += f"\t<order>{i // 3}</order>\n"
                        file_text += f"\t</actor>\n"
                    if self.radio_var.get() == 0:
                        file_text += "</movie>"
                    elif self.radio_var.get() == 1:
                        file_text += "</tvshow>"
                    elif self.radio_var.get() == 2:
                        file_text += "</episodedetails>"
                    
                    
                    # Ask the user where to save the file, but if they cancel, break the loop
                    if self.radio_var.get() == 2:
                        if first_episode_data == int(self.first_episode_box.get()):
                            file_directory = tkinter.filedialog.askdirectory(title = "Select where to save ")
                    elif self.radio_var.get() in [0, 1]:
                        file_directory = tkinter.filedialog.askdirectory(title = "Select where to save ")
                    if not file_directory:
                        tkinter.messagebox.showinfo("File Not Saved", "The file was not saved.")
                        break
                    
                    
                    # Try to save the file with the given name, but if it already exists, ask the user if they want to overwrite it
                    try:
                        if self.radio_var.get() == 0:
                            with open(os.path.join(file_directory, f"{title_data}.nfo"), "x") as file:
                                file.write(file_text)
                        elif self.radio_var.get() == 1:
                            with open(os.path.join(file_directory, "tvshow.nfo"), "x") as file:
                                file.write(file_text)
                        elif self.radio_var.get() == 2:
                            with open(os.path.join(file_directory, f"S{season_data:02d}E{first_episode_data:02d}.nfo"), "x") as file:
                                file.write(file_text)
                    
                    except FileExistsError:
                        if tkinter.messagebox.askyesno("File Exists", "The file already exists. Do you want to overwrite it?"):
                            if self.radio_var.get() == 0:
                                with open(os.path.join(file_directory, f"{title_data}.nfo"), "w") as file:
                                    file.write(file_text)
                            elif self.radio_var.get() == 1:
                                with open(os.path.join(file_directory, "tvshow.nfo"), "w") as file:
                                    file.write(file_text)
                            elif self.radio_var.get() == 2:
                                with open(os.path.join(file_directory, f"S{season_data:02d}E{first_episode_data:02d}.nfo"), "w") as file:
                                    file.write(file_text)
                        else:
                            if self.radio_var.get() in [0, 1]:
                                tkinter.messagebox.showinfo("File Not Saved", "The file was not saved.")
                    
                    
                    # If the user wants to create multiple episodes, increment the episode number, if not, break the loop
                    if self.radio_var.get() in [0, 1]:
                        break
                    elif not self.multiple_episodes_var.get():
                        break
                    elif first_episode_data < last_episode_data:
                        first_episode_data += 1
                    else:
                        break


        # Clear the data from the entry boxes
        def clear_data():
            self.title_name_box.delete(0, "end")
            self.uniqueid_type_box.delete(0, "end")
            self.uniqueid_box.delete(0, "end")
            self.country_box.delete(0, "end")
            self.credits_box.delete(0, "end")
            self.director_box.delete(0, "end")
            self.premiered_box.delete(0, "end")
            self.studio_box.delete(0, "end")
            self.genre_box.delete(0, "end")
            self.tag_box.delete(0, "end")
            self.actor_box.delete(0, "end")
            self.plot_box.delete(0.0, "end")


        # Delete the selected entry from the listbox if there is one
        def delete_entry(listbox, entry):
            try:
                listbox.delete(entry)
            except tkinter.TclError:
                pass


        # Make it so when you click on a field in the listbox, it selects the whole entry
        def _reselect(self = self):
            selection = self.widget.curselection()
            if not selection:
                return
            _select(num = selection[0])


        # Select the whole entry in the listbox
        def _select(self = self, num=0):
            if num % 3 == 0:
                self.actor_box.selection_set(num+1, num+2)
                self.actor_box.activate(num)
            elif num % 3 == 1:
                self.actor_box.selection_set(num-1, num+1)
                self.actor_box.activate(num)
            elif num % 3 == 2:
                self.actor_box.selection_set(num-2, num-1)
                self.actor_box.activate(num)


        # Delete the selected entry from the actor listbox
        def delete_actor(listbox = self.actor_box):
            for i in listbox.curselection()[::-1]:
                listbox.delete(i)


        # Save Button
        save_NFO = customtkinter.CTkButton(self.radiobutton_frame, text='Save', command= lambda : collect_data(self), width=100)
        save_NFO.grid(row=9, column=0, sticky = 'SW', padx = (10, 5), pady = (15, 25))


        # Clear all data Button
        clear_data = customtkinter.CTkButton(self.radiobutton_frame, text='Clear All', command=clear_data, width=100)
        clear_data.grid(row=9, column=0, sticky = 'SE', padx =(5, 15), pady = (15, 25))


        # Delete Buttons
        delete_genre = customtkinter.CTkButton(self.main_frame, text='Delete',
                                            command=lambda:delete_entry(self.genre_box, self.genre_box.curselection()))
        delete_genre.grid(row=4, column=2, pady = (10, 15))

        delete_tags = customtkinter.CTkButton(self.main_frame, text='Delete',
                                            command=lambda: delete_entry(self.tag_box, self.tag_box.curselection()))
        delete_tags.grid(row=4, column=4, pady = (10, 15))

        delete_actor = customtkinter.CTkButton(self.main_frame, text='Delete', command=delete_actor)
        delete_actor.grid(row=4, column=6, pady = (10, 15))

        clear_plot = customtkinter.CTkButton(self.main_frame, text='Clear Plot', command=lambda: self.plot_box.delete(0.0, "end"))
        clear_plot.grid(row=4, column=8, pady = (10, 15))


        # Popup windows
        open_genre_popup = customtkinter.CTkButton(self.main_frame, text='Add Genre',
                                                command=lambda: single_field_popup_window(self, 'Genre'))
        open_genre_popup.grid(row=3, column=2, pady = (10,0))

        open_tag_popup = customtkinter.CTkButton(self.main_frame, text='Add Tag',
                                                command=lambda : single_field_popup_window(self, 'Tag'))
        open_tag_popup.grid(row=3, column=4, pady = (10,0))

        open_actor_popup = customtkinter.CTkButton(self.main_frame, text='Add Actor',
                                                command=lambda : actor_popup_window(self))
        open_actor_popup.grid(row=3, column=6, pady = (10,0))


        # Bind the actor listbox to the _reselect function so that when you click on an entry, it selects the whole entry
        self.actor_box.bind("<<ListboxSelect>>", _reselect)


# Create a popup window for adding actors
def actor_popup_window(self):
    
    # Create a new window and set the window attributes
    if self.toplevel is not None:
        self.toplevel.destroy()
    self.toplevel = customtkinter.CTkToplevel(self)
    self.toplevel.title("Actor")
    self.toplevel.wm_attributes('-toolwindow', True)
    self.toplevel.geometry("310x175")
    self.toplevel.minsize(310, 175)
    self.toplevel.maxsize(310, 175)


    # Create a new frame
    actor_input_frame = customtkinter.CTkFrame(self.toplevel)
    actor_input_frame.grid(row = 3, column = 2, padx = 10, pady = 10)


    # Create the labels and entry boxes
    self.toplevel.actor_name = customtkinter.CTkLabel(actor_input_frame, text="Actor Name: ")
    self.toplevel.actor_name_box = customtkinter.CTkEntry(actor_input_frame)
    self.toplevel.actor_role = customtkinter.CTkLabel(actor_input_frame, text="Actor Role: ")
    self.toplevel.actor_role_box = customtkinter.CTkEntry(actor_input_frame)
    self.toplevel.actor_thumb = customtkinter.CTkLabel(actor_input_frame, text="Actor Thumbnail: ")
    self.toplevel.actor_thumb_box = customtkinter.CTkEntry(actor_input_frame)


    # Place the labels and entry boxes
    self.toplevel.actor_name.grid(row = 0, column = 0, sticky = 'E', pady = (10,2), padx = 10)
    self.toplevel.actor_name_box.grid(row = 0, column = 1, pady = (10, 2), ipadx=5, padx=10)
    self.toplevel.actor_role.grid(row = 1, column = 0, sticky = 'E', pady = 2, padx = 10)
    self.toplevel.actor_role_box.grid(row = 1, column = 1, pady = 2, ipadx=5, padx=10)
    self.toplevel.actor_thumb.grid(row = 2, column = 0, sticky = 'E', pady = 2, padx = 10)
    self.toplevel.actor_thumb_box.grid(row = 2, column = 1, pady = 2, ipadx=5, padx=10)


    # Bind the enter and escape keys to make it easier to use
    self.toplevel.bind('<Return>', lambda event : add_actor(self))
    self.toplevel.bind('<Escape>', lambda event : [self.toplevel.destroy(), set_toplevel(self)])


    # Add and close Buttons
    add_input_button = customtkinter.CTkButton(actor_input_frame, text = "Add", width = 10, 
                                            command = lambda : add_actor(self))
    add_input_button.grid(row = 3, column = 1, pady = 10, padx = 10, sticky = 'W')
    
    close_button = customtkinter.CTkButton(actor_input_frame, text = "Close", width = 10,
                                        command = lambda : [self.toplevel.destroy(), set_toplevel(self)])
    close_button.grid(row = 3, column = 1, pady = 10, padx = 10, sticky = 'E')


    # Focus on the first entry box
    self.toplevel.actor_name_box.after(10, self.toplevel.actor_name_box.focus_force)


# Create a popup window for adding genres and tags
def single_field_popup_window(self, item):
    
    # Create a new window and set the window attributes
    if self.toplevel is not None:
        self.toplevel.destroy()
    self.toplevel = customtkinter.CTkToplevel(self)
    self.toplevel.configure(bg = BACKGROUND_COLOR)
    self.toplevel.title(f"{item}")
    self.toplevel.wm_attributes('-toolwindow', True)
    self.toplevel.geometry("245x105")
    self.toplevel.minsize(245, 105)
    self.toplevel.maxsize(245, 105)


    # Create a new frame
    self.toplevel.input_frame = customtkinter.CTkFrame(self.toplevel)
    self.toplevel.input_frame.grid(row = 3, column = 2, padx = 10, pady = 10)


    # Create the label and entry box
    self.toplevel.input_data = customtkinter.CTkLabel(self.toplevel.input_frame, text=f"{item}: ")
    self.toplevel.input_box = customtkinter.CTkEntry(self.toplevel.input_frame)


    # Place the label and entry box
    self.toplevel.input_data.grid(row = 0, column = 0, pady = 5, padx = 10)
    self.toplevel.input_box.grid(row = 0, column = 1, ipadx=5, padx=10)


    # Bind the enter and escape keys to make it easier to use
    self.toplevel.bind('<Return>', lambda event : add_to_textbox(self, item))
    self.toplevel.bind('<Escape>', lambda event : [self.toplevel.destroy(), set_toplevel(self)])


    # Add and close buttons
    add_input_button = customtkinter.CTkButton(self.toplevel.input_frame, text = "Add", width = 10,
                                            command=lambda : add_to_textbox(self, item))
    add_input_button.grid(row = 3, column = 1, pady = 10, padx = 10, sticky = 'W')

    close_button = customtkinter.CTkButton(self.toplevel.input_frame, text = "Close", width = 10,
                                        command = lambda : [self.toplevel.destroy(), set_toplevel(self)])
    close_button.grid(row = 3, column = 1, pady = 10, padx = 10, sticky = 'E')
    
    
    # Focus on the entry box
    self.toplevel.input_box.after(10, self.toplevel.input_box.focus_force)


# Set the toplevel variable to None so we can continue to check if a window is open, only called when closing a window
def set_toplevel(self):
    self.toplevel = None


# Check where to add the input, then add it if it is not empty
def add_to_textbox(self, item):
    if (item == 'Genre') & (self.toplevel.input_box.get() != ''):
        self.genre_box.insert('end', self.toplevel.input_box.get())
    elif (item == 'Tag') & (self.toplevel.input_box.get() != ''):
        self.tag_box.insert('end', self.toplevel.input_box.get())
    self.toplevel.input_box.delete(0, 'end')


# Add actors to the actor listbox
def add_actor(self):
    if (self.toplevel.actor_name_box.get() == ''):
        tkinter.messagebox.showerror("Error", "Please fill in Actor Name")
        self.toplevel.lift()
        self.toplevel.actor_name_box.focus_set()
    elif (self.toplevel.actor_role_box.get() == ''):
        tkinter.messagebox.showerror("Error", "Please fill in Actor Role")
        self.toplevel.lift()
        self.toplevel.actor_role_box.focus_set()
    else:
        self.actor_box.insert('end', f"Name: {self.toplevel.actor_name_box.get()}")
        self.actor_box.insert('end', f"Role: {self.toplevel.actor_role_box.get()}")
        self.actor_box.insert('end', f"Thumbnail: {self.toplevel.actor_thumb_box.get()}")
        self.toplevel.actor_name_box.focus_set()
        self.toplevel.actor_name_box.delete(0, 'end')
        self.toplevel.actor_role_box.delete(0, 'end')
        self.toplevel.actor_thumb_box.delete(0, 'end')


# Start the main loop
if __name__ == "__main__":
    app = App()
    app.mainloop()