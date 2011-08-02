import csv

__author__ = 'Jon Tedesco'

class CSVParser(object):
    """
     This object represents a parser for an input CSV file. From this input file, we can parse either a list of mentors,
      or a list of mentees.
    """

    def __init__(self, filePath, delimiter=' ', quoteCharacter='|'):
        """
         Builds a CSV parser to parse the given file.

            @param  filePath        The path to the file to parse
            @param  delimeter       The delimeter between data entries
            @param  quoteCharacter  The character to create quotation marks
        """

        # Open the file for reading
        self.csvFile = csv.reader(open(filePath, 'rb'), delimiter=delimiter, quotechar=quoteCharacter)


    def parseMentees(self):
        """
         From the input file, parse a list of mentee objects.

            @return     The list of mentees parsed from the input file
        """

        # Dictionary of applicants, indexed by userId (assumed to be first entry),
        #   where each is a dictionary of properties of the mentee
        mentees = {}

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
                        mentees[netId][key] = value.strip()

                    else:
                        netId = value.split("@")[0].strip()
                        mentees[netId] = {}

                    cellIndex += 1
                    pass
            rowIndex += 1

        return mentees


    def parseMentors(self):
        """
         From the input file, parse a list of mentor objects

            @return     The list of mentor objects parsed from the input file
        """
        return None