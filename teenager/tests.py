from django.test import Client, TestCase

# Create your tests here.
from django.urls import reverse
from .models import Student, Institution



class StudentTest(TestCase):
	def setUp(self):
		self.student = Student.objects.create(

			first_name = 'michael',
			last_name = 'craine',
			middle_name = 'Duff',
			sex = 'M',
			date_of_birth = '2020-01-01',
			state_of_origin = 'ABJ',
			email_address = 'musamoh@gmail.com',
			parent_full_name = 'Damian Duff',
			parent_phone_number='08099224431',
			address = '21, railway street wentworthville',
			active = True,
			image = 'teenager',
			phone_number = '0803698459'

			)


	def test_student_list(self):
		self.assertEquals(f'{self.student.first_name}', 'michael')
		self.assertEquals(f'{self.student.last_name}', 'craine')
		self.assertEquals(f'{self.student.middle_name}', 'Duff')
		self.assertEquals(f'{self.student.sex}', 'M')
		self.assertEquals(f'{self.student.date_of_birth}', '2020-01-01')
		self.assertEquals(f'{self.student.state_of_origin}', 'ABJ')
		self.assertEquals(f'{self.student.email_address}', 'musamoh@gmail.com')
		self.assertEquals(f'{self.student.parent_full_name}', 'Damian Duff')
		self.assertEquals(f'{self.student.parent_phone_number}', '08099224431')
		self.assertEquals(f'{self.student.address}', '21, railway street wentworthville')
		self.assertEquals(f'{self.student.active}', True)
		self.assertEquals(f'{self.student.image}', 'teenager')
		self.assertEquals(f'{self.student.phone_number}', '0803698459')
		




