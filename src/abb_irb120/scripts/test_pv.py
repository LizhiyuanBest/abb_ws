# coding=UTF-8
import abb
import time

# connecting to robot
R = abb.Robot('192.168.125.1') 
R.set_speed([200, 200, 200, 200])
# start point
# R.set_cartesian([[350, 0, 212], [0.707,0,0.707,0]])
#time.sleep(1) #加入延时会让后面的PT控制的计时有些干扰，实际机器人运动时间没有什么干扰，但是time计时器会有干扰
R.set_joints_t([-60, -15, 60.3, 16.3, -31.5, -17.45],1.5)

# firstly,start robot. the first step is less than you setting
time_start = time.time() #start timing
R.set_joints_t([-50, -15, 60.3, 16.3, -31.5, -17.45],0.6)
time_end = time.time()    #stop timing
time_c= time_end - time_start   #running time
# print('time cost', time_c, 's')

# # firstly,start robot. the first step is less than you setting
# time_start = time.time() #start timing
# R.set_cartesian_v([[350, 0, 250], [0.707,0,0.707,0]],100) 
# time_end = time.time()    #stop timing
# time_c= time_end - time_start   #running time
# # print('time cost', time_c, 's')

# #v
# time_start = time.time() #start timing
# R.set_cartesian_v([[350, 0, 300], [0.707,0,0.707,0]],50) # move
# time_end = time.time()    #stop timing
# time_c= time_end - time_start   #running time
# print('time cost', time_c, 's')

# time_start = time.time() #start timing
# R.set_cartesian_v([[350, 0, 350], [0.707,0,0.707,0]],100) # move
# time_end = time.time()    #stop timing
# time_c= time_end - time_start   #running time
# print('time cost', time_c, 's')

# time_start = time.time() #start timing
# R.set_cartesian_v([[350, 0, 400], [0.707,0,0.707,0]],50) # move
# time_end = time.time()    #stop timing
# time_c= time_end - time_start   #running time
# print('time cost ', time_c, 's')


#V
time_start = time.time() #start timing
R.set_joints_v([-30, -15, 60.3, 16.3, -31.5, -17.45],100) # move
time_end = time.time()    #stop timing
time_c= time_end - time_start   #running time
print('time cost', time_c, 's')

time_start = time.time() #start timing
R.set_joints_v([-10, -15, 60.3, 16.3, -31.5, -17.45],200) # move
time_end = time.time()    #stop timing
time_c= time_end - time_start   #running time
print('time cost', time_c, 's')

time_start = time.time() #start timing
R.set_joints_v([10, -15, 60.3, 16.3, -31.5, -17.45],50) # move
time_end = time.time()    #stop timing
time_c= time_end - time_start   #running time
print('time cost', time_c, 's')





# #end point
# R.set_cartesian([[350, 0, 212], [0.707,0,0.707,0]])
