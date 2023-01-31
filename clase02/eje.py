peso_producto_en_gramos = 100
precio_producto = 5.95
peso_kilo_en_gramos = 1000

precio_correcto = ( peso_kilo_en_gramos / peso_producto_en_gramos ) * precio_producto
print(precio_correcto) 

precio_error = peso_kilo_en_gramos / peso_producto_en_gramos  * precio_producto
print(precio_error)