from django.db import models
from django.urls import reverse
from PIL import Image
from datetime import datetime, date
# Create your models here.

#models for the teenagers.
class Student(models.Model):

	STATE_CHOICE = (('FCT' , 'Abuja'),('AB' , 'Abia'),('AD' , 'Adamawa'),('AK' , 'Akwa Ibom'),
	('AN' , 'Anambra'),('BA' , 'Bauchi'),('BY' , 'Bayelsa'),('BE' , 'Benue'),('BO' , 'Borno'),
	('CR' , 'Cross River'),('DE' , 'Delta'),('EB' , 'Ebonyi'),('ED' , 'Edo'),('EK' , 'Ekiti'),
	('EN' , 'Enugu'),('GO' , 'Gombe'),('IM' , 'Imo'),('JI' , 'Jigawa'),('KD' , 'Kaduna'),
	('KN' , 'Kano'),('KT' , 'Katsina'),('KE' , 'Kebbi'),('KO' , 'Kogi'),('KW' , 'Kwara'),
	('LA' , 'Lagos'),('NA' , 'Nassarawa'),('NI' , 'Niger'),('OG' , 'Ogun'),('ON' , 'Ondo'),
	('OS' , 'Osun'),('OY' , 'Oyo'),('PL' , 'Plateau'),('RI' , 'Rivers'),('SO' , 'Sokoto'),
	('TA' , 'Taraba'),('YO' , 'Yobe'),('ZA' , 'Zamfara'),)
	CLASS = (('JSS-1','JSS-1'),('JSS-2','JSS-2'),('JSS-3','JSS-3'),('SS-1','SS-1'),('SS-2','SS-2'),('SS-3','SS-3'),('100L','100L'),
		('200L','200L'),('300L','300L'),('400L','400L'),('500L','500L'),
		('ND1','ND1'),('ND-2','ND-2'),('HND-1','HND-2'))
	GENDER = (('FEMALE', 'FEMALE'), ('MALE', 'MALE'))

	first_name = models.CharField(max_length=225)
	last_name = models.CharField(max_length =225)
	middle_name = models.CharField(max_length=225, null=True)
	sex = models.CharField(max_length=20, choices = GENDER, null=False)
	date_of_birth = models.DateField(max_length=225)
	state_of_origin = models.CharField(max_length=20, choices = STATE_CHOICE, default='Abuja')
	email_address = models.EmailField(unique = True)
	parent_full_name = models.CharField(max_length=225)
	parent_phone_number=models.CharField(max_length=225)
	address = models.TextField()
	active = models.BooleanField(default= True)
	image = models.ImageField(upload_to='teenager/%Y/%m/%d/', null=True)
	phone_number = models.CharField(max_length = 225)

	class Meta:
		ordering = ['-date_of_birth', ]

	def __str__(self):
		return self.first_name


	def get_absolute_url(self):
		return reverse('teen_detail',kwargs={'pk':self.pk})


	def save(self, *args, **kwargs):
	    super().save(*args, **kwargs)
	    img = Image.open(self.image.path)

	    if img.height > 300 or img.width > 300:
	        output_size = (300, 300)
	        img.thumbnail(output_size)
	        img.save(self.image.path)

	@property
	def bday(self):
		bdate = self.date_of_birth
		bdate2 = date.today()
		yr = bdate2.year
		current = bdate.replace(year=yr)
		#datetime_object = datetime.strptime( " bdate.month bate.day", "%m %d")
		return current





class Institution(models.Model):
   
	CLASS = (('JSS-1','JSS-1'),('JSS-2','JSS-2'),('JSS-3','JSS-3'),('SS-1','SS-1'),('SS-2','SS-2'),('SS-3','SS-3'),('100L','100L'),
		('200L','200L'),('300L','300L'),('400L','400L'),('500L','500L'),
		('ND1','ND1'),('ND-2','ND-2'),('HND-1','HND-2'))
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	school = models.CharField(max_length=300)
	degree = models.CharField(max_length=200, default="Nil")
	field_of_study=models.CharField(max_length=200, default="Nil")
	grade_or_class = models.CharField(max_length=200, choices=CLASS)
	started = models.DateField(auto_now=False, auto_now_add=False , null=True)
	ended = models.DateField(auto_now=False, auto_now_add=False , null=True)
	timestamp = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True)


	def __str__(self):
	    return self.school + " : " + self.grade_or_class

	class Meta:
	    ordering = ['-updated', '-timestamp']