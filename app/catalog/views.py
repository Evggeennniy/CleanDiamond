from .models import Category
from django.views.generic import ListView, RedirectView
from django.shortcuts import render
from catalog.models import Category
from django.views.generic import TemplateView, ListView
from django.db.models import Min, Max
from utils.utils import send_telegram_message
from settings.settings import TBOT_API_KEY, RECEIVER_TG_ID
from django.utils import timezone


class IndexView(TemplateView):
    template_name = 'index.html'


class CatalogView(ListView):
    template_name = 'catalog.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Category.objects.annotate(
            min_price=Min('services__price'),
            max_price=Max('services__price')
        ).prefetch_related('services')


class ServicesView(TemplateView):
    template_name = 'services.html'


class SendOrderForm(RedirectView):
    pattern_name = 'index'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', 'Не вказано')
        email = request.POST.get('email', 'Не вказано')
        message = request.POST.get('description', 'Без коментарів')
        square = request.POST.get('square', 0)

        selected_services = [key for key, value in request.POST.items() if value == 'on']

        form = f"""
📩 *Новий запит з сайту!*

👤 *Ім'я:* {name}
📧 *Email:* {email}

📏 *Площа об'єкта:* {square} м²
📝 *Коментар користувача:* {message if message.strip() else "Немає додаткових коментарів"}

🛠️ *Обрані послуги:*
{chr(10).join(f"🔹 {service}" for service in selected_services) if selected_services else "❌ Послуги не вибрані"}

📅 *Дата та час запиту:* {timezone.now().strftime('%d.%m.%Y %H:%M')}
"""

        send_telegram_message(RECEIVER_TG_ID, form, TBOT_API_KEY)

        return self.get(request, *args, **kwargs)
