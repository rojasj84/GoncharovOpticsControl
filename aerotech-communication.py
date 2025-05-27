import socket

END_OF_STRING_CHARACTER = '\n'      # End of string character
ACKNOWLEDGE_CHARACTER = '%'         #  indicate success.
NAK_CHAR = '!'                      #  command error.
FAULT_CHARACTER = '#'               #  task error.
TIMEOUT_CHARACTER = '$'

class Ensemble_Motors:
    def __init__(self):
        #creating arrays that store the information for the different motor drivers
        self.device_name = ["Emsemble Epaq", "Emsemble MLs"]
        self.device_ip = ["192.168.1.100","192.168.1.101"]
        self.device_number = ["0","1"]
        self.device_port = ["8000", "8000"]
        
        #The Ensemble Epaq operates 4 Axis, the MLs operate 2 Axis which drive the nano steppers.
        self.axis_names = ["X", "Y", "Z", "XX", "YY", "ZZ"]        
        self.axis_in_device = ["0", "0", "0", "0", "1", "1"]        

        self.ensemble_epaq_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ensemble_ml_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_devices(self):
        # open connection to device
        try:
            self.ensemble_epaq_connection.connect((self.device_ip[0], self.device_port[0]))
            print("Connected to " + self.device_name[0] + ".")
        except ConnectionRefusedError:
            #if a connection error happens, indicate which device failed
            print("Failed to connect to " + self.device_name[self.device_identification_number] + ".")

        try:
            self.ensemble_ml_connection.connect((self.device_ip[1], self.device_port[1]))
            print("Connected to " + self.device_name[1] + ".")
        except ConnectionRefusedError:
            #if a connection error happens, indicate which device failed
            print("Failed to connect to " + self.device_name[1] + ".")


    def write_command(self, axis, command):
        if END_OF_STRING_CHARACTER not in command:
            #add end of line to command
            command = ''.join((command, END_OF_STRING_CHARACTER))

        #Send command to the device determined by the axis
        #Find where in the list of axis names this axis is located and locate the device that runs this axis
        value_of_index = self.axis_names.index(axis)
        selected_device_axis = self.axis_in_device(value_of_index)

        if selected_device_axis == "0":
            self.ensemble_epaq_connection(command.encode())

            #Read response back from the device
            read = self.ensemble_epaq_connection.recv(4096).decode().strip()
            code_from_device, device_response = read[0], read[1:]
            
            if code_from_device != ACKNOWLEDGE_CHARACTER:
                print("Error from write_command attempt.")
                print(device_response)

        elif selected_device_axis == "1":
            self.ensemble_ml_connection.send(command.encode())

            #Read response back from the device
            read = self.ensemble_ml_connection.recv(4096).decode().strip()
            code_from_device, device_response = read[0], read[1:]
            
            if code_from_device != ACKNOWLEDGE_CHARACTER:
                print("Error from write_command attempt.")
                print(device_response)
        
        if code_from_device != ACKNOWLEDGE_CHARACTER:
            print("Error from write_command attempt.")
            print(device_response)

    # Functions for controlling the Axis
    def enable_axis(self, axis_name):
        "Enable the axis"
        command = "ENABLE" + axis_name
        self.write_command(axis_name, command)
        print("Axis " + axis_name + " enabled.")

    def home_axis(self, axis_name):
        "Enable the axis"
        command = "HOME" + axis_name
        self.write_command(axis_name, command)
        print("Axis " + axis_name + " enabled.")

if __name__ == "__main__":
    A = Ensemble_Motors()
