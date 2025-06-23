from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForms
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.

# def index(request):
#     # template=loader.get_template('food/index.html')
#     item_list = Item.objects.all()
#     context = {
#         'item_list': item_list,
#     }
#     return render(request,'food/index.html',context)

class IndexClassView(ListView):
    model =Item;
    template_name = 'food/index.html'
    context_object_name = 'item_list'

    # return HttpResponse(template.render(context,request))

def items(request):
    return HttpResponse('I love you')
# view
# def detail(request,item_id):
#     match_item = Item.objects.get(pk=item_id)
#     context={
#         'match_item':match_item,
#     }
#     return render(request,'food/detail.html',context)

class FoodDetail(DetailView):
    
    model=Item
    template_name = 'food/detail.html'

# add
# def create_item(request):
#     form = ItemForms(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#     return render(request,'food/form_item.html',{'form':form})

class CreateItem(CreateView):
    model=Item
    fields= ['item_name','item_desc','item_price','item_img']
    template_name= 'food/form_item.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

    


# edit
def update_item(request,item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForms(request.POST or None,instance=item)

    if form.is_valid():
       form.save()
       return redirect('food:index')
    return render(request,'food/form_item.html',{'form':form,'item':item})

# delete
def delete_item(request,item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/delete_item.html',{'item':item})
