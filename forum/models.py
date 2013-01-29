from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    name = models.CharField(u'Category', max_length=50, unique=True)

    class Meta:
        verbose_name = u'Category'
        verbose_name_plural = u'Categories'

    @models.permalink
    def get_absolute_url(self):
        return ('forum_categroy', None, {
            'categroy_id': self.id
        })


    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(u'Title', max_length=100)
    content = models.TextField(u'Content')

    author = models.ForeignKey(User, verbose_name=u'Author', related_name='add_posts')
    category = models.ForeignKey(Category, verbose_name=u'Category', related_name='posts')

    STATUS = ((1,u'publish'),(0,u'draft'))
    status = models.SmallIntegerField(u'status', choices=STATUS, default=1)

    PIN = ((1,u'Pined'), (0,u'Unpind'))
    announcement = models.SmallIntegerField(u'Pin', choices=PIN, default=0)

    created_at = models.DateTimeField(u'created_date', auto_now_add=True)
    publish_at = models.DateTimeField(u'published_date', auto_now_add=True)
    update_at = models.DateTimeField(u'updated_date', auto_now=True)
    #TODO: change this to foreign Key to comment
    reply_at = models.DateTimeField(u'reply_date', auto_now_add=True)
    tags = TaggableManager(blank=True)

    num_views = models.IntegerField(u'views',default=0)

    class Meta:
        verbose_name = u'Post'
        verbose_name_plural = u'Posts'

    @models.permalink
    def get_absolute_url(self):
        return ('forum_posts', None, {
            'post_id':self.id
        })

    def __unicode__(self):
        return self.title

