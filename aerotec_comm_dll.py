assembly_path1 = r"C:\Users\jarojas\Desktop\Alex Laser System\_Control Program Code\GoncharovOpticsControl\aerotech_dotnet_dlls"

import sys

sys.path.append(assembly_path1)

import clr
clr.AddReference('AerotechEnsemble')
clr.AddReference('AerotechCommon')

from AerotechEnsemble import Controller

A = Controller()