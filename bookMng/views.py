from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Book
from .models import Message

# Create your views here.
from .models import MainMenu
from .forms import BookForm
from .forms import MessageForm

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

def index(request):
   return render(request,
                 'bookMng/index.html',
                 {
                    'item_list': MainMenu.objects.all()
                 })

@login_required(login_url=reverse_lazy('login'))
def postbook(request):
   submitted = False
   if request.method == 'POST':
       form = BookForm(request.POST, request.FILES)
       if form.is_valid():
           #form.save()
           book = form.save(commit=False)
           try:
               book.username = request.user
           except Exception:
               pass
           book.save()
           return HttpResponseRedirect('/postbook?submitted=True')
   else:
       form = BookForm()
       if 'submitted' in request.GET:
           submitted=True
   return render(request,
                 'bookMng/postbook.html',
                 {
                    'form': form,
                    'item_list': MainMenu.objects.all(),
                    'submitted': submitted
                 })

@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
   books = Book.objects.all()
   for b in books:
       b.pic_path = b.picture.url[14:]
   return render(request,
                 'bookMng/displaybooks.html',
                 {
                    'item_list': MainMenu.objects.all(),
                     'books': books
                 })


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
   book = Book.objects.get(id=book_id)
   book.pic_path = book.picture.url[14:]
   return render(request,
                 'bookMng/book_detail.html',
                 {
                    'item_list': MainMenu.objects.all(),
                     'book': book
                 })

@login_required(login_url=reverse_lazy('login'))
def mybooks(request):
   books = Book.objects.filter(username=request.user)
   for b in books:
       b.pic_path = b.picture.url[14:]
   return render(request,
                 'bookMng/mybooks.html',
                 {
                    'item_list': MainMenu.objects.all(),
                     'books': books
                 })

@login_required(login_url=reverse_lazy('login'))
def book_delete(request, book_id):
   book = Book.objects.get(id=book_id)
   book.delete()
   return render(request,
                 'bookMng/book_delete.html',
                 {
                    'item_list': MainMenu.objects.all(),
                     'book': book
                 })

@login_required(login_url=reverse_lazy('login'))
def inbox(request):
    messages = Message.objects.filter(to_user=request.user)
    return render(request,
                  'bookMng/inbox.html',
                  {
                     'item_list': MainMenu.objects.all(),
                     'messages': messages
                  })

@login_required(login_url=reverse_lazy('login'))
def sendmessage(request):
   submitted = False
   if request.method == 'POST':
       form = MessageForm(request.POST, request.FILES)
       if form.is_valid():
           message = form.save(commit=False)
           try:
               message.from_user = request.user
           except Exception:
               pass
           message.save()
           return HttpResponseRedirect('/sendmessage?submitted=True')
   else:
       form = MessageForm()
       if 'submitted' in request.GET:
           submitted=True
   return render(request,
                 'bookMng/sendmessage.html',
                 {
                    'form': form,
                    'item_list': MainMenu.objects.all(),
                    'submitted': submitted
                 })

@login_required(login_url=reverse_lazy('login'))
def search(request):
   return render(request,
                 'bookMng/search.html',
                 {
                    'item_list': MainMenu.objects.all()
                 })