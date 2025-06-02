#assembly_path1 = "aerotech_dotnet_dlls"

import sys

#sys.path.append(assembly_path1)

#from pythonnet import load
#load("coreclr")

import clr

assemblydir = "aerotech_dotnet_dlls"
assembly_1 = "Aerotech.Ensemble"
assembly_2= "Aerotech.Common"
assembly_3= "EnsembleCore64"


#sys.path.insert(0, "C:/Windows/System32")
sys.path.insert(0, assemblydir)

#print(clr.FindAssembly('AerotechCommon'))

clr.AddReference(assembly_1)
clr.AddReference(assembly_2)
#clr.AddReference(assembly_3)

import Aerotech.Ensemble # type: ignore
import Aerotech.Ensemble.Status # type: ignore
import Aerotech.Common # type: ignore

from Aerotech.Ensemble import Controller # type: ignore

Aerotech.Ensemble.Controller.Connect()

A = Controller.ConnectedControllers[0]

print("Controller Name: {0}", A.Information.Name)

A.Commands.Axes["nanoY"].Motion.Enable()
A.Commands.Axes["nanoY"].Motion.Home();

#A.Commands.Axes.Enable("X", "Z")
#A.Home("X")

#print(A)