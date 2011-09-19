from pprint import pprint
from CSVParser import CSVParser
from Matcher import Matcher

__author__ = 'Jon Tedesco'


# Parse the mentees & mentors out of it
applicantFile = "/home/jon/Desktop/mentees.csv"
mentorFile = "/home/jon/Desktop/mentors.csv"
parser = CSVParser(applicantFile, mentorFile, ',', '"')
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
        print '\t\t' + mentee.firstName + ' ' + mentee.lastName + '(' + mentee.email + ')'
print

print "Unmatched Mentees:"
for mentee in unmatchedMentees:
    print '\t' + mentee.firstName + ' ' + mentee.lastName + '(' + mentee.email + ')'