# Overview

Simple matching engine for automating the mentee-mentor matching process for the PURE undergraduate research organization
in engineering at UIUC. To learn more about the PURE program, see https://wiki.engr.illinois.edu/display/PURE/Home


# Process and Usage

This script is used in two stages:

<ol>
<li>
    The preliminary matching stage, where mentors are paired with all mentees that applied to him / her.

    ## Input

    To generate the lists of mentees assigned to mentors, run the <tt>RunPreliminaryMatching.py</tt> script. This expects two
    CSV input files

    * The mentor file

        Contains the names of mentors, separated on each line. Formatted as:

        <pre>
        Name
        Mentor X
        Mentor Y
        ...
        </pre>

        This will be parsed into two <tt>Mentor</tt> objects.

    * The mentee application file

        Contains the survey responses of mentee applicants. Specifically, this file is formatted as a CSV file, formatted as:

        <table>
            <tr>
                <th>UserId</th> <th>Q1: First Name</th> <th> ... </th> <th>Mentor X</th> <th>Mentor Y</th> <th> ... </th> <th>Mentor X</th> <th>Mentor Y</th>
            </tr>
            <tr>
                <td>student1@illinois.edu</td> <td>John</td> <td> ... </td> <td>1</td> <td>0</td> <td>...</td> <td>0</td> <td>1</td>
            </tr>
            <tr>
                <td>student2@illinois.edu</td> <td>Jane</td> <td> ... </td> <td>1</td> <td>0</td> <td>...</td> <td>0</td> <td>0</td>
            </tr>
        </table>

        Arbitrary student data could be in the omitted columns, but we focus on the mentor application columns. In this example,
        mentee applicants were given two choices (first and second choices) for mentors to work with. This student, *student1*,
        selected *Mentor X* as his first choice, and *Mentor Y* as his second choice.

        During the preliminary matching, this means that *student1* will be added to the preference lists of *Mentor X*
        and *Mentor Y*.

    ## Output

    The output for the prelimary stage will be in a folder specified by the user, where a CSV will generated for each mentor,
    showing the list of students who applied to him / her and their application information.

</li>
<li>  The final matching stage, where the actual matching is performed, given the preference lists for both mentors and mentees.

    To generate the mentor / mentee matchings, run the <tt>RunMatching.py</tt> script. This expects two CSV input files:

    * The mentor file

        Contains the names of mentors, the number of mentees they are willing to take, and an ordered list of their top
        choices for students.

        For example, continuing our example from above, the mentors input may look like this:

        <table>
            <tr>
                <th>Name</th> <th>Number of Mentees</th> <th>Mentee 1</th> <th>Mentee 2</th> <th>...</th>
            </tr>
            <tr>
                <td>Mentor X</td> <td>1</td> <td> student1 </td> <td><td> <td><td>
            </tr>
            <tr>
                <td>Mentor Y</td> <td>1</td> <td> student1 </td> <td> student2 <td> <td><td>
            </tr>
        </table>

    * The mentee application file

        This should be the same file as in the first stage

    ## Matching Process

    This is the core of the application, which pairs up mentors and mentees given their mutual preference lists. The
    matching will strive for a maximum matching on the data, and satisfy mentor preference lists wherever possible.

    In the above exampe, the following matching will be obtained:

    > Mentor X: student1
    > Mentor Y: student2

    This is because, although *Mentor Y* placed *student1* above *student2* in his/her preference list, pairing *Mentor Y*
    with *student1* would have resulted in a smaller matching, since *Mentor X* would have been unmatched.

    ## Output

    Once a matching has been found, the script will simply output the matching via the console.
</li>
</ol>

# Requirements

* Python 2.7 or newer
