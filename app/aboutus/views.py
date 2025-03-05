from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from utils.utils import send_telegram_message
from settings.settings import TBOT_API_KEY, RECEIVER_TG_ID


# Create your views here.


class AboutUsView(TemplateView):
    template_name = 'aboutus.html'


class ContactUsView(TemplateView):
    template_name = 'contactus.html'


class SendContactForm(RedirectView):
    pattern_name = 'contact_us'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        form = f"""
📩 *Новий запит з сайту!*

👤 *Ім'я:* {name}
📧 *Email:* {email}

📝 *Повідомлення:* {message}
"""

        send_telegram_message(RECEIVER_TG_ID, form, TBOT_API_KEY)

        return self.get(request, *args, **kwargs)
