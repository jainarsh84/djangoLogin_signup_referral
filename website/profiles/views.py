from django.shortcuts import render

# Create your views here.
def my_recommendations_view(request):
  context = {}
  return render{request,'base_profile.html',context)
