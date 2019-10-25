import os

from django.conf import settings
from django.db import models


class DonwloadFileModel(models.Model):
    """
    파일 모델

    title : 파일명
    file : 파일
    """
    title = models.CharField(max_length=100, verbose_name="File name", default='unnamed')
    file = models.FileField(upload_to="files", default='')

    def __str__(self):
        return self.title

class ResultFileModel(models.Model):
    """
    사우론 결과파일 모델

    user_id : 요청자 아이디
    title : 파일명
    file : 파일
    """
    user_id = models.CharField(max_length=20, default='unnamed')
    title = models.CharField(max_length=100, verbose_name="Sauron Results Files", default='untitled')
    file = models.FileField(upload_to="sauron_results", default='')

    def __str__(self):
        return self.user_id
