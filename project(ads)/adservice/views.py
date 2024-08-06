from django.shortcuts import render
from rest_framework import viewsets
from .models import Ad
from .serializers import AdSerializer
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Ad
from .forms import AdForm
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

class UserListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            response = requests.get('http://127.0.0.1:8000/users/')
            users = response.json()
            return Response(users)
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=500)


def Ad_list(request):
    ads = Ad.objects.all()
    return render(request, 'ads/ad_list.html', {'ads': ads})


def Ad_create(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('ad_list')
    else:
        form = AdForm()
    return render(request, 'ads/ad_form.html', {'form': form})


def Ad_edit(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if request.method == 'POST':
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ad_list')
    else:
        form = AdForm(instance=ad)
    return render(request, 'ads/ad_form.html', {'form': form})


def Ad_delete(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if request.method == 'POST':
        ad.delete()
        return redirect('ad_list')
    return render(request, 'ads/ad_confirm_delete.html', {'ad': ad})