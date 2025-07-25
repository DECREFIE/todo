from django.db import models #DB classes
from django.contrib.auth.models import User #User model from auth framework

class TODOO(models.Model):
    srno = models.AutoField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=25)
    data = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)