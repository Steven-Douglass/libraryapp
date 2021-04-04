from django.urls import path

from . import views

urlpatterns = [
    # ex: /library/
    path('', views.index, name='index'),
    # ex: /library/author/2
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    # ex: /library/book/2
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    # ex: /library/location/1
    path('location/<int:library_id>/', views.library_detail, name='library_detail'),
    # ex: /library/member/1
    path('member/<int:member_id>/', views.member_detail, name='member_detail'),
]