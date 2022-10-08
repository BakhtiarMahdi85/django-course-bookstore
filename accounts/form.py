from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username', 'email', 'age', )

class CustomUserchangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields =UserChangeForm.Meta.fields
        fields = ('username', 'email', 'age', )

