from src.matcher.Matcher import Matcher
from src.parser.CSVParser import CSVParser

__author__ = 'jtedesco'


# Parse the mentees & mentors out of it
applicantFile = "/Users/jontedesco/Desktop/mentees.csv"
mentorFile = "/Users/jontedesco/Desktop/mentors.csv"
parser = CSVParser(applicantFile, mentorFile, ',', '"')
mentees, mentors = parser.parseMentorsAndMentees()

# Generate the output files for each mentor
matcher = Matcher(mentors, mentees)
matcher.generateMentorApplicantLists("/Users/jontedesco/Desktop/Mentor Lists/", applicantFile)