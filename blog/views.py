from django.shortcuts import get_object_or_404
from .models import WildLife
from rest_framework.response import Response
from rest_framework.decorators import *
from .serializers import WildLifeSerializer
from rest_framework import viewsets
from rest_framework.throttling import UserRateThrottle


class WildLifeView(viewsets.ModelViewSet):
    queryset = WildLife.objects.all()
    serializer_class = WildLifeSerializer


@api_view(['GET'])
def url_list(request):
    serializer = {
        'for all': 'http://127.0.0.1:8000/all/',
        'find by name': '/animal_name',
        'find by id': '/id',
        'to post': 'http://127.0.0.1:8000/wild/post/',
        'to update': 'wild/update/title'
    }
    return Response(serializer)


@api_view(['GET'])
@throttle_classes([UserRateThrottle])
def home(request):
    wildlife = WildLife.objects.all()  # SELECT * FROM  article
    serializer = WildLifeSerializer(wildlife, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post(request):
    serializer = WildLifeSerializer(data=request.data)
    serializer.is_valid()
    print(serializer.errors)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT', 'GET', 'DELETE'])
def wildupdate(request, title):
    wild = WildLife.objects.get(title=title)
    if request.method == 'GET':
        serializer = WildLifeSerializer(wild, many=False)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        serializer = WildLifeSerializer(wild, many=False)
        del serializer
        return  Response(serializer.data)
    else:
        serializer = WildLifeSerializer(wild, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)



@api_view(['GET'])
@throttle_classes([UserRateThrottle])
def detail(request, title='', n=0):
    if n != 0:
        wild = get_object_or_404(WildLife, pk=n)
    else:
        wild = get_object_or_404(WildLife, title=title)
    serializer = WildLifeSerializer(wild, many=False)
    return Response(serializer.data)

# @api_view(['GET'])
# def users(request):
#     serializer = UserSerializer(User.objects.all())
#     return Response(serializer.data)

# # def register(request):
# #     if request.method == 'POST':
# #         username = request.POST['username']
# #         email = request.POST['email']
# #         password = request.POST['password']
# #         password2 = request.POST['password2']
# #
# #         if password == password2:
# #             if User.objects.filter(username=username).exists():
# #                 messages.info(request, 'username taken')
# #                 return redirect('register')
# #             elif User.objects.filter(email=email).exists():
# #                 messages.info(request, 'email taken')
# #                 return redirect('register')
# #             user = User.objects.create_user(username=username, email=email, password=password)
# #             user.save()
# #             return redirect('login/')
# #         else:
# #             messages.info(request, 'wrong password')
# #             return redirect('register/')
# #     return render(request, 'blog/register.html')
#
#
# # def login(request):
# #
# #     if request.method == 'POST':
# #         username = request.POST['username']
# #         password = request.POST['password']
# #         user = auth.authenticate(username=username, password=password)
# #         if user is not None:
# #             auth.login(request,user)
# #             return redirect('home/')
# #         else:
# #             messages.info(request, 'invalid credential')
# #             return redirect('login/')
# #     return render(request, 'blog/login.html')
#
#
# # def logout(request):
# #     auth.logout(request)
# #     return redirect('home/')
#
#
# # def currency(request):
# #     if request.method == 'POST':
# #         symbols = request.POST['to']
# #         amount1 = request.POST['amount']
# #         try:
# #             amount = int(amount1)
# #         except:
# #             messages.info(request, 'amount must be an integer.')
# #             return redirect('currency/')
# #
# #         if symbols != '':
# #             res = requests.get('https://api.currencyfreaks.com/latest?apikey=3795b985fd7e40f1a98b51971e0bc0c6&',
# #                                params={'symbols':symbols})
# #             if res.status_code != 200:
# #                 messages.info(request, 'something goes wrong')
# #                 return redirect('currency/')
# #             data = res.json()
# #             rate = float(data['rates'][symbols])
# #             # revers = 1/rate
# #             curr = f'{amount} USD is equal to {rate*amount} {symbols}'
# #             # rev = f'{amount} {symbols} is equal to {revers*amount} USD'
# #             # currencies = [curr,rev]
# #             return render(request, 'blog/currency.html', {'currency': curr, 'symbols': symbols})
# #         else:
# #             messages.info(request, 'invalid symbol.')
# #             return redirect('currency/')
# #     return render(request, 'blog/currency.html')
# #
# def WildLifeView(request):
#     return None
