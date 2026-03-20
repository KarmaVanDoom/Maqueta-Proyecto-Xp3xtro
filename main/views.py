from django.shortcuts import render, redirect
from django.contrib import messages

import urllib.parse

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
        
        if nombre and email and mensaje:
            # --- LÓGICA DE WHATSAPP ---
            # Tu número de WhatsApp real
            mi_numero = "56999580822"
            
            # Formatear el mensaje para que se vea profesional en el chat
            texto_mensaje = (
                f"🔥 *NUEVO MENSAJE DESDE LA WEB* 🔥\n\n"
                f"*Nombre:* {nombre}\n"
                f"*Asunto:* {asunto}\n"
                f"*Email:* {email}\n\n"
                f"*Mensaje:* {mensaje}"
            )
            
            # Codificar el texto para que sea seguro en una URL
            texto_codificado = urllib.parse.quote(texto_mensaje)
            whatsapp_url = f"https://api.whatsapp.com/send?phone={mi_numero}&text={texto_codificado}"
            
            # Retornar la redirección a WhatsApp
            return redirect(whatsapp_url)
        else:
            messages.error(request, "Error: Por favor completa todos los campos obligatorios.")
            
    return render(request, 'contact/contacto.html')
