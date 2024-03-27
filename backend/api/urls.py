from django.urls import path
from . import views


urlpatterns = [
    path('notes/', views.NotesListCreateView.as_view(), name='notes-list'),
    path('notes/delete/<int:pk>/',
         views.DeleteNoteView.as_view(), name='delete-note'),
    # path('register/', views.CreateUserView.as_view(), name='register'),
    # path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    # path('refresh/', views.MyTokenRefreshView.as_view(), name='refresh'),
]
