################################################################################
## CS 101 Lab
## Program Lab Week 9
## Date : Fall 2021
## Name: Tin Nguyen
## Email: tdnng2@umsystem.edu
##
##
## Problem: Our program will allow the user to enter 2 types of grades; 
##          Tests and Programs.  Each of our scores is assumed to be out of 100, 
##          so we only need the users score.  The tests are 60% of a student’sgrade, 
##          while the assignments are 40%.  In order to calculate the final score, 
##          we multiply the mean score of the tests by 0.6 and add it to the mean of 
##          assignments multiplied by 0.4.
##
##
##
##
## Algorithm: The mean is the average.  To calculate the mean you would 
##            sum all the values and divide by the number of values.
##            The standard deviation is calculated by taking each value 
##            and subtracting the mean, and squaring the value.  Divide 
##            the sum of those values by the numbers of values, 
##            and take the square root of that result.
##
##
################################################################################

tests = []

assignments = []

test_weight = 0.6

assignment_weight = 0.4

MENU = """

\t\tGrade Menu

1 - Add Test

2 - Remove Test

3 - Clear Test

4 - Add Assignment

5 - Remove Assignment

6 - Clear Assignment

D - Display Scores

Q - Quit

==>"""

CHOICES = ['1', '2', '3', '4', '5', '6', 'D', 'Q']



def get_prompt(prompt, options):
    choice = input(prompt).upper()
    while choice not in CHOICES:
        choice = input(prompt).upper()
    return choice

def get_scores(prompt):
    while True:
        try:
            score = float(input(prompt))
            if score < 0:
                score = float(input(prompt))
            break
        except ValueError:
            pass
    return score

def remove_score(scores, prompt):
    score = get_scores(prompt)
    if score not in scores:
        print(score, " not found")
    else:
        scores.remove(score)

def calc_std(scores, avg):
    squared_diff = 0
    for score in scores:
        squared_diff += (avg - score) ** 2
    return (squared_diff / len(scores))**0.5

def display_scores(scores, prompt):
    if len(scores) == 0:
        print("{:<10} {:>10} {:>10} {:>10} {:>10} {:>10}".format( prompt, "0", "n/a", "n/a", "n/a", "n/a"))
    else:
        avg = sum(scores) / len(scores)
        std = calc_std(scores, avg)
        minimum = min(scores)
        maximum = max(scores)
        print("{:<10} {:>10d} {:>10.2f} {:>10.2f} {:>10.2f} {:>10.2f}".format( prompt, len(scores), minimum, maximum, avg, std))

def get_avg(scores):
    if len(scores) == 0:
        return 0
    else:
        return sum(scores) / len(scores)

def display_results(tests, assignments):
    test_avg = get_avg(tests)
    assignment_avg = get_avg(assignments)
    print("{:<10} {:>10} {:>10} {:>10} {:>10} {:>10}".format( "Type", "#", "min", "max", "avg", "std"))
    print("="*70)
    display_scores(tests, "Tests")
    display_scores(assignments, "Programs")
    weighted = test_avg * test_weight + assignment_avg * assignment_weight
    print("The weighted scores is {:5.2f}".format(weighted))

running = True
while running:
    choice = get_prompt(MENU, CHOICES)
    if choice == '1':  
        score = get_scores('\nEnter the new Test score 0-100 ==> ')
        tests.append(score)
    elif choice == '2':  
        remove_score(tests, '\nEnter the Test score to remove 0-100 ==> ')
    elif choice == '3':  
        tests.clear()
    elif choice == '4':  
        score = get_scores('\nEnter the new Assignment score 0-100 ==> ')
        assignments.append(score)
    elif choice == '5':
        remove_score(assignments, '\nEnter theAssignment to remove 0-100 ==> ')
    elif choice == '6':  
        assignments.clear()
    elif choice == 'D':  
        display_results(tests, assignments)
    elif choice == 'Q':
        running = False

