from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST

from lists.models import Item, List


# Create your views here.
def home_page(request):
    # if request.method == 'POST':
    #     new_item_text = request.POST['item_text']
    #     Item.objects.create(text=new_item_text)
    #     return redirect('/lists/the-only-list-in-the-world/')

    return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'items': items, 'list': list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request, list_id):
    new_item_text = request.POST['item_text']
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=new_item_text, list=list_)
    return redirect(f'/lists/{list_id}/')


@require_POST
def delete_item(request, list_id):
    text = request.POST.get('text')
    list_ = List.objects.get(id=list_id)
    try:
        item = Item.objects.filter(text=text, list=list_).first()
        item.delete()
        return redirect(f'/lists/{list_id}/')
    except Item.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item does not exist'})
