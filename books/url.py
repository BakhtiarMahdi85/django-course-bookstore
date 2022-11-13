from django.urls import path
from.views import BookListView, BookDetailView, CreatNewBookView, UpdateBookView, DeleteBooViews
urlpatterns = (
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create/', CreatNewBookView.as_view(), name='new_book'),
    path('<int:pk>/update/', UpdateBookView.as_view(), name='book_update'),
    path('<int:pk>/delete/', DeleteBooViews.as_view(), name='delete_book'),


)


