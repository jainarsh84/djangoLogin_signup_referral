from django.shortcuts import render

# Create your views here.
def my_recommendations_view(request):
  profile= Profile.objects.get(user=request.user)
  recs = profile.get_recommended_profiles()
  
  context = {'recs',recs}
  
  return render{request,'profiles/main.html',context)
