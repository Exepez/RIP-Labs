from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Motherboard, CPU, Manufacturer
import django.template.context_processors
 
# получение данных из бд
def index(request):
    return render(request, "index.html")
 
# сохранение данных в бд
# def create(request):
#     if request.method == "POST":
#         tom = Person()
#         tom.name = request.POST.get("name")
#         tom.age = request.POST.get("age")
#         tom.save()
#     return HttpResponseRedirect("/")

# изменение данных в бд
def editcpu(request, id):
    try:
        cpu = CPU.objects.get(id=id)
 
        if request.method == "POST":
            s = request.POST.get("rate")
            a = s[1:2]
            cpu.rate = cpu.rate+int(a)
            cpu.countrate += 1
            cpu.avrrate = round(cpu.rate/cpu.countrate, 2)
            cpu.save()
            return HttpResponseRedirect("/catalog/cpus")
        else:
            return render(request, "editcpu.html", {"cpu": cpu})
    except CPU.DoesNotExist:
        return HttpResponseNotFound("<h2>CPU not found</h2>")

def editmotherboard(request, id):
    try:
        motherboard = Motherboard.objects.get(id=id)
 
        if request.method == "POST":
            s = request.POST.get("rate")
            a = s[1:2]
            motherboard.rate = motherboard.rate+int(a)
            motherboard.countrate += 1
            motherboard.avrrate = round(motherboard.rate/motherboard.countrate, 2)
            motherboard.save()
            return HttpResponseRedirect("/catalog/motherboards")
        else:
            return render(request, "editmotherboard.html", {"motherboard": motherboard})
    except Motherboard.DoesNotExist:
        return HttpResponseNotFound("<h2>Motherboard not found</h2>")
 
# сохранение данных в бд
# def create(request):
#     if request.method == "POST":
#         tom = CPU()
#         # people = CPU.objects.rate()
#         # # tom.comment = request.POST.get("comment")
#         # a =request.POST.get("rate")
#         # b=a+people
#         tom.rate = request.POST.get("rate")
#         # tom.cpu = request.POST.get("id")
#         tom.save()
#     return HttpResponseRedirect("/")

# изменение данных в бд
# def edit(request, id):
#     try:
#         CPU = CPU.objects.get(id=id)
 
#         if request.method == "POST":
#             CPU.rate = request.POST.get("rate")
#             CPU.save()
#             return HttpResponseRedirect("/")
#         else:
#             return render(request, "edit.html", {"CPU": CPU})
#     except CPU.DoesNotExist:
#         return HttpResponseNotFound("<h2>CPU not found</h2>")


# def cpu1(request):
#     return render(
#     request,
#     'cpu1.html'
#     )

# def cpu2(request):
#     return render(
#     request,
#     'cpu2.html'
#     )

# def cpu3(request):
#     return render(
#     request,
#     'cpu3.html'
#     )

from django.views import generic

class MotherboardListView(generic.ListView):
    model = Motherboard
    # context_object_name = 'my_motherboard_list'   # ваше собственное имя переменной контекста в шаблоне
    # queryset = Motherboard.objects.filter(title__icontains='Z490')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    # template_name = 'motherboards/my_arbitrary_template_name_list.html'  # Определение имени вашего шаблона и его расположения
    # def get_queryset(self):
    #     return Motherboard.objects.filter(title__icontains='Z490')[:5]

class MotherboardDetailView(generic.DetailView):
    model = Motherboard
    paginate_by = 3

class CPUListView(generic.ListView):
    model = CPU
    paginate_by = 2

class CPUDetailView(generic.DetailView):
    model = CPU
    
class ManufacturerListView(generic.ListView):
    model = Manufacturer
    paginate_by = 6

class ManufacturerDetailView(generic.DetailView):
    model = Manufacturer
# def create(request):
#     if request.method == "POST":
#         tom = Motherboard()
#         tom.title = request.POST.get("title")
#         tom.socket = request.POST.get("socket")
#         tom.save()
#     return HttpResponseRedirect("/")

