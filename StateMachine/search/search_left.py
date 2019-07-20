#!/usr/bin/env python

from StateMachine.sub import *

# define state search_left
class search_left(sub):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Found_Object','Not_Found_Object'])

    def execute(self, userdata):
        self.init_state()
        msg = self.init_joy_msg()
        msg.axes[self.axes_dict['rotate']] = -.05
        

        while(1):
            self.joy_pub.publish(msg)
            if self.get_box_of_class(gbl.detections, gbl.current_target):
                if self.search_frames_seen <= 2:
                    self.search_frames_seen += 1
                else:
                    return "Found_Object" # Transitions to TRACK_GATE

            elif (rospy.get_time() - self.current_state_start_time) > 2:
                self.search_frames_seen = 0
                return "Not_Found_Object" # Transitions to SEARCH_RIGHT_GATE

            else:
                self.search_frames_seen = 0

            rospy.sleep(gbl.const.const.SLEEP_TIME)

