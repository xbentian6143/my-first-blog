from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'), 
    path('<int:post_pk>/detail/', views.post_detail, name='post_detail'),
    path('<int:post_pk>/post_delete/', views.post_delete, name='post_delete'),
    path('<int:post_pk>/post_delete_confirm/', views.post_delete_confirm, name='post_delete_confirm'),
    path('<pk>/idea_create/', views.idea_create, name='idea_create'),
    path('sympathy1/<int:post_pk>/<int:sympathys_count>/', views.sympathy1, name='sympathy1'),
    path('sympathy2/<int:post_pk>/<int:sympathys_count>/', views.sympathy2, name='sympathy2'),
    path('good1/<int:idea_pk>/<int:goods_count>/', views.good1, name='good1'),
    path('good2/<int:idea_pk>/<int:goods_count>/', views.good2, name='good2'),
    path('<int:idea_pk>/idea_delete/', views.idea_delete, name='idea_delete'),
    path('<int:post_pk>/<int:idea_pk>/idea_delete_confirm/', views.idea_delete_confirm, name='idea_delete_confirm'),
]
