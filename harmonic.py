import matplotlib.pyplot as plt




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
            if len(parts) == 2:
                depth = float(parts[0])
                velocity = float(parts[1])
                if (svp_data == []):
                    delta_depth = float(depth)
                    delta_time = depth / velocity
                
                else:
                    last_element = svp_data[-1]
                    delta_depth = depth - last_element[0]
                    delta_time = delta_depth / velocity

                sum_depth = delta_depth + sum_depth
                sum_time = delta_time + sum_time
                harmonic_sound_speed = (sum_depth/sum_time)

                    
                
                svp_data.append((depth, velocity,delta_depth, delta_time, harmonic_sound_speed))
    
    return svp_data, sum_depth, sum_time

file_path = 'C:/Users/rlfer/Downloads/PSJ_CTD_Data/2024-09-19_23-12-12.svp'
svp_data, sum_depth, sum_time = read_svp_file(file_path)

# Output the SVP data

for depth, velocity, delta_depth, delta_time, harmonic_sound_speed in svp_data:
    
    print(f"Depth: {depth} m, Velocity: {velocity} m/s, Delta Depth: {delta_depth}, Delta Time: {delta_time}, Harmonic Sound Speed : {harmonic_sound_speed} ")

print(len(svp_data))
print('Total change in depth (Final depth): ', sum_depth ) # total depth 

print('Total time taken in each layer: ', sum_time)

print('Harmonic Mean Sound Speed at the bottom of profile in (m/s) : ', (sum_depth/sum_time))


plot_svp(svp_data)
