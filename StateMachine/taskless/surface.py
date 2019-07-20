#!/usr/bin/env python

from StateMachine.sub import *

# define state surface
class Surface(Sub):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Surfaced'])

    def execute(self, userdata):
        rospy.loginfo('Executing state SURFACE')
        return 'Surfaced'
