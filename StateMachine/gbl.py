#Global Variables:
run_start_time = None
depth = None #current depth in meters
init_depth = None #depth at beginning of run - should be near 0
depth_const = -0.28 #downward thrust to maintain depth without a depth sensor or other reference point
heading = None #current compass heading in degrees from 0-360
init_heading = None #compass heading at beginning of run
detections = [] #list of detections that will be filled by the neural network
num_detections = 0 #why would we not just use len(detections)?
current_target = None #the current object being targeted TODO: allow multiple targets
sleep_time = 0.05 #the amount of time to sleep before looking for another frame

current_target = None
sleep_time = 0.05
debug = False
