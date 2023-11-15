from django.shortcuts import render
from .models import Final_1, Final1, DistrictCode, BusinessCode, BusinessLocation
from django.db.models import Avg
import folium
import pandas as pd

# 최초 상권분석 서비스 소개 페이지
def index(request):
    return render(request, 'output/index.html')

# 사용자 업종, 행정동 입력 페이지
def input(request):
    return render(request, 'output/input.html')

# 지도에 상권 마커 표시, 해당 지역 상권 목록과 분류된 그룹 보여주는 페이지
def output(request):
    if request.method == 'GET':
        return render(request, 'output/group.html')

    # 사용자 입력(post)요청 받았을 때 실행하는 코드
    elif request.method == 'POST':
        selected_industry = request.POST.get('industry') # 업종코드 값 가져오기
        selected_neighborhood = request.POST.get('neighborhood') # 행정동 값 가져오기

        try:
            # 행정동명과 매핑되는 행정동코드 값 가져오기
            neighborhood = DistrictCode.objects.get(행정동명=selected_neighborhood)
            neighborhood_code = neighborhood.행정동코드

            # 상권 1분기에서(임시로) 입력받은 행정동코드, 업종코드에 해당되는 행들 필터링
            business_list = Final_1.objects.filter(행정동코드=neighborhood_code, 업종코드=selected_industry)

            # 위에서 가져온 데이터에서 상권코드 값만 리스트로 가져옴
            business_codes = [item.상권코드 for item in business_list]

            # 상권코드 값이 일치하는 행들 필터링 - 상권명
            business_names = BusinessCode.objects.filter(구상권코드__in=business_codes)

            # 상권코드 값이 일치하는 행들 필터링 - 상권 좌표
            business_locations = BusinessLocation.objects.filter(상권코드__in=business_codes)

            # folium 지도 띄우기
            m = folium.Map(location=[37.5, 127], zoom_start=12)

            # 지도에 좌표 넣고 마커 표시하기
            for business_location in business_locations:
                folium.Marker(
                    location=[business_location.y, business_location.x],
                    popup=business_location.상권코드명,
                ).add_to(m)

        except DistrictCode.DoesNotExist:
            # 예외 처리 로직 추가
            pass

        # 매개변수 넘겨주기
        data = {
             'selected_neighborhood': selected_neighborhood,
             'business_list': business_list,
             'business_names': business_names,
             'map': m._repr_html_(),
        }

        return render(request, 'output/group.html', data)
    
# 그룹별 상세 페이지
def group_detail(request, group_id):
    # 여기에서 group_id를 사용하여 필요한 데이터를 조회하고 렌더링하는 로직을 추가하세요.
    # 예를 들어, 그룹에 해당하는 상세 정보를 가져와서 템플릿에 전달할 수 있습니다.
    # 그런 다음, 템플릿에서 해당 정보를 사용하여 원하는 형태로 표시할 수 있습니다.
    data = Final1.objects.all()  # 데이터베이스에서 데이터 가져오기

    context = {
        'data_00_06': data.aggregate(Avg('시간대0006유동인구수'))['시간대0006유동인구수__avg'],
        'data_06_11': data.aggregate(Avg('시간대0611유동인구수'))['시간대0611유동인구수__avg'],
        'data_11_14': data.aggregate(Avg('시간대1114유동인구수'))['시간대1114유동인구수__avg'],
        'data_14_17': data.aggregate(Avg('시간대1417유동인구수'))['시간대1417유동인구수__avg'],
        'data_17_21': data.aggregate(Avg('시간대1721유동인구수'))['시간대1721유동인구수__avg'],
        'data_21_24': data.aggregate(Avg('시간대2124유동인구수'))['시간대2124유동인구수__avg'],

        'mon_sail': data.aggregate(Avg('월요일매출금액'))['월요일매출금액__avg'],
        'tue_sail': data.aggregate(Avg('화요일매출금액'))['화요일매출금액__avg'],
        'wed_sail': data.aggregate(Avg('수요일매출금액'))['수요일매출금액__avg'],
        'thu_sail': data.aggregate(Avg('목요일매출금액'))['목요일매출금액__avg'],
        'fri_sail': data.aggregate(Avg('금요일매출금액'))['금요일매출금액__avg'],
        'sat_sail': data.aggregate(Avg('토요일매출금액'))['토요일매출금액__avg'],
        'sun_sail': data.aggregate(Avg('일요일매출금액'))['일요일매출금액__avg']
    }

    return render(request, 'output/chart.html', context)
    

# chart.js 테스트 뷰
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

    return render(request, 'output/chart.html', context)

