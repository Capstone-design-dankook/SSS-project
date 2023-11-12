from django.shortcuts import render
from .models import Final1, DistrictCode
from django.db.models import Avg

def input(request):
    return render(request, 'output/input.html')

def output(request):
    if request.method == 'GET':
        return render(request, 'output/group.html')

    elif request.method == 'POST':
        district_name = request.POST.get('neighborhood')  # 사용자가 입력한 행정동명
        data = {
             'neighborhood': district_name
        }

        return render(request, 'output/group.html', data)
    

def chart_view(request):
    data = Final1.objects.all()  # 데이터베이스에서 데이터 가져오기

    context = {
        'data_00_06': data.aggregate(Avg('시간대0006유동인구수'))['시간대0006유동인구수__avg'],
        'data_06_11': data.aggregate(Avg('시간대0611유동인구수'))['시간대0611유동인구수__avg'],
        'data_11_14': data.aggregate(Avg('시간대1114유동인구수'))['시간대1114유동인구수__avg'],
        'data_14_17': data.aggregate(Avg('시간대1417유동인구수'))['시간대1417유동인구수__avg'],
        'data_17_21': data.aggregate(Avg('시간대1721유동인구수'))['시간대1721유동인구수__avg'],
        'data_21_24': data.aggregate(Avg('시간대2124유동인구수'))['시간대2124유동인구수__avg']
    }

    return render(request, 'output/group.html', context)

