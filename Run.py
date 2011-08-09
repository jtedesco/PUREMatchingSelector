from pprint import pprint
from CSVParser import CSVParser

__author__ = 'jtedesco'


# Parse the mentees out of it
parser = CSVParser("/home/jtedesco/Desktop/sp11PUREapplicants.csv", "/home/jtedesco/Desktop/sp11PUREmentors.csv", ',', '"')
applicants = parser.parseMentees()
mentors = parser.parseMentors()

pprint(applicants)
pprint(mentors)