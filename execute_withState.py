#!/usr/bin/env python2

import rospy
import StateMachine.machines.BaseStateMachine as base
import StateMachine.machines.PrequalifyMachine as prequal
import StateMachine.machines.TestSpinMachine as testspin
import StateMachine.machines.QualifyStraightMachine as dumbqualify
import StateMachine.machines.TestTrackMachine as testtrack
import argparse
import StateMachine.gbl as gbl

parser = argparse.ArgumentParser(description="execute a state machine for the submarine")
parser.add_argument('-m', '--machine', default="BaseStateMachine", help="the name of the state machine to execute (default: %(default)s)")
parser.add_argument('-d', '--debug', action="store_true", help='Launches in debug mode. Will try to go through entire state machine.')
parser.add_argument('-l', '--list', action="store_true", help="List the available state machines.")
args = parser.parse_args()

states = {
    'BaseStateMachine': base.createStateMachine,
    'PrequalifyMachine': prequal.createStateMachine,
    'TestSpinMachine': testspin.createStateMachine,
    'QualifyStraightMachine': dumbqualify.createStateMachine,
    'TestTrackMachine': testtrack.createStateMachine
}

def main():
    if args.list:
        print("Available State Machines:")
        for machine in states:
            print(machine)
        return

    rospy.loginfo("Running {}".format(args.machine))
    try:
        states[args.machine]()
    except KeyError:
        rospy.logfatal("Error: state machine name not recognized")

if __name__ == '__main__':
    gbl.debug = args.debug
    main()

