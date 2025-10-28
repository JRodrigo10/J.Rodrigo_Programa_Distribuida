function calcularTotal() {
  let nombre = document.getElementById("nombre").value;
  let precio = parseInt(document.getElementById("producto").value);
  let cantidad = parseInt(document.getElementById("cantidad").value);
  
  let total = precio * cantidad;

  document.getElementById("resultado").innerText =
    `Gracias ${nombre}, el total de tu pedido es: S/ ${total}`;
}
