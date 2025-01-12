from django.contrib import admin
from .models import Nome, Produto, carrinho, User

# ----- Configuração para o modelo Nome -----
@admin.register(Nome)
class NomeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


# ----- Configuração para o modelo Produto -----
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco', 'quantidade')
    list_filter = ('nome',)
    search_fields = ('nome__nome', 'descricao')  # Busca no campo nome do modelo Nome
    
# ----- Configuração para o modelo carrinho -----
@admin.register(carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade')
    list_filter = ('produto__nome',)
    search_fields = ('produto__nome__nome', 'produto__descricao') # Busca em produto.nome.nome e produto.descricao
    
# ----- Configuração para o modelo User -----
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')