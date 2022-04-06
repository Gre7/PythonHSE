# class Student:
#   def __init__(self, id, title, place, gradeMid, gradeMin, percentil, gpa):
#       self.id = id
#       self.title = title
#       self.place = place
#       self.gradeMid = gradeMid
#       self.gradeMid = gradeMid
#       self.gradeMin = gradeMin
#       self.percentil = percentil
#       self.gpa = gpa

from dataclasses import dataclass


@dataclass
class Student:
    id: int
    title: str
    place: int
    gradeMid: float
    gradeMin: int
    percentil: int
    gpa: float

    def __init__(self, id: int, title: str, place: int, gradeMid: float, gradeMin: int, percentil: int, gpa: float) -> None:
        self.id = id
        self.title = title
        self.place = place
        self.gradeMid = gradeMid
        self.gradeMin = gradeMin
        self.percentil = percentil
        self.gpa = gpa