from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'YOPT - Main page'
        context['content'] = 'YOPT - Your Optimal Parts & Technology'
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'YOPT - Main page'
        context['content'] = 'About us'
        context['text_on_page'] = 'About us'
        return context
