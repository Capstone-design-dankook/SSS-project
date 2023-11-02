from django.shortcuts import render
from .models import Final1
from django.db.models import Avg

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams["font.family"] = "Malgun Gothic"
rcParams["axes.unicode_minus"] = False

def grapgh_view(request):
    data = Final1.objects.all()

    x = ['00~06', '06~11', '11~14', '14~17', '17~21', '21~24']

    y_values = [data.aggregate(Avg('시간대0006유동인구수'))['시간대0006유동인구수__avg'],
               data.aggregate(Avg('시간대0611유동인구수'))['시간대0611유동인구수__avg'],
               data.aggregate(Avg('시간대1114유동인구수'))['시간대1114유동인구수__avg'],
               data.aggregate(Avg('시간대1417유동인구수'))['시간대1417유동인구수__avg'],
               data.aggregate(Avg('시간대1721유동인구수'))['시간대1721유동인구수__avg'],
               data.aggregate(Avg('시간대2124유동인구수'))['시간대2124유동인구수__avg']]

    #x = [entry.상권코드 for entry in data]  # 필요한 필드로 데이터 구성
    #y = [entry.점포수 for entry in data]

    # 그래프 그리기
    plt.bar(x, y_values, color='skyblue')
    plt.title('시간대별 평균 유동인구수')
    plt.xlabel('시간대')
    plt.ylabel('유동인구수')
    plt.grid(axis='y', alpha=0.5)

    # 그래프를 이미지로 변환
    import io
    import urllib, base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'output/graphic.html', {'graphic': graphic})

def index(request):
    return render(request, 'output/index.html',)