from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import Author
from django.shortcuts import HttpResponseRedirect
# Create your views here.

class AuthorCreateView(CreateView):
    template_name = 'author-create.html'
    success_url = 'success'
    model = Author
    fields = (
        'first_name',
        'last_name',
        'photo',
        'email',
    )
    def form_valid(self, form):
        self.object = Author(photo=self.get_form_kwargs().get('files')['photo'])
        self.object = form.save()
        

        return HttpResponseRedirect(self.get_success_url())


class CreateSuccessView(TemplateView):
    template_name = 'success.html'