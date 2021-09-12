
from django.urls import path

from .views import *

urlpatterns = [
    #path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    #path('category/<int:category_id>/' , get_category, name='category'),
    path('category/<int:category_id>/' , NewsbyCategory.as_view(), name='category'),
    path('news/<int:pk>/' , ViewNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),

]