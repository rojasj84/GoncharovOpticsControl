# Importing python libraries
import tkinter as tk
from PIL import ImageTk, Image

import motor_controls as MotorControls

# Importing local libraries


win_color = "light gray"

if __name__ == "__main__":

    #***** Building USER GUI *****

    # Begin code with window code
    window = tk.Tk()
    window.title("Alex Laser Heating Control")
    window.geometry("600x600")

    objectivePositioner = MotorControls.ThreeAxisControlPanel(window, 5, 5,["X","Y","Z"])
    nanoPositioner = MotorControls.ThreeAxisControlPanel(window, 225, 5,["nanoX","nanoY","nanoZ"])




    window.mainloop()