from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from django_claudius.models import Case

class CaseListView(LoginRequiredMixin, ListView):
    model = Case
    template_name = "dashboard/index.html"
    ordering = ['-id']
    def get_queryset(self):
        return Case.objects.filter(owner=self.request.user)

