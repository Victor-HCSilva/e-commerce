from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Produto
from django.contrib.auth import authenticate

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

        labels = {
             'username':'Nome de Usuário:',
            'password': 'Senha:'
        }

    def save(self, commit=True):
      user = super().save(commit=False) # Salvando utilizando o próprio save do AbstractUser
      if commit:
          user.save()
      return user
    
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'preco': forms.NumberInput(attrs={'step': '0.01'}),
            'quantidade': forms.NumberInput()
        }
        labels = {
            'nome':'Produto:',
            'descricao': 'Descrição:',
            'preco': 'Preço(R$):',
            'quantidade': 'Quantidade em Estoque:'
        }

class LoginForm(forms.Form):
    username = forms.CharField(label="Nome", max_length=150)
    password = forms.CharField(widget=forms.PasswordInput(), label="Senha")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Credenciais inválidas.")
            cleaned_data['user'] = user
        return cleaned_data