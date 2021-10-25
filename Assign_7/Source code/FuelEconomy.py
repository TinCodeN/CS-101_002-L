################################################################################
## CS 101 Lab
## Program Lab Week 8
## Date : Fall 2021
## Name: Tin Nguyen
## Email: tdnng2@umsystem.edu
##
##
## Problems: If the user wants to see all vehicles with a combined mpg greater than 50, 
##           then yourprogram will output that information to the file of their choosing.
##           The information is tab-delimited.  When you read a line from the file,
##           the values are separated by the tab character \t. 
##           There are many ways to split this string data.
##
## Algorithm: The program will need to ask the user for a minimum fuel economy, 
##            and be able to handle non float data being entered.  
##            It should continually ask for a correct value.  
##            It should also make sure they don’t enter a value less than 
##            or equal to zero or greater than 100.  The program will ask for an input
##            file and should loop until the user gives a valid file that can be opened
##
##################################################################################

def get_minimum_mpg():
    while True:
        try:
            min_mpg=float(input("Enter the minimum mpg ==> "))
            if min_mpg<0:
                print('Fuel economy given must be greater than 0')
            elif min_mpg>100:
                print('Fuel economy must be less than 100')
            else:
                return min_mpg
        except:
            print('You must enter a number for the fuel economy')

def get_input_file():
    while True:
        file_name=input('Enter the name of the input vehicle file ==> ')
        try:
            with open(file_name,'r') as read_file:
                return [[data.strip() for data in line.strip().split('\t')] for line in read_file.readlines()]

        except:
            print('Could not open file',file_name)


def write_to_file(min_mileage,file_data):
    while True:
        try:
            file_name = input('Enter the name of the file to output to ==> ')
            with open(file_name,'w') as write_file:
                for data in file_data:
                    try:
                        if min_mileage>=float(data[7]):
                            write_file.write('{0:<5}{1:<40}{2:<40}{3:>10}\n'.format(data[0],\
                            data[1],data[2],data[7]))
                    except:
                        print('Could not convert value invalid for vehicle',data[0],data[1],data[2])
        except:
            print('There is an IO Error',file_name)


def main():
    min_mileage=get_minimum_mpg()
    file_data=get_input_file()[1:]
    write_to_file(min_mileage,file_data)

main()
