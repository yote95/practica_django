let fecha_llegada = document.getElementById('fecha_llegada');
let fecha_salida = document.getElementById('fecha_salida');
let now = new Date();
let now_string = now.getFullYear();
now_string += (now.getMonth() + 1) < 10 ? '-0' + (now.getMonth() + 1): '-' + (now.getMonth() + 1)
now_string += now.getDate() < 10 ? '-0' + now.getDate() : '-' + now.getDate()
fecha_llegada.setAttribute('min', now_string);
fecha_salida.setAttribute('min', now_string);
fecha_llegada.addEventListener("change", (e) => {
    fecha_salida.setAttribute('min', fecha_llegada.value); 
})