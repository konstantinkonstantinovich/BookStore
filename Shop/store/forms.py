from django import forms

from .models import Category


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,
                              widget=forms.TextInput(attrs={'size': '40',
                                                            'class': 'form-control'}))  # noqa: E501
    from_email = forms.EmailField(widget=forms.
                                  TextInput(attrs={'size': '40',
                                                   'class': 'form-control'}))
    message = forms.CharField(widget=forms.
                              Textarea(attrs={'class': 'form-control'}))


# class FilterForm(forms.Form):
#     sorting = forms.ChoiceField(
#         choices=(
#             ("reviews", "According to reviews"),
#             ("popularity", "By popularity"),
#         ),
#         initial="popularity",
#         label="Sorting",
#         widget=forms.RadioSelect
#     )
#     price_sorting = forms.IntegerField(
#         max_value=30,
#         min_value=0,
#         label="Sorting"
#     )
#     category = forms.ChoiceField(
#         choices=[
#             (category.pk, category.name)
#             for category in Category.objects.all()
#         ],
#         required=False
#
#     )
#
