
class Student(object):
    """
    Description of the class

    Methods:
        name: str represents the name of the student
    Attributes:
        ....
    """

    def __init__(self, name, course):
        self.__name = name
        self._course = course
        self.__age = None

    def print_my_name(self):
        """
        This function prints the name of the student
        :return: None
        """

        print self.__name

    def what_is_my_age(self, age):
        """

        :param age:
        :return:
        """
        print "Student " + str(self.__name) + " has the age of " + str(age) + ""

    def set_my_age(self, age):
        """

        :param age:
        :return:
        """
        self.__age = age
        print "Updated the age..."

    def get_my_age(self):
        """

        :return:
        """
        return self.__age




# design patterns
# I am X bootstrap


