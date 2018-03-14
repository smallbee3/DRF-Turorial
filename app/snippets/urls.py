from django.urls import path

from snippets.views import snippet_list, snippet_detail

app_name = 'snippet'
urlpatterns = [
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail')
]
