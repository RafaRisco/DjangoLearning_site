from django.urls import path

from . import views

urlpatterns = [
    path('', views.course_list, name="course"),
    path('<course_pk>/t<step_pk>/', views.text_detail, name='text'),
    path('<course_pk>/q<step_pk>/', views.quiz_detail, name='quiz'),
    path('<course_pk>/create_quiz/', views.quiz_create, name='create_quiz'),
    path('<course_pk>/edit_quiz/<quiz_pk>/', views.quiz_edit, name='edit_quiz'),
    path('<quiz_pk>/create_question/<question_type>/', views.create_question, name='create_question'),
    path('<quiz_pk>/edit_question/<question_pk>/', views.edit_question, name='edit_question'),
    path('<question_pk>/create_answer/', views.answer_form, name="create_answer"),
    path('by/<teacher>/', views.courses_by_teacher, name='by_teacher'),
    path('search/', views.search, name='search'),
    path('<int:pk>/', views.course_detail, name='detail'),
]

# url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(),
# name='post_detail'),

# path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
