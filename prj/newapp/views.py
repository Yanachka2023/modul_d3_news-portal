# импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'name'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'posts.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_publication'] = "Чуть позже сообщим о предстоящих публикациях!"
        return context


class PostDetail(DetailView):
        # Модель всё та же, но мы хотим получать информацию по отдельному товару
        model = Post
        # Используем другой шаблон — post.html
        template_name = 'post.html'
        # Название объекта, в котором будет выбранный пользователем продукт
        context_object_name = 'post'





