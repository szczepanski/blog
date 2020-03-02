from django.db import models
import re


def removeHtmlTags(raw_html):
  remove_regex = re.compile('<.*?>')
  raw_text = re.sub(remove_regex, '', raw_html)
  return raw_text


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    brief = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='app_blog/images/')

    # tags
    # categories


# below function allows to deispaly new post titles
# in gui admin menu instead of object 1, 2 ...
    def __str__(self):
        brief_html = self.brief[:100]
        brief_text = removeHtmlTags(brief_html)
        return '%s - %s' %(self.title, brief_text)