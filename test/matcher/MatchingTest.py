import unittest
from src.matcher.Matching import Matching
from src.model.Mentee import Mentee
from src.model.Mentor import Mentor

__author__ = 'jontedesco'

class MatchingTest(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super(MatchingTest, self).__init__(methodName)

        # Construct basic mentor & mentee structures
        self.mentors = [
            Mentor("Mentor", "A", None, 1, ["John Smith"]),
            Mentor("Mentor", "B", None, 1, ["John Smith","James Smith"]),
            Mentor("Mentor", "C", None, 2, ["James Smith","Joe Smith"])
        ]
        self.mentees = [
            Mentee('user1', 'John', 'Smith', 'Freshman', 'user1@illinois.edu', 3.76, [self.mentors[0]]),
            Mentee('user2', 'Joe', 'Smith', 'Sophomore', 'user2@illinois.edu', 2.76, [self.mentors[2]]),
            Mentee('user3', 'James', 'Smith', 'First Year Transfer', 'user3@illinois.edu', 3.42, [self.mentors[1]])
        ]


    def testMatchedMentorsAndMentees(self):

        # Construct a matching with no unmatched mentors or mentees
        self.mentors[0].mentees = [self.mentees[0]]
        self.mentors[1].mentees = [self.mentees[2]]
        self.mentors[2].mentees = [self.mentees[1]]

        matching = Matching(self.mentees, self.mentors)
        expectedMatchedMentees = self.mentees
        expectedUnmatchedMentees = []
        expectedMatchedMentors = self.mentors
        expectedUnmatchedMentors = []

        self.assertItemsEqual(expectedMatchedMentees, matching.getMatchedMentees())
        self.assertItemsEqual(expectedMatchedMentors, matching.getMatchedMentors())
        self.assertItemsEqual(expectedUnmatchedMentees, matching.getUnmatchedMentees())
        self.assertItemsEqual(expectedUnmatchedMentors, matching.getUnmatchedMentors())


    def testUnmatchedMenteesAndMentors(self):

        # Construct a matching with no unmatched mentors or mentees
        self.mentors[0].mentees = [self.mentees[0]]
        self.mentors[1].mentees = []
        self.mentors[2].mentees = [self.mentees[1]]

        matching = Matching(self.mentees, self.mentors)
        expectedMatchedMentees = [self.mentees[0],self.mentees[1]]
        expectedUnmatchedMentees = [self.mentees[2]]
        expectedMatchedMentors = [self.mentors[0], self.mentors[2]]
        expectedUnmatchedMentors = [self.mentors[1]]

        self.assertItemsEqual(expectedMatchedMentees, matching.getMatchedMentees())
        self.assertItemsEqual(expectedMatchedMentors, matching.getMatchedMentors())
        self.assertItemsEqual(expectedUnmatchedMentees, matching.getUnmatchedMentees())
        self.assertItemsEqual(expectedUnmatchedMentors, matching.getUnmatchedMentors())