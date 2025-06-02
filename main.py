# Importing python libraries
import tkinter as tk
from PIL import ImageTk, Image

import motor_controls as MotorControls
from aerotech_communication import Ensemble_Motors
from aerotech_comm import EnsembleController

# Importing local libraries


win_color = "light gray"

if __name__ == "__main__":

    #***** Building USER GUI *****

    # Begin code with window code
    window = tk.Tk()
    window.title("Alex Laser Heating Control")
    window.geometry("600x600")

    aerotech_epaq = EnsembleController()
    objectivePositioner = MotorControls.ThreeAxisControlPanel(window, 5, 5,["X","Z","Y"],[1,-1,-1],aerotech_epaq)
    nanoPositioner = MotorControls.ThreeAxisControlPanel(window, 225, 5,["nanoX","nanoY","nanoZ"],[1,-1,1],aerotech_epaq)




    window.mainloop()