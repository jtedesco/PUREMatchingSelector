import csv

__author__ = 'Jon Tedesco'

class CSVParser(object):
    """
     This object represents a parser for an input CSV file. From this input file, we can parse either a list of mentors,
      or a list of mentees.
    """

    def __init__(self, filePath, delimiter=' ', quoteCharacter='"'):
        """
         Builds a CSV parser to parse the given file.

            @param  filePath        The path to the file to parse
            @param  delimeter       The delimeter between data entries
            @param  quoteCharacter  The character to create quotation marks
        """

        # Open the file for reading
        self.csvFile = csv.reader(open(filePath, 'rb'), delimiter=delimiter, quotechar=quoteCharacter)


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
        menteesData = self.parseCSV()

        # A list of mentee objects
        mentees = []

        for netId in menteesData:

            # Get the data for this mentee
            firstName = self.findField(menteesData, 'first name')
            lastName = self.findField(menteesData, 'last name')
            gpa = self.findField(menteesData, 'gpa')

#            newMentee = Mentee()


        return mentees


    def parseMentors(self):
        """
         From the input file, parse a list of mentor objects

            @return     The list of mentor objects parsed from the input file
        """
        return None


    def parseCSV(self):
        """
         Parses a CSV and returns a dictionary of mentors or mentees, indexed by
            netid.

            @return The parsed data
        """

        objects = {}

        # Grab the fields for a mentee out of the first row of the spreadsheet
        fields = None
        for row in self.csvFile:
            fields = []
            for value in row:
                if value.startswith("Q"):
                    fields += [value.split(":")[1]]
                else:
                    fields += [value]
            break

        # Iterate through the rows of the csv
        rowIndex = 0
        for row in self.csvFile:
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
        except:
            return None

