from django.db import models

class TextModel(models.Model):

  text =models.CharField(max_length=500)

  def __str__(self):
    return self.text