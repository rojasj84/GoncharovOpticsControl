assembly_path1 = "aerotech_dotnet_dlls"

import sys

sys.path.append(assembly_path1)

from pythonnet import load
load("coreclr")

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference('AerotechEnsemble.dll')
clr.AddReference('AerotechCommon.dll')

from Aerotech.Ensemble import Controller

A = Controller()