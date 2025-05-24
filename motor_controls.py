# Importing python libraries
import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path

# Importing local libraries

#*****Global Variables*****
win_color = "light gray"

#***** Define Functions*****
def do_nothing():
    x = 0
    print("Nothing is done")

def get_image(file_loc):
    # Valve images are 100x56
    img = Image.open(file_loc)
    return img

def scale_images(file_loc,scale):
    img = Image.open(file_loc)
    img_width, img_height = img.size
    img = img.resize((img_width // scale, img_height // scale), resample=Image.Resampling.LANCZOS)
    return img

#***** Define Classes to build Gui*****
class ObjectivePositionPanel(tk.Frame):

    jog_speed_local = 1
    bt_scale = 8

    def __init__(self, container, x_location, y_location):
        super().__init__(container)
        
        frame_width = 200
        frame_height = 400

        button_spacing = 5
        button_long_dimension = 223/4 + button_spacing
        button_short_dimension = 138/4 + button_spacing

        cross_center_x_position = frame_width/2
        cross_center_y_position = 135


        # build labels and buttons
        self.config(background=win_color, highlightbackground="black", highlightthickness=1, relief="raised")
        self.place(x=x_location,y=y_location,width = frame_width,height = frame_height)

        travel_label = tk.Label(self, text="XY TRAVEL")
        travel_label.place(x = 5, y = 5, width=frame_width-10, height=25)

        self.jog_up_button_image = ImageTk.PhotoImage(scale_images(Path(r"images\up.png"),4))
        jog_up = tk.Button(self, text="UP", image=self.jog_up_button_image, relief=tk.FLAT, background=win_color)
        jog_up.place(x = cross_center_x_position - 1*(button_short_dimension)/2, y = cross_center_y_position - 1*button_long_dimension - button_short_dimension, width = button_short_dimension-button_spacing, height = button_long_dimension-button_spacing)
        jog_up.bind("<ButtonPress>", lambda event:  self.motor_motion(1))
        #jog_up.bind("<ButtonRelease>", lambda event:   self.motor_motion(0))

        self.jog_down_button_image = ImageTk.PhotoImage(scale_images(Path(r"images\down.png"),4))
        jog_down = tk.Button(self, text="DOWN", image=self.jog_down_button_image, relief=tk.FLAT, background=win_color)
        jog_down.place(x = cross_center_x_position - 1*(button_short_dimension)/2, y = cross_center_y_position, width = button_short_dimension-button_spacing, height = button_long_dimension-button_spacing)
        jog_down.bind("<ButtonPress>", lambda event:  self.motor_motion(1))
        #jog_down.bind("<ButtonRelease>", lambda event:   self.motor_motion(0))

        self.jog_right_button_image = ImageTk.PhotoImage(scale_images(Path(r"images\right.png"),4))
        jog_right = tk.Button(self, text="RIGHT", image=self.jog_right_button_image, relief=tk.FLAT, background=win_color)
        jog_right.place(x = cross_center_x_position - 0*button_long_dimension + 1*(button_short_dimension)/2, y = cross_center_y_position - button_short_dimension , width = button_long_dimension-button_spacing, height = button_short_dimension-button_spacing)
        jog_right.bind("<ButtonPress>", lambda event:  self.motor_motion(1))
        #jog_right.bind("<ButtonRelease>", lambda event:   self.motor_motion(0))

        self.jog_left_button_image = ImageTk.PhotoImage(scale_images(Path(r"images\left.png"),4))
        jog_left = tk.Button(self, text="LEFT", image=self.jog_left_button_image, relief=tk.FLAT, background=win_color)
        jog_left.place(x = cross_center_x_position - 1*button_long_dimension - 1*(button_short_dimension)/2, y = cross_center_y_position - button_short_dimension , width = button_long_dimension-button_spacing, height = button_short_dimension-button_spacing)
        jog_left.bind("<ButtonPress>", lambda event:  self.motor_motion(1))
        #jog_left.bind("<ButtonRelease>", lambda event:   self.motor_motion(0))

        focus_label = tk.Label(self, text="FOCUS")
        focus_label.place(x = 5, y = 200, width=frame_width-10, height=25)

        self.jog_focusin_button_image = ImageTk.PhotoImage(scale_images(Path(r"images\focus-in.png"),4))
        focus_in = tk.Button(self, text="FOCUS IN", image=self.jog_focusin_button_image, relief=tk.FLAT, background=win_color)
        focus_in.place(x = cross_center_x_position - 1*button_long_dimension - 1*(button_short_dimension)/2, y = 200 + button_short_dimension , width = button_long_dimension-button_spacing, height = button_short_dimension-button_spacing)
        focus_in.bind("<ButtonPress>", lambda event:  self.motor_motion(1))
        #focus_in.bind("<ButtonRelease>", lambda event:   self.motor_motion(0))

        self.jog_focusout_button_image = ImageTk.PhotoImage(scale_images(Path(r"images\focus-out.png"),4))
        focus_out = tk.Button(self, text="FOCUS OUT", image=self.jog_focusout_button_image, relief=tk.FLAT, background=win_color)
        focus_out.place(x = cross_center_x_position - 0*button_long_dimension + 1*(button_short_dimension)/2, y = 200 + button_short_dimension , width = button_long_dimension-button_spacing, height = button_short_dimension-button_spacing)
        focus_out.bind("<ButtonPress>", lambda event:  self.motor_motion(1))
        #focus_out.bind("<ButtonRelease>", lambda event:   self.motor_motion(0))

    def motor_motion(self, motor_state):
        if motor_state == 1:
            print("1")
        elif motor_state == 0:
            print("0")

if __name__ == "__main__":

    #***** Building USER GUI *****

    # Begin code with window code
    window = tk.Tk()
    window.title("Motor Control Gui")
    window.geometry("210x410")

    A = ObjectivePositionPanel(window, 5, 5)


    window.mainloop()