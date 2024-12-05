from django.shortcuts import render

# Create your views here.
def show_view(request):
    return render(request, 'main_page.html')

def show_one(request):

    context = {
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    }
    return render(request, 'page_one.html', context)

def show_two(request):
    return render(request, 'page_two.html')
