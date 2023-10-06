# Club example main program
from Club import *

# Create a club with at most 5 members
programmingClub = Club('Programming', 5)
programmingClub.addMember('Joe')
programmingClub.addMember('Bob')
programmingClub.addMember('Sue')
programmingClub.addMember('Amy')
programmingClub.addMember('Kim')

programmingClub.report()