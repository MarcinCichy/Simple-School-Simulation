class School:
    def __init__(self, place):
        self.place = place

    def where(self):
        return self.place
   
    
class SchoolCommunity(School):
    def __init__(self, name, surname, profession, place):
        super().__init__(place)
        self.name = name
        self.surname = surname
        self.profession = profession
  
        
    def talk(self, sentence):
        return f"{self.profession} {self.name} says {sentence}."

    def walk(self):
        return f"{self.profession} {self.name} {self.surname} walk  around {super().where()}"

    def is_present(self, presence):
        if presence == "present":
            return f" is in {super().where()}."
        else:
            return f" is somwhere in space."
        

class Pupil(SchoolCommunity):
    def __init__(self, name, surname, profession, place, age, grade, avr_grade, presence):
        super().__init__(name,surname, profession, place)
        self.age = age
        self.grade = grade
        self.avr_grade = avr_grade
        self.presence = super().is_present(presence)
     
   
    def run(self):
        return f"{self.profession} {self.name} runs back and forth in the {self.place}."

    def learn(self):
        if self.presence == " is somwhere in space.":
            return f"{self.name} {self.surname} is not in {self.place} and he will be Blue Bird."
        else:
            return f"{self.name} {self.surname} is in {self.place} and learns."

class Teacher(SchoolCommunity):
    def __init__(self, name, surname, profession, subject, place):
        super().__init__(name,surname,profession, place)
        self.subject = subject
        self.place = super().where()

    def teach(self):
        return f"teachs {self.subject}"

    def issue_grade(self):
        pass

    def drink_coffee(self):
        if self.place == "Teacher room":
            return f"{self.name} {self.surname} is in {super().where()} and drinks coffee." 
    
class Headmaster(SchoolCommunity):
    pass




pup1 = Pupil("Marcin", "Cichy", "pupil", "classroom_3", 10, "IIID", 4.5, "absent")
pup2 = Pupil("Kevin", "Arnold", "pupil", "Teacher room", 10, "IIA", 2.5, "absent")
teacher1 = Teacher("Anna", "Nowak", "teacher","matematyka", "classroom_3")
school_room1 = School("classroom_2")
print(pup1.talk("I'm boring"))
print(teacher1.talk("Sit down!"))
print(f"{teacher1.walk()} and {teacher1.teach()}" )
print(f"{pup2.name} {pup2.surname} is in a {School.where(school_room1)}")
pup2.place = "corridor"
print(pup2.run())
print(f"{pup1.name} {pup1.surname} has a {pup1.avr_grade} average grades")
pup2.place = "library"
print(pup1.surname + pup1.is_present("absent"))
print(pup2.surname + pup2.is_present("absent"))
pup1.presence = "present"
pup2.presence = "present"
print(pup1.learn())
print(pup2.learn())
teacher1.place = "Teacher room"
print(teacher1.drink_coffee())

headmaster = Headmaster("John", "Rambo", "Headmaster", "School office")
print(f"{headmaster.profession} {headmaster.name} {headmaster.surname} is in {headmaster.place}")


# print(Teacher.__mro__)
# print(Pupil.__mro__)
# print(SchoolCommunity.__mro__)