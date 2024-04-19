from django.urls import path
from payments.views import HomePageView, stripe_config, create_checkout_session, SuccessView, CancelledView, \
    stripe_webhook

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('config/', stripe_config),
    path('create-checkout-session/', create_checkout_session),
    path('success/', SuccessView.as_view()),
    path('canceled/', CancelledView.as_view()),
    path('webhook/', stripe_webhook),
]