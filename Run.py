from pprint import pprint
from CSVParser import CSVParser
from Matcher import Matcher

__author__ = 'jtedesco'


# Parse the mentees & mentors out of it
applicantFile = "/home/jon/Desktop/mentees.csv"
mentorFile = "/home/jon/Desktop/mentors.csv"
parser = CSVParser(applicantFile, mentorFile, ',', '"')
mentees, mentors = parser.parseMentorsAndMentees()

# Perform the matching on the mentors & mentees
matcher = Matcher(mentors, mentees)
mentees, mentors = matcher.generateMenteeMentorMatching()
