from django.shortcuts import render, HttpResponse
from django.core.files.base import ContentFile
from django.conf import settings
import openpyxl
from datetime import datetime
from django.views.generic import TemplateView
from .models import *
from pairfinder.models.peer_analysis import PeerGroup
import pandas as pd
from wsgiref.util import FileWrapper
import shutil
from django.contrib.auth.decorators import login_required
from background_task import background
from django.contrib.auth.models import User

@background(schedule=60)
def notify_user(user_id):
    # lookup user by id and send them a message
    user = User.objects.get(pk=user_id)
    user.email_user('Here is a notification', 'You have been notified')

# Create your views here.
class SauronTemplateView(TemplateView):
    """
    Sauron 템플릿 뷰
    """
    template_name = 'sauron.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['sample'] = DonwloadFileModel.objects.filter(title='sample')[0].file
        return context


@background(queue='sauron')
def write_result(request):
    # 유저 정보
    current_user = request.user.id
    user_excel_file = request.FILES["excel_file"]

    user_pair_list = pd.read_excel(user_excel_file, engine='openpyxl', sheet_name='List')
    user_pair_settings = pd.read_excel(user_excel_file, engine='openpyxl', sheet_name='Settings')

    # 설정값
    user_settings = {
        'window': int(user_pair_settings.iloc[2, 2]),
        'analysis': (pd.to_datetime(user_pair_settings.iloc[0, 2]).strftime("%Y-%m-%d"),
                     pd.to_datetime(user_pair_settings.iloc[1, 2]).strftime("%Y-%m-%d")),
        'plot': (pd.to_datetime(user_pair_settings.iloc[0, 5]).strftime("%Y-%m-%d"),
                 pd.to_datetime(user_pair_settings.iloc[1, 5]).strftime("%Y-%m-%d")),
    }

    # 경로 설정
    timestamp = str(datetime.now().timestamp())
    outpath = os.path.join(settings.MEDIA_ROOT, 'temp', timestamp)

    # 피어 분석
    peer_group = PeerGroup(params=user_settings)
    peer_group.set_peer_group(peer_group=user_pair_list)
    peer_group.analyze(filter_ks=True)
    peer_group.summarize(outpath=outpath)

    # TODO: 이후 데이터 클리닝

    # 결과 파일 로드
    file_path = os.path.join(outpath, 'summary.xlsx')
    # wrapper = FileWrapper(open(file_path, 'rb'))
    # response = HttpResponse(
    #     wrapper,
    #     content_type='application/force-download'
    # )
    # response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
    # shutil.rmtree(outpath)

    result = ResultFileModel()
    result.title = 'summary'
    result.file.name = file_path
    result.user_id = current_user
    result.save()

@login_required
def upload_xlsx(request):
    """
    유저가 업로드한 페어 리스트 파일을 처리하여 반환

    :param request:
    :return:
    """
    # 렌더링 할 페이지
    template_name = 'sauron.html'

    if request.method == 'GET':
        return render(request, template_name, {})
    else:
        write_result(request)

    return HttpResponse("Submit Complete")
    # return render(request, template_name, {"excel_data": result})

