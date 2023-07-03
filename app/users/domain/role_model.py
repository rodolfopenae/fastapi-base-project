from enum import Enum

class Role(str, Enum):
    admin = "admin"
    mentor = "mentor"
    coach = "coach"
    trainee = "trainee"