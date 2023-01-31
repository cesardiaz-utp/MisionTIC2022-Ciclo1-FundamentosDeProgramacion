def ejercicio1():
    calculo = 6 / 2 * (1 + 2)
    return calculo;

def ejercicio2(ProductoGramos: float, precioProducto: float, pesoGramos: int = 1000 ):
    """Retorna la conversion del precio de un producto en deferente presentaciones"""
    precioConversion = precioProducto * pesoGramos / ProductoGramos
    
    return precioConversion
