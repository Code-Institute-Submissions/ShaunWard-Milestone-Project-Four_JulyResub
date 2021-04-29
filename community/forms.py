from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)

        # def __init__(self, *args, **kwargs):
        # """
        # Add placeholders and classes, remove auto-generated
        # labels and set autofocus on first field
        # """
        # super().__init__(*args, **kwargs)
        # placeholders = {
        #     'full_name': 'Full Name',
        #     'email': 'Email Address',
        #     'phone_number': 'Phone Number',
        #     'postcode': 'Postal Code',
        #     'town_or_city': 'Town or City',
        #     'street_address1': 'Street Address 1',
        #     'street_address2': 'Street Address 2',
        #     'county': 'County, State or Locality',
        # }