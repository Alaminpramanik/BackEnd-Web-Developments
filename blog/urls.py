from django.urls import path

from.views import (
    home,
    vegitable,
    fish,
    meet,
    rice,
    machine,
    madichine,
    order,
    chart,
    register,
    login,
    about,
    agency,
    blog,
    training,
    
    )
    
urlpatterns =[
    path('', home, name='home'),
    path('vegitable/', vegitable, name='vegitable'),
    path('fish/', fish, name='fish'),
    path('meet/', meet, name='meet'),
    path('rice/', rice, name='rice'),
    path('machine/', machine, name='machine'),
    path('madichine/', madichine, name='madichine'),
    path('order/', order, name='order'),
    path('chart/', chart, name='chart'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('about/', about, name='about'),
    path('agency/', agency, name='agency'),
    path('blog/', blog, name='blog'),
    path('training/', training, name='training'),
    path('home/', home, name='home'),
    ]
