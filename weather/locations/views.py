from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
from locations.models import City
from django.contrib.auth.mixins import LoginRequiredMixin

LOGIN_URL = "users:login"


class ListLocations(LoginRequiredMixin, ListView):
    model = City
    template_name = 'locations/list.html'
    context_object_name = 'locations'
    queryset = City.objects.all().order_by('name')
    paginate_by = 10
    login_url = LOGIN_URL


class AddLocation(LoginRequiredMixin, CreateView):
    model = City
    template_name = 'locations/add.html'
    success_url = reverse_lazy('locations:list')
    fields = ('name', 'latitude', 'longitude')


class DeleteLocation(LoginRequiredMixin, DeleteView):
    model = City
    template_name = 'locations/delete.html'
    success_url = reverse_lazy('locations:list')
    context_object_name = 'location'


class UpdateLocation(LoginRequiredMixin, UpdateView):
    model = City
    template_name = 'locations/update.html'
    success_url = reverse_lazy('locations:list')
    context_object_name = 'location'
    fields = ('name', 'latitude', 'longitude')
