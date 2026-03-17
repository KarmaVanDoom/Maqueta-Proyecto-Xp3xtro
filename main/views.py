from django.shortcuts import render, redirect
from django.contrib import messages

def home_view(request):
    return render(request, 'home/index.html')

def music_view(request):
    # Aquí puedes pasar beats desde la base de datos
    # beats = Beat.objects.all()
    # return render(request, 'music/musica.html', {'beats': beats})
    return render(request, 'music/musica.html')

def contact_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')
        
        # Lógica de validación nivel Experto
        if nombre and email and mensaje:
            # En producción: EmailMessage(...) o Contacto.objects.create(...)
            messages.success(request, f"¡Gracias por tu mensaje, {nombre}! Me ponderé en contacto pronto.")
            return redirect('main:contact')
        else:
            messages.error(request, "No se ha podido enviar. Error en los campos.")
            
    return render(request, 'contact/contacto.html')
