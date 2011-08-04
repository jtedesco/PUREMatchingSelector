__author__ = 'Jon Tedesco'

class Mentee(object):
    """
     Represents a PURE mentee, containing information such as their year, interests, and qualifications.
    """

    def __init__(self, netId, firstName, lastName, year, email, qualifications, courses, mentors, areas):
        """
         Builds a mentee object with the given fields.

            @param  netId           the netid of the mentee
            @param  firstName       the mentee's first name
            @param  lastName        the mentee's last name
            @param  year            the year of the mentee (junior, sophomore, freshman, senior)
            @param  email           the mentee's email address
            @param  qualifications  the mentee's listed qualifications
            @param  courses         the mentee's list of courses complete
            @param  mentors         the list of mentors (mentor objects) that this mentee is interested in working with
            @param  areas           the areas in which the mentee is interested in working
        """

        self.netId = netId
        self.firstName = firstName
        self.lastName = lastName
        self.year = year
        self.email = email
        self.qualifications = qualifications
        self.courses = courses
        self.mentors = mentors
        self.areas = areas

        
    def __eq__(self, otherMentee):
         """
          Compares this mentee to another to determine if they are equal

            @param  otherMentor     The mentor to which to compare this mentor object
         """
         return (self.netId == otherMentee.netId) and (self.firstName == otherMentee.firstName) and (self.lastName == otherMentee.lastName)