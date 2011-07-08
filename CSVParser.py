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
        self.csvFile = csv.reader(open(filePath, 'rb'), delimiter=delimiter, quoateChar=quoteCharacter)


    def parseMentees(self):
        """
         From the input file, parse a list of mentee objects.

            @return     The list of mentees parsed from the input file
        """
        return None


    def parseMentors(self):
        """
         From the input file, parse a list of mentor objects

            @return     The list of mentor objects parsed from the input file
        """
        return None