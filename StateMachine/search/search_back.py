#!/usr/bin/env python

import rospy
import smach
import smach_ros

from StateMachine.sub import *

# define state Foo
class search_back(sub):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Found_Object','Not_Found_Object'])

    def log(self):
    	pass

    def execute(self, userdata):
    	self.log()
        return 'Not_Found_Object'
