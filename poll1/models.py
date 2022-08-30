from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
# Create your models here.
class ques(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    ch1=models.CharField(max_length=50,null=True)
    ch2=models.CharField(max_length=50,null=True)
    ch3=models.CharField(max_length=50,null=True)
    ch4=models.CharField(max_length=50,null=True)
    vote1=models.IntegerField(default=0,null=True)
    vote2=models.IntegerField(default=0,null=True)
    vote3=models.IntegerField(default=0,null=True)
    vote4=models.IntegerField(default=0,null=True)
    
  
    def user_can_vote(self, user):
        """ 
        Return False if user already voted
        """
        user_votes = user.vote_set.all()
        qs = user_votes.filter(ques=self)
        if qs.exists():
            return False
        return True

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently'
    

    def __str__(self):
        return self.question_text
    def total(self):
        return self.vote1 + self.vote2 + self.vote3 +self.vote4

