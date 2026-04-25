"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
  
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)

    Raises:
        ValueError: Si no hay acciones disponibles
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")
    
    return random.choice(acciones_disponibles)

def minimax_max(tateti: Tateti, estado: List[List[str]]) -> float:
    """
    Calcula recursivamente el valor minimax en un nodo MAX

    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado del tablero

    Returns:
        float: Valor minimax
    """

    if tateti.test_terminal(estado):
        return tateti.utilidad(estado)

    valor_minimax = -float("inf")

    for accion in tateti.acciones(estado):
        estado_sucesor = tateti.resultado(estado, accion)
        valor_minimax = max(valor_minimax, minimax_min(tateti, estado_sucesor))

    return valor_minimax

def minimax_min(tateti: Tateti, estado: List[List[str]]) -> float:
    """
    Calcula recursivamente el valor minimax en un nodo MIN

    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado del tablero

    Returns:
        float: Valor minimax
    """
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado)

    valor_minimax = float("inf")

    for accion in tateti.acciones(estado):
        estado_sucesor = tateti.resultado(estado, accion)
        valor_minimax = min(valor_minimax, minimax_max(tateti, estado_sucesor))

    return valor_minimax

def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)
        
    Raises:
        NotImplementedError: Hasta que el alumno implemente el algoritmo
    """

    jugador = tateti.jugador(estado)

    estados_sucesores: dict[tuple[int, int], float] = {}

    for accion_posible in tateti.acciones(estado):
        if jugador == JUGADOR_MAX:
            estados_sucesores[accion_posible] = minimax_min(tateti, estado)
        else:
            estados_sucesores[accion_posible] = minimax_max(tateti, estado)
        
    if jugador == JUGADOR_MAX:
        return max(estados_sucesores, key=lambda key: estados_sucesores[key])
    else:
        return min(estados_sucesores, key=lambda key: estados_sucesores[key])
