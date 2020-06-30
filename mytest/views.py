from django.shortcuts import render
from . import models
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def save_keyrecord(request, machine_id, active_time, scene_name, text_index):
    key_record = models.KeyRecord(m_id=machine_id, m_scene_name=scene_name, m_text_index=text_index, m_active_time=active_time)
    key_record.save()
    return HttpResponse("id=%s time=%s name=%s index=%d" % (machine_id, key_record.m_active_time, key_record.m_scene_name, key_record.m_text_index))

