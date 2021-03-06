from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.core.urlresolvers import *

from joinme import views, api, social


urlpatterns = patterns(
    "",
    url(r"^$", views.index, name="index"),
    url(r"^thanks/$", TemplateView.as_view(template_name="joinme/thanks.html"), name="thanks"),

    url(r"^confirm/(?P<activation_key>[a-z0-9]{0,32})/$", views.confirm, name="confirm-key"),
    url(r"^logout/$",
        "django.contrib.auth.views.logout",
        {"next_page": reverse_lazy("joinme:index")},
        name="logout"),
    url(r"^reset-password/$", views.ResetPassword.as_view(), name="reset-password"),
    url(r"^settings/$", views.SettingsView.as_view(), name="settings"),

    url(r"^category/$", views.index, name="categories"),
    url(r"^category/(?P<pk>\d+)/$", views.CategoryView.as_view(), name="category"),
    # TODO:: add form for creation of category if user is_staff

    url(r"^event/$", views.AllEventsList.as_view(), name="events"),
    url(r"^event/(?P<pk>\d+)/$", views.EventView.as_view(), name="event"),
    url(r"^event/(?P<pk>\d+)/join/$", views.join_event, name="join-event"),
    url(r"^event/(?P<pk>\d+)/leave/$", views.leave_event, name="leave-event"),
    url(r"^event/(?P<pk>\d+)/delete/$", views.DeleteEventView.as_view(), name="delete-event"),
    url(r"^event/(?P<pk>\d+)/edit/$", views.EditEventView.as_view(), name="edit-event"),
    url(r"^event/(?P<pk>\d+)/comment/$", views.add_comment_event, name="add-comment-event"),
    url(r"^event/(?P<pk>\d+)/rating/$", views.add_rating_event, name="add-rating-event"),

    url(r"^event/my/$", views.MyEventsList.as_view(), name="my-events"),
    url(r"^event/created/$", views.CreatedEventsList.as_view(), name="created-events"),
    url(r"^event/all/$", views.AllEventsList.as_view(), name="all-events"),
    url(r"^event/new/$", views.CreateEventView.as_view(), name="create-event"),
    url(r"^search/$", views.SearchList.as_view(), name="search"),

    # API
    url(r"^api/csrf/$", api.csrf, name="android-csrf"),
    url(r"^api/reg/$", api.reg, name="api-reg"),
    url(r"^api/login/$", api.login, name="api-login"),
    url(r"^api/events/$", api.get_events_by_category, name="api-events"),
    url(r"^api/events/next/$", api.get_next_events, name="api-next-events"),
    url(r"^api/event/join/$", api.join_event, name="api-join-event"),
    url(r"^api/event/leave/$", api.leave_event, name="api-leave-event"),
    url(r"^api/event/delete/$", api.delete_event, name="api-delete-event"),

    # Social
    url(r"^vk_auth/$", social.vk_auth, name="vk-auth"),
    url(r"^vk_auth/delete/$", social.vk_auth_delete, name="vk-auth-delete"),

)
# TODO: add 404 and other errors
