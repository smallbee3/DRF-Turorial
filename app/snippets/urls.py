from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# from snippets.views import snippet_list, snippet_detail
from snippets import views

app_name = 'snippet'
urlpatterns = [
    # path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),

    # path('snippets/<int:pk>/', snippet_detail, name='snippet-detail')
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail')

]

urlpatterns = format_suffix_patterns(urlpatterns)
