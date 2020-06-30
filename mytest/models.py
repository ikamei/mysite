from django.db import models

# Create your models here.
class KeyRecord(models.Model):
    m_id = models.CharField(max_length=200, default=0)
    m_scene_name = models.CharField(max_length=200)
    m_text_index = models.IntegerField(default=0)
    m_active_time = models.DateTimeField('date published')
