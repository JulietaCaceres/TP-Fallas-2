from enum import Enum


class Edad(str, Enum):
    MENOR = "MENOR"
    APTO = "APTO"
    MAYOR = "MAYOR"


class Sexo(str, Enum):
    FEMENINO = "FEMENINO"
    MASCULINO = "MASCULINO"


class MetodoAnticonceptivo(str, Enum):
    NO_USA = "NO_USA"
    PRESERVATIVO = "PRESERVATIVO"
    OTROS = "OTROS"
    NO_APLICA = "NO_APLICA"


class ExamenFisico(str, Enum):
    INTERMEDIO = "INTERMEDIO"
    NORMAL = "NORMAL"
    GRAVE = "GRAVE"


class AuscultacionRespiratoria(str, Enum):
    INTERMEDIO = "INTERMEDIO"
    NORMAL = "NORMAL"
    GRAVE = "GRAVE"


class AuscultacionCardiaca(str, Enum):
    INTERMEDIO = "INTERMEDIO"
    NORMAL = "NORMAL"
    GRAVE = "GRAVE"


class Pulso(str, Enum):
    INTERMEDIO = "INTERMEDIO"
    NORMAL = "NORMAL"
    GRAVE = "GRAVE"
