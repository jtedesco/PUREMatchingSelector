import os
import sys
from src.matcher.Matcher import Matcher
from src.parser.CSVParser import CSVParser
from src.constants.UserInputConstants import UserInputConstants

__author__ = 'jtedesco'

# Get input files & output directory
applicantFileName = raw_input(UserInputConstants.APPLICANT_FILE_PROMPT)
mentorFileName = raw_input(UserInputConstants.MENTOR_FILE_PROMPT)
outputDirectoryPath = raw_input(UserInputConstants.OUTPUT_DIRECTORY_PROMPT)

# Check user/input (only existence)
if not os.path.exists(applicantFileName):
    print(UserInputConstants.MISSING_FILE_MESSAGE % applicantFileName)
    sys.exit()
if not os.path.exists(mentorFileName):
    print(UserInputConstants.MISSING_FILE_MESSAGE % mentorFileName)
    sys.exit()
if not os.path.exists(outputDirectoryPath):
    os.makedirs(outputDirectoryPath)

# Parse the mentees & mentors out of it
parser = CSVParser(applicantFileName, mentorFileName, ',', '"')
mentees, mentors = parser.parseMentorsAndMentees()

# Generate the output files for each mentor
matcher = Matcher(mentors, mentees)
matcher.generateMentorApplicantLists(outputDirectoryPath, applicantFileName)