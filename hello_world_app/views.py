# from django.http import HttpResponse
from django.views.generic import TemplateView

# def homeView(request):
#     return HttpResponse("<h1>Hello World !!</h1>")

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['name'] = "Md Rakib Uddin Rana"
        context['country'] = "Bangladesh"

        list = [1, 2, 3, 4, 5, 6]
        context['list'] = list

        return context
    