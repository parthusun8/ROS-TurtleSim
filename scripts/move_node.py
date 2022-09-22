#!/usr/bin/env python
'''
#####################################
NAME - PARTH SUNDARKA
BATCH - RMP0014
TASK - TO MOVE THE TURTLE IN ANY SHAPE, BUT ATLEAST MOVE IT
'''


import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import numpy as np
import time


def move():
	velocity_msg = Twist()
	rate = rospy.Rate(10)

	cmd_vel = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size = 10)

	rospy.subsc


