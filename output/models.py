from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class BusinessLocation(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    상권코드명 = models.CharField(max_length=100, blank=True, null=True)
    x = models.FloatField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    y = models.FloatField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)

class DistrictCode(models.Model):
    행정동코드 = models.CharField(max_length=10, blank=True, null=True)
    행정동명 = models.CharField(max_length=15, blank=True, null=True)

class BusinessCode(models.Model):
    구상권코드 = models.CharField(max_length=10, blank=True, null=True)
    상권코드명 = models.CharField(max_length=100, blank=True, null=True)
    행정동코드 = models.CharField(max_length=10, blank=True, null=True)

class Final1(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    분기코드 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(4)], blank=True, null=True)
    행정동코드 = models.CharField(max_length=10, blank=True, null=True)

class Final2(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    분기코드 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(4)], blank=True, null=True)
    행정동코드 = models.CharField(max_length=10, blank=True, null=True)

class Final3(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    분기코드 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(4)], blank=True, null=True)
    행정동코드 = models.CharField(max_length=10, blank=True, null=True)

class Final4(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    분기코드 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(4)], blank=True, null=True)
    행정동코드 = models.CharField(max_length=10, blank=True, null=True)

class Final_1(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    업종코드 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(9)], blank=True, null=True)
    분기코드 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(4)], blank=True, null=True)
    행정동코드 = models.CharField(max_length=10, blank=True, null=True)

class Final_2(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    업종코드 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(9)], blank=True, null=True)
    분기코드 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(4)], blank=True, null=True)
    행정동코드 = models.CharField(max_length=10, blank=True, null=True)

class Final_3(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    업종코드 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(9)], blank=True, null=True)
    분기코드 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(4)], blank=True, null=True)
    행정동코드 = models.CharField(max_length=10, blank=True, null=True)

class Final_4(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    업종코드 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(9)], blank=True, null=True)
    분기코드 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(4)], blank=True, null=True)
    행정동코드 = models.CharField(max_length=10, blank=True, null=True)
    
'''
class Industry(models.Model):
    업종코드 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)  
'''

class BBANG_1(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class BBANG_2(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class BBANG_3(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)
    
class BBANG_4(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)
    
class BUNSIC_1(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class BUNSIC_2(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)
    
class BUNSIC_3(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class BUNSIC_4(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class CAFE_1(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class CAFE_2(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class CAFE_3(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)
    
class CAFE_4(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class CHICKEN_1(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class CHICKEN_2(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class CHICKEN_3(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class CHICKEN_4(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class FASTFOOD_1(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class FASTFOOD_2(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class FASTFOOD_3(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class FASTFOOD_4(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class HANSIC(models.Model):
    name = 'HANSIC'
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)
    
    def __str__(self):
        return self.name

class HANSIC_2(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class HANSIC_3(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class HANSIC_4(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)


class HOF_1(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class HOF_2(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class HOF_3(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class HOF_4(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class ILSIC_1(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class ILSIC_2(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class ILSIC_3(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class ILSIC_4(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class YANGSIC_1(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class YANGSIC_2(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class YANGSIC_3(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class YANGSIC_4(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class ZUNGSIC_1(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class ZUNGSIC_2(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class ZUNGSIC_3(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)

class ZUNGSIC_4(models.Model):
    상권코드 = models.CharField(max_length=10, blank=True, null=True)
    분기당매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주중매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    주말매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    화요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    수요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    목요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    금요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    토요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    일요일매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0006매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    남성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대20매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대30매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대40매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대50매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    연령대60이상매출건수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    분기당매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주중매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    주말매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    월요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    화요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    수요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    목요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    금요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    토요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    일요일매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0006매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대0611매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1114매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1417매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대1721매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    시간대2124매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    남성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    여성매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대10매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대20매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대30매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대40매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대50매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    연령대60이상매출금액 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000000)], blank=True, null=True)
    점포수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000)], blank=True, null=True)
    총생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    남성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    여성생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대10생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대20생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대30생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대40생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대50생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    연령대60이상생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0006생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대0611생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1114생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1417생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대1721생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    시간대2124생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    월요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    화요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    수요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    목요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    금요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    토요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    일요일생활인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(10000000)], blank=True, null=True)
    총직장인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100000)], blank=True, null=True)
    집객시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], blank=True, null=True)
    관공서수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    은행수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    대학교수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    백화점수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    슈퍼마켓수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    의료시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교육시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    여가시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    교통시설수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    시간대0006유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대0611유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1114유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1417유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대1721유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    시간대2124유동인구수 = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
    총유동인구수 = models.BigIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000000)], blank=True, null=True)
    cluster = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3)], blank=True, null=True)
        