from django.shortcuts import render
from .models import PageCount

def count_view(request):
    counter, created = PageCount.objects.get_or_create(id=1)
    counter.count += 1
    counter.save()
    return render(request, 'counter/count.html', {'count': counter.count})
