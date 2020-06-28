# coding=UTF-8
import abb
import time

# connecting to robot
R = abb.Robot('192.168.125.1') 
R.set_speed([200, 200, 100, 100])
# start point
R.set_cartesian([[350, 0, 250], [0.707,0,0.707,0]])

time_start = time.time() #start timing
R.wait_time(0.5)
R.set_cartesian_t([[350, 0, 300], [0.707,0,0.707,0]],0.5) # move
time_end = time.time()    #stop timing
time_c= time_end - time_start + 0.5  #running time
print('time cost', time_c, 's')

time_start = time.time() #start timing
R.set_cartesian_t([[350, 0, 400], [0.707,0,0.707,0]],1) # move
time_end = time.time()    #stop timing
time_c= time_end - time_start   #running time
print('time cost', time_c, 's')

time_start = time.time() #start timing
R.set_cartesian_t([[350, 0, 300], [0.707,0,0.707,0]],1) # move
time_end = time.time()    #stop timing
time_c= time_end - time_start   #running time
print('time cost', time_c, 's')

time_start = time.time() #start timing
R.set_cartesian_t([[350, 0, 250], [0.707,0,0.707,0]],0.5) # move
R.wait_time(0.5)
time_end = time.time()    #stop timing
time_c= time_end - time_start   #running time
print('time cost', time_c, 's')




# #end point
# R.set_cartesian([[350, 0, 212], [0.707,0,0.707,0]])
