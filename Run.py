from pprint import pprint
from CSVParser import CSVParser

__author__ = 'jtedesco'


# Parse the mentees out of it
parser = CSVParser("/home/jtedesco/sp11PUREapplicants.csv", ',', '"')
applicants = parser.parseMentees()

pprint(applicants)