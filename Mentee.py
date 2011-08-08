__author__ = 'Jon Tedesco'

class Mentee(object):
    """
     Represents a PURE mentee, containing information such as their year, interests, and qualifications.
    """

    def __init__(self, netId, firstName, lastName, year, email, gpa, mentors):
        """
         Builds a mentee object with the given fields.

            @param  netId           the netid of the mentee
            @param  firstName       the mentee's first name
            @param  lastName        the mentee's last name
            @param  year            the year of the mentee (junior, sophomore, freshman, senior)
            @param  email           the mentee's email address
            @param  gpa             the technical gpa of the applicant
            @param  mentors         the list of mentors (mentor objects) that this mentee is interested in working with
        """

        self.netId = netId
        self.firstName = firstName
        self.lastName = lastName
        self.year = year
        self.email = email
        self.gpa = gpa
        self.mentors = mentors

        
    def __eq__(self, otherMentee):
         """
          Compares this mentee to another to determine if they are equal

            @param  otherMentor     The mentor to which to compare this mentor object
         """
         return (self.netId == otherMentee.netId) and (self.firstName == otherMentee.firstName) and (self.lastName == otherMentee.lastName)