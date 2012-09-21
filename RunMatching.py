import os
import sys
from src.constants.UserInputConstants import UserInputConstants
from src.matcher.Matcher import Matcher
from src.parser.CSVParser import CSVParser

__author__ = 'Jon Tedesco'

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

# Parse the mentees & mentors out of it
parser = CSVParser(applicantFileName, mentorFileName, ',', '"')
mentees, mentors = parser.parseMentorsAndMentees()

# Perform the matching on the mentors & mentees
matcher = Matcher(mentors, mentees)
matching = matcher.generateMenteeMentorMatching()

# Get the information about the resulting matching
matchedMentors = matching.getMatchedMentors()
matchedMentees = matching.getMatchedMentees()
unmatchedMentors = matching.getUnmatchedMentors()
unmatchedMentees = matching.getUnmatchedMentees()

# Output the results
print "Matching:"
for mentor in matchedMentors:
    print '\t' + mentor.firstName + ' ' + mentor.lastName
    for mentee in mentor.mentees:
        print '\t\t' + mentee.firstName + ' ' + mentee.lastName + ' (' + mentee.email + ')'
print

print "Unmatched Mentees:"
for mentee in unmatchedMentees:
    print '\t' + mentee.firstName + ' ' + mentee.lastName + ' (' + mentee.email + ')'
print

print "Unmatched Mentors:"
for mentor in unmatchedMentors:
    print '\t' + mentor.firstName + ' ' + mentor.lastName