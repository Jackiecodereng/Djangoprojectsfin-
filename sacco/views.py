from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from sacco.app_forms import CustomerForm, DepositForm
from sacco.models import Customer, Deposit


# Create your views here.
def test(request):
    # c1 = Customer(first_name='John', last_name='Smith',email='j@gmail.com',dob='2000-11-22',gender='Male',weight=63.5)
    # c1.save()
    #
    # c2 = Customer(first_name='Jack', last_name='Smen', email='alan@gmail.com', dob='2001-12-22', gender='Male',
    #               weight=62.5)
    # c2.save()

    # fetching one customer
    customers_count = Customer.objects.count()
    c1 = Customer.objects.get(id=1)  # select*from customers where id=1
    print(c1)

    d1 = Deposit(amount=1000, status=True, customer=c1)
    d1.save()
    deposit_count = Deposit.objects.count()


    return HttpResponse(f"Hello World the {customers_count} Customers are listed here and their{deposit_count} Deposits are listed here")


def customers(request):
    data = Customer.objects.all().order_by('id').values()   # select*from all orm object relational mapper. -id means in descending orderwhile id is in ascending order
    paginator = Paginator(data, 15)  #this one separets the data in pages
    page_number = request.GET.get('page', 1)
    try:
        paginated_data = paginator.page(page_number)
    except PageNotAnInteger |EmptyPage:
        paginated_data = paginator.page(1)
    return render(request, "customers.html", {"data": paginated_data})


def delete_customer(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()   # delete where id =7
    messages.info(request, f"customer {customer_id} has been deleted")
    return redirect('customers')


# line 34 deleting customer in views file.
def add_customer(request):
    if request.method == "POST":
      form = CustomerForm(request.POST,request.FILES)
      if form.is_valid():
          form.save() # saves customer and redirects to home page
          messages.success(request, f"Customer {form.cleaned_data['first_name']} has been added")
          return redirect('customers')
    else:
        form = CustomerForm()
    return render(request,'customer_form.html',{"form":form})



def update_customer(request,customer_id):
    customer = get_object_or_404(Customer,id=customer_id)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()  # saves customer and redirects to home page
            messages.success(request, f"Customer {form.cleaned_data['first_name']} was updated")
            return redirect('customers')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_update_form.html', {"form": form})



def search_customer(request):
    search_term = request.GET.get('search')
    data = Customer.objects.filter(Q(first_name__icontains=search_term) | Q(last_name__icontains=search_term) | Q(email__icontains=search_term))
    #select* from customers where first name is like %noel% or last_name like
    return render(request, "search.html", {"customers": data})




def deposit(request,customer_id):
    customer = get_object_or_404(Customer,id=customer_id)
    if request.method == "POST":
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            depo = Deposit(amount=amount, status=True, customer=customer)
            depo.save()
            messages.success(request,'Your deposited have been successfully saved.') # import from django contrib messages
            return redirect('customers')
    else:
        form = DepositForm()
    return render(request, template_name= 'customer_form_deposits.html', context={"form": form, "customer": customer})


def customer_details(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    deposits = Deposit.objects.filter(customer_id=customer_id)
    total = Deposit.objects.filter(customer=customer).filter(status=True).aggregate(Sum('amount'))["amount__sum"]
    return render(request,template_name="details.html", context={"deposits": deposits ,"customer": customer ,"total": total })




# beautifies the form using bootstrap use in terminal
# pip install django-crispy-forms
#pip install crispy-bootstrap5
# line 43 and 44 saves data
#pip install Pillow




