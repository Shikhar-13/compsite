from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.text
 
class SubjectEntry(models.Model):
    topic =models.ForeignKey(Topic, on_delete=models.CASCADE , related_name='entries')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='doc/')
    

    class Meta:
       verbose_name_plural = 'entries'

    def _str_(self):
        return self.text[:50] + "..."
    
#class Entry(models.Model):
    #topic =models.ForeignKey(Topic, on_delete=models.CASCADE , related_name='entras')
    #text = models.TextField()
    #date_added = models.DateTimeField(auto_now_add=True)

    #class Meta:
     #  verbose_name_plural = 'ework'
    #def _str_(self):
       # return self.text[:50] + "..." ***
        
