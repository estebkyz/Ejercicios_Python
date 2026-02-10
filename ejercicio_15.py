monto_venta = float(input("Digite el monto de la venta: "))

iva = monto_venta * 0.19

total_a_pagar = monto_venta + iva

pago_cliente = float(input("Digite el pago del cliente: "))

cambio = pago_cliente - total_a_pagar

print("Monto de venta:", monto_venta)
print("IVA (19%):", iva)
print("Total a pagar:", total_a_pagar)
print("Pago del cliente:", pago_cliente)
print("Cambio:", cambio)
