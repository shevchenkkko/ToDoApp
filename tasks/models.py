from django.db import models
from django.urls import reverse
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=35, verbose_name='Title')
    description = models.TextField(blank=True, null=True,verbose_name='Description')
    date = models.DateField(verbose_name='Date', auto_now_add=True)
    time = models.TimeField(verbose_name='Time', auto_now_add=True)
    completed = models.BooleanField(default=False,verbose_name='Is completed?')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})
    