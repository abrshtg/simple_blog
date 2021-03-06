from django.db import models



class WildLife(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=20, default='animal')
    img = models.ImageField(upload_to= 'pics',default='',null=True)
    article = models.TextField()
    pub_date = models.DateTimeField(blank=True,null=True)
    # json = models.JSONField()
    
    

    def intro(self):
        intr = ' '
        words = self.article.split(' ')[:50]
        return intr.join(words)

    def __str__(self):
        return self.title
