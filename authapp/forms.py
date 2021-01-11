from django.contrib.auth.forms import AuthenticationForm

from .models import Teacher


class TeacherLoginForm(AuthenticationForm):
    class Meta:
        model = Teacher
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(TeacherLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'