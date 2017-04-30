from django.shortcuts import redirect
from django.views.generic.dates import ArchiveIndexView
from django.contrib import messages
from .models import Guestbook
from .forms import GuestbookForm
from generic.mixins import CategoryListMixin


class GuestbookView(ArchiveIndexView, CategoryListMixin):
    model = Guestbook
    date_field = 'posted'
    template_name = 'guestbook.html'
    paginate_by = 10
    allow_empty = True
    form = None

    def get(self, request, *args, **kwargs):
        self.form = GuestbookForm()
        return super(GuestbookView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GuestbookView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        self.form = GuestbookForm(request.POST)
        if self.form.is_valid():
            if self.form.cleaned_data['honeypot'] == '':
                self.form.save()
                messages.add_message(request, messages.SUCCESS, 'ADD')
            return redirect('http://127.0.0.1:8000/guestbook/')
        else:
            return super(GuestbookView, self).get(request, *args, **kwargs)