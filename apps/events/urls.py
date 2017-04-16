from django.conf.urls import patterns, url
from django.contrib import admin

from apps.events.views import EventDetail, ApplyToEvent, confirm_event, \
    FillInTransport, UpdateTransport, ChangeDescription, ChangeDetails, EventImages, \
    AddEvents, DeleteApplication, EditApplication, IncomingApplications, CreateEvent, \
    Participations, InternationalEvents, JsonInternationalEvents, ExportApplications, \
    ExportParticipants, ExportFeedback, InternationalProjects
from apps.feedback.views import NewQuestionset, AnswerFeedback, FillOutQuestionaire


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^/?$', InternationalEvents.as_view(), name='events'),
    url(r'^/list_json?$', JsonInternationalEvents().json_view, name='events_list_json'),
    url(r'^/projects/?$', InternationalProjects.as_view(), name='projects'),
    url(r'^/questionaire/create/?$', NewQuestionset.as_view(), name='newquestionset'),
    url(r'^/add_batch/?$', AddEvents.as_view(), name='batch_add_events'),
    url(r'^/create/?$', CreateEvent.as_view(), name='create_event'),
    url(r'^/(?P<slug>[-\w]+)/?$', EventDetail.as_view(), name='event'),
    url(r'^/(?P<slug>[-\w]+)/applications/?$', IncomingApplications.as_view(),
        name='eventapplications'),
    url(r'^/(?P<slug>[-\w]+)/applications/export/?$', ExportApplications.as_view(),
        name='exportapplications'),
    url(r'^/(?P<slug>[-\w]+)/participants/export/?$', ExportParticipants.as_view(),
        name='exportparticipations'),
    url(r'^/(?P<slug>[-\w]+)/feedback/export/?$', ExportFeedback.as_view(),
        name='exportfeedback'),
    url(r'^/(?P<slug>[-\w]+)/participants/?$', Participations.as_view(),
        name='eventparticipation'),
    url(r'^/(?P<slug>[-\w]+)/apply/delete/?', DeleteApplication.as_view(),
        name='application-delete'),
    url(r'^/(?P<slug>[-\w]+)/apply/edit/?', EditApplication.as_view(),
        name='application-edit'),
    url(r'^/(?P<slug>[-\w]+)/apply/?', ApplyToEvent.as_view(), name='eventapplication'),
    url(r'^/(?P<slug>[-\w]+)/confirm/?$', confirm_event, name='eventconfirmation'),
    url(r'^/(?P<slug>[-\w]+)/description/?$',
        ChangeDescription.as_view(), name='eventdescription'),
    url(r'(?P<slug>[-\w]+)/images/?$', EventImages.as_view(),
        name='eventimages'),
    url(r'^/(?P<slug>[-\w]+)/transportation/?$', FillInTransport.as_view(),
        name='eventtransportation'),
    url(r'^/(?P<slug>[-\w]+)/transportation/update/?', UpdateTransport.as_view(),
        name='updatetransportation'),
    url(r'^/(?P<slug>[-\w]+)/details/?$', ChangeDetails.as_view(),
        name='eventchangedetails'),
    url(r'^/(?P<slug>[-\w]+)/feedback/?$', AnswerFeedback.as_view(),
        name='answer_feedback'),
    url(r'^/(?P<slug>[-\w]+)/questionaire/?$', FillOutQuestionaire.as_view(),
        name='fill_out_questionaire'),
)
