# Given arrival and departure times of trains on a single day in a railway platform, 
# find out the minimum number of platforms required so that no train has to wait for 
# the other(s) to leave. In other words, when a train is about to arrive, at least 
# one platform must be available to accommodate it.
# You will be given arrival and departure times both in the form of a list. The size 
# of both the lists will be equal, with each common index representing the same train. 
# Note: Time hh:mm would be written as integer hhmm for e.g. 9:30 would be written as 
# 930. Similarly, 13:45 would be given as 1345
# Example:
# Input: A schedule of 6 trains:
# arrival = [900,  940, 950,  1100, 1500, 1800]
# departure = [910, 1200, 1120, 1130, 1900, 2000]
# Expected output: Minimum number of platforms required = 3
