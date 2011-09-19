__author__ = 'jon'

class Matching(object):
    """
     Represents a completed matching, and exposes various useful functions, such as functions to find the list of
      matched or unmatched mentors and mentees
    """

    def __init__(self, mentees, mentors):

        self.mentees = mentees
        self.mentors = mentors

        self.matchedMentors = []
        self.matchedMentees = []
        self.unmatchedMentors = []
        self.unmatchedMentees = []

        # Generate the list of matched mentees & mentors, and unmatched mentors
        for mentor in mentors:
            if len(mentor.mentees) > 0:
                self.matchedMentors.append(mentor)
                for mentee in mentor.mentees:
                    self.matchedMentees.append(mentee)
            else:
                self.unmatchedMentors.append(mentor)

        # Generate the list of unmatched mentees
        for mentee in self.mentees:
            if mentee not in self.matchedMentees:
                self.unmatchedMentees.append(mentee)

        
    def getUnmatchedMentees(self):
        return self.unmatchedMentees

    def getMatchedMentees(self):
        return self.matchedMentees
    
    def getUnmatchedMentors(self):
        return self.unmatchedMentors

    def getMatchedMentors(self):
        return self.matchedMentors
    