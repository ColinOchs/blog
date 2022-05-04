
from django.views.generic import TemplateView

#Homepaveview is extending templateview
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
