from django.shortcuts import render
from board.models import Contents
from django.utils import timezone


# テキストは必須項目であるため、空の際に投げる例外クラス
class EmptyTextException(Exception):
    pass


def index(request):
    # テキストは必須なので、なければ何も更新せずテンプレートを返す
    try:
        # 最初のアクセスではキーが存在していないため、len(request.POST)で判断する
        if len(request.POST) == 0 or len(request.POST['main_text']) == 0:
            raise EmptyTextException
        text = request.POST['main_text']
    except EmptyTextException:
        d = {'all_objects': Contents.objects.all()}
        return render(request, 'board.html', d)
    date = timezone.now()
    if len(request.FILES) == 0:
        c = Contents(main_text=text, pub_date=date)
        c.save()
    else:
        posted_image = request.FILES['image_file']
        c = Contents(main_text=text, pub_date=date, image=posted_image)
        c.save()
    d = {'all_objects': Contents.objects.all()}
    return render(request, 'board.html', d)
