from pprint import pprint
from CSVParser import CSVParser
from Matcher import Matcher

__author__ = 'jtedesco'


# Parse the mentees & mentors out of it
applicantFile = "/home/jon/Desktop/Mentees.csv"
mentorFile = "/home/jon/Desktop/Mentors.csv"
parser = CSVParser(applicantFile, mentorFile, ',', '"')
mentees, mentors = parser.parseMentorsAndMentees()

# Generate the output files for each mentor
matcher = Matcher(mentors, mentees)
matcher.generateMentorApplicantLists("/home/jon/Desktop/Mentor Lists/", applicantFile)