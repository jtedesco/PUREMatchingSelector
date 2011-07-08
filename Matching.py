__author__ = 'Jon Tedesco'

class Matching(object):
    """
     This class represents a matching between mentors and mentees.
    """

    def __init__(self):
        """
         Build a matching with an empty set of mentor matching lists. Mentor preference lists are represented as a
          dicitonary of lists, where each dictionary key is a mentor, and its value is the ranked list of mentees assigned
          to this mentor.
        """

        self.matching = {}


    def addPairToMatching(self, mentor, mentee):
        """
         Add a pair of mentor, mentee to this matching.

            @param  mentor  The mentor who we are adding
            @param  mentee  The mentee who we are adding
        """

        # Check to see if this mentor is already in our dictionary, and add him if not
        if mentor not in self.matching.keys():
            self.matching[mentor] = []

        # Add this mentee to the mentor's matching list, throw an exception if it makes the mentor exceed his/her wanted
        #  number of mentees
        if len(self.matching[mentor]) < mentor.numberOfMenteesWanted:
            self.matching[mentor].append(mentee)
        else:
            raise Exception("Exceeding number of mentees for mentor:\n" + mentor)
  