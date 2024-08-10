from django.db import models

class AddModel(models.Model):
	Subject = models.CharField(max_length=30)
	Assignment = models.CharField(max_length=30)
	RMaterial = models.FileField()

	def __str__(self):
		return str(self.Subject)

class AnotesModel(models.Model):
	sid = models.IntegerField(primary_key = True,default=0)
	Subject = models.CharField(max_length=30)
	Chp_name = models.CharField(max_length=30)
	Material = models.FileField()

	def __str__(self):
		return str(self.Subject)

class UploadModel(models.Model):
	name = models.CharField(max_length=30)
	prn = models.IntegerField(primary_key = True)
	subject = models.CharField(max_length=30)
	Submission = models.FileField()


	def __str__(self):
		return str(self.prn)
class PollModel(models.Model):
	question = models.TextField()
	op1 = models.CharField(max_length=40)
	op2 = models.CharField(max_length=40)
	op3 = models.CharField(max_length=40)
	op1c = models.IntegerField(default=0)
	op2c = models.IntegerField(default=0)
	op3c = models.IntegerField(default=0)

	def __str__(self):
		return self.question

	