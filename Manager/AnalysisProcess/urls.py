from django.urls import include, path

from Manager.AnalysisProcess import views

urlpatterns = [
    # path('charts/', views.chart, name='chart'),
    path('list/', views.analysis_process_list, name='analysis_process-list'),
    path('add/', views.analysis_process_add, name='analysis_process-add'),
    path('<int:analysis_process_id>/detail/', views.analysis_process_detail, name='analysis_process-detail'),
    path('<int:analysis_process_id>/analysis_cost/', views.analysis_process_make, name='analysis_process-make'),
    path('<int:analysis_process_id>/analysis_importance/', views.analysis_importance_works,
         name='analysis_importance_works'),
    path('<int:analysis_process_id>/delete/', views.analysis_process_delete, name='analysis_process-delete'),
    path('<int:analysis_process_id>/abc', views.analysis_process_abc, name='analysis_process-abc'),
    path('<int:analysis_process_id>/abc-second', views.analysis_process_abc_second, name='analysis_process-abc-second'),

]
