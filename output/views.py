from django.shortcuts import render
from django.http import HttpResponse
from .models import Final_1, Final1, DistrictCode, BusinessCode
from django.db.models import Avg
import pandas as pd

def index(request):
    return render(request, 'output/index.html')

def input(request):
    return render(request, 'output/input.html')

def output(request):
    if request.method == 'GET':
        return render(request, 'output/group.html')

    elif request.method == 'POST':
        selected_industry = request.POST.get('industry')
        selected_neighborhood = request.POST.get('neighborhood')

        try:
            neighborhood = DistrictCode.objects.get(행정동명=selected_neighborhood)
            neighborhood_code = neighborhood.행정동코드

            business_list = Final_1.objects.filter(행정동코드=neighborhood_code, 업종코드=selected_industry)

            business_codes = [item.상권코드 for item in business_list]

            business_names = BusinessCode.objects.filter(구상권코드__in=business_codes)

            names = [business_names.상권코드명 for business_names in business_names]

            value = [business_list.분기당매출금액 for business_list in business_list]

            storenum = [business_list.점포수 for business_list in business_list]

        except DistrictCode.DoesNotExist:
            # 예외 처리 로직 추가
            pass

        data = {
             'neighborhood': selected_neighborhood,
             'neighborhood_code': neighborhood_code,
             'a': value[0],
             'names': names,
             'store': storenum
        }

        return render(request, 'output/group.html', data)
    
def group_detail(request, group_id):
    # 여기에서 group_id를 사용하여 필요한 데이터를 조회하고 렌더링하는 로직을 추가하세요.
    # 예를 들어, 그룹에 해당하는 상세 정보를 가져와서 템플릿에 전달할 수 있습니다.
    # 그런 다음, 템플릿에서 해당 정보를 사용하여 원하는 형태로 표시할 수 있습니다.

    # 아래는 임시로 HttpResponse를 반환하는 예시입니다.
    return HttpResponse(f'Group Detail Page for Group ID {group_id}')
    

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

