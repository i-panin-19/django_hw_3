import transliterate

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from shop.forms import ProductForm, VersionForm
from shop.models import Product, Category, BlogEntry, Version

'''def index(request):
    context = {
        'product_list': Product.objects.all(),
        'category_list': Category.objects.all(),
        'title': 'Магазин "Ромашка"',
    }
    return render(request, 'shop/index.html', context)'''


class IndexListView(ListView):

    # задаю путь к шаблону
    template_name = 'shop/index_list.html'

    # задаю имя представлению
    context_object_name = 'product_list'

    # указываю имя модели
    model = Product
    extra_context = {'title': 'Магазин "Ромашка"'}

    '''
    формирую данные из модели Product
    '''
    def get_queryset(self):
        return Product.objects.all()

    '''
    получаю контекст из класса IndexListView и обновляю его из модели Category.
    на выходе получаю обновленный контекст
    '''
    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context.update({
            'category_list': Category.objects.all(),
        })
        return context


class BlogCreateView(CreateView):
    model = BlogEntry
    fields = ('title', 'content', 'product')
    success_url = reverse_lazy('list')


class BlogListView(ListView):
    model = BlogEntry
    extra_context = {'title': 'Отзывы'}


class BlogDetailView(DetailView):
    model = BlogEntry
    extra_context = {'title': 'Карточка отзыва'}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        #text = transliterate.translit(self.object.product, reversed=True).lower()
        #self.object.slug = '-'.join(e for e in text if e.isalnum()) + '--' + str(self.object.pk)
        self.object.save()
        return self.object

class BlogUpdateView(UpdateView):
    model = BlogEntry
    fields = ('title', 'content', 'product', 'publication')
    success_url = reverse_lazy('list')


class BlogDeleteView(DeleteView):
    model = BlogEntry
    success_url = reverse_lazy('list')


def toggle_activity(request, pk):
    blog_item = get_object_or_404(BlogEntry, pk=pk)
    if blog_item.publication:
        blog_item.publication = False
    else:
        blog_item.publication = True

    blog_item.save()

    return redirect(reverse('list'))


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('index')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('index')


class VersionListView(ListView):
    model = Version
    context_object_name = 'version_list'
    extra_context = {'title': 'Версии'}


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('list_version')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('list_version')


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('list_version')
