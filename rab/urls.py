from django.conf.urls.static import static
from django.urls import path

from config import settings
from . import views

app_name = 'rab'

urlpatterns = [
    path('', views.index, name='index'),
    path('intro/', views.intro, name='intro'),

    # path('board/', views.board, name='board'),
    path('board_reptiles/', views.board_reptiles, name='board_reptiles'),
    path('board_birds/', views.board_birds, name='board_birds'),

    # path('board/<int:board_id>/', views.detail, name='detail'),
    path('board_reptiles/<int:board_id>/', views.detail_reptiles, name='detail_reptiles'),
    path('board_birds/<int:board_id>/', views.detail_birds, name='detail_birds'),

    # path('board/create/', views.board_create, name='board_create'),
    path('board_reptiles/create_reptiles/', views.board_create_reptiles, name='board_create_reptiles'),
    path('board_birds/create_birds/', views.board_create_birds, name='board_create_birds'),

    # path('board/update/<int:board_id>/', views.board_update, name='board_update'),
    path('board_reptiles/update_reptiles/<int:board_id>/', views.board_update_reptiles, name='board_update_reptiles'),
    path('board_birds/update_birds/<int:board_id>/', views.board_update_birds, name='board_update_birds'),

    # path('board/delete/<int:board_id>/', views.board_delete, name='board_delete'),
    path('board_reptiles/delete_reptiles/<int:board_id>/', views.board_delete_reptiles, name='board_delete_reptiles'),
    path('board_birds/delete_birds/<int:board_id>/', views.board_delete_birds, name='board_delete_birds'),

    # path('board/<int:board_id>/comment/create/', views.comment_create, name='comment_create'),
    path('board_reptiles/<int:board_id>/comment/create_reptiles/', views.comment_create_reptiles, name='comment_create_reptiles'),
    path('board_birds/<int:board_id>/comment/create_birds/', views.comment_create_birds, name='comment_create_birds'),

    # path('board/<int:board_id>/application/create/', views.application_create, name='application_create'),
    path('board_reptiles/<int:board_id>/application/create_reptiles/', views.application_create_reptiles, name='application_create_reptiles'),
    path('board_birds/<int:board_id>/application/create_birds/', views.application_create_birds, name='application_create_birds'),

    # path('application/delete/<int:application_id>/', views.application_delete, name='application_delete'),
    path('application/delete_reptiles/<int:application_id>/', views.application_delete_reptiles, name='application_delete_reptiles'),
    path('application/delete_birds/<int:application_id>/', views.application_delete_birds, name='application_delete_birds'),

    # path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('comment/delete_reptiles/<int:comment_id>/', views.comment_delete_reptiles, name='comment_delete_reptiles'),
    path('comment/delete_birds/<int:comment_id>/', views.comment_delete_birds, name='comment_delete_birds'),

    path('mypage/', views.mypage, name='mypage'),

    path('profile/', views.profile, name='profile'),

    # path('want_board/', views.want_board, name='want_board'),
    path('want_board_reptiles/', views.want_board_reptiles, name='want_board_reptiles'),
    path('want_board_birds/', views.want_board_birds, name='want_board_birds'),

    # path('want_board/<int:board_id>/', views.want_board_detail, name='want_board_detail'),
    path('want_board_reptiles/<int:board_id>/', views.want_board_detail_reptiles, name='want_board_detail_reptiles'),
    path('want_board_birds/<int:board_id>/', views.want_board_detail_birds, name='want_board_detail_birds'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
