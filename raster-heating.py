import tkinter as tk
import numpy as np


win_color = "light gray"

class RasterWindow(tk.Frame):

    jog_speed_local = 1
    bt_scale = 8

    def __init__(self, container, x_location, y_location):
        super().__init__(container)
        
        frame_width = 175
        frame_height = 480

        #Build labels and buttons 
        self.config(background=win_color, highlightbackground="black", highlightthickness=1, relief="raised")
        self.place(x=x_location,y=y_location,width = frame_width,height = frame_height)

        self.raster_height_label = tk.Label(self,text="Raster Height (μm)", highlightbackground="black", highlightthickness=1)
        self.raster_height_label.place(x = 10, y = 10, width=150, height=25)
        self.raster_height_input = tk.Text(self, relief="sunken" )
        self.raster_height_input.place(x = 10, y = 40, width=150, height=25)
        self.raster_height_input.insert(tk.INSERT, "100")

        self.raster_width_label = tk.Label(self,text="Raster Width (μm)", highlightbackground="black", highlightthickness=1)
        self.raster_width_label.place(x = 10, y = 70, width=150, height=25)
        self.raster_width_input = tk.Text(self, relief="sunken" )
        self.raster_width_input.place(x = 10, y = 100, width=150, height=25)
        self.raster_width_input.insert(tk.INSERT, "100")

        self.raster_rows_label = tk.Label(self,text="Raster Rows", highlightbackground="black", highlightthickness=1)
        self.raster_rows_label.place(x = 10, y = 130, width=150, height=25)
        self.raster_rows_input = tk.Text(self, relief="sunken" )
        self.raster_rows_input.place(x = 10, y = 160, width=150, height=25)
        self.raster_rows_input.insert(tk.INSERT, "10")

        self.raster_generate_button = tk.Button(self, text="Generate Raster Path", command=self.generate_raster)
        self.raster_generate_button.place(x = 10, y = 200, width=150, height=25)

    def generate_raster(self):
        #Get the values from the text boxes
        raster_height_value = self.raster_height_input.get("1.0", "end-1c")
        raster_width_value = self.raster_width_input.get("1.0", "end-1c")
        raster_spacing_value = self.raster_rows_input.get("1.0", "end-1c")

        #Raster reference point is the current center of the view
        self.start_point = [-float(raster_width_value)/2,float(raster_height_value)/2]
        current_x_position = self.start_point[0]
        current_y_position = self.start_point[1]

        raster_path = np.array(self.start_point)

        raster_x_range = float(raster_width_value)
        raster_y_step = float(raster_height_value)/float(raster_spacing_value)
        #print(raster_y_step)
        raster_step_count = 0
        raster_forward = True

        #print(raster_spacing_value)

        #Expression that loops through the raster to generate the travel end points into an array 
        while raster_step_count < int(raster_spacing_value):
            if raster_forward == True:
                #Travel Forward
                current_x_position = current_x_position + raster_x_range
                raster_path = np.vstack((raster_path, [current_x_position,current_y_position]))
                
                #Travel Down
                current_x_position = current_x_position
                current_y_position = current_y_position - raster_y_step
                raster_path = np.vstack((raster_path, [current_x_position,current_y_position]))
                raster_forward = False

            elif raster_forward == False:
                #Travel Backwards
                current_x_position = current_x_position - raster_x_range
                current_y_position = current_y_position
                raster_path = np.vstack((raster_path, [current_x_position,current_y_position]))                

                #Travel Down
                current_x_position = current_x_position
                current_y_position = current_y_position - raster_y_step
                raster_path = np.vstack((raster_path, [current_x_position,current_y_position])) 
                raster_forward = True           
    
            raster_step_count = raster_step_count + 1

        #Final Raster End Points
        self.raster_end_points = raster_path

        raster_vectors = np.array(self.start_point)
        #Generate the Travel Vectors per step        
        for i in range(1,raster_path.shape[0]):
            raster_vectors = np.vstack((raster_vectors, raster_path[i] - raster_path[i-1])) 
        
        #Remove extra row
        self.raster_vectors = np.delete(raster_vectors, 0, axis=0)
        
        print(self.raster_vectors)
        #This class will have a start point, relative to the current center on the screen and relative vector paths that outline the paths of the vectors
        

if __name__ == "__main__":

    #***** Building USER GUI *****

    # Begin code with window code
    window = tk.Tk()
    window.title("Raster Heating Path Control")
    window.geometry("800x500")

    A = RasterWindow(window,10,10)

    window.mainloop()