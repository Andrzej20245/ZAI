from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Klub
from .forms import KlubForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

def wszystkie(request):
    kluby=Klub.objects.all()
    context = {'kluby': kluby}
    return render(request, 'kluby/wszystkie.html', context)





def szczegoly(request, klub_id):
    klub = get_object_or_404(Klub, pk=klub_id)
    field_names = [k.name for k in Klub._meta.get_fields()]
    for i,k in enumerate(field_names):
        if k == "sezon":
            field_names[i] = "sezon_set"
        elif k == "zawodnik":
            field_names[i] = "zawodnik_set"
    return render(request, 'kluby/szczegoly.html', {'klub': klub, 'field_names': field_names})

def nowy(request):
    form = KlubForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(wszystkie)
    return render(request, 'kluby/nowy.html', {'form': form})

def edytuj(request, klub_id):
    klub = get_object_or_404(Klub, pk=klub_id)
    form = KlubForm(request.POST or None, instance=klub)
    if form.is_valid():
        form.save()
        return redirect(wszystkie)
    return render(request, 'kluby/nowy.html', {'form':form})
def usun(request, klub_id):
    klub = get_object_or_404(Klub, pk=klub_id)
    if request.method=="POST":
        klub.delete()
        return redirect(wszystkie)
    return render(request, 'kluby/usun.html', {'klub': klub})

def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse('login'))