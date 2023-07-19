from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.db.models import Q
from .forms import *



# Create your views here.

def index(request):
    urunler = Urun.objects.all()
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        urunler = Urun.objects.filter(
            Q(isim__icontains = search) |
            Q(kategori__isim__icontains = search)
        )
    context = {
        'urunler':urunler,
        'search' : search
    }
    return render(request, 'index.html', context)

def urun(request, urunId):
    urunum = Urun.objects.get(id = urunId)
    context = {
        'urun':urunum
    }
    return render(request, 'detail.html', context)

def olustur(request):
    # kategori = Kategori.objects.all()
    # if request.method == 'POST':
    #     resim = request.FILES['resim']
    #     isim = request.POST['isim']
    #     aciklama = request.POST['aciklama']
    #     fiyat = request.POST['fiyat']
    #     kategori = request.POST['kategori']

    #     urun = Urun.objects.create(
    #         kategori_id = kategori,
    #         isim = isim,
    #         aciklama = aciklama,
    #         fiyat = fiyat,
    #         resim = resim,
    #     )
    #     urun.save()
    #     print("Ürün Oluşturuldu")
    #     return redirect('olustur')
    form = UrunForm()
    if request.method == 'POST':
        form = UrunForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        # 'kategoriler' : kategori
        'form':form
    }
    return render(request, 'olustur.html', context)