#!/usr/bin/env python2

from StateMachine.sub import *

# define state interact_gate
class Straight_Ahead(Sub):
    def __init__(self):
        smach.State.__init__(self, outcomes=['through_gate'])

    def execute(self, userdata):
        self.init_state()
        gbl.state_heading = gbl.heading

        msg = self.init_joy_msg()
        msg.axes[const.AXES['frontback']] = 0.6     

        rospy.loginfo('Charging forward for 40ish seconds')
        
        if not gbl.debug:
            #leave 3 seconds for spin2win
            while rospy.get_time() < (self.current_state_start_time + 37):
                msg.axes[const.AXES['frontback']] = 0.4
                self.publish(msg)
                rospy.sleep(const.SLEEP_TIME)

            #turn to buoy
            while(abs(self.angle_diff(gbl.heading, gbl.state_heading + 10)) < 2):
                msg = self.center_on_heading(gbl.state_heading + 10, msg)
                self.search_frames_seen = 0

        #set current target
        gbl.current_target = const.CLASSES['buoy_jiangshi']

        rospy.loginfo('done')

        return 'through_gate'


    def log(self):
        rospy.loginfo('Executing state straight_ahead')
