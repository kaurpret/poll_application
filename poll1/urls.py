from django.urls import path
from . import views
urlpatterns=[
    path('add',views.add,name='add'),
    path('detail',views.detail,name="detail"),
    path('vote/<int:poll1_id>',views.vote,name="vote"),
    path('result/<int:poll1_id>',views.result,name="result"),
    path('delete/<int:id>', views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('show/<int:id>',views.show,name='show'),
]