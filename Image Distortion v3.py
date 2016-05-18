import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1,5)
ax.set_ylim(-0.4,0.4)
ax.set_zlim(-0.6,0.6)

	#ellipsoid parameters
a1 = 1
a2 = .5
a3 = .1

	#transform (T)
x1_0 = 3.5
x2_0 = 0
x3_0 = 0

	#view vector (v)
x1_1 = 0
x2_1 = 0
x3_1 = 0

	#T - v = B
x1_2 = x1_0 - x1_1
x2_2 = x2_0 - x2_1
x3_2 = x3_0 - x3_1

	#Space
angle = np.pi
rotangle = (2.75)*np.pi  # rotang > 5*np.pi spirals
time_1 = 200
theta = np.linspace(0,2*angle,num=50)
phi = np.linspace(0,angle,num=50)
time = np.linspace(0,time_1,num=1500) 

for i in range(0,1500):
	for j in range(0,50):
		for k in range(0,50):
				#Rotated object due to time
                        print i
			x1_obj = a1*np.sin(phi[j])*np.sin(theta[k])+x1_2
			x2_obj = a2*np.sin(phi[j])*np.cos(theta[k])*np.cos(time[i]*(rotangle/time_1)) + a3*np.cos(phi[j])*np.sin(time[i]*(rotangle/time_1)) + x2_2
			x3_obj = -1*a2*np.sin(phi[j])*np.cos(theta[k])*np.sin(time[i]*(rotangle/time_1)) + a3*np.cos(phi[j])*np.cos(time[i]*(rotangle/time_1)) + x3_2
			
			n_obj = math.sqrt((x1_obj**2)+(x2_obj**2)+(x3_obj**2))
			
			nx1_obj = x1_obj/n_obj
			nx2_obj = x2_obj/n_obj
			nx3_obj = x3_obj/n_obj
			
			l_t = (n_obj/time_1)*time[i]
			
			x1_hom = (n_obj - l_t)*nx1_obj
			x2_hom = (n_obj - l_t)*nx2_obj
			x3_hom = (n_obj - l_t)*nx3_obj
			
			n_hom = math.sqrt((x1_hom**2)+(x2_hom**2)+(x3_hom**2))
			
			if(n_hom > 0.975 and n_hom <= 1.0):
				
				print '('+str(i)+', '+str(j)+', '+str(k)+', '+str(x1_obj)+', '+str(x2_obj)+', '+str(x3_obj)+', '+str(n_hom)+')'
				
				if(time[i]<10 and time[i]>=0):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='r')
				elif(time[i]<20 and time[i]>=10):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='g')
				elif(time[i]<30 and time[i]>=20):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='b')
				elif(time[i]<40 and time[i]>=30):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='r')
				elif(time[i]<50 and time[i]>=40):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='g')
				elif(time[i]<60 and time[i]>=50):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='b')
				elif(time[i]<70 and time[i]>=60):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='r')
				elif(time[i]<80 and time[i]>=70):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='g')
				elif(time[i]<90 and time[i]>=80):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='b')
				elif(time[i]<100 and time[i]>=90):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='r')
				elif(time[i]<110 and time[i]>=100):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='g')
				elif(time[i]<120 and time[i]>=110):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='b')
				elif(time[i]<130 and time[i]>=120):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='r')
				elif(time[i]<140 and time[i]>=130):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='g')
				elif(time[i]<150 and time[i]>=140):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='b')
				elif(time[i]<160 and time[i]>=150):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='r')
				elif(time[i]<170 and time[i]>=160):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='g')
				elif(time[i]<180 and time[i]>=170):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='b')
				elif(time[i]<190 and time[i]>=180):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='r')
				elif(time[i]<200 and time[i]>=190):
					ax.scatter(x1_obj,x2_obj,x3_obj,c='g')
				
			


ax.scatter(0,0,0)			
plt.show()
