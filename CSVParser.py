import csv
from Mentee import Mentee
from Mentor import Mentor

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
        self.menteeCsvFile = csv.reader(open(menteeFilePath, 'rb'), delimiter=delimiter, quotechar=quoteCharacter)
        self.mentorCsvFile = csv.reader(open(mentorFilePath, 'rb'), delimiter=delimiter, quotechar=quoteCharacter)


    def parseMentorsAndMentees(self):
        """
         From the input file, parse the lists of mentor and mentee objects.

            @return
                1)  The list of mentees parsed from the input file
                2)  The list of mentors parsed from the input file
        """



    def parseMentees(self):
        """
         From the input file, build the list of mentee objects (without the mentor objects).

            @return
        """

        # Build a dictionary of mentee data, indexed by netid
        menteesData = self.parseCSV(self.menteeCsvFile)

        # A list of mentee objects
        mentees = []

        for netId in menteesData:

            # Get the data for this mentee
            firstName = self.findField(menteesData[netId], 'first name')
            lastName = self.findField(menteesData[netId], 'last name')
            gpa = self.findField(menteesData[netId], 'gpa')
            year = self.parseMultipleChoice(menteesData[netId], ['freshman', 'sophomore', 'junior', 'senior'])
            email = netId + '@illinois.edu'
            first_choice = self.findField(menteesData[netId], 'first choice')
            second_choice = self.findField(menteesData[netId], 'second choice')

            # Create a list of mentor names for now
            if len(first_choice) > 0 and len(second_choice) > 0:
                mentors = [first_choice, second_choice]
            elif len(first_choice) > 0:
                mentors = [first_choice]
            else:
                mentors = []

            # Create the mentee object and add it to our list
            newMentee = Mentee(netId, firstName, lastName, year, email, gpa, mentors)
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
        
        for netId in mentorsData:
            
            # Get the data for this mentor
            firstName = self.findField(mentorsData[netId], 'first name')
            lastName = self.findField(mentorsData[netId], 'last name')
            email = netId + '@illinois.edu'
            numberOfMenteesWanted = self.findField(mentorsData[netId], 'number')

            # Build this mentee object and add it to our list
            newMentor = Mentor(firstName, lastName, email, numberOfMenteesWanted)
            mentors.append(newMentor)

        return mentors


    def parseCSV(self, csvFile):
        """
         Parses a CSV and returns a dictionary of mentors or mentees, indexed by
            netid.

            @return The parsed data
        """

        objects = {}

        # Grab the fields for a mentee out of the first row of the spreadshee
        fields = []
        for row in csvFile:
            for value in row:
                if value.startswith("Q"):
                    fields += [value.split(":")[1]]
                else:
                    fields += [value]
            break

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



    def findField(self, propertyList, field):
        """
         Loops through a list of tuples, where each tuple is a key-value pair,
            and returns the second (value) entry of the first tuple whose key
            contains 'field'.

            @param  propertyList    The list of key-value pairs
            @param  field           The search key

            @return The value, or None if it could not be found
        """

        try:
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