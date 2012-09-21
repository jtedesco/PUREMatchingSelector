import csv
from src.model.Mentor import Mentor
from src.model.Mentee import Mentee

__author__ = 'Jon Tedesco'

class CSVParser(object):
    """
     This object represents a parser for an input CSV file. From this input file, we can parse either a list of mentors,
      or a list of mentees.
    """

    def __init__(self, menteeFilePath, mentorFilePath, delimiter=' ', quoteCharacter='"'):
        """
         Builds a CSV parser to parse the given file.

            @param  menteeFilePath  The path to the file that holds mentee/applicant data
            @param  mentor FIlePath The path to the file that holds mentor data
            @param  delimeter       The delimeter between data entries
            @param  quoteCharacter  The character to create quotation marks
        """

        # Open the files for reading
        self.delimiter = delimiter
        self.quoteCharacter = quoteCharacter
        self.menteeCsvFile = open(menteeFilePath, 'r')
        self.mentorCsvFile = open(mentorFilePath, 'r')


    def parseMentorsAndMentees(self):
        """
         From the input file, parse the lists of mentor and mentee objects.

            @return
                1)  The list of mentees parsed from the input file
                2)  The list of mentors parsed from the input file
        """

        # Parse the mentors and mentees individually
        mentors = self.parseMentors()
        mentees = self.parseMentees(mentors)

        # Parse each mentor's mentee list into actual mentee objects
        for mentor in mentors:
            newMentees = []
            for oldMentee in mentor.menteesWanted:
                for mentee in mentees:
                    if len(oldMentee)>0 and (mentee.firstName.title() + ' ' + mentee.lastName.title()) == oldMentee:
                        newMentees.append(mentee)
            mentor.menteesWanted = newMentees

        return mentees, mentors


    def parseMentees(self, mentors):
        """
         From the input file, build the list of mentee objects (without the mentor objects).

            @param  mentors a list of mentor objects, so that we can detect if

            @return The list of mentees
        """

        # Build a dictionary of mentee data, indexed by netid
        menteesData = self.parseCSV(self.menteeCsvFile)

        # A list of mentee objects
        mentees = []

        for netId in menteesData:

            # Get the data for this mentee
            data = menteesData[netId]
            firstName = self.findField(data, 'first name').title()
            lastName = self.findField(data, 'last name').title()
            try:
                gpa = float(self.findField(data, 'gpa'))
            except Exception:
                gpa = None
            year = self.parseMultipleChoice(data, ['Freshman', 'Sophomore', 'Junior', 'Senior'])
            email = netId + '@illinois.edu'

            # Create a list of mentor names for now
            selectedMentors = []
            for mentor in mentors:
                mentorName = mentor.firstName + ' ' + mentor.lastName
                mentorSelectionData = self.findField(data, mentorName.lower(), True)
                if mentorSelectionData and int(mentorSelectionData) == 1:
                    selectedMentors.append(mentor)

            # Create the mentee object and add it to our list
            newMentee = Mentee(netId, firstName, lastName, year, email, gpa, selectedMentors)
            mentees.append(newMentee)

        return mentees


    def parseMentors(self):
        """
         From the input file, parse a list of mentor objects

            @return     The list of mentor objects parsed from the input file
        """

        # Build a dictionary of mentee data, indexed by netid
        mentorsData = self.parseCSV(self.mentorCsvFile)

        # A list of mentor objects
        mentors = []
        
        for name in mentorsData:
            
            # Get the data for this mentor
            firstNameArray = name.split()[0:-1]
            firstName = ""
            for firstNameEntry in firstNameArray:
                firstName += firstNameEntry + ' '
            firstName = firstName.rstrip().title()
            lastName = name.split()[-1].strip().title()
            email = self.findField(mentorsData[name], 'email')
            numberOfMenteesWanted = self.findField(mentorsData[name], 'number of mentees')
            if numberOfMenteesWanted is not None and len(numberOfMenteesWanted) > 0 :
                numberOfMenteesWanted = int(numberOfMenteesWanted)
            else:
                numberOfMenteesWanted = None
            mentee1 = self.findField(mentorsData[name], 'mentee 1')
            mentee2 = self.findField(mentorsData[name], 'mentee 2')
            mentee3 = self.findField(mentorsData[name], 'mentee 3')
            mentee4 = self.findField(mentorsData[name], 'mentee 4')
            mentee5 = self.findField(mentorsData[name], 'mentee 5')
            mentee6 = self.findField(mentorsData[name], 'mentee 6')
            mentee7 = self.findField(mentorsData[name], 'mentee 7')
            mentee8 = self.findField(mentorsData[name], 'mentee 8')

            # Build this mentee object and add it to our list
            menteesWanted = []
            if mentee1 is not None and len(mentee1) > 0:
                menteesWanted.append(mentee1)
            if mentee2 is not None and len(mentee2) > 0:
                menteesWanted.append(mentee2)
            if mentee3 is not None and len(mentee3) > 0:
                menteesWanted.append(mentee3)
            if mentee4 is not None and len(mentee4) > 0:
                menteesWanted.append(mentee4)
            if mentee5 is not None and len(mentee5) > 0:
                menteesWanted.append(mentee5)
            if mentee6 is not None and len(mentee6) > 0:
                menteesWanted.append(mentee6)
            if mentee7 is not None and len(mentee7) > 0:
                menteesWanted.append(mentee7)
            if mentee8 is not None and len(mentee8) > 0:
                menteesWanted.append(mentee8)
            try:
                menteesWanted.remove('')
            except Exception:
                pass
            newMentor = Mentor(firstName, lastName, email, numberOfMenteesWanted, menteesWanted)
            mentors.append(newMentor)

        return mentors


    def parseCSV(self, csvFile):
        """
         Parses a CSV and returns a dictionary of mentors or mentees, indexed by
            netid.

            @return The parsed data
        """

        csvObject = csv.reader(csvFile, delimiter=self.delimiter, quotechar=self.quoteCharacter)
        objects = {}

        # Grab the fields for a mentee out of the first row of the spreadsheet
        fields = []
        for row in csvObject:
            for value in row:
                if value.startswith("Q"):
                    fields += [value.split(":")[1]]
                else:
                    fields += [value]
            break
        csvFile.seek(0)
        csvFile = csv.reader(csvFile, delimiter=self.delimiter, quotechar=self.quoteCharacter)

        # Iterate through the rows of the csv
        rowIndex = 0
        for row in csvFile:
            # For keeping track of the mentee we're currently building
            cellIndex = 0
            netId = None

            # Skip the title row
            if rowIndex > 0:
                for value in row:
                    if cellIndex > 0:
                        key = fields[cellIndex]
                        objects[netId.lower()].append((key.lower(), value.strip()))

                    else:
                        netId = value.split("@")[0].strip()
                        objects[netId.lower()] = []

                    cellIndex += 1
                    pass
            rowIndex += 1

        return objects


    def findField(self, propertyList, field, isBoolean = False):
        """
         Loops through a list of tuples, where each tuple is a key-value pair,
            and returns the second (value) entry of the first tuple whose key
            contains 'field'.

            @param  propertyList    The list of key-value pairs
            @param  field           The search key
            @param  isBoolean       Setting this flag will cause this method to try to parse "0" and "1" as True/False,
                                    but continue to look for "True" columns until one is found or we run out of columns

            @return The value, or None if it could not be found
        """

        try:

            if isBoolean:
                for pair in propertyList:
                    if field in pair[0].lower() and int(pair[1]):
                        return pair[1]
                return None

            else:
                for pair in propertyList:
                    if field in pair[0].lower():
                        return pair[1]
                return None
        except Exception:
            return None


    def parseMultipleChoice(self, propertyList, choices):
        """
         Loops througha  list of tuples, where each tuple is a key-value pair, and
            returns the value of whichever fields value (of the choices) is 1. This
            would be used for parsing the responses to a multiple choice question.

            @param  propertyList    The list of key-value pairs
            @param  choices         The field keys consisting of the choices

            @return The value
        """

        try:
            for pair in propertyList:
                for choice in choices:
                    if choice in pair[0] and pair[1] == "1":
                        return pair[0]
            return None
        except Exception:
            return None