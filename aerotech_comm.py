import sys
import clr

# Importing Aerotech.Ensemble and Aerotech.Common
assemblydir = "aerotech_dotnet_dlls"
assembly_1 = "Aerotech.Ensemble"
assembly_2= "Aerotech.Common"
assembly_3= "EnsembleCore64"

sys.path.insert(0, assemblydir)
clr.AddReference(assembly_1)
clr.AddReference(assembly_2)

import Aerotech.Ensemble # type: ignore
#import Aerotech.Ensemble.Status # type: ignore
import Aerotech.Common # type: ignore

from Aerotech.Ensemble import Controller # type: ignore

#Class to call when connecting to the Ensemble Epaq Controller
class EnsembleController():
    def __init__(self):
        try:
            Aerotech.Ensemble.Controller.Connect()
        except:
            print("Aerotech Ensemble Controller Connection Error.")
        else:
            self.MotorController = Controller.ConnectedControllers[0]
            print("Controller Name: {0}", self.MotorController.Information.Name)        

    def EnableAxes(self, axis_names):
        #Axis names should be a string or array of strings ["X", "Y", "Z"]
        self.MotorController.Commands.Axes[axis_names].Motion.Enable()

    def DisableAxes(self, axis_names):
        #Axis names should be a string or array of strings ["X", "Y", "Z"]
        self.MotorController.Commands.Axes[axis_names].Motion.Disable();
    
    def HomeAxes(self, axis_names):
        #Axis names should be a string or array of strings ["X", "Y", "Z"]
        self.MotorController.Commands.Axes[axis_names].Motion.Home();

    def MoveINC(self, axis_names, distance, velocity):
        #Axis names should be a string or array of strings ["X", "Y", "Z"]
        #Distance is a double or array of doubles
        #Velocity is a double or array of doubles
        self.MotorController.Commands.Axes[axis_names].Motion.MoveInc(distance, velocity);        


if __name__ == "__main__":
    #Create an controller class and attempt to connect

    A = EnsembleController()
    

    #A.Commands.Axes.Enable("X", "Z")
    #A.Home("X")

    #print(A)