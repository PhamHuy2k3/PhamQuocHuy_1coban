from django.shortcuts import render, get_object_or_404
from .models import Post, Product, AboutDetail

def index(request):
    posts = Post.objects.all().order_by('-created_at')[:3]
    all_products = Product.objects.all().order_by('-created_at') # Fetch all products for the main section
    new_arrival_products = Product.objects.filter(category='new_arrival').order_by('-created_at')[:5]
    best_selling_products = Product.objects.filter(category='best_selling').order_by('-created_at')[:5]
    you_may_also_like_products = Product.objects.filter(category='you_may_also_like').order_by('?')[
                                 :5]  # '?' for random order
    men_products = Product.objects.filter(category='men').order_by('-created_at')[:3]
    women_products = Product.objects.filter(category='women').order_by('-created_at')[:3]
    accessories_products = Product.objects.filter(category='accessories').order_by('-created_at')[:3]

    dic = {
        'posts': posts,
        'all_products': all_products, # Pass all products
        'new_arrival_products': new_arrival_products,
        'best_selling_products': best_selling_products,
        'you_may_also_like_products': you_may_also_like_products,
        'men_products': men_products,
        'women_products': women_products,
        'accessories_products': accessories_products,
        'title': 'Home',
    }
    return render(request, 'index.html', context=dic)

def category_detail(request, category_slug):
    # Map slug to display name
    category_display_name = dict(Product.CATEGORY_CHOICES).get(category_slug, category_slug.replace('_', ' ').title())
    products = Product.objects.filter(category=category_slug).order_by('-created_at')
    dic = {
        'category_slug': category_slug,
        'category_display_name': category_display_name,
        'products': products,
        'title': category_display_name,
    }
    return render(request, 'category_detail.html', context=dic)

def contact(request):
    dic = {
        'title': 'Contact',
    }
    return render(request, 'contact.html', context=dic)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    dic = {
        'post': post,
        'title': post.title,
    }
    return render(request, 'post_detail.html', context=dic)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    dic = {
        'product': product,
        'title': product.name,
    }
    return render(request, 'product_detail.html', context=dic)

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    dic = {
        'posts': posts,
        'title': 'Blog',
    }
    return render(request, 'post_list.html', context=dic)

def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    dic = {
        'products': products,
        'title': 'Products',
    }
    return render(request, 'product_list.html', context=dic)

def about(request):
    about_details = AboutDetail.objects.all()
    dic = {
        'about_details': about_details,
        'title': 'About',
    }
    return render(request, 'about.html', context=dic)

def about_detail(request, slug):
    about_detail = get_object_or_404(AboutDetail, slug=slug)
    dic = {
        'about_detail': about_detail,
        'title': about_detail.title,
    }
    return render(request, 'about_detail.html', context=dic)
