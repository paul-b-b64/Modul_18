from django.shortcuts import render

# Create your views here.
def show_view(request):
    return render(request, 'main_page.html')

def show_one(request):
    list_of_things = [
        "Первое",
        "Второе",
        "Салат_",
        "Десерт"
    ]

    context = {
        'p1': list_of_things[0],
        'p2': list_of_things[1],
        'p3': list_of_things[2],
        'p4': list_of_things[3]
    }
    return render(request, 'page_one.html', context)

def show_two(request):
    return render(request, 'page_two.html')
