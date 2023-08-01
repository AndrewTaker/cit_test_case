import json
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, UpdateView, ListView, View
)
from django.contrib.auth.mixins import LoginRequiredMixin
from records.models import Record
from records.forms import AddRecord, GetRecord

LOGIN_URL = "users:login"


class ListRecords(LoginRequiredMixin, ListView):
    model = Record
    template_name = 'records/list.html'
    context_object_name = 'records'
    queryset = Record.objects.all().order_by('-datetime')
    paginate_by = 10
    login_url = LOGIN_URL


class AddRecord(LoginRequiredMixin, CreateView):
    model = Record
    template_name = 'records/add.html'
    success_url = reverse_lazy('records:list')
    form_class = AddRecord
    login_url = LOGIN_URL


class DeleteRecord(LoginRequiredMixin, DeleteView):
    model = Record
    template_name = 'records/delete.html'
    success_url = reverse_lazy('records:list')
    context_object_name = 'record'
    login_url = LOGIN_URL


class UpdateRecord(LoginRequiredMixin, UpdateView):
    model = Record
    template_name = 'records/update.html'
    success_url = reverse_lazy('records:list')
    fields = ('city', 'datetime', 'c_value')
    context_object_name = 'record'
    login_url = LOGIN_URL


class ChartView(LoginRequiredMixin, View):
    form_class = GetRecord
    initial = {}
    template_name = "records/chart_data.html"
    http_method_names = ["get"]
    login_url = LOGIN_URL

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        if self.request.GET:
            data = Record.objects.filter(
                city_id=self.request.GET['city'],
                datetime__contains=self.request.GET['datetime']
            ).values(
                'city__name',
                'datetime__date',
                'datetime__time',
                'c_value',
            )
            if data:
                js_labels = [
                    i['datetime__time'].strftime('%H:%M')
                    for i in data
                ]
                js_data = [i['c_value'] for i in data]
                context = {
                    "form": form,
                    "data": data,
                    "js_labels": json.dumps(js_labels),
                    "js_data": json.dumps(js_data),
                }
                return render(request, self.template_name, context)
        return render(request, self.template_name, {'form': form})
