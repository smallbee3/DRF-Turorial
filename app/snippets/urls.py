from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# from snippets.views import snippet_list, snippet_detail
from snippets import views
from snippets.views import UserList, UserDetail

app_name = 'snippet'
urlpatterns = [
    # path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),

    # path('snippets/<int:pk>/', snippet_detail, name='snippet-detail')
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),


    # DRF3 튜토리얼 4 - 인증과 권한
    path('users/', UserList.as_view(), name='post-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='post-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
