# Importing python libraries
import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path

# Importing local libraries
from aerotech_communication import Ensemble_Motors

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
class ThreeAxisControlPanel(tk.Frame):

    jog_speed_local = 1
    bt_scale = 8

    def __init__(self, container, x_location, y_location, axis_names, axis_directions, motor_comm_object):
        super().__init__(container)
        
        frame_width = 200
        frame_height = 360

        button_spacing = 5
        button_long_dimension = 223/4 + button_spacing
        button_short_dimension = 138/4 + button_spacing

        cross_center_x_position = frame_width/2
        cross_center_y_position = 135

        self.axis_names = axis_names
        self.axis_direction_correct = axis_directions


        # build labels and buttons
        self.config(background=win_color, highlightbackground="black", highlightthickness=1, relief="raised")
        self.place(x=x_location,y=y_location,width = frame_width,height = frame_height)
        #self.pack(pady=10)

        #Creating the object that communicates with the motors through Aerotech Ensemble
        self.motor_comm_object = motor_comm_object
        #self.motor_comm_object = Ensemble_Motors()
        #self.motor_comm_object.connect_to_devices()
        # 

        #enable all axis
        for i in range(3):            
            self.motor_comm_object.enable_axis(axis_names[i])

        travel_label = tk.Label(self, text="XY TRAVEL")
        #travel_label.place(x = 5, y = 5, width=frame_width-10, height=25)
        travel_label.grid(row = 0, column = 1, columnspan=3)

        self.jog_up_button_image = ImageTk.PhotoImage(scale_images(Path(r"images/up.png"),4))
        jog_up = tk.Button(self, text="UP", image=self.jog_up_button_image, relief=tk.FLAT, background=win_color)
        #jog_up.place(x = cross_center_x_position - 1*(button_short_dimension)/2, y = cross_center_y_position - 1*button_long_dimension - button_short_dimension, width = button_short_dimension-button_spacing, height = button_long_dimension-button_spacing)
        jog_up.grid(row = 1, column = 2)
        jog_up.bind("<ButtonPress>", lambda event:  self.motor_inc_motion(axis_names[1],"+"))
        #jog_up.bind("<ButtonRelease>", lambda event:   self.motor_inc_motion(0))

        self.jog_down_button_image = ImageTk.PhotoImage(scale_images(Path(r"images/down.png"),4))
        jog_down = tk.Button(self, text="DOWN", image=self.jog_down_button_image, relief=tk.FLAT, background=win_color)
        jog_down.grid(row = 3, column = 2)
        #jog_down.place(x = cross_center_x_position - 1*(button_short_dimension)/2, y = cross_center_y_position, width = button_short_dimension-button_spacing, height = button_long_dimension-button_spacing)
        jog_down.bind("<ButtonPress>", lambda event:  self.motor_inc_motion(axis_names[1],"-"))
        #jog_down.bind("<ButtonRelease>", lambda event:   self.motor_inc_motion(0))

        self.jog_right_button_image = ImageTk.PhotoImage(scale_images(Path(r"images/right.png"),4))
        jog_right = tk.Button(self, text="RIGHT", image=self.jog_right_button_image, relief=tk.FLAT, background=win_color)
        #jog_right.place(x = cross_center_x_position - 0*button_long_dimension + 1*(button_short_dimension)/2, y = cross_center_y_position - button_short_dimension , width = button_long_dimension-button_spacing, height = button_short_dimension-button_spacing)
        jog_right.grid(row = 2, column = 3)
        jog_right.bind("<ButtonPress>", lambda event:  self.motor_inc_motion(axis_names[0],"+"))
        #jog_right.bind("<ButtonRelease>", lambda event:   self.motor_inc_motion(0))

        self.jog_left_button_image = ImageTk.PhotoImage(scale_images(Path(r"images/left.png"),4))
        jog_left = tk.Button(self, text="LEFT", image=self.jog_left_button_image, relief=tk.FLAT, background=win_color)
        #jog_left.place(x = cross_center_x_position - 1*button_long_dimension - 1*(button_short_dimension)/2, y = cross_center_y_position - button_short_dimension , width = button_long_dimension-button_spacing, height = button_short_dimension-button_spacing)
        jog_left.grid(row = 2, column = 1)
        jog_left.bind("<ButtonPress>", lambda event:  self.motor_inc_motion(axis_names[0],"-"))
        #jog_left.bind("<ButtonRelease>", lambda event:   self.motor_inc_motion(0))

        focus_label = tk.Label(self, text="FOCUS")
        #focus_label.place(x = 5, y = 200, width=frame_width-10, height=25)
        focus_label.grid(row = 4, column = 1, columnspan=3)

        self.jog_focusin_button_image = ImageTk.PhotoImage(scale_images(Path(r"images/focus-in.png"),4))
        focus_in = tk.Button(self, text="FOCUS IN", image=self.jog_focusin_button_image, relief=tk.FLAT, background=win_color)
        #focus_in.place(x = cross_center_x_position - 1*button_long_dimension - 1*(button_short_dimension)/2, y = 200 + button_short_dimension , width = button_long_dimension-button_spacing, height = button_short_dimension-button_spacing)
        focus_in.grid(row = 5, column = 0, columnspan=2, sticky='e', padx=10)
        focus_in.bind("<ButtonPress>", lambda event:  self.motor_inc_motion(axis_names[2],"+"))
        #focus_in.bind("<ButtonRelease>", lambda event:   self.motor_inc_motion(0))

        self.jog_focusout_button_image = ImageTk.PhotoImage(scale_images(Path(r"images/focus-out.png"),4))
        focus_out = tk.Button(self, text="FOCUS OUT", image=self.jog_focusout_button_image, relief=tk.FLAT, background=win_color)
        #focus_out.place(x = cross_center_x_position - 0*button_long_dimension + 1*(button_short_dimension)/2, y = 200 + button_short_dimension , width = button_long_dimension-button_spacing, height = button_short_dimension-button_spacing)
        focus_out.grid(row = 5, column = 3, columnspan=2, sticky='w', padx=10)
        focus_out.bind("<ButtonPress>", lambda event:  self.motor_inc_motion(axis_names[2],"-"))
        #focus_out.bind("<ButtonRelease>", lambda event:   self.motor_inc_motion(0))

        step_size_label = tk.Label(self, text="Step Size (μm)")
        #step_size_label.place(x = 0, y = 285, width = 100, height=25)
        step_size_label.grid(row = 6, column = 0, columnspan=5)

        self.step_size_text = tk.Entry(self)
        #self.step_size_text.place(x = 100, y = 285, width = 50, height=25)
        self.step_size_text.grid(row = 7, column = 0, columnspan=5)
        self.step_size_text.insert(tk.END, "5")

        step_velocity_label = tk.Label(self, text="Velocity (μm/s)")
        #step_velocity_label.place(x = 0, y = 315, width = 100, height=25)
        step_velocity_label.grid(row = 8, column = 0, columnspan=5)

        self.step_velocity_text = tk.Entry(self)
        #self.step_velocity_text.place(x = 100, y = 315, width = 50, height=25)
        self.step_velocity_text.grid(row = 9, column = 0, columnspan=5)
        self.step_velocity_text.insert(tk.END, "2")

        reset_faults = tk.Button(self, text="RESET ALL")
        reset_faults.grid(row=10,column=1)
        reset_faults.bind("<ButtonPress>", lambda event:  self.reset_errors_on_epaq())

        connect_to_devices = tk.Button(self, text="CONNECT",command=self.connect_to_motors())
        connect_to_devices.grid(row=10,column=2)
        connect_to_devices.bind("<ButtonPress>", lambda event:  self.connect_to_motors())

    def motor_inc_motion(self, axis, direction):        
        #Convert the inputs from mm to microns.
        step_size_float = float(self.step_size_text.get())/1000
        velocity_float = float(self.step_velocity_text.get())/1000

        step_size = str(step_size_float)
        velocity = str(velocity_float)

        if direction == "+":
             command_string = "MOVEINC " + axis + " " + step_size + " " + axis  + "F " + velocity
        elif direction == "-":
            command_string = "MOVEINC " + axis + " -" + step_size + " " + axis  + "F "+ velocity

        
        #self.motor_comm_object.connect_to_devices()
        self.motor_comm_object.write_command(command_string)        
        print(command_string)

    def reset_errors_on_epaq(self):
        self.motor_comm_object.write_command("ACKNOWLEDGEALL")
    
    def connect_to_motors(self):
        x = 0
        #self.motor_comm_object.connect_to_devices()
        ##self.motor_comm_object.write_command("HOME " + self.axis_names[1])
        #self.motor_comm_object.write_command("HOME " + self.axis_names[2])
        

if __name__ == "__main__":

    #***** Building USER GUI *****

    # Begin code with window code
    window = tk.Tk()
    window.title("Motor Control Gui")
    window.geometry("210x390")

    A = Ensemble_Motors()
    B = ThreeAxisControlPanel(window, 5, 5,["nanoX","nanoY","nanoZ"],["+","+","-"], A)


    window.mainloop()