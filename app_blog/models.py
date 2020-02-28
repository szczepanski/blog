from django.db import models
import re


def removeHtmlTags(raw_html):
  remove_regex = re.compile('<.*?>')
  raw_text = re.sub(remove_regex, '', raw_html)
  return raw_text


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()


# below function allows to deispaly new post titles
# in gui admin menu instead of object 1, 2 ...
    def __str__(self):
        description_html = self.description[:100]
        description_text = removeHtmlTags(description_html)
        return '%s - %s' %(self.title, description_text)