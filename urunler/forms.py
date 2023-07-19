from typing import Any, Dict, Mapping, Optional, Type, Union
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from .models import *

class UrunForm(ModelForm):
    class Meta:
        model = Urun
        fields = ['kategori', 'altKategori', 'isim', 'aciklama', 'fiyat', 'resim']

    def __init__(self, *args, **kwargs):
        super(UrunForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})