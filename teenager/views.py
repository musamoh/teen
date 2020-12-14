from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Student,Institution
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404 
from .forms import StudentCreateForm, InstitutionCreateForm
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HomePageView(TemplateView):
	template_name = 'teenager/home.html'


class StudentCreateView(LoginRequiredMixin, CreateView):
	model = Student
	form_class = StudentCreateForm

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    context_object_name = 'teen'




class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = 'teens'

    def get_querset(self):
        return Student.objects.all()

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        context['males'] = Student.objects.all().filter(sex__iexact = "MALE")
        context['females'] = Student.objects.all().filter(sex__iexact = "FEMALE")
        # Add any other variables to the context here
        return context

class StudentUpdateView(LoginRequiredMixin, UpdateView):
	model = Student
	form_class = StudentCreateForm
	template_name ='teenager/student_form.html'


class InstitutionCreateView(LoginRequiredMixin, CreateView):
	model = Institution
	form_class = InstitutionCreateForm

	def form_valid(self,form):
		form.instance.student = Student.objects.get(id=self.kwargs.get('pk'))
		return super(InstitutionCreateView, self).form_valid(form)

@login_required
def institute_create(request, stud_id):
    form = InstitutionCreateForm(request.POST or None, request.FILES or None)
    student = get_object_or_404(Student, pk=stud_id)
    if form.is_valid():
        student_institution = student.institution_set.all()
        institution = form.save(commit=False)
        institution.student = student
        institution.save()
        return HttpResponseRedirect(student.get_absolute_url())
    context = {
        'student': student,
        'form': form,
    }
    return render(request, 'teenager/institution_form.html', context)



class InstituteEditView(UpdateView):
	model = Institution
	form_class = InstitutionCreateForm

	def form_valid(self,form):
		form.instance.student = Student.objects.get(id=self.kwargs.get('pk'))
		return super(InstitutionCreateView, self).form_valid(form)

@login_required
def edit_inst(request, stud_id, inst_id):
    student = get_object_or_404(Student, pk=stud_id)
    institution = get_object_or_404(Institution, pk=inst_id)
    form = InstitutionCreateForm(request.POST or None, request.FILES or None, instance=institution)
    if form.is_valid():
        institution = form.save()
        return HttpResponseRedirect(student.get_absolute_url())
    context = {'student': student,
               'form': form
               }
    return render(request, 'teenager/institution_form.html', context)

@login_required
def delete_inst(request, stud_id, inst_id):
    student = get_object_or_404(Student, pk=stud_id)
    institution = Institution.objects.get(pk=inst_id)
    institution.delete()
    return HttpResponseRedirect(student.get_absolute_url())



class BirdayView(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = 'birthdays'
    template_name = 'teenager/birthday.html'
    






