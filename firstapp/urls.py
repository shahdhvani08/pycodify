from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.python_course, name='python_course'),
    url(r'^python_course/overview/$', views.overview, name='overview'),
    url(r'^setup/$', views.setup, name='setup'),
    url(r'^day1/introduction/$', views.intro, name='intro'),
    url(r'^day1/objects/$', views.objects, name='objects'),
    url(r'^day1/basic_operators/$', views.basic_operators, name='basic_operators'),
    url(r'^day1/decision_making/$', views.decision_making, name='decision_making'),
    url(r'^day1/loops/$', views.loops, name='loops'),
    url(r'^day1/strings/$', views.strings, name='strings'),
    url(r'^day1/lists/$', views.lists, name='lists'),
    url(r'^day1/dict_tuples/$', views.dict_tuples, name='dict_tuples'),
    url(r'^day1/datetime/$', views.datetime, name='datetime'),
    url(r'^day1/map_reduce_filter_lambda/$', views.map_reduce_filter_lambda, name='map_reduce_filter_lambda'),
    url(r'^day1/list_comprehension/$', views.list_comprehension, name='list_comprehension'),

    url(r'^day2/functions/$', views.functions, name='functions'),
    url(r'^day2/file_handling/$', views.file_handling, name='file_handling'),
    url(r'^day2/exceptions/$', views.exceptions, name='exceptions'),
    url(r'^day2/classes_and_objects/$', views.classes_and_objects, name='classes_and_objects'),
    url(r'^interview_questions/$', views.interview_questions, name='interview_questions'),
    url(r'^day4/data_scraping/$', views.data_scraping, name='data_scraping'),
    url(r'^day4/reg_expressions/$', views.reg_expressions, name='reg_expressions'),
     

 ]
