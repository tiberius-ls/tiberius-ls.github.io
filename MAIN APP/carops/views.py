from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import MultipleObjectMixin
from django.views import generic
from .models import (Car, Client, Contact, MissingCar,)


# Create your views here.
def index(request):
    missing_cars = Car.objects.filter(publish=True)
    data = {
        "missing_car": missing_cars,
        "page_title": "Homepage"

    }

    return render(request, "contents/pages/index.html", data)


class ClientDetailView(LoginRequiredMixin, generic.DetailView,):
    model = Client
    paginate_by = 4
    template_name = 'clientpage.html'

    def get_context_data(self, **kwargs):
        object_list = Car.object.filter(
            owner=self.get_object(), publish=True).order_by(-created-at)
        context = super(ClientDetailView, self).get_context_data(
            object_list=object_list, **kwargs)
        context["title_tag"] = 'Profile'
        return context
