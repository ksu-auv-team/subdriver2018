#!/usr/bin/env python2

from StateMachine.sub import *

# define state search_right
class Search_Right(Sub):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Found_Object','Not_Found_Object'])

    def execute(self, userdata):
        self.init_state()
        msg = self.init_joy_msg()
        msg.axes[const.AXES['rotate']] = .4
        

        while(1):
            self.publish(msg)
            if self.get_box_of_class(gbl.detections, gbl.current_target):
                if self.search_frames_seen <= 2:
                    self.search_frames_seen += 1
                else:
                    return "Found_Object" # Transitions to TRACK_GATE

            elif self.angle_diff(gbl.heading, gbl.state_heading + 45) > -5:
                self.search_frames_seen = 0
                return "Not_Found_Object" # Transitions to SEARCH_RECENTER_GATE

            else:
                self.search_frames_seen = 0

            rospy.sleep(const.SLEEP_TIME)

