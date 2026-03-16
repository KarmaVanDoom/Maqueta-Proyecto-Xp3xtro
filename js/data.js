// Este archivo se encarga exclusivamente de leer los datos de tu 'base de datos' gratuita (.json)

async function cargarCatalogo() {
    try {
        // En un futuro, este JSON será modificado por el Launcher de Python
        const respuesta = await fetch('assets/canciones.json');
        const canciones = await respuesta.json();
        console.log("Canciones cargadas con éxito:", canciones);
        return canciones;
    } catch (error) {
        console.error("Error al cargar el catálogo de canciones:", error);
        return [];
    }
}

// Puedes probar en la consola si funciona llamando a cargarCatalogo()
