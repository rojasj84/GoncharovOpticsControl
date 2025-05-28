# Importing python libraries
import tkinter as tk
from PIL import ImageTk, Image

import motor_controls as MotorControls
from aerotech_communication import Ensemble_Motors

# Importing local libraries


win_color = "light gray"

if __name__ == "__main__":

    #***** Building USER GUI *****

    # Begin code with window code
    window = tk.Tk()
    window.title("Alex Laser Heating Control")
    window.geometry("600x600")

    aerotech_epaq = Ensemble_Motors()
    objectivePositioner = MotorControls.ThreeAxisControlPanel(window, 5, 5,["Y","Z","X"],["+","+","-"],aerotech_epaq)
    nanoPositioner = MotorControls.ThreeAxisControlPanel(window, 225, 5,["nanoX","nanoY","nanoZ"],["+","+","-"],aerotech_epaq)




    window.mainloop()