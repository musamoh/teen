from django.urls import path

from .views import HomePageView, StudentCreateView, StudentDetailView, StudentListView,StudentUpdateView,\
InstitutionCreateView,InstituteEditView, edit_inst, institute_create, delete_inst, BirdayView

urlpatterns = [
path('create/', StudentCreateView.as_view(), name ='student_create' ),
path('all/', StudentListView.as_view(), name='all_teens'),
path('<pk>/detail/', StudentDetailView.as_view(), name="teen_detail"),
path('<pk>/update/', StudentUpdateView.as_view(), name="update_teen"),
path('<stud_id>/create_institute/', institute_create, name="teen_school"),
path('<stud_id>/update_school/<inst_id>/', edit_inst, name="edit_school"),
path('<stud_id>/delete_inst/<inst_id>', delete_inst, name="delete_inst"),
path('birthday/', BirdayView.as_view(), name="birthdays")

]


