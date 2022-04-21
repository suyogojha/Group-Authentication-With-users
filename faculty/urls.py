from django.urls import path
from faculty.views import *

app_name = "faculty"

urlpatterns = [
    path('Faculty_Dashboard/', Faculty_Dashboard, name='Faculty_Dashboard'),
    path('Faculty_1/', Faculty_1, name='Faculty_1'),
    path('Faculty_2/', Faculty_2, name='Faculty_2'),
    path('Faculty_3/', Faculty_3, name='Faculty_3'),
    path('Faculty_4/', Faculty_4, name='Faculty_4'),
    path('Student_Dashboard/', Student_Dashboard, name='Student_Dashboard'),
    path('Student_1/', Student_1, name='Student_1'),
    path('Student_2/', Student_2, name='Student_2'),
    path('Student_3/', Student_3, name='Student_3'),
    path('Student_4/', Student_4, name='Student_4'),
]
