from django import forms
TOPPINGS = [
    ('bacon', 'Bacon'),
    ('salami', 'Salami'),
    ('olives', 'Olives'),
]

class ToppingsForm(forms.Form):
    toppings = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=TOPPINGS)
