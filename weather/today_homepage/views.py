from django.shortcuts import render
from today_homepage.models import Test
# Create your views here.


def test_view(request):
    db_vi = Test.objects.all()
    context = {'db': db_vi}
    return render(request, "today_homepage/test.html", context)