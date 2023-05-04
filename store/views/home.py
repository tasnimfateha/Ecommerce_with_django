from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}

    products = Products.get_all_products();

    data = {}
    data['products'] = products


    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)

def product_search(request):
    query = request.GET.get('q')
    if query:
        products = Products.objects.filter(title__icontains=query)
    else:
        products = Products.objects.all()
    return render(request, 'index.html', {'products': products})
