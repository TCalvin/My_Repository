from django.db import models
from accounts.models import User


class Course(models.Model):

    level = (
        ('1', '4-5'),
        ('2', '6-8'),
        ('3', '9-12'),
        ('U', 'Undefined')
    )
    course_level = models.CharField(max_length=1, choices=level, default='U')
    instructor = models.CharField(max_length=255, default='TBA')

    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Section(models.Model):
    capacity = models.IntegerField(default=0)
    course = models.ForeignKey(Course)
    session_time = (
        ('1', 'first week of June'),
        ('2', 'second week of June'),
        ('3', 'third week of June'),
        ('U', 'Undefined')
    )
    session = models.CharField(max_length=1, choices=session_time, default='U')
    time_slot = (
        ('1', '9:45-11:15am'),
        ('2', '1:15-2:45pm'),
        ('U', 'Undefined')
    )
    section_time = models.CharField(max_length=1, choices=time_slot, default='U')

    def __str__(self):                              ########
        return self.session + self.section_time     ########


class Take(models.Model):
    user = models.ForeignKey(User)
    section = models.ForeignKey(Section)
