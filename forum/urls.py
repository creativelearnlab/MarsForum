__author__ = 'jxl'

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MarsForum.views.home', name='home'),
    # url(r'^MarsForum/', include('MarsForum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^createpost/$', 'forum.views.new_post', name='new_post'),
    url(r'^index/$', 'forum.views.index', name='index'),
    url(r'^register/$', 'forum.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'discussion/login.html'}, name='login'),
    url(r'^logout/$', 'forum.views.logout_user', name='logout'),
    url(r'^category/(?P<category_id>\d+)/$', 'forum.views.category_post_list', name='category'),
    url(r'^tags/(?P<tag_name>[-\w]+)/$', 'forum.views.tag_post_list', name='forum_tags'),
    url(r'^post/(?P<post_id>\d+)/$', 'forum.views.post', name='post'),
)