from django.shortcuts import render, get_object_or_404
from home.models import UserProfile


def home_id(request):
	
	#location = get_object_or_404(UserProfile, pk=id)

	return render(request, 'home/home.html')
