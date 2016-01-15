from django.forms import widgets
from rest_framework import serializers
from foot.models import  LANGUAGE_CHOICES, STYLE_CHOICES,Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
	model = Author
        fields = ('id','first_name','last_name','email')

