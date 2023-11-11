from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import DistrictCode

def input_neighborhood(request):
    if request.method == 'POST':
        neighborhood_name = request.POST.get('neighborhood')
        try:
            neighborhood = DistrictCode.objects.get(행정동명=neighborhood_name)
            neighborhood_code = neighborhood.행정동코드
            return render(request, 'output/group.html', {'neighborhood_code': neighborhood_code})
        except DistrictCode.DoesNotExist:
            # 예외 처리
            return render(request, 'output/group.html', {'error': '해당 행정동명을 찾을 수 없습니다.'})
    else:
        # GET 요청 처리
        return render(request, 'input/index.html')

def index(request):
    return render(request, 'input/index.html')
