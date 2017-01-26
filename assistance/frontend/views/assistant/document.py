# coding= utf-8
from django.shortcuts import redirect
from django.views.generic import CreateView
from frontend.views.assistant import forms
from assistant.models import Document, Post


class LossCreateForm(CreateView):
    template_name = 'document/create_document.html'
    model = Document
    fields = ['type_document', 'place']

    def get_success_url(self):
        return redirect(self.request.path)

    def get_context_data(self, **kwargs):
        context = super(LossCreateForm, self).get_context_data(**kwargs)
        context['post_form'] = forms.CreatePostForm()
        return context

    def form_valid(self, form):
        data = self.request.POST
        obj = form.save(commit=False)
        post = Post.objects.create(title=data['title'], text=data['text'], user=self.request.user)
        obj.post = post
        obj.type = 'loss'
        obj.save()
        return self.get_success_url()
