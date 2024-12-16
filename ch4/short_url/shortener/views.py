import random
import string

from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from shortener.forms import ShortURLForm
from shortener.models import ShortURL

from rest_framework.generics import GenericAPIView

class HomeView(View):
    def get(self, request):
        short_urls = ShortURL.objects.all()
        context = {"short_urls": short_urls, "form": ShortURLForm}
        return render(request, "home.html", context=context)


class ShortURLCreateView(View):
    def _generate_short_url(self):
        characters = string.ascii_letters + string.digits  # 대소문자 알파벳 + 숫자
        return ''.join(random.choices(characters, k=8))

    def post(self, request):
        form = ShortURLForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)  # DB 저장 전 객체 생성

            # 중복 검사
            while True:
                code = self._generate_short_url()
                duplicate = ShortURL.objects.filter(code=code).exists()
                if not duplicate:
                    break

            obj.code = code
            obj.save()
            return HttpResponseRedirect(reverse("home"))


class ShortURLDetailView(View):
    def get(self, request, code):
        short_url = get_object_or_404(ShortURL, code=code)
        short_url.access_count = F("access_count") + 1
        short_url.save()
        return redirect(short_url.original_url)

    def delete(self, request, code):
        short_url = get_object_or_404(ShortURL, code=code)
        short_url.delete()
        return HttpResponseRedirect(reverse("home"))
