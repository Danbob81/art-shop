""" Product form for staff users """
from django import forms
from .models import Product, Category, SubCategory


class ProductForm(forms.ModelForm):
    """ Product admin form """
    class Meta:
        """ Get product model and all form fields """
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        sub_categories = SubCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_names_sub = [(c.id, c.get_friendly_name())
                              for c in sub_categories]

        self.fields['category'].choices = friendly_names
        self.fields['sub_category'].choices = friendly_names_sub
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
