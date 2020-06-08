from django.urls import path

from . import views

urlpatterns = [
    path('<int:page_num>/', views.serve_prediction_survey, name='prediction_survey_index'),
    path('<int:page_num>/<int:case_id>/', views.serve_prediction_survey, name='prediction_survey_index')
]