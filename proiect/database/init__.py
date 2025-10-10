# هذا الملف يجعل المجلد package في Python
from .db import db
from .models import (
    ImamModel, 
    PrayerTimeModel, 
    DonorModel, 
    DonationModel,
    StudentModel, 
    GroupModel, 
    ScheduleModel
)

__all__ = [
    'db',
    'ImamModel',
    'PrayerTimeModel', 
    'DonorModel',
    'DonationModel',
    'StudentModel',
    'GroupModel', 
    'ScheduleModel'
]