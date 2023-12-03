from django.shortcuts import render
from .models import *
from django.db.models import Avg
import folium
import pandas as pd

# 최초 상권분석 서비스 소개 페이지
def index(request):
    return render(request, 'output/index.html')

def intro(request):
    return render(request, 'output/intro.html')

def industry(request):
    return render(request, 'output/industry.html')

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
        selected_industry_name = get_industry_name(selected_industry)
        selected_district = request.POST.get('district')
        selected_neighborhood = request.POST.get('neighborhood') # 행정동 값 가져오기

        business_list = None
        business_names = None
        m = None

        try:
            
            # 행정동명과 매핑되는 행정동코드 값 가져오기
            if selected_neighborhood == '신사동':
                if selected_district == '강남구':
                    neighborhood_code = '11680510'
                else:
                    neighborhood_code = '11620685'
            else:
                neighborhood = DistrictCode.objects.get(행정동명=selected_neighborhood)
                neighborhood_code = neighborhood.행정동코드

        # 업종/분기 매핑
            industry_table_mapping = {
                '한식': Final_3,
                '양식': Final_3,
                '일식': Final_3,
                '중식': Final_2,
                '호프': Final_4,
                '분식': Final_2,
                '패스트푸드': Final_2,
                '치킨': Final_4,
                '카페': Final_4,
                '제과점': Final_3,
            }

            final_table = industry_table_mapping.get(selected_industry_name)

            # 입력받은 행정동코드, 업종코드에 해당되는 행들 필터링
            business_list = final_table.objects.filter(행정동코드=neighborhood_code, 업종코드=selected_industry)

            # 위에서 가져온 데이터에서 상권코드 값만 리스트로 가져옴
            business_codes = [item.상권코드 for item in business_list]

            # 상권코드 값이 일치하는 행들 필터링 - 상권명
            business_names = BusinessCode.objects.filter(구상권코드__in=business_codes)

            if business_list.exists():
                # 상권코드 값이 일치하는 행들 필터링 - 상권 좌표
                business_locations = BusinessLocation.objects.filter(상권코드__in=business_codes)

                # folium 지도 띄우기
                m = folium.Map(location=[business_locations[0].y, business_locations[0].x], zoom_start=14)

                # 지도에 좌표 넣고 마커 표시하기
                for business_location in business_locations:
                    folium.Marker(
                        location=[business_location.y, business_location.x],
                        popup=business_location.상권코드명,
                    ).add_to(m)
            else:
                # 해당 지역에는 해당 업종 상권이 존재하지 않는 경우
                m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

        except DistrictCode.DoesNotExist:
            # 예외 처리 로직 추가
            # 지도에 좌표 넣고 마커 표시하기
            for business_location in business_locations:
                folium.Marker(
                    location=[business_location.y, business_location.x],
                    popup=business_location.상권코드명,
                ).add_to(m)

        except DistrictCode.DoesNotExist as e:
            print(f"Error: {e}")
            pass
        
        #상권명 가져오기
        group_data_business_names = BusinessCode.objects.filter(행정동코드=neighborhood_code)
            
        # cluster_group 함수 호출
        group_data = cluster_group(selected_industry, neighborhood_code)

        #중요피처 가져오는 함수 호출
        important_data = important_feature(selected_industry)

        # 매개변수 넘겨주기
        data = {
             'selected_district': selected_district,
             'selected_neighborhood': selected_neighborhood,
             'selected_industry_name': selected_industry_name,
             'selected_industry' : selected_industry,
             'neighborhood_code' : neighborhood_code,
             'business_list': business_list,
             'business_names': business_names,
             'map': m._repr_html_() if m else None,
             'group_data' : group_data['group'],
             'important_data' : important_data['important_feature'],
             'group_data_business_names' : group_data_business_names,
        }

        return render(request, 'output/group.html', data)


def cluster_group(selected_industry, neighborhood_code) : 
    
    # 분기별 상권 데이터 = area 
    area_list = {'0':Final3, '1':Final3, '2':Final3, '3':Final2, '4':Final2,
                     '5':Final3, '6':Final4, '7':Final4, '8':Final4, '9':Final2}
    area_name = area_list.get(selected_industry)
    data_from_db = area_name.objects.all()
    area_1 = pd.DataFrame(list(data_from_db.values()))
    
    # 분기별 업종 데이터 = category
    category_list = {'0':HANSIC_3, '1':YANGSIC_3, '2':ILSIC_3, '3':ZUNGSIC_2, '4':BUNSIC_2,
                     '5':BBANG_3, '6':CAFE_4, '7':CHICKEN_4, '8':HOF_4, '9':FASTFOOD_2}
    name = category_list.get(selected_industry)
    
    data_from_db = name.objects.all()
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
    location_1 = area_1[area_1['행정동코드']==neighborhood_code]
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
    
    context = {'group' : data_1.to_dict(orient='records')}
    
    return context

#해당 분기의 상권데이터+업종데이터 가져와서 그룹핑
def cluster_group_quarter(selected_industry, neighborhood_code, quarter_code) :
    
    # quarter_code에 맞는 분기의 상권데이터 가져오기
    quarter_list = {'1':Final1, '2':Final2, '3':Final3, '4':Final4}
    quarter_name = quarter_list.get(quarter_code)
    data_from_db = quarter_name.objects.all()
    area_1 = pd.DataFrame(list(data_from_db.values()))
    
    # quarter_code에 맞는 분기의 업종데이터 가져오기
    # 분기별 업종 데이터 = category
    category_list = {'0':'HANSIC', '1':'YANGSIC', '2':'ILSIC', '3':'ZUNGSIC', '4':'BUNSIC',
                     '5':'BBANG', '6':'CAFE', '7':'CHICKEN', '8':'HOF', '9':'FASTFOOD'}
    category_name = category_list.get(selected_industry)
    
    category_name = category_name+'_'+quarter_code

    model_class = globals()[category_name]
    data_from_db = model_class.objects.all()
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
    location_1 = area_1[area_1['행정동코드']==neighborhood_code]
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
            
    
    return data_1
     
#분기별 대표 데이터 생성 함수
def final_data(selected_industry, neighborhood_code, quarter_code, group_id) : 
    
    #그룹핑 데이터 가져오기
    data_1 = cluster_group_quarter(selected_industry,neighborhood_code, quarter_code)
    
    df = pd.DataFrame({})
    if len(data_1.loc[group_id,'상권코드']) == 0:
        return df
    else :
        #해당 분기의 상권데이터 가져오기 + 사용자 입력 행정동 코드만 남기기 = location_1
        quarter_list = {'1':Final1, '2':Final2, '3':Final3, '4':Final4}
        quarter_name = quarter_list.get(quarter_code)
        data_from_db = quarter_name.objects.all()
        area_1 = pd.DataFrame(list(data_from_db.values()))
        location_1 = area_1[area_1['행정동코드']==neighborhood_code]
        location_1 = location_1.reset_index(drop=True)
        location_1.drop(['분기코드'], axis=1, inplace=True)
        location_1.drop(['행정동코드'], axis=1, inplace=True)
        
        #해당 분기의 업종데이터 가져오기
        category_list = {'0':'HANSIC', '1':'YANGSIC', '2':'ILSIC', '3':'ZUNGSIC', '4':'BUNSIC',
                        '5':'BBANG', '6':'CAFE', '7':'CHICKEN', '8':'HOF', '9':'FASTFOOD'}
        category_name = category_list.get(selected_industry)
        category_name = category_name+'_'+quarter_code
        model_class = globals()[category_name]
        data_from_db = model_class.objects.all()
        category_1 = pd.DataFrame(list(data_from_db.values()))
        
        #대표데이터(final_data, 행 하나)만들기
        
        #group_id 매개변수로 받기
        #group_id는 인덱스 번호로 -> 백분율로 정렬했을 때 같은 인덱스를 같은 그룹으로 보기로 함.
        
        # 해당 클러스터에 분류된 상권이 하나도 없을 경우 아예 그룹이 뜨지 않으니 코드에서는 고려하지 않음.(else 문)
        
        category_1.drop(['상권코드'], axis=1, inplace=True)
        grouped_category = category_1.groupby('cluster').mean().reset_index()
        
        final = grouped_category[grouped_category['cluster']==data_1.loc[group_id,'cluster']]
        final.drop(['cluster'], axis=1, inplace=True)
        
        for i in range(len(data_1.loc[group_id, '상권코드'])):
            df = pd.concat([df, location_1[location_1['상권코드']==data_1.loc[group_id,'상권코드'][i]]])
        
        '''if len(data_1.loc[group_id,'상권코드']) > 0 :
            df = pd.DataFrame({})

            for i in range(len(data_1.loc[group_id,'상권코드'])):
                df = pd.concat([df, location_1[location_1['상권코드']==data_1.loc[group_id,'상권코드'][i]]])
        else : 
            pass'''
        
        df.drop(['상권코드'],axis=1, inplace=True)
        dff = df.mean(axis=0).to_frame().T
        
        final = pd.concat([final,dff])
        final = final.mean().to_frame().T

        return final

#클러스터별 중요 피처 가져오는 함수 - DB문제로 잘 돌아가는지 확인 안 됨...
def important_feature(selected_industry):
    data_from_db = Feature.objects.filter(업종코드=int(selected_industry))
    context = {'important_feature' : data_from_db}
    return context

def get_industry_name(code):
    industry_mapping = {
        '0': '한식',
        '1': '양식',
        '2': '일식',
        '3': '중식',
        '4': '분식',
        '5': '제과점',
        '6': '카페',
        '7': '치킨',
        '8': '호프',
        '9': '패스트푸드',
    }
    return industry_mapping.get(code, '알 수 없는 업종')

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
def group_detail_sales(request, selected_district, selected_industry, neighborhood_code, group_id):
    
    #상권명 받아오기
    include_codes = cluster_group(selected_industry, neighborhood_code)
    include_code = include_codes['group'][group_id]['상권코드']
    business_names = BusinessCode.objects.filter(구상권코드__in=include_code)
    business_name = []
    for item in business_names :
        business_name.append(item.상권코드명)
        
    #대표 데이터 가져오는 함수 호출. 1분기~4분기
    final_data_1 = final_data(selected_industry, neighborhood_code, '1', group_id)
    final_data_2 = final_data(selected_industry, neighborhood_code, '2', group_id)
    final_data_3 = final_data(selected_industry, neighborhood_code, '3', group_id)
    final_data_4 = final_data(selected_industry, neighborhood_code, '4', group_id)   
    
    #1분기~4분기 합친 것 = final
    final_quarter = pd.DataFrame({})
    if not final_data_1.empty : 
        final_quarter = pd.concat([final_quarter, final_data_1], ignore_index=True)
    if not final_data_2.empty : 
        final_quarter = pd.concat([final_quarter, final_data_2], ignore_index=True)
    if not final_data_3.empty : 
        final_quarter = pd.concat([final_quarter, final_data_3], ignore_index=True)
    if not final_data_4.empty : 
        final_quarter = pd.concat([final_quarter, final_data_4], ignore_index=True)
    
    # 매출 최저, 최고
    max_sell = final_quarter.loc[0,'분기당매출금액']
    min_sell = final_quarter.loc[0,'분기당매출금액']
    if len(final_quarter)>1 : 
        for i in range(1,len(final_quarter)) : 
            if max_sell < final_quarter.loc[i,'분기당매출금액'] :
                max_sell = final_quarter.loc[i,'분기당매출금액']
            if min_sell>final_quarter.loc[i,'분기당매출금액'] :
                min_sell = final_quarter.loc[i,'분기당매출금액']

    #업종명 리턴
    industry_list = { '0': '한식음식점', '1': '양식음식점', '2': '일식음식점', '3': '중식음식점', '4': '분식전문점',
                              '5': '제과점', '6': '카페', '7': '치킨', '8': '호프-주점', '9': '패스트푸드'}
    selected_industry_name = industry_list.get(selected_industry, '알 수 없는 업종')
    
    #행정동명 리턴
    selected_neighborhood = DistrictCode.objects.get(행정동코드=neighborhood_code).행정동명
    
    #요일 매출 최댓값
    day_columns = final_quarter.columns[28:35]
    max_day_name = find_max(final_quarter, day_columns)
    day_list = {'월요일매출금액' : '월요일', '화요일매출금액':'화요일', '수요일매출금액':'수요일',
                '목요일매출금액':'목요일','금요일매출금액':'금요일','토요일매출금액':'토요일','일요일매출금액':'일요일'}
    max_day = day_list.get(max_day_name)
    
    #시간대 매출 최댓값
    time_columns = final_quarter.columns[35:41]
    max_time_name = find_max(final_quarter, time_columns)
    time_list = {'시간대0006매출금액':'00시~06시','시간대0611매출금액':'06시~11시','시간대1114매출금액':'11시~14시',
                 '시간대1417매출금액':'14시~17시','시간대1721매출금액':'17시~21시','시간대2124매출금액':'21시~24시'}
    max_time = time_list.get(max_time_name)
    
    #연령대 매출 최댓값
    age_columns = final_quarter.columns[43:49]
    max_age_name = find_max(final_quarter, age_columns)
    age_list = {'연령대10매출금액':'10대','연령대20매출금액':'20대','연령대30매출금액':'30대',
                '연령대40매출금액':'40대','연령대50매출금액':'50대','연령대60이상매출금액':'60대이상'}
    max_age = age_list.get(max_age_name)
    
    #유동인구 최댓값
    flo_popul_columns = final_quarter.columns[83:89]
    max_flo_popul_name = find_max(final_quarter, flo_popul_columns)
    flo_popul_list = {'시간대0006유동인구수':'00시~06시', '시간대0611유동인구수':'06시~11시', '시간대1114유동인구수':'11시~14시', 
                      '시간대1417유동인구수':'14시~17시','시간대1721유동인구수':'17시~21시', '시간대2124유동인구수':'21시~24시'}
    max_flo_popul = flo_popul_list.get(max_flo_popul_name)

    #final 평균내서 리턴
    final = final_quarter.mean(axis=0).to_frame().T
    
    #매출단가
    total_price = final.loc[0,'분기당매출금액']/final.loc[0,'분기당매출건수']
    week_price = final.loc[0,'주중매출금액']/final.loc[0,'주중매출건수']
    weekend_price = final.loc[0,'주말매출금액']/final.loc[0,'주말매출건수']
    
    #행정동 평균 매출
    district_price = neighborhood_price(neighborhood_code,selected_industry)
    
    #지도 띄우기
    business_locations = BusinessLocation.objects.filter(상권코드__in=include_code)
    # folium 지도 띄우기
    m = folium.Map(location=[business_locations[0].y, business_locations[0].x], zoom_start=14)
    # 지도에 좌표 넣고 마커 표시하기
    for business_location in business_locations:
        folium.Marker(
            location=[business_location.y, business_location.x],
            popup=business_location.상권코드명,
        ).add_to(m)
  
    context = {
        'final' : final.to_dict(orient='records'),
        'final_quarter' : final_quarter.to_dict(orient='records'),
        'selected_industry_name' : selected_industry_name,
        'selected_industry': selected_industry,
        'selected_district' :  selected_district,
        'selected_neighborhood' : selected_neighborhood,
        'neighborhood_code': neighborhood_code,
        'group_id': group_id,
        'max_day' : max_day,
        'max_time' : max_time,
        'max_age' : max_age,
        'max_sell' : max_sell,
        'min_sell' : min_sell,
        'max_flo_popul' : max_flo_popul,
        'business_name' : business_name,
        'total_price' : total_price,
        'week_price' : week_price,
        'weekend_price' : weekend_price,  
        'district_price' : district_price,  
        'map': m._repr_html_() if m else None,    
    }
    
    return render(request, 'output/sales.html', context)

def group_detail_floating(request, selected_district, selected_industry, neighborhood_code, group_id):
    
    #상권명 받아오기
    include_codes = cluster_group(selected_industry, neighborhood_code)
    include_code = include_codes['group'][group_id]['상권코드']
    business_names = BusinessCode.objects.filter(구상권코드__in=include_code)
    business_name = []
    for item in business_names :
        business_name.append(item.상권코드명)
        
    #대표 데이터 가져오는 함수 호출. 1분기~4분기
    final_data_1 = final_data(selected_industry, neighborhood_code, '1', group_id)
    final_data_2 = final_data(selected_industry, neighborhood_code, '2', group_id)
    final_data_3 = final_data(selected_industry, neighborhood_code, '3', group_id)
    final_data_4 = final_data(selected_industry, neighborhood_code, '4', group_id)   
    
    #1분기~4분기 합친 것 = final
    final_quarter = pd.DataFrame({})
    if not final_data_1.empty : 
        final_quarter = pd.concat([final_quarter, final_data_1], ignore_index=True)
    if not final_data_2.empty : 
        final_quarter = pd.concat([final_quarter, final_data_2], ignore_index=True)
    if not final_data_3.empty : 
        final_quarter = pd.concat([final_quarter, final_data_3], ignore_index=True)
    if not final_data_4.empty : 
        final_quarter = pd.concat([final_quarter, final_data_4], ignore_index=True)
    
    # 매출 최저, 최고
    max_floating = final_quarter.loc[0,'총유동인구수']
    min_floating = final_quarter.loc[0,'총유동인구수']
    if len(final_quarter)>1 : 
        for i in range(1,len(final_quarter)) : 
            if max_floating < final_quarter.loc[i,'총유동인구수'] :
                max_floating = final_quarter.loc[i,'총유동인구수']
            if min_floating>final_quarter.loc[i,'총유동인구수'] :
                min_floating = final_quarter.loc[i,'총유동인구수']

    #업종명 리턴
    industry_list = { '0': '한식음식점', '1': '양식음식점', '2': '일식음식점', '3': '중식음식점', '4': '분식전문점',
                              '5': '제과점', '6': '카페', '7': '치킨', '8': '호프-주점', '9': '패스트푸드'}
    selected_industry_name = industry_list.get(selected_industry, '알 수 없는 업종')
    
    #행정동명 리턴
    selected_neighborhood = DistrictCode.objects.get(행정동코드=neighborhood_code).행정동명
    
    #유동인구 최댓값
    floating_time_columns = final_quarter.columns[83:89]
    max_floating_time_name = find_max(final_quarter, floating_time_columns)
    floating_time_list = {'시간대0006유동인구수':'00시~06시', '시간대0611유동인구수':'06시~11시', '시간대1114유동인구수':'11시~14시', 
                      '시간대1417유동인구수':'14시~17시','시간대1721유동인구수':'17시~21시', '시간대2124유동인구수':'21시~24시'}
    max_floating_time = floating_time_list.get(max_floating_time_name)

    #직장인구
    district_job = neighborhood_job(neighborhood_code, selected_industry)
    
    # 직장인구 최저, 최고
    max_job = final_quarter.loc[0,'총직장인구수']
    min_job = final_quarter.loc[0,'총직장인구수']
    if len(final_quarter)>1 :
        for i in range(1,len(final_quarter)) :
            if max_job < final_quarter.loc[i,'총직장인구수'] :
                max_job = final_quarter.loc[i,'총직장인구수']
            if min_job>final_quarter.loc[i,'총직장인구수'] :
                min_job = final_quarter.loc[i,'총직장인구수']
    
    district_floating = neighborhood_floating(neighborhood_code, selected_industry)
                    
    #final 평균내서 리턴
    final = final_quarter.mean(axis=0).to_frame().T
    
    #지도 띄우기
    business_locations = BusinessLocation.objects.filter(상권코드__in=include_code)
    # folium 지도 띄우기
    m = folium.Map(location=[business_locations[0].y, business_locations[0].x], zoom_start=14)
    # 지도에 좌표 넣고 마커 표시하기
    for business_location in business_locations:
        folium.Marker(
            location=[business_location.y, business_location.x],
            popup=business_location.상권코드명,
        ).add_to(m) 
     
    context = {
        'final' : final.to_dict(orient='records'),
        'final_quarter' : final_quarter.to_dict(orient='records'),
        'selected_industry_name' : selected_industry_name,
        'selected_industry': selected_industry,
        'selected_district' :  selected_district,
        'selected_neighborhood' : selected_neighborhood,
        'neighborhood_code': neighborhood_code,
        'group_id': group_id,
        'max_floating' : max_floating,
        'min_floating' : min_floating,
        'max_floating_time' : max_floating_time,
        'max_job' : max_job,
        'min_job' : min_job,
        'business_name' : business_name,  
        'district_floating' : district_floating,  
        'district_job' : district_job, 
        'map': m._repr_html_() if m else None, 
    }
    
    return render(request, 'output/floating.html', context)

def group_detail_facility(request, selected_district, selected_industry, neighborhood_code, group_id):
    
    #상권명 받아오기
    include_codes = cluster_group(selected_industry, neighborhood_code)
    include_code = include_codes['group'][group_id]['상권코드']
    business_names = BusinessCode.objects.filter(구상권코드__in=include_code)
    business_name = []
    for item in business_names :
        business_name.append(item.상권코드명)
        
    #대표 데이터 가져오는 함수 호출. 1분기~4분기
    final_data_1 = final_data(selected_industry, neighborhood_code, '1', group_id)
    final_data_2 = final_data(selected_industry, neighborhood_code, '2', group_id)
    final_data_3 = final_data(selected_industry, neighborhood_code, '3', group_id)
    final_data_4 = final_data(selected_industry, neighborhood_code, '4', group_id)   
    
    #1분기~4분기 합친 것 = final
    final_quarter = pd.DataFrame({})
    if not final_data_1.empty : 
        final_quarter = pd.concat([final_quarter, final_data_1], ignore_index=True)
    if not final_data_2.empty : 
        final_quarter = pd.concat([final_quarter, final_data_2], ignore_index=True)
    if not final_data_3.empty : 
        final_quarter = pd.concat([final_quarter, final_data_3], ignore_index=True)
    if not final_data_4.empty : 
        final_quarter = pd.concat([final_quarter, final_data_4], ignore_index=True)

    #업종명 리턴
    industry_list = { '0': '한식음식점', '1': '양식음식점', '2': '일식음식점', '3': '중식음식점', '4': '분식전문점',
                              '5': '제과점', '6': '카페', '7': '치킨', '8': '호프-주점', '9': '패스트푸드'}
    selected_industry_name = industry_list.get(selected_industry, '알 수 없는 업종')
    
    #행정동명 리턴
    selected_neighborhood = DistrictCode.objects.get(행정동코드=neighborhood_code).행정동명

    #final 평균내서 리턴
    final = final_quarter.mean(axis=0).to_frame().T
    
    district_facility = neighborhood_facility(neighborhood_code, selected_industry)
    
    #교통시설 최댓값
    facility_columns = final_quarter.columns[74:83]
    max_facility_name = find_max(final_quarter, facility_columns)
    floating_time_list = {'관공서수':'관공서', '은행수':'은행', '대학교수':'대학교', '백화점수':'백화점', '슈퍼마켓수':'슈퍼마켓', '의료시설수':'의료시설',
                          '교육시설수':'교육시설','여가시설수':'여가시설', '교통시설수':'교통시설'}
    max_facility = floating_time_list.get(max_facility_name)
    
    #지도 띄우기
    business_locations = BusinessLocation.objects.filter(상권코드__in=include_code)
    # folium 지도 띄우기
    m = folium.Map(location=[business_locations[0].y, business_locations[0].x], zoom_start=14)
    # 지도에 좌표 넣고 마커 표시하기
    for business_location in business_locations:
        folium.Marker(
            location=[business_location.y, business_location.x],
            popup=business_location.상권코드명,
        ).add_to(m) 
    
    context = {
        'final' : final.to_dict(orient='records'),
        'final_quarter' : final_quarter.to_dict(orient='records'),
        'selected_industry_name' : selected_industry_name,
        'selected_industry': selected_industry,
        'selected_district' :  selected_district,
        'selected_neighborhood' : selected_neighborhood,
        'neighborhood_code': neighborhood_code,
        'group_id': group_id,
        'business_name' : business_name,  
        'district_facility' : district_facility,   
        'max_facility' : max_facility,
        'map': m._repr_html_() if m else None,
    }
    
    return render(request, 'output/facility.html', context)

def group_detail_living(request, selected_district, selected_industry, neighborhood_code, group_id):
    
    #상권명 받아오기
    include_codes = cluster_group(selected_industry, neighborhood_code)
    include_code = include_codes['group'][group_id]['상권코드']
    business_names = BusinessCode.objects.filter(구상권코드__in=include_code)
    business_name = []
    for item in business_names :
        business_name.append(item.상권코드명)
        
    #대표 데이터 가져오는 함수 호출. 1분기~4분기
    final_data_1 = final_data(selected_industry, neighborhood_code, '1', group_id)
    final_data_2 = final_data(selected_industry, neighborhood_code, '2', group_id)
    final_data_3 = final_data(selected_industry, neighborhood_code, '3', group_id)
    final_data_4 = final_data(selected_industry, neighborhood_code, '4', group_id)   
    
    #1분기~4분기 합친 것 = final
    final_quarter = pd.DataFrame({})
    if not final_data_1.empty : 
        final_quarter = pd.concat([final_quarter, final_data_1], ignore_index=True)
    if not final_data_2.empty : 
        final_quarter = pd.concat([final_quarter, final_data_2], ignore_index=True)
    if not final_data_3.empty : 
        final_quarter = pd.concat([final_quarter, final_data_3], ignore_index=True)
    if not final_data_4.empty : 
        final_quarter = pd.concat([final_quarter, final_data_4], ignore_index=True)
    
    # 생활인구 최저, 최고
    max_living = final_quarter.loc[0,'총생활인구수']  #51열
    min_living = final_quarter.loc[0,'총생활인구수']
    if len(final_quarter)>1 :
        for i in range(1,len(final_quarter)) :
            if max_living < final_quarter.loc[i,'총생활인구수'] :
                max_living = final_quarter.loc[i,'총생활인구수']
            if min_living>final_quarter.loc[i,'총생활인구수'] :
                min_living = final_quarter.loc[i,'총생활인구수']

    #업종명 리턴
    industry_list = { '0': '한식음식점', '1': '양식음식점', '2': '일식음식점', '3': '중식음식점', '4': '분식전문점',
                              '5': '제과점', '6': '카페', '7': '치킨', '8': '호프-주점', '9': '패스트푸드'}
    selected_industry_name = industry_list.get(selected_industry, '알 수 없는 업종')
    
    #행정동명 리턴
    selected_neighborhood = DistrictCode.objects.get(행정동코드=neighborhood_code).행정동명
    
    #연령대 생활인구 최댓값
    living_age_columns = final_quarter.columns[53:59]
    max_living_age_name = find_max(final_quarter, living_age_columns)
    living_age_list = {'연령대10생활인구수':'10대','연령대20생활인구수':'20대','연령대30생활인구수':'30대',
                '연령대40생활인구수':'40대','연령대50생활인구수':'50대','연령대60이상생활인구수':'60대이상'}
    max_living_age = living_age_list.get(max_living_age_name)
    
    #시간대 생활인구 최댓값
    living_time_columns = final_quarter.columns[59:65]
    max_living_time_name = find_max(final_quarter, living_time_columns)
    living_time_list = {'시간대0006생활인구수':'00시~06시','시간대0611생활인구수':'06시~11시','시간대1114생활인구수':'11시~14시',
                 '시간대1417생활인구수':'14시~17시','시간대1721생활인구수':'17시~21시','시간대2124생활인구수':'21시~24시'}
    max_living_time = living_time_list.get(max_living_time_name)
    
    #요일 생활인구 최댓값
    living_day_columns = final_quarter.columns[65:72]
    max_living_day_name = find_max(final_quarter, living_day_columns)
    living_day_list = {'월요일생활인구수' : '월요일', '화요일생활인구수':'화요일', '수요일생활인구수':'수요일',
                '목요일생활인구수':'목요일','금요일생활인구수':'금요일','토요일생활인구수':'토요일','일요일생활인구수':'일요일'}
    max_living_day = living_day_list.get(max_living_day_name)
    
    #행정동 평균 생활인구수
    district_living = neighborhood_living(neighborhood_code,selected_industry)

    #final 평균내서 리턴
    final = final_quarter.mean(axis=0).to_frame().T
    
    #지도 띄우기
    business_locations = BusinessLocation.objects.filter(상권코드__in=include_code)
    # folium 지도 띄우기
    m = folium.Map(location=[business_locations[0].y, business_locations[0].x], zoom_start=14)
    # 지도에 좌표 넣고 마커 표시하기
    for business_location in business_locations:
        folium.Marker(
            location=[business_location.y, business_location.x],
            popup=business_location.상권코드명,
        ).add_to(m)
    
    context = {
        'final' : final.to_dict(orient='records'),
        'final_quarter' : final_quarter.to_dict(orient='records'),
        'selected_industry_name' : selected_industry_name,
        'selected_industry': selected_industry,
        'selected_district' :  selected_district,
        'selected_neighborhood' : selected_neighborhood,
        'neighborhood_code': neighborhood_code,
        'group_id': group_id,
        'max_living_day' : max_living_day,
        'max_living_time' : max_living_time,
        'max_living_age' : max_living_age,
        'max_living' : max_living,
        'min_living' : min_living,
        'business_name' : business_name,
        'district_living' : district_living,
        'map': m._repr_html_() if m else None,   
    }
    
    return render(request, 'output/living.html', context)

def get_industry_name(code):
    industry_mapping = {
        '0': '한식',
        '1': '양식',
        '2': '일식',
        '3': '중식',
        '4': '분식',
        '5': '제과점',
        '6': '카페',
        '7': '치킨',
        '8': '호프',
        '9': '패스트푸드',
    }
    return industry_mapping.get(code, '알 수 없는 업종')

def find_max(final_quarter, columns) : 
    max_value = final_quarter.loc[0, columns[0]]
    max_value_name = columns[0]
    
    for column in columns[1:] :
        if final_quarter.loc[0, column] > max_value :
            max_value = final_quarter.loc[0, column]
            max_value_name = column
    
    return max_value_name

#행정동 평균 매출
def neighborhood_price(neighborhood_code, selected_industry):
    filtered_list = Final1.objects.filter(행정동코드=neighborhood_code)
    total = filtered_list.aggregate(total=models.Sum('분기당매출금액'))['total']
    location_price = total/len(filtered_list)
    
    category_list = {'0':HANSIC_3, '1':YANGSIC_3, '2':ILSIC_3, '3':ZUNGSIC_2, '4':BUNSIC_2,
                     '5':BBANG_3, '6':CAFE_4, '7':CHICKEN_4, '8':HOF_4, '9':FASTFOOD_2}
    name = category_list.get(selected_industry)
    data_from_db = name.objects.all()
    category_1 = pd.DataFrame(list(data_from_db.values()))
    category_1.fillna(0,inplace=True)
    category_price = category_1['분기당매출금액'].mean()

    return (location_price+category_price)/2

#행정동 평균 유동인구
def neighborhood_floating(neighborhood_code, selected_industry):
    filtered_list = Final1.objects.filter(행정동코드=neighborhood_code)
    total = filtered_list.aggregate(total=models.Sum('총유동인구수'))['total']
    location_floating = total/len(filtered_list)
    
    category_list = {'0':HANSIC_3, '1':YANGSIC_3, '2':ILSIC_3, '3':ZUNGSIC_2, '4':BUNSIC_2,
                     '5':BBANG_3, '6':CAFE_4, '7':CHICKEN_4, '8':HOF_4, '9':FASTFOOD_2}
    name = category_list.get(selected_industry)
    data_from_db = name.objects.all()
    category_1 = pd.DataFrame(list(data_from_db.values()))
    category_1.fillna(0,inplace=True)
    category_floating = category_1['총유동인구수'].mean()

    return (location_floating+category_floating)/2

#행정동 평균 집객시설수
def neighborhood_facility(neighborhood_code, selected_industry):
    filtered_list = Final1.objects.filter(행정동코드=neighborhood_code)
    total = filtered_list.aggregate(total=models.Sum('집객시설수'))['total']
    location_facility = total/len(filtered_list)
    
    category_list = {'0':HANSIC_3, '1':YANGSIC_3, '2':ILSIC_3, '3':ZUNGSIC_2, '4':BUNSIC_2,
                     '5':BBANG_3, '6':CAFE_4, '7':CHICKEN_4, '8':HOF_4, '9':FASTFOOD_2}
    name = category_list.get(selected_industry)
    data_from_db = name.objects.all()
    category_1 = pd.DataFrame(list(data_from_db.values()))
    category_1.fillna(0,inplace=True)
    category_facility = category_1['집객시설수'].mean()

    return (location_facility+category_facility)/2

#행정동 평균 생활인구수
def neighborhood_living(neighborhood_code, selected_industry):
    filtered_list = Final1.objects.filter(행정동코드=neighborhood_code)
    total = filtered_list.aggregate(total=models.Sum('총생활인구수'))['total']
    location_living = total/len(filtered_list)
    
    category_list = {'0':HANSIC_3, '1':YANGSIC_3, '2':ILSIC_3, '3':ZUNGSIC_2, '4':BUNSIC_2,
                     '5':BBANG_3, '6':CAFE_4, '7':CHICKEN_4, '8':HOF_4, '9':FASTFOOD_2}
    name = category_list.get(selected_industry)
    data_from_db = name.objects.all()
    category_1 = pd.DataFrame(list(data_from_db.values()))
    category_1.fillna(0,inplace=True)
    category_living = category_1['총생활인구수'].mean()

    return (location_living+category_living)/2

#행정동 평균 직장인구수
def neighborhood_job(neighborhood_code, selected_industry):
    filtered_list = Final1.objects.filter(행정동코드=neighborhood_code)
    total = filtered_list.aggregate(total=models.Sum('총직장인구수'))['total']
    location_job = total/len(filtered_list)
    
    category_list = {'0':HANSIC_3, '1':YANGSIC_3, '2':ILSIC_3, '3':ZUNGSIC_2, '4':BUNSIC_2,
                     '5':BBANG_3, '6':CAFE_4, '7':CHICKEN_4, '8':HOF_4, '9':FASTFOOD_2}
    name = category_list.get(selected_industry)
    data_from_db = name.objects.all()
    category_1 = pd.DataFrame(list(data_from_db.values()))
    category_1.fillna(0,inplace=True)
    category_job = category_1['총직장인구수'].mean()

    return (location_job+category_job)/2

