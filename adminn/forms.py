from django.forms import ModelForm
from products.models import Category

class UpdateCategoryForm(ModelForm):
    class Meta:
        model=Category
        fields='__all__'