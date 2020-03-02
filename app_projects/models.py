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
    title = models.CharField(max_length=200)
    date = models.DateField()
    brief = models.TextField()
    content = models.TextField()    
    slug = models.SlugField(null=False, unique=True, primary_key=True)
    image = models.ImageField(upload_to='app_projects/images/')
    
    # tags
    # categories

    # below function allows to deispaly projects titles and brief
    # in gui admin menu instead of object 1, 2 ...
    def __str__(self):
        brief_html = self.brief[:100]
        brief_text = removeHtmlTags(brief_html)
        return '%s - %s' %(self.title, brief_text)
    

    def getAbsoluteUrl(self):
        return reverse('detail', kwargs={'slug': self.slug})
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)