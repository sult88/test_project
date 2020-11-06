from django.shortcuts import render

from .models import Category, Post


#Получение всех объектов модели: Model.objects.all()
# SELECT * FROM model;
#Получение объектов по условию: Model.objects.filter(условие)
# SELECT * FROM model WHERE условие;
# Исключение объектов из результата по условию: Model.objects.exclude(условие)
# .filter(age > 35) -> SELECT * FROM employee WHERE age > 35;
# .exclude(age > 35) -> SELECT * FROM employee WHERE NOT age > 35;
#Получение объекта по условию или id: Model.objects.get(условие)
# SELECT * FROM model WHERE условие;
# Получение первого объекта из списка: Model.objects.first() или Model.objects.filter().first()
# SELECT * FROM model [WHERE ...] [ORDER BY ...] LIMIT 1;
#Получение последнего объекта из списка: Model.objects.last() или Model.objects.filter().last()
# создание объекта: Model.objects.create()
# INSERT INTO model (поля) VALUES ();
# Обновление объектов: Model.objects.update() или Model.objects.filter().update()
# UPDATE model SET ... WHERE
# Удаление объектов: Model.objects.delete() или Model.objects.filter().delete()
# DELETE FROM model WHERE....;
# Получение количества объектов в запросе: Model.objects.count() или Model.objects.filter().count()
# SELECT COUNT(*) FROM model WHERE ...;


def index_page(request):
    categories_list = Category.objects.all()
    return render(request, 'blog/index.html', {'categories': categories_list})

# categories/slug/
# def category_details(request, slug):
#     category = Category.objects.get(slug=slug)
#     # posts = Post.objects.filter(category=category)
#     posts = category.posts.all()
#     return render(request, 'blog/category_details.html', {'category': category, 'posts': posts})
    # return render(request=request, template_name='blog/category_details.html', context={'category': category, 'posts': posts})

# posts/?category='slug'
# request.GET -> {'category': 'slug'}

# /notebooks
# /notebooks/?disk=hdd&price_from=10000&price_to=1000000
# request.GET -> {'disk': 'hdd', 'price_from': '10000', 'price_to': '100000'}
def posts_list(request):
    category_slug = request.GET.get('category')
    posts = Post.objects.all()
    if category_slug is not None:
        posts = posts.filter(category_id=category_slug)
    return render(request, 'blog/posts_list.html', {'posts': posts})
