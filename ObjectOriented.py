# class Person():
#     def __init__(self):
#         print('Person Initialized')
#
# person1 = Person()


# class Person():
#     is_staff= False
#     def __init__(self,fname,lname):
#         self.fname= fname
#         self.lname = lname
#
# person1 = Person('Apoorba','Rana')
# print(person1.fname)
# print(person1.lname)
# # print(Person.fname) Class cannot access instance attribute
# print(Person.is_staff)


# class Person():
#     TITLES = ['Mr', 'Mrs', 'Ms']
#     def __init__(self,title,fname,lname,allowed_title=TITLES):
#
#         if title not in allowed_title:
#             raise ValueError('That is not a valid title')
#         self.title = title
#         self.fname = fname
#         self.lname = lname
#
# person1 = Person('Mr','Apoorba','Rana')
# print('Hello {} {} {}'.format(person1.title,person1.fname,person1.lname))
# person2 = Person('Mrs','Srijana','Shakya')
# print('Hello {} {} {}'.format(person2.title,person2.fname,person2.lname))
# print(Person.TITLES)


# class Animal():
#     #global pets
#
#     def __init__(self):
#         self.pets = []
#
#     def add_pets(self,name):
#         self.pets.append(name)
#     def get_pets(self):
#         return self.pets
#
# a1 = Animal()
# a1.add_pets('Cat')
# print(a1.get_pets())
# a2 = Animal()
# print(a2.get_pets())
# a3= Animal()
# a3.add_pets('Dog')
# print(a3.get_pets())


# class Student():
#     def __init__(self,fname,lname,email,contact,address):
#         self.fname = fname
#         self.lname = lname
#         self.email = email
#         self.contact = contact
#         self.address = address
#
#     def display_full_name(self):
#         full_name = self.fname+''+self.lname
#         return full_name
#     def display_email(self):
#         return self.email
#     def display_contact(self):
#         return self.contact
#     def display_address(self):
#         return self.address
#
# student1 = Student('Apoorba','Rana','apoorba@gmail.com','1234567890','Nepal')
# print(student1.display_full_name())
# print(student1.display_email())
# print(student1.display_contact())
# print(student1.display_address())


# class Traniee():
#
#     def set_height(self,height):
#         self.height = height
#
#     def get_height(self):
#         return self.height
#
# trainee1= Traniee()
# trainee1.set_height('5ft')
# print(trainee1.get_height())


class College():

    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name

c1 = College('Kantipur')
print(c1)


