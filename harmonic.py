import matplotlib.pyplot as plt


file_path = '2024-09-19_23-12-12.svp'

def plot_svp(svp_data):
    depths = [d[0] for d in svp_data]  # Extract depth
    velocities = [d[1] for d in svp_data]  # Extract velocity
    harmonic_speeds = [d[4] for d in svp_data]  # Extract harmonic sound speed

    plt.figure(figsize=(12, 6))

    # Plot Depth vs Velocity
    plt.subplot(1, 2, 1)
    plt.plot(velocities, depths, marker='o', color='b', label='Velocity')
    plt.title('Depth vs. Velocity')
    plt.xlabel('Velocity (m/s)')
    plt.ylabel('Depth (m)')
    plt.gca().invert_yaxis()  
    plt.grid()
    plt.legend()

    # Plot Depth vs Harmonic Speed
    plt.subplot(1, 2, 2)
    plt.plot(harmonic_speeds, depths, marker='o', color='r', label='Harmonic Speed of Sound')
    plt.title('Depth vs. Harmonic Speed of Sound')
    plt.xlabel('Harmonic Speed of Sound (m/s)')
    plt.ylabel('Depth (m)')
    plt.gca().invert_yaxis()  
    plt.grid()
    plt.legend()

    plt.tight_layout()
    plt.show()


'''
This function processes the velocity profile and calculates the harmonic mean sound speed
'''
def read_svp_file(file_path):
    svp_data = []

    sum_depth = 0
    sum_time = 0 

    
    with open(file_path, 'r') as file:
        # Skip the first three lines of the header 
        next(file)
        next(file)
        next(file)
        
        # Process each line after the headers
        for line in file:
            # Split the line by whitespace to get depth and velocity
            parts = line.split()
            
            # Ensure we have two columns in the file (depth and velocity)
            # Each entry in the file is considered to be a layer
            if len(parts) == 2:
                depth = float(parts[0])

                # We assume for each layer that the velocity is constant i.e. There is no sound speed variation within the layer itself 
                velocity = float(parts[1]) 

                #if first entry/layer
                if (svp_data == []):

                     #Distance between layers (For first layer - it would just be the depth of that layer)
                    delta_depth = float(depth)
                    # The time it takes for the sound to propagate in that layer
                    delta_time = depth / velocity 
                
                #For other entries/layers
                #get the most recent layer data
                #calculate the distance between the new layer and the previous layer
                else:
                    last_element = svp_data[-1] 
                    delta_depth = depth - last_element[0]
                    delta_time = delta_depth / velocity 


                #Harmonic Mean Sound Speed 
                sum_depth = delta_depth + sum_depth
                sum_time = delta_time + sum_time
                harmonic_sound_speed = (sum_depth/sum_time)

                    
                 
                svp_data.append((depth, velocity,delta_depth, delta_time, harmonic_sound_speed))
    
    return svp_data, sum_depth, sum_time



svp_data, sum_depth, sum_time = read_svp_file(file_path)


# Output the SVP data along with the changes in depth and time and the resulting harmonic sound speed
'''for depth, velocity, delta_depth, delta_time, harmonic_sound_speed in svp_data:
    
    print(f"Depth: {depth} m, Velocity: {velocity} m/s, Delta Depth: {delta_depth}, Delta Time: {delta_time}, Harmonic Sound Speed : {harmonic_sound_speed} ")

#print(len(svp_data))'''

print('Total change in depth (Final depth): ', sum_depth ) 

print('Total time taken in each layer: ', sum_time) 

print('Harmonic Mean Sound Speed at the bottom of profile in (m/s) : ', (sum_depth/sum_time))


plot_svp(svp_data)
