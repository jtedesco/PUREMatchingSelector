from copy import deepcopy
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

        self.simpleMenteeInputFileName = 'data/mentee/simpleMentee.csv'
        self.multipleMenteeMentorFileName = 'data/mentee/multipleMentorMentee.csv'
        self.mentorNameFile = 'data/mentor/mentorNames.csv'
        self.mentorChoicesFileName = 'data/mentor/mentorChoices.csv'

        self.mentors = [
            Mentor("Mentor", "A", None, None, []),
            Mentor("Mentor", "B", None, None, []),
            Mentor("Mentor", "C", None, None, [])
        ]

        self.maxDiff = None

        self.preliminaryMatchingParser = CSVParser(self.simpleMenteeInputFileName, self.mentorNameFile, ',', '"')
        self.advancedMatchingParser = CSVParser(self.multipleMenteeMentorFileName, self.mentorChoicesFileName, ',', '"')


    def __assertObjectListsEqual(self, expectedList, actualList):

        self.assertEqual(len(expectedList), len(actualList))
        expectedList = list(a.__dict__ for a in expectedList)
        actualList = list(a.__dict__ for a in actualList)
        self.assertItemsEqual(expectedList, actualList)


    def testParseMentorNamesFile(self):

        expectedMentors = [
            Mentor("Mentor", "A", None, None, []),
            Mentor("Mentor", "B", None, None, []),
            Mentor("Mentor", "C", None, None, [])
        ]
        actualMentors = self.preliminaryMatchingParser.parseMentors()

        self.__assertObjectListsEqual(expectedMentors, actualMentors)


    def testParseSimpleMenteesFile(self):

        expectedMentees = [
            Mentee('user1', 'John', 'Smith', 'Freshman', 'user1@illinois.edu', 3.76, [self.mentors[0]]),
            Mentee('user2', 'Joe', 'Smith', 'Sophomore', 'user2@illinois.edu', 2.76, [self.mentors[2]]),
            Mentee('user3', 'James', 'Smith', 'First Year Transfer', 'user3@illinois.edu', 3.42, [self.mentors[1]])
        ]
        actualMentees = self.preliminaryMatchingParser.parseMentees(self.mentors)

        self.__assertObjectListsEqual(expectedMentees, actualMentees)


    def testParseMultipleMentorMenteeFile(self):

        expectedMentees = [
            Mentee('user1', 'John', 'Smith', 'Freshman', 'user1@illinois.edu', 3.76, [self.mentors[0], self.mentors[1]]),
            Mentee('user2', 'Joe', 'Smith', 'Sophomore', 'user2@illinois.edu', 2.76, [self.mentors[2]]),
            Mentee('user3', 'James', 'Smith', 'First Year Transfer', 'user3@illinois.edu', 3.42, [self.mentors[1], self.mentors[2]])
        ]
        actualMentees = self.advancedMatchingParser.parseMentees(self.mentors)

        self.__assertObjectListsEqual(expectedMentees, actualMentees)

    def testParseMentorChoicesFile(self):

        expectedMentorA, expectedMentorB, expectedMentorC = tuple(deepcopy(self.mentors))
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

        self.__assertObjectListsEqual(expectedMentors, actualMentors)