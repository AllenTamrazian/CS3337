from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('inbox',views.inbox, name="inbox"),
    path('sendmessage',views.sendmessage, name="sendmessage"),
    path('displaybooks/<int:book_id>/add-comment/', views.add_comment, name='add-comment')

]

