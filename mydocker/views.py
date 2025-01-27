from django.http import HttpResponse
from django.shortcuts import render, redirect
import os
from django.conf import settings
from users.models import Media_file #settings.py에 있는 경로설정 때문에 쉽게 이용함
from users.models import MedicalStatistics_2
import pandas as pd
from django.db import IntegrityError, DatabaseError
from datetime import datetime
from django.db.models.functions import TruncDay
from django.db.models import Sum
import json
from django.db.models.functions import ExtractMonth, Cast
from django.db.models import DateField

# 서버 사이드 렌더링
def index(request):
    return render(request, 'index.html')

def save_excel(df):
   
    for i in range(len(df)):
        try:
                
            medical_statistics = MedicalStatistics_2()
            medical_statistics.treatment_date = df['진료일'].iloc[i]
            medical_statistics.chart_number = df['차트번호'].iloc[i]
            medical_statistics.name = df['이름'].iloc[i]
            medical_statistics.insurance_classification = df['보험구분'].iloc[i]
            medical_statistics.income_aggregation = df['수입집계'].iloc[i]
            medical_statistics.treating_doctor = df['진료의사'].iloc[i]
            medical_statistics.assist = df['어시스트'].iloc[i]
            medical_statistics.same_day_reception = df['당일접수'].iloc[i]
            medical_statistics.recipient = df['수납자'].iloc[i]
            medical_statistics.total_medical_expenses = df['총진료비'].iloc[i].astype(float)
            medical_statistics.bill_amount = df['청구액'].iloc[i].astype(float)
            medical_statistics.out_of_pocket_expenses = df['본인부담금'].iloc[i].astype(float)
            medical_statistics.non_salary = df['비급여'].iloc[i].astype(float)
            medical_statistics.vat = df['부가가치세'].iloc[i].astype(float)
            medical_statistics.discount_amount = df['할인액'].iloc[i].astype(float)
            medical_statistics.total_amount_received = df['총수납액'].iloc[i].astype(float)
            medical_statistics.card_storage = df['카드수납'].iloc[i].astype(float)
            medical_statistics.cash_receipt = df['현금수납'].iloc[i].astype(float)
            medical_statistics.other_online = df['기타(온라인)'].iloc[i].astype(float)
            medical_statistics.prefectural_issued_amount = df['현영발행액'].iloc[i].astype(float)
            medical_statistics.disapproval_for_healthy_lifestyle = df['건강생활유지비승인'].iloc[i].astype(float)
            medical_statistics.unexpected_player = df['미수(+)선수(-)'].iloc[i].astype(float)
            medical_statistics.total_number_of_outstanding_players = df['총미수/선수'].iloc[i].astype(float)
            medical_statistics.classification_of_medical_expenses = df['진료비구분'].iloc[i]
            medical_statistics.medical_history = df['진료내역'].iloc[i]
            medical_statistics.memo = df['메모'].iloc[i]
            medical_statistics.first_visit = df['최초내원'].iloc[i]
            medical_statistics.visit_path = df['내원경로'].iloc[i]
            medical_statistics.customer_propensity = df['고객성향'].iloc[i]
            medical_statistics.customer_classification = df['고객구분'].iloc[i]
            medical_statistics.customer_classification_2 = df['고객구분2'].iloc[i]
            medical_statistics.recall_classification = df['리콜구분'].iloc[i]

                    
            medical_statistics.save()

        except IntegrityError as e:
            print(e)
        except DatabaseError as e:
            print(e)
    
    

# request.method == 'POST'
# request.method == 'GET'
# request.method == 'PUT'
# request.method == 'DELETE'    
def upload(request):
    if request.method == 'POST':
        new_media = Media_file(
            file = request.FILES['file'],
            description = request.POST.get('Description')
        ) 
        new_media.save()
        df = pd.read_excel(new_media.file, sheet_name=1) 
        duplicates = df[df.duplicated(subset=['진료일', '차트번호'], keep=False)] # 두 번째 시트를 읽음
        print(duplicates)

        if df is not None:
            save_excel(df)

        #return HttpResponse('성공적으로 업로드 되었습니다.')
        return redirect('result')
    
           
    return render(request, 'upload.html')



def list(request):
    
    # 현재 연도와 월 가져오기
    current_year_month = datetime.now().strftime("%Y-%m")
    #medical_statistics = MedicalStatistics_2.objects.all()
       # 현재 연도와 월의 데이터를 필터링
    filtered_data = MedicalStatistics_2.objects.filter(
        treatment_date__startswith=current_year_month
    )
    total_amount= 0 
    for ms in filtered_data:
        total_amount += ms.total_amount_received
    print(total_amount)
    return render(request, 'list.html', {'medical_statistics': filtered_data, 'total_amount': total_amount})

def render_result_page(request):
    # 현재 연도와 월 가져오기
    current_year_month = datetime.now().strftime("%Y-%m")

    # 데이터 필터링 및 날짜별 합계 계산
    filtered_data = (
        MedicalStatistics_2.objects.annotate(
            treatment_date_date=Cast('treatment_date', DateField())
        )
        .annotate(month=ExtractMonth('treatment_date_date'))
        .filter(month=10)
        .values('treatment_date_date')
        # MedicalStatistics_2.objects.filter(treatment_date__startswith=current_year_month)
        # .values('treatment_date')
        .annotate(total_amount_received_sum=Sum('total_amount_received'))
        .order_by('treatment_date_date')
    )
    
    # 날짜를 문자열로 변환
    dates = [data['treatment_date_date'].strftime('%Y-%m-%d') for data in filtered_data]
    total_amounts = [float(data['total_amount_received_sum']) for data in filtered_data]

    # 두 리스트의 길이가 같은지 확인
    if len(dates) != len(total_amounts):
        print("Error: dates and total_amounts lists have different lengths.")
        return HttpResponse('데이터 처리 중 오류가 발생했습니다.', status=500)

    date_amount_pairs = []
    for i in range(len(dates)):
    # 천 단위마다 콤마 추가 및 소숫점 이하 제거
        formatted_amount = "{:,}".format(int(total_amounts[i]))  
        date_amount_pairs.append((dates[i], formatted_amount))

    context = {
        'dates': json.dumps(dates),
        'total_amounts': json.dumps(total_amounts),
        'date_amount_pairs': date_amount_pairs,  # JSON으로 변환하여 전달
    }

    return render(request, 'display_result.html', context)
