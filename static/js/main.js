// Archivo principal para controlar el flujo general de la página.
// Aquí conectamos las piezas (la data, las animaciones y el reproductor)

document.addEventListener('DOMContentLoaded', async () => {
    console.log("Sistema iniciado: 🟢 El Comedor está abierto.");

    // 1. Muestra un mensaje en consola (Para probar que todo funciona)
    if(typeof cargarCatalogo === 'function' && document.getElementById('contenedor-canciones')) {
        const catalogo = await cargarCatalogo(); // Llama a la función de data.js
    }
    
    // --- LÓGICA DEL SLIDER (ESTUDIO) ---
    const sliderTrack = document.getElementById('slider-track');
    const prevBtn = document.getElementById('slider-prev');
    const nextBtn = document.getElementById('slider-next');
    
    if (sliderTrack && prevBtn && nextBtn) {
        let currentIndex = 0;
        const totalSlides = sliderTrack.children.length;

        const updateSlider = () => {
            sliderTrack.style.transform = `translateX(-${currentIndex * 100}%)`;
        };

        nextBtn.addEventListener('click', () => {
            currentIndex = (currentIndex + 1) % totalSlides;
            updateSlider();
        });

        prevBtn.addEventListener('click', () => {
            currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
            updateSlider();
        });
    }

});
