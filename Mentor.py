__author__ = 'Jon Tedesco'

class Mentor(object):
    """
     This class represents a mentor object, and contains all information for a mentor.
    """

    def __init__(self, firstName, lastName, email, numberOfMenteesWanted, menteesWanted=None):
        """
         Builds a mentor given all information for this mentor

            @param  firstName               the mentor's first name
            @param  lastName                the mentor's last name
            @param  email                   the mentor's email address
            @param  numberOfMenteesWanted   the mentor's current research area
            @param  menteesWanted           the preference list of mentees for this mentor
        """

        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.numberOfMenteesWanted = numberOfMenteesWanted
        self.menteesWanted = menteesWanted
        self.mentees = []

        
    def __eq__(self, otherMentor):
         """
          Compares this mentor to another to determine if they are equal

            @param  otherMentor     The mentor to which to compare this mentor object
         """
         return (self.firstName == otherMentor.firstName) and (self.lastName == otherMentor.lastName)