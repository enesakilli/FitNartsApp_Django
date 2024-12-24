from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .forms import DiaryEntryForm
from .models import DiaryEntry

@login_required
def diary_list(request):
    entries = DiaryEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'diary/diary_list.html', {'entries': entries})


@login_required
def add_entry(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False) # Direkt save olmaz, hata veya eksik bir şeyler varsa diye
            entry.user = request.user # Kullanıcıya özgü olarak save olur
            entry.save()
            return redirect('diary_list')
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/add_entry.html', {'form': form})


@login_required
def edit_entry(request, pk):
    try:
        entry = DiaryEntry.objects.get(id=pk, user=request.user)  # Kullanıcıya ait olan entry'yi alıyoruz
    except DiaryEntry.DoesNotExist:
        return HttpResponseForbidden("You do not have permission to edit this entry.")
    
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, instance=entry)  # Var olan entry'yi düzenlemek için instance ekliyoruz
        if form.is_valid():
            form.save()
            # messages.success(request, 'Entry updated successfully.')
            return redirect('diary_list')
    else:
        form = DiaryEntryForm(instance=entry)  # Formu mevcut entry ile dolduruyoruz
    
    return render(request, 'diary/edit_entry.html', {'form': form})


@login_required
def delete_entry(request, pk):  # primary key kullanarak belirli bir entry'yi silmemiz gerekli
    entry = DiaryEntry.objects.get(id=pk, user=request.user) # Veritabanından kullanıcıya ait olan entry'yi alıyoruz
    
    if entry: # Entry bulunduysa silme işlemi
        entry.delete() # Entry silinir ORM sayesinde
        # messages.success(request, 'Entry deleted successfully')
    return redirect('diary_list')  # Kullanıcıyı diary listesine yönlendiriyoruz

