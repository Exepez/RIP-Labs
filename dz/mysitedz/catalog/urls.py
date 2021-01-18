from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
# path('', views.index, name='index'),
# path('i7-10700k/', views.cpu1, name='cpu1'),
# path('i9-10900k/', views.cpu2, name='cpu2'),
# path('ryzen-7-3800x/', views.cpu3, name='cpu3'),
# path('create/', views.create),

# url(r'^$', views.index, name='index'),
# url(r'^motherboards/$', views.MotherboardListView.as_view(), name='motherboards'),
# url(r'^motherboard/(?P<pk>\d+)$', views.MotherboardDetailView.as_view(), name='motherboard-detail'),
# url(r'^cpus/$', views.CPUListView.as_view(), name='cpus'),
# url(r'^cpu/(?P<pk>\d+)$', views.CPUDetailView.as_view(), name='cpu-detail'),

    path('', views.index, name='index'),
    path('motherboards/', views.MotherboardListView.as_view(), name='motherboards'),
    path('motherboard/<int:pk>', views.MotherboardDetailView.as_view(), name='motherboard-detail'),
    path('cpus/', views.CPUListView.as_view(), name='cpus'),
    path('cpu/<int:pk>',views.CPUDetailView.as_view(), name='cpu-detail'),
    path('manufacturers/', views.ManufacturerListView.as_view(), name='manufacturers'),
    path('manufacturer/<int:pk>',views.ManufacturerDetailView.as_view(), name='manufacturer-detail'),
    # path('create/', views.create),
    path('cpu/editcpu/<int:id>/', views.editcpu),
    path('motherboard/editmotherboard/<int:id>/', views.editmotherboard),
]
