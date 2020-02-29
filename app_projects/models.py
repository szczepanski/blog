from django.db import models
import re

# regex value to capture HTML texts that can also
# contain entities, that are not enclosed in brackets such as '&nsbm
regex_tags = """<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});"""


def removeHtmlTags(raw_html):
  remove_regex = re.compile(regex_tags)
  raw_text = re.sub(remove_regex, '', raw_html)
  return raw_text


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='app_projects/images/')
    date = models.DateField()
    url = models.URLField(blank=True)

    # below function allows to deispaly projects titles and description
    # in gui admin menu instead of object 1, 2 ...
    def __str__(self):
        description_html = self.description[:100]
        description_text = removeHtmlTags(description_html)
        return '%s - %s' %(self.title, description_text)