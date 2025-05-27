import socket

END_OF_STRING_CHARACTER = '\n'      # End of string character
ACKNOWLEDGE_CHARACTER = '%'         #  indicate success.
NAK_CHAR = '!'                      #  command error.
FAULT_CHARACTER = '#'               #  task error.
TIMEOUT_CHARACTER = '$'

class Ensemble_Motors():
    def __init__(self):
        #creating arrays that store the information for the different motor drivers
        self.device_name = "Emsemble Epaq"
        self.device_ip = "192.168.1.100"
        self.device_port = 8000
        #print("test")
        #The Ensemble Epaq operates 4 Axis, the MLs operate 2 Axis which drive the nano steppers.
        self.axis_names = ["X", "Y", "Z", "nanoZ", "nanoX", "nanoY"]        

        self.ensemble_epaq_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.connect_to_devices()

    def connect_to_devices(self):
        # open connection to device
        try:
            self.ensemble_epaq_connection.connect((self.device_ip, self.device_port))
            print("Connected to " + self.device_name + ".")
        except ConnectionRefusedError:
            #if a connection error happens, indicate which device failed
            print("Failed to connect to " + self.device_name + ".")

    def write_command(self, command):
        if END_OF_STRING_CHARACTER not in command:
            #add end of line to command
            command = ''.join((command, END_OF_STRING_CHARACTER))

        #Send command to the device
        self.ensemble_epaq_connection.send(command.encode())

        #Read response back from the device
        read = self.ensemble_epaq_connection.recv(4096).decode().strip()
        code_from_device, device_response = read[0], read[1:]
        
        if code_from_device != ACKNOWLEDGE_CHARACTER:
            print("Error from write_command attempt.")
            print(device_response)    

    # Functions for controlling the Axis
    def enable_axis(self, axis_name):
        "Enable the axis"
        command = "ENABLE " + axis_name
        self.write_command(axis_name, command)
        print("Axis " + axis_name + " is enabled.")

    def home_axis(self, axis_name):
        #home the axis
        command = "HOME " + axis_name
        print(command)
        self.write_command(command)
        #print("Axis " + axis_name + " is Home.")

    def move_increment(self, axis_name, distance, direction, speed):
        x = 0

    def close_connection(self):
        #Close the connection
        self.ensemble_epaq_connection.close()

    def reset_connection(self):
        self.write_command('RESET')

if __name__ == "__main__":
    
    A = Ensemble_Motors()
    A.connect_to_devices()
    #A.enable_axis("nanoX")
    A.home_axis("nanoX")
