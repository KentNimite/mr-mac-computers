from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import HomePage, ShoppingItem, Gallery

from django.views import generic
from .forms import ExampleForm
from django.utils import timezone

# I merely guessed that the system would throw no errors when i added ListView as a third  positional parameter
def index(request):
    page = HomePage.objects.all()
    # There are two places you can maqke querysets from, either from the view or directly
    # ..in the template. Django is not allowing mw pass in the queyset as a
    # ..context, like " 'title':page.page_title ", it raises a queryset error
    # .. saying object does not contain pageaa-title attribute, even though it
    # ..actually does! .. so i am passing in the entire
    # .. page variable object into the template and there i can access it like 
    # .."{% if page %} {{page.page_title}}"..... Now it doesnt raise any 
    # ..queryset errors
    context = {
        'page': page,
        'my_gallery': Gallery.objects.all(),
    }
    return render(request, 'base2.html', context)


class shoppingitemsListView(generic.ListView):
    model = ShoppingItem
    template_name = 'shoppingitem_list.html'



class shoppingitemsDetailView(generic.DetailView):
    model = ShoppingItem
    context_object_name = 'my_shoppingitem_details'
    # MY OWN NAME FOR THE DETAILS AS A TEMPLATE VARIABLE
    template_name = 'shoppingitem_detail.html'




