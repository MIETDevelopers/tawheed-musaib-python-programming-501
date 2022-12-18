#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Class and child class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def display(self):
        print(self.firstname, self.lastname)


class Student(Person):
    pass


obj = Student("TAWHEED,MUSAIB")
obj.display()
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms

