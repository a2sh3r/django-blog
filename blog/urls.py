from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.get_all_post, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/',
         views.get_all_post, name='post_list_by_tag'),

    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),

    path('<int:post_id>/share/',
         views.share_post, name='post_share'),

    path('<int:post_id>/comment/',
         views.comment_post, name='post_comment'),

    path('search/', views.post_search, name='post_search'),
]
