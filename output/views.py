from django.shortcuts import render
from .models import *
from django.db.models import Avg
import folium
import pandas as pd
from django.http import HttpResponse
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

def cluster_group(request) : 
    # 분기별 상권 데이터 = area
    data_from_db = Final1.objects.all()
    area_1 = pd.DataFrame(list(data_from_db.values()))
    
    # 분기별 업종 데이터 = category
    data_from_db = HANSIC_1.objects.all()
    category_1 = pd.DataFrame(list(data_from_db.values()))
    category_1.fillna(0,inplace=True)
    category_1_sales = category_1.groupby('cluster')['분기당매출금액'].mean().reset_index()
    category_1_population = category_1.groupby('cluster')['총유동인구수'].mean().reset_index()
    
    #업종 백분위구하기
    total_1 = category_1.loc[0,'분기당매출금액']+category_1_sales.loc[1,'분기당매출금액']+category_1_sales.loc[2,'분기당매출금액']+category_1_sales.loc[3,'분기당매출금액']+category_1_sales.loc[4,'분기당매출금액']
    data_1 = pd.DataFrame({'cluster':[0,1,2,3,4], 
                     '매출백분율':[round(category_1_sales.loc[0,'분기당매출금액']/total_1*100.0, 4),
                               round(category_1_sales.loc[1,'분기당매출금액']/total_1*100.0, 4),
                               round(category_1_sales.loc[2,'분기당매출금액']/total_1*100.0, 4),
                               round(category_1_sales.loc[3,'분기당매출금액']/total_1*100.0, 4),
                               round(category_1_sales.loc[4,'분기당매출금액']/total_1*100.0, 4)]})
    
    # 사용자 입력 업종의 유동인구 총합
    total_1 = 0
    total_1 = category_1_population.loc[0,'총유동인구수']+category_1_population.loc[1,'총유동인구수']+category_1_population.loc[2,'총유동인구수']+category_1_population.loc[3,'총유동인구수']+category_1_population.loc[4,'총유동인구수']
    
    #업종 유동인구 백분율
    data_1['유동인구백분율'] = [round(category_1_population.loc[0,'총유동인구수']/total_1*100.0, 4),
                            round(category_1_population.loc[1,'총유동인구수']/total_1*100.0, 4),
                            round(category_1_population.loc[2,'총유동인구수']/total_1*100.0, 4),
                            round(category_1_population.loc[3,'총유동인구수']/total_1*100.0, 4),
                            round(category_1_population.loc[4,'총유동인구수']/total_1*100.0, 4)]
    
    data_1['총백분율'] = (data_1['매출백분율']+data_1['유동인구백분율'])/2  
    data_1 = data_1[['cluster','총백분율']]
    data_1 = data_1.sort_values('총백분율')
    data_1 = data_1.reset_index(drop=True)
    data_1['상권코드'] = [[],[],[],[],[]]
    
    for i in range(1,5):
        data_1.loc[i,'총백분율'] = data_1['총백분율'].values[i-1] + data_1['총백분율'].values[i]
    data_1.loc[4,'총백분율'] = 100.0

    
    # 사용자 입력 행정동의 상권 모음 = location
    location_1 = area_1[area_1['행정동코드']=='11740620']
    location_1 = location_1.reset_index(drop=True)
    
    #location안 상권들의 분기당매출금액 백분율 구하기
    t = 0
    for i in range(len(location_1)):
        t = t+location_1.loc[i,'분기당매출금액']
    location_1['백분율'] = location_1['분기당매출금액']/t*100.0
    
    location_1 = location_1.sort_values('백분율')
    location_1 = location_1.reset_index(drop = True)
    
    #location 안 상권들 누적 백분율로 만들기
    for i in range(1,len(location_1)-1) :
        location_1.loc[i,'백분율'] = location_1['백분율'].values[i-1] + location_1['백분율'].values[i]
    location_1.loc[len(location_1)-1,'백분율'] = 100.0
    
    #상권 데이터의 백분율이 업종 데이터 클러스터 중 어디에 포함되는지 분류
    for i in range(len(location_1)) :
        value = location_1['백분율'].values[i]
        
        if value <= data_1['총백분율'].values[0] :
            data_1.loc[0]['상권코드'].append(location_1['상권코드'].values[i])
        elif ((value > data_1['총백분율'].values[0]) & (value <= data_1['총백분율'].values[1])) :
            data_1.loc[1]['상권코드'].append(location_1['상권코드'].values[i])
        elif ((value > data_1['총백분율'].values[1]) & (value <= data_1['총백분율'].values[2])) :
            data_1.loc[2]['상권코드'].append(location_1['상권코드'].values[i])
        elif ((value > data_1['총백분율'].values[2]) & (value <= data_1['총백분율'].values[3])) :
            data_1.loc[3]['상권코드'].append(location_1['상권코드'].values[i])
        elif ((value > data_1['총백분율'].values[3]) & (value <= data_1['총백분율'].values[4])) :
            data_1.loc[4]['상권코드'].append(location_1['상권코드'].values[i])
        else :
            print("잘못된 값입니다.")


    data_1 = data_1.sort_values(['cluster']).reset_index(drop=True)
    
        
    context = {'group' : data_1.to_dict(orient='records')}
    
    return render(request, 'output/group.html', context)



def final_data(request) : 
    # 분기별 상권 데이터 = area
    data_from_db = Final1.objects.all()
    area_1 = pd.DataFrame(list(data_from_db.values()))
    
    # 분기별 업종 데이터 = category
    data_from_db = HANSIC_1.objects.all()
    category_1 = pd.DataFrame(list(data_from_db.values()))
    category_1.fillna(0,inplace=True)
    category_1_sales = category_1.groupby('cluster')['분기당매출금액'].mean().reset_index()
    category_1_population = category_1.groupby('cluster')['총유동인구수'].mean().reset_index()
    
    #업종 백분위구하기
    total_1 = category_1.loc[0,'분기당매출금액']+category_1_sales.loc[1,'분기당매출금액']+category_1_sales.loc[2,'분기당매출금액']+category_1_sales.loc[3,'분기당매출금액']+category_1_sales.loc[4,'분기당매출금액']
    data_1 = pd.DataFrame({'cluster':[0,1,2,3,4], 
                     '매출백분율':[round(category_1_sales.loc[0,'분기당매출금액']/total_1*100.0, 4),
                               round(category_1_sales.loc[1,'분기당매출금액']/total_1*100.0, 4),
                               round(category_1_sales.loc[2,'분기당매출금액']/total_1*100.0, 4),
                               round(category_1_sales.loc[3,'분기당매출금액']/total_1*100.0, 4),
                               round(category_1_sales.loc[4,'분기당매출금액']/total_1*100.0, 4)]})
    
    # 사용자 입력 업종의 유동인구 총합
    total_1 = 0
    total_1 = category_1_population.loc[0,'총유동인구수']+category_1_population.loc[1,'총유동인구수']+category_1_population.loc[2,'총유동인구수']+category_1_population.loc[3,'총유동인구수']+category_1_population.loc[4,'총유동인구수']
    
    #업종 유동인구 백분율
    data_1['유동인구백분율'] = [round(category_1_population.loc[0,'총유동인구수']/total_1*100.0, 4),
                            round(category_1_population.loc[1,'총유동인구수']/total_1*100.0, 4),
                            round(category_1_population.loc[2,'총유동인구수']/total_1*100.0, 4),
                            round(category_1_population.loc[3,'총유동인구수']/total_1*100.0, 4),
                            round(category_1_population.loc[4,'총유동인구수']/total_1*100.0, 4)]
    
    data_1['총백분율'] = (data_1['매출백분율']+data_1['유동인구백분율'])/2  
    data_1 = data_1[['cluster','총백분율']]
    data_1 = data_1.sort_values('총백분율')
    data_1 = data_1.reset_index(drop=True)
    data_1['상권코드'] = [[],[],[],[],[]]
    
    for i in range(1,5):
        data_1.loc[i,'총백분율'] = data_1['총백분율'].values[i-1] + data_1['총백분율'].values[i]
    data_1.loc[4,'총백분율'] = 100.0

    
    # 사용자 입력 행정동의 상권 모음 = location
    location_1 = area_1[area_1['행정동코드']=='11740620']
    location_1 = location_1.reset_index(drop=True)
    
    #location안 상권들의 분기당매출금액 백분율 구하기
    t = 0
    for i in range(len(location_1)):
        t = t+location_1.loc[i,'분기당매출금액']
    location_1['백분율'] = location_1['분기당매출금액']/t*100.0
    
    location_1 = location_1.sort_values('백분율')
    location_1 = location_1.reset_index(drop = True)
    
    #location 안 상권들 누적 백분율로 만들기
    for i in range(1,len(location_1)-1) :
        location_1.loc[i,'백분율'] = location_1['백분율'].values[i-1] + location_1['백분율'].values[i]
    location_1.loc[len(location_1)-1,'백분율'] = 100.0
    
    #상권 데이터의 백분율이 업종 데이터 클러스터 중 어디에 포함되는지 분류
    for i in range(len(location_1)) :
        value = location_1['백분율'].values[i]
        
        if value <= data_1['총백분율'].values[0] :
            data_1.loc[0]['상권코드'].append(location_1['상권코드'].values[i])
        elif ((value > data_1['총백분율'].values[0]) & (value <= data_1['총백분율'].values[1])) :
            data_1.loc[1]['상권코드'].append(location_1['상권코드'].values[i])
        elif ((value > data_1['총백분율'].values[1]) & (value <= data_1['총백분율'].values[2])) :
            data_1.loc[2]['상권코드'].append(location_1['상권코드'].values[i])
        elif ((value > data_1['총백분율'].values[2]) & (value <= data_1['총백분율'].values[3])) :
            data_1.loc[3]['상권코드'].append(location_1['상권코드'].values[i])
        elif ((value > data_1['총백분율'].values[3]) & (value <= data_1['총백분율'].values[4])) :
            data_1.loc[4]['상권코드'].append(location_1['상권코드'].values[i])
        else :
            print("잘못된 값입니다.")


    data_1 = data_1.sort_values(['cluster']).reset_index(drop=True)
    #print('<<data_1>>\n', data_1)
    
    # 만약 2번 클러스터에 대해서 대표 데이터를 뽑는다면
    # 해당 클러스터에 분류된 상권이 하나도 없을 경우도 생각. 
    if len(data_1.loc[2,'상권코드']) > 0 :
        df = pd.DataFrame({})

        for i in range(len(data_1.loc[2,'상권코드'])):
            df = pd.concat([df, location_1[location_1['상권코드']==data_1.loc[2,'상권코드'][i]]])
    else : 
        print('지나가세요')

    
    df.drop(['상권코드'],axis=1, inplace=True)
    df.drop(['행정동코드'],axis=1, inplace=True)
    df.drop(['백분율'], axis=1, inplace=True)

    dff = df.mean(axis=0).to_frame().T    


    category_1.drop(['상권코드'], axis=1, inplace=True)   
    grouped_category = category_1.groupby('cluster').mean().reset_index()
    final = grouped_category[grouped_category['cluster']==2]
    dff.drop(['분기코드'], axis=1, inplace=True)
    final.drop(['cluster'], axis=1, inplace=True)
    


    final = pd.concat([final,dff])
    final = final.mean().to_frame().T

    
    
    
    context = {'final' : final.to_dict(orient='records')}
    
    return render(request, 'output/group.html', context)




def input_district(request):
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

