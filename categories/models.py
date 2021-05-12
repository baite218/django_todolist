from django.db import models

class Category(models.Model):
    title = models.CharField('Название', max_length=255)
    text = models.TextField('Описание')
    user = models.ForeignKey('users.User', models.SET_NULL, related_name='user_category', null=True)

    def __str__(self):
        return self.title