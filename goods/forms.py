from django import forms


class FilterForm(forms.Form):
    only_promo = forms.BooleanField(
        label='Only Promo',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'flexCheckDefault'})
    )
    CHOICES = [
        ('1', 'Default'),
        ('2', 'Low'),
        ('3', 'High'),
    ]
    sort_by = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=CHOICES
    )

# form = FilterForm()
# for f in form:
#     print(f)
