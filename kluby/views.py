from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Klub, ExtraInfo, Zawodnik, Sezon
from .forms import KlubForm, ExtraInfoFormWszystko, SezonFormWszystko, ZawodnikFormWszystko, ExtraInfoForm, SezonForm, ZawodnikForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required


def portal(request):
    return render(request, 'main/portal.html')

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
@login_required
@permission_required("kluby.add_klub")
def nowy(request):
    form = KlubForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(wszystkie)
    return render(request, 'kluby/nowy.html', {'form': form})
@login_required
@permission_required("kluby.change_klub")
def edytuj(request, klub_id):
    klub = get_object_or_404(Klub, pk=klub_id)
    form = KlubForm(request.POST or None, instance=klub)
    if form.is_valid():
        form.save()
        return redirect(wszystkie)
    return render(request, 'kluby/nowy.html', {'form':form})

@login_required
@permission_required("kluby.delete_klub")
def usun(request, klub_id):
    klub = get_object_or_404(Klub, pk=klub_id)
    if request.method=="POST":
        klub.delete()
        return redirect(wszystkie)
    return render(request, 'kluby/usun.html', {'klub': klub})


@login_required
@permission_required("kluby.add_film")
def nowy_wszystko(request):
    form = KlubForm(request.POST or None)
    form_einfo = ExtraInfoFormWszystko(request.POST or None)
    form_sezon = SezonFormWszystko(request.POST or None)
    form_zawodnik = ZawodnikFormWszystko(request.POST or None)

    if all([form.is_valid(), form_einfo.is_valid(), form_sezon.is_valid(), form_zawodnik.is_valid()]):
        klub = form.save()
        einfo = form_einfo.save(commit=False)
        einfo.klub = klub
        einfo.save()
        sezon = form_sezon.save(commit=False)
        sezon.klub = klub
        sezon.save()
        zawodnik = form_zawodnik.save()
        zawodnik.kluby.add(klub.id)
        zawodnik.save()
        return redirect(wszystkie)
    return render(request, 'kluby/nowy_wszystko.html', {'form': form, 'form_einfo':form_einfo, 'form_sezon': form_sezon, 'form_zawodnik': form_zawodnik})



def extra_wszystkie(request):
    extra = ExtraInfo.objects.all()
    context = {'extra': extra}
    return render(request, 'extra_info/wszystkie.html', context)

def extra_szczegoly(request, extra_id):
    extra = get_object_or_404(ExtraInfo, pk=extra_id)
    return render(request, 'extra_info/szczegoly.html', {'extra': extra})

@login_required
@permission_required("kluby.add_extra")
def extra_nowy(request):
    form = ExtraInfoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(extra_wszystkie)
    return render(request, 'extra_info/nowy.html', {'form': form})
@login_required
@permission_required("kluby.change_extra")
def extra_edytuj(request, extra_id):
    extra = get_object_or_404(ExtraInfo, pk=extra_id)
    form = ExtraInfoForm(request.POST or None, instance=extra)
    if form.is_valid():
        form.save()
        return redirect(extra_wszystkie)
    return render(request, 'extra_info/nowy.html', {'form':form})
@login_required
@permission_required("kluby.delete_extra")
def extra_usun(request, extra_id):
    extra = get_object_or_404(ExtraInfo, pk=extra_id)
    if request.method=="POST":
        extra.delete()
        return redirect(extra_wszystkie)
    return render(request, 'extra_info/usun.html', {'extra': extra})

def sezon_wszystkie(request):
    sezon = Sezon.objects.all()
    context = {'sezony': sezon}
    return render(request, 'sezony/wszystkie.html', context)
def sezon_szczegoly(request, sezon_id):
    sezon = get_object_or_404(Sezon, pk=sezon_id)
    return render(request, 'sezony/szczegoly.html', {'sezony': sezon})


@login_required
@permission_required("kluby.add_sezon")
def sezon_nowy(request):
    form = SezonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(sezon_wszystkie)
    return render(request, 'sezony/nowy.html', {'form': form})
@login_required
@permission_required("kluby.change_sezon")
def sezon_edytuj(request, sezon_id):
    sezon = get_object_or_404(Sezon, pk=sezon_id)
    form = SezonForm(request.POST or None, instance=sezon)
    if form.is_valid():
        form.save()
        return redirect(sezon_wszystkie)
    return render(request, 'sezony/nowy.html', {'form':form})
@login_required
@permission_required("kluby.delete_sezon")
def sezon_usun(request, sezon_id):
    sezon = get_object_or_404(Sezon, pk=sezon_id)
    if request.method=="POST":
        sezon.delete()
        return redirect(sezon_wszystkie)
    return render(request, 'sezony/usun.html', {'sezon': sezon})





def zawodnik_wszystkie(request):
    zawodnik = Zawodnik.objects.all()
    context = {'zawodnicy': zawodnik}
    return render(request, 'zawodnicy/wszystkie.html', context)
def zawodnik_szczegoly(request, zawodnik_id):
    zawodnik = get_object_or_404(Zawodnik, pk=zawodnik_id)
    return render(request, 'zawodnicy/szczegoly.html', {'zawodnicy': zawodnik})


@login_required
@permission_required("kluby.add_zawodnik")
def zawodnik_nowy(request):
    form = ZawodnikForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(zawodnik_wszystkie)
    return render(request, 'zawodnicy/nowy.html', {'form': form})
@login_required
@permission_required("kluby.change_zawodnik")
def zawodnik_edytuj(request, zawodnik_id):
    zawodnik = get_object_or_404(Zawodnik, pk=zawodnik_id)
    form = ZawodnikForm(request.POST or None, instance=zawodnik)
    if form.is_valid():
        form.save()
        return redirect(zawodnik_wszystkie)
    return render(request, 'zawodnicy/nowy.html', {'form':form})
@login_required
@permission_required("kluby.delete_zawodnik")
def zawodnik_usun(request, zawodnik_id):
    zawodnik = get_object_or_404(Zawodnik, pk=zawodnik_id)
    if request.method=="POST":
        zawodnik.delete()
        return redirect(zawodnik_wszystkie)
    return render(request, 'zawodnicy/usun.html', {'zawodnik': zawodnik})



def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse('login'))