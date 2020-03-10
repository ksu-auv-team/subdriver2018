#!/usr/bin/env python2

from StateMachine.sub import *

# define state surface
class Dive(Sub):
    def __init__(self):
        smach.State.__init__(self, outcomes=['dived'])

    def execute(self, userdata):
        rospy.loginfo('Executing state DIVE')
        gbl.diving = True

        msg = self.init_joy_msg()

        while self.get_depth() > 0.2:
            msg.axes[const.AXES['vertical']] = -0.3
            self.publish_joy(msg)

        self.thrust_start_time = rospy.get_time()

        gbl.diving = False
	return 'Dived'