import unittest
from src.model.Mentee import Mentee
from src.model.Mentor import Mentor
from src.parser.CSVParser import CSVParser

__author__ = 'jontedesco'

class CSVParserTest(unittest.TestCase):
    """
      Tests the parsing of mentee & mentor input CSV files
    """

    def __init__(self, methodName='runTest'):
        super(CSVParserTest, self).__init__(methodName)

        # Input files
        self.simpleMenteeInputFileName = 'data/mentee/simpleMentee.csv'
        self.multipleMenteeMentorFileName = 'data/mentee/multipleMentorMentee.csv'
        self.mentorNameFile = 'data/mentor/mentorNames.csv'
        self.mentorChoicesFileName = 'data/mentor/mentorChoices.csv'

        # Construct basic mentor & mentee structures
        self.mentors = [
            Mentor("Mentor", "A", None, None, []),
            Mentor("Mentor", "B", None, None, []),
            Mentor("Mentor", "C", None, None, [])
        ]
        self.mentees = [
            Mentee('user1', 'John', 'Smith', 'Freshman', 'user1@illinois.edu', 3.76, [self.mentors[0]]),
            Mentee('user2', 'Joe', 'Smith', 'Sophomore', 'user2@illinois.edu', 2.76, [self.mentors[2]]),
            Mentee('user3', 'James', 'Smith', 'First Year Transfer', 'user3@illinois.edu', 3.42, [self.mentors[1]])
        ]

        self.maxDiff = None

        # Simple & complex situation parsers for testing
        self.preliminaryMatchingParser = CSVParser(self.simpleMenteeInputFileName, self.mentorNameFile, ',', '"')
        self.advancedMatchingParser = CSVParser(self.multipleMenteeMentorFileName, self.mentorChoicesFileName, ',', '"')


    def __assertObjectListsEqual(self, expectedList, actualList):

        self.assertEqual(len(expectedList), len(actualList))
        expectedList = list(a.__dict__ for a in expectedList)
        actualList = list(a.__dict__ for a in actualList)
        self.assertItemsEqual(expectedList, actualList)


    def __getMenteeFromListByName(self, menteeList, name):

        for mentee in menteeList:
            if mentee.firstName + ' ' + mentee.lastName == name:
                return mentee
        return None


    def testParseMentorNamesFile(self):
        """
          Tests the simple case of the mentors file for preliminary matching, when only the mentor names are included
        """

        expectedMentors = [
            Mentor("Mentor", "A", None, None, []),
            Mentor("Mentor", "B", None, None, []),
            Mentor("Mentor", "C", None, None, [])
        ]
        actualMentors = self.preliminaryMatchingParser.parseMentors()

        self.__assertObjectListsEqual(expectedMentors, actualMentors)


    def testParseSimpleMenteesFile(self):
        """
          Tests the simple case for parsing mentees, where each mentee has some data (string, numeric, and multiple
          choice types), and has chosen only one mentor
        """

        actualMentees = self.preliminaryMatchingParser.parseMentees(self.mentors)

        self.__assertObjectListsEqual(self.mentees, actualMentees)


    def testParseMultipleMentorMenteeFile(self):
        """
          Tests the complex case for parsing mentees input file, where each mentee has some data (string, numeric, and
          multiple choice types), and may have chosen multiple mentors to apply to
        """

        expectedMentees = self.mentees
        expectedMentees[0].mentors = [self.mentors[0], self.mentors[1]]
        expectedMentees[1].mentors = [self.mentors[2]]
        expectedMentees[2].mentors = [self.mentors[1], self.mentors[2]]

        actualMentees = self.advancedMatchingParser.parseMentees(self.mentors)

        self.__assertObjectListsEqual(expectedMentees, actualMentees)


    def testParseMentorChoicesFile(self):
        """
          Tests the complex case for parsing mentors input file, where each mentor has a number of mentees requested,
          and a preference list of their top choices for applicants.
        """

        # The mentor objects when mentees are not parsed simultaneously
        expectedMentorA, expectedMentorB, expectedMentorC = tuple(self.mentors)
        expectedMentorA.numberOfMenteesWanted = 1
        expectedMentorA.menteesWanted = ["John Smith"]
        expectedMentorB.numberOfMenteesWanted = 1
        expectedMentorB.menteesWanted = ["John Smith","James Smith"]
        expectedMentorC.numberOfMenteesWanted = 2
        expectedMentorC.menteesWanted = ["James Smith","Joe Smith"]
        expectedMentors = [
            expectedMentorA,
            expectedMentorB,
            expectedMentorC
        ]

        actualMentors = self.advancedMatchingParser.parseMentors()

        # Test that mentor preference lists (string only, and number of requested mentees) are parsed correctly
        self.__assertObjectListsEqual(expectedMentors, actualMentors)


        actualMentees = self.advancedMatchingParser.parseMentees(actualMentors)

        # Replace the text choices of applicants for mentors by the actual corresponding mentee objects
        expectedMentorA.menteesWanted = [
            self.__getMenteeFromListByName(actualMentees, "John Smith")
        ]
        expectedMentorB.menteesWanted = [
            self.__getMenteeFromListByName(actualMentees, "John Smith"),
            self.__getMenteeFromListByName(actualMentees, "James Smith")
        ]
        expectedMentorC.menteesWanted = [
            self.__getMenteeFromListByName(actualMentees, "James Smith"),
            self.__getMenteeFromListByName(actualMentees, "Joe Smith")
        ]

        oldActualMentees = actualMentees
        oldActualMentors = actualMentors
        actualMentees, actualMentors = self.advancedMatchingParser.parseMentorsAndMentees()

        # Test that the lists are not recomputed if parseX is called separately first
        self.assertEqual(actualMentees, oldActualMentees)
        self.assertEqual(actualMentors, oldActualMentors)
        self.assertItemsEqual(actualMentees, oldActualMentees)
        self.assertItemsEqual(actualMentors, oldActualMentors)

        # Test that mentee names are replaced with corresponding objects as expected
        self.__assertObjectListsEqual(actualMentors, expectedMentors)
