################################################################################
## CS 101 Lab
## Program Lab Week 13
## Date : Fall 2021
## Name: Tin Nguyen
## Email: tdnng2@umsystem.edu
##
##
##
## Problems: We’ll use our skills to create a clock class that can 
##           keeptrack of hours, minutes and seconds. 
##           The you should be able to create an instance
##           with values for hour, minutes and seconds.  
##           You’ll want to make a new class with a __ini__ method.  
##           You’ll want to set the attributes 
##           for hour, minute, and second in the init.
##
##
## Algorithm: Using the clock classwe’ve built create a program 
##            to ask a user for hours, minutes and seconds, 
##            and create a clock based on that.  
##            Then write a loop that calls tick() once a second 
##            and then sleeps for a second.  Use time module to sleep.
##
##
##
###############################################################################




import time


class Clock:
    # init method takes hour, minute and second
    # clock_type with default value 0
    # 0 - 24 HR format
    # 1 - 12 HR Format
    def __init__(self, hour, minute, second, clock_type=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.clock_type = clock_type

    # tick method to increase time by one second
    def tick(self):
        # add one second
        self.second += 1
        # if second is 60
        if self.second == 60:
            # reset second
            self.second = 0
            # increase minute
            self.minute += 1
            # if minute is 60
            if self.minute == 60:
                # reset minute
                self.minute = 0
                # increase hour
                self.hour += 1
                # if 24 hours passed
                if self.hour == 25:
                    # reset hour
                    self.hour = 0

    # str method returns the string representation of current clock
    def __str__(self):
        # if 24 hour mode, return HH:MM:SS format
        # {:02} in format creates two digit numbers eg 1 will be 01 ..etc
        if self.clock_type == 0:
            return "{:02}:{:02}:{:02}".format(self.hour, self.minute, self.second)
        # else 12 hour mode, return HH:MM:SS am/pm format
        # {:02} in format creates two digit numbers eg 1 will be 01 ..etc
        else:
            # for 0 to 11 will be am, print as it is
            if self.hour <= 11:
                # 0 represents 12
                if self.hour == 0:
                    return "{:02}:{:02}:{:02} am".format(12, self.minute, self.second)
                # else normally print in the format
                else:
                    return "{:02}:{:02}:{:02} am".format(self.hour, self.minute, self.second)
            # for 12 - 24, we have to subtract 12 in order to get hours
            else:
                return "{:02}:{:02}:{:02} pm".format(self.hour - 12, self.minute, self.second)


# read time details from the user
hour = int(input("What is the current hour ==> "))
minute = int(input("What is the current minute ==> "))
second = int(input("What is the current second ==> "))
# create a clock object with given time
clock = Clock(hour, minute, second, clock_type=1)
# infinite loop
# use CTRL+C to close
while True:
    # print the clock
    print(clock)
    # tick the clock,
    # increase by 1 second
    clock.tick()
    # sleep for 1 second
    time.sleep(1)

