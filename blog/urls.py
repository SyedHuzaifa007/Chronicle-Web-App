from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, GeneratePdf
from . import views
from .views import voice_to_text
from django_pdfkit import PDFView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('pdf/', GeneratePdf),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('voice-to-text/', voice_to_text, name='voice_to_text'),
]