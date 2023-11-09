from django.db import models

class DistrictCode(models.Model):
    행정동코드 = models.CharField(max_length=10, blank=True, null=True)
    행정동명 = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.행정동명
