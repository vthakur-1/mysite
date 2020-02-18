from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='main_page'),
    # path('registration/', views.registration, name='registration'),
    path('', views.dashbosrd , name='profile'),
    path('album/', views.addalbum, name='add-album'),
    path('album/<int:album_id>/photo/add', views.addphoto , name='add-photo'),
    # path('album/<int:album_id/photo/view>',views.viewphoto,name='view-photo'),
]
    # path('add-book/', views.add_book, name='add-book'),
    # path('books/<int:author_id>', views.book_list, name='book-list'),