__author__ = 'Jon Tedesco'

class Matcher(object):
    """
     This file should perform the matchings of mentees to mentors
    """

    def __init__(self, mentors, mentees):
        """
         Build this matcher utility from a list of mentors and mentees.

            @param  mentors     The list of mentors for this semester
            @param  mentees     The list of mentees for this semester
        """

        self.mentors = mentors
        self.mentees = mentees

        # Build the inverted index for mentors to mentees, specifically mentees that are interested in a given mentor, that
        #   have not yet been claimed by some mentor
        self.menteesInterestedInMentors = {}
        for mentor in mentors:
            self.menteesInterestedInMentors[mentor] = self.generateMenteeListForMentor(mentor)


    def generateMenteeListForMentor(self, mentor):
        """
          Returns the list of mentees that have applied for a given mentor.

            @param  mentor  The mentor for which to find applicants
            @return         The list of mentees that applied to this mentor
        """

        # The list of mentees that chose this mentor
        menteesWhoChoseMentor = []

        # Loop through all the mentees
        for mentee in self.mentees:
            if mentor in mentee.mentors:
                menteesWhoChoseMentor.append(mentee)

        # Return the list of mentees who chose this mentor
        return menteesWhoChoseMentor


    def generateMentorListForMentee(self, mentee):
        """
          Returns the list of mentors that have be chosen by a given mentee.

            @param  mentee  The mentee whose choices to find
            @return         The list of mentors chosen by this mentee
        """
        return mentee.mentors


    def generateMenteeMentorMatching(self):
        """
          Find the best matching for the list of mentees and mentors for this matcher object. The rules are as follows:

            <ul>
             <li> A mentor is given his/her first choice where ever possible.
             <li> In the event that the sets of students given to each mentor overlap, the mentor with fewer applicants
                    wins the tie.
            </ul>

            @return a <code>Matching</code> object that contains the matching generated
        """

        # Create a dictionary for the mentors that will hold the number of mentees assigned to each mentor in this matching
        mentorMatchCounts = {}
        for mentor in self.mentors:
            mentorMatchCounts[mentor] = 0

        # While this matching is not complete, continue matching
        assignedMentees = []
        while not self.isComplete():

            # Greedily try to assign mentees to mentors, and fix conflicts if we find them
            for mentor in self.mentors:

                # If this mentor can take any more mentees
                if self.wantsMoreMentees(mentor):
                    
                    # Case where we have no conflict, add him to this matching
                    nextMenteeWanted = mentor.menteesWanted[0]
                    if nextMenteeWanted not in assignedMentees:
                        assignedMentees.append(mentor.menteesWanted)
                        mentor.menteesWanted.remove(nextMenteeWanted)
                        mentor.mentees.append(nextMenteeWanted)

                    # Handle a conflict
                    else:

                        # Find the mentor who already 'claimed' this mentee, and remove him from his mentees list
                        otherMentor = self.findMentorWhoHasMentee(nextMenteeWanted)

                        # The case that the new mentor should have this mentee
                        if len(self.menteesInterestedInMentors[mentor]) < len(self.menteesInterestedInMentors[otherMentor]):
                            mentor.mentees.append(nextMenteeWanted)
                            otherMentor.mentees.remove(nextMenteeWanted)

                        # Remove him from the queue of mentees to try to match to this mentor
                        mentor.mentesWanted.remove(nextMenteeWanted)

        return None


    def isComplete(self):
        """
         Helper function to determine whether the mentors are matched up to their capacity yet

            @return true or false, depending on whether the matching is 'complete'
        """

        for mentor in self.mentors:

            # If this mentor is not up to capacity, then check to see if there are any available mentees remaining. If
            #  both of these cases is true, then this matching is not complete
            if self.wantsMoreMentees(mentor):
                return False

        # Otherwise, this is complete
        return True


    def wantsMoreMentees(self, mentor):
        """
         Helper function that determines whether a mentor wants more mentees or not
        """
        return (mentor.numberOfMenteesWanted > len(mentor.mentees)) and (len(self.menteesInterestedInMentors[mentor]) > 0)

    
    def findMentorWhoHasMentee(self, mentee):
        """
         Helper function to find the mentor who has a given mentee in his 'mentees' list
        """
        for mentor in self.mentors:
            if mentee in mentor.mentees:
                return mentor
        return None