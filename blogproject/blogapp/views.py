
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import BlogPost
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.
def index_view(request): 
    records = BlogPost.objects.order_by('-posted_at')
    paginator = Paginator(records, 4)
    page_number =request.GET.get('page',1)
    pages = paginator.page(page_number)
    return render(
        request, 'index.html', {'orderby_records': pages})

def blog_detail(request, pk):
    record = BlogPost.objects.get(id=pk)
    return render(
        request, 'post.html', {'object': record})

def science_view(request):
    records = BlogPost.objects.filter(category='science').order_by('-posted_at')
    paginator = Paginator(records, 2)
    page_number = request.GET.get('page',1)
    pages = paginator.page(page_number)
    return render(
        request, 'science_list.html', {'orderby_records':pages})

def dailylife_view(request):
    records = BlogPost.objects.filter(category='dailylife'
    ).order_by('-posted_at')
    
    paginator = Paginator(records, 2)
    page_number = request.GET.get('page', 1)
    pages = paginator.page(page_number)

    return render(
       request, 'dailylife_list.html', {'orderby_records':pages})

def music_view(request):
    records = BlogPost.objects.filter(category='music').order_by('-posted_at')
    paginator = Paginator(records,2)
    page_number = request.GET.get('page',1)
    pages = paginator.page(page_number)
    return render(
        request, 'music_list.html',{'orderby_records':pages})
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('blogapp:contact')
    def form_valid(self, form):
           name = form.cleaned_data['name']
           email = form.cleaned_data['email']
           title = form.cleaned_data['title']
           messages = form.cleaned_data['message']
           subject = 'お問い合わせ:{}'.format(title)
           message = \
            '送信者名: {0}\nメールアドレス: {1}\n タイトル: {2}\n メッセージ:\n{3}' \
            .format(name, email, title, message)

           from_email = 'admin@example.com'
           to_list = ['admin@example.com']
           message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,
                                       )
           message.send()
           messages.success(
           self.request, 'お問い合わせは正常に送信されました。')
           return super().form_valid(form)

