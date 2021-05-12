from django.db import models


class Task(models.Model):
    heading = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Описание')
    date = models.DateTimeField('Дэдлайн', null=True)
    category = models.ForeignKey('categories.Category', models.CASCADE, related_name='task_category', null=True)
    user = models.ForeignKey('users.User', models.CASCADE, related_name='task_user', null=True)

    def __str__(self):
        return self.heading