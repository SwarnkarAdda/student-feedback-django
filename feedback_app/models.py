from django.db import models

class Feedback(models.Model):
    student_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    instructor_name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    comments = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.course_name}"
