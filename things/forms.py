"""Forms of the project."""

# Create your forms here.

class ThingForm(forms.form):
    name = forms.charField(label="Fullname")
    description = forms.charField(label="Description")
    Quantity = forms.charField(label="quantity")
    