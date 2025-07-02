from collections import deque

ALMACEN = [
    [0, 0, 0, 1, 0],      # 0 = vacío, 1 = obstáculo, 2 = robot, 3 = paquete, 4 = entrega
    [0, 2, 0, 1, 3],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 4]
]

POSICION_INICIAL = [1, 1]      # Posición inicial del robot
ZONA_ENTREGA = [4, 4]          # Posición de entrega

def buscar_paquete(almacen):
    """Busca paquetes en el almacén y retorna la posición del primero encontrado"""
    for i in range(len(almacen)):
        for j in range(len(almacen[0])):
            if almacen[i][j] == 3:  # 3 representa un paquete
                return [i, j]
    return None  

def buscar_camino(origen, destino, almacen):
    """Implementa BFS para encontrar el camino más corto evitando obstáculos"""
    cola = deque()
    cola.append(origen)
    visitados = set()
    padres = {}
    visitados.add(tuple(origen))
    
    # Movimientos posibles: arriba, abajo, izquierda, derecha
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while cola:
        actual = cola.popleft()
        
        if actual == destino:
            camino = []
            while tuple(actual) in padres:
                camino.insert(0, actual)
                actual = padres[tuple(actual)]
            return camino
        
        for movimiento in movimientos:
            nueva_pos = [actual[0] + movimiento[0], actual[1] + movimiento[1]]
            
            # Verificar límites del almacén
            if (nueva_pos[0] < 0 or nueva_pos[0] >= len(almacen) or 
                nueva_pos[1] < 0 or nueva_pos[1] >= len(almacen[0])):
                continue
            
            # Verificar si es transitable 
            if (almacen[nueva_pos[0]][nueva_pos[1]] != 1 and 
                tuple(nueva_pos) not in visitados):
                
                cola.append(nueva_pos)
                visitados.add(tuple(nueva_pos))
                padres[tuple(nueva_pos)] = actual
    
    return None  

def mover_robot(camino):
    """Simula el movimiento del robot a través del camino"""
    for paso in camino:
        print(f"Moviendo robot a posición: {paso}")

def principal():
    """Función principal que coordina todo el proceso"""
    posicion_actual = POSICION_INICIAL.copy()
    
    while True:
        paquete_pos = buscar_paquete(ALMACEN)
        
        if paquete_pos is None:
            print("No hay más paquetes para recoger")
            break
        
        print(f"\nPaquete encontrado en: {paquete_pos}")
        
        # Buscar camino al paquete
        camino_paquete = buscar_camino(posicion_actual, paquete_pos, ALMACEN)
        
        if camino_paquete is None:
            print("No se puede llegar al paquete")
            continue
        
        # Mover al paquete
        print("Moviendo hacia el paquete...")
        mover_robot(camino_paquete)
        
        # Recoger paquete 
        print(f"Recogiendo paquete en: {paquete_pos}")
        ALMACEN[paquete_pos[0]][paquete_pos[1]] = 0  # Eliminar paquete del almacén
        
        # Buscar camino a zona de entrega
        camino_entrega = buscar_camino(paquete_pos, ZONA_ENTREGA, ALMACEN)
        
        if camino_entrega is None:
            print("No se puede llegar a la zona de entrega")
            continue
        
        # Mover a zona de entrega
        print("Moviendo a zona de entrega...")
        mover_robot(camino_entrega)
        
        # Dejar paquete 
        print("Paquete entregado en zona de entrega")
        
        # Actualizar posición actual del robot para el próximo ciclo
        posicion_actual = ZONA_ENTREGA.copy()

    print("\nProceso completado: todos los paquetes entregados")

if __name__ == "__main__":
    principal()