from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page requested")
    friends=[
        'Mohammed',
        'Minhaj',
        'Qureshi'
    ]
    return JsonResponse(friends,safe=False)