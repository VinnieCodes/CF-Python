from django import forms

CHART__CHOICES = (
  ('#1', 'Bar Chart'),
  ('#2', 'Pie Chart'),
  ('#3', 'Line Chart'),
)

class SalesSearchForm(forms.Form):
  book_title = forms.CharField(max_length = 120)
  chart_type = forms.ChoiceField(choices = CHART__CHOICES)