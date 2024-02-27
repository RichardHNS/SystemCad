from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome =  request.POST.get('Nome')
    novo_usuario.idade =  request.POST.get('Idade')
    novo_usuario.save()
    
    usuarios = {
    'usuarios': Usuario.objects.all()
}
   
    
    return render(request, 'usuarios/usuarios.html', usuarios)

 

