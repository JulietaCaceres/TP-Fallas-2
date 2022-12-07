from responses import Edad, Sexo, MetodoAnticonceptivo,\
    ExamenFisico, AuscultacionRespiratoria,\
    AuscultacionCardiaca, Pulso

SINTOMAS = ['edad', 'sexo', 'embarazo_actual', 'embarazo_planificado',
            'metodo_anticonceptivo', 'enfermedad_patologica', 'controlada',
            'auscultacion_respiratoria', 'auscultacion_cardiaca',
            'pulso', 'covid', 'vacunacion', 'enfermedad_grave']

NO_SE_PUEDE_DETERMINAR = 'No se puede determinar la enfermedad con\
                              los datos de entrada.'
NO_APTO_MENOR_EDAD = 'NO APTO: No puede realizar prueba si es menor de edad.'
NO_APTO_MAYOR_EDAD = 'NO APTO: No puede realizar prueba si es menor de edad.'
NO_APTO_DURANTE_EMBARAZO = 'NO APTO: No puede realizar prueba durante\
                            el embarazo.'
NO_APTO_PLANIFICA_EMBARAZO = 'NO APTO: No puede realizar la prueba\
                              si esta planificando un embarazo.'
NO_APTO_SIN_METODO_ANTICONCEPTIVO = 'NO APTO: No puede realizar la prueba\
                                     si no usa métodos anticonceptivos.'
NO_APTO_PRESERVATIVO= "RECALL: Si incorpora otro metodo mas efectivo, se le llamara a futuro."
NO_APTO_CONDICION_FISICA_GRAVE = 'NO APTO: Condición física grave.'
NO_APTO_CONDICION_RESPIRATORIA_GRAVE = 'NO APTO: Condición respiratoria grave.'
NO_APTO_CONDICION_CARDIACA_GRAVE = 'NO APTO: Condición cardiaca grave.'
NO_APTO_PULSO_GRAVE = 'NO APTO: Pulso grave.'
NO_APTO_PASADO_COVID = 'NO APTO: No se puede realizar el estudio si ya\
                        tuvo COVID.'
NO_APTO_VACUNADO_COVID = 'NO APTO: No puede participar del estudio si ya\
                          tiene una vacuna.'
NO_APTO_VACUNADO_ANTES = 'NO APTO: Fue vacunade anteriormente'
NO_APTO_SISTEMA_INMUNOLOGICO = 'NO APTO: Tiene enfermedad grave que\
                                compromete al sistema inmunológico'
RECALL_METODO_EFECTIVO = 'RECALL: Si incorpora otro metodo mas efectivo,\
                          se le llamara a futuro.'
RECALL_CONDICION_MEJORA = 'RECALL: Si su condición mejora se le volverá\
                           a llamar.'
RECALL_NO_CONTROLADA = 'RECALL: No puede realizar la prueba si tiene una\
                        enfermedad o patología no controlada.'
APTO_PARTICIPAR = 'APTO: Puede participar en el estudio"'

DIAGNOSTICOS = [NO_SE_PUEDE_DETERMINAR, NO_APTO_MENOR_EDAD, NO_APTO_MAYOR_EDAD,
                NO_APTO_DURANTE_EMBARAZO, NO_APTO_PLANIFICA_EMBARAZO,
                NO_APTO_SIN_METODO_ANTICONCEPTIVO,
                NO_APTO_CONDICION_FISICA_GRAVE,
                NO_APTO_CONDICION_RESPIRATORIA_GRAVE,
                NO_APTO_CONDICION_CARDIACA_GRAVE,
                NO_APTO_PULSO_GRAVE, NO_APTO_PASADO_COVID,
                NO_APTO_VACUNADO_ANTES, NO_APTO_VACUNADO_COVID,
                NO_APTO_SISTEMA_INMUNOLOGICO,
                RECALL_CONDICION_MEJORA, RECALL_NO_CONTROLADA,
                RECALL_METODO_EFECTIVO, APTO_PARTICIPAR]


r1 = {'diagnostico': NO_APTO_MENOR_EDAD,
      'sintomas': {'edad': Edad.MENOR}}

r2 = {'diagnostico': NO_APTO_MAYOR_EDAD,
      'sintomas': {'edad': Edad.MAYOR}}

r3 = {'diagnostico': NO_APTO_DURANTE_EMBARAZO,
      'sintomas': {'edad': Edad.APTO,
                   'sexo': Sexo.FEMENINO,
                   'embarazo_actual': True}}

r4 = {
    'diagnostico': NO_APTO_PLANIFICA_EMBARAZO,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': True
    }
}

r5 = {
    'diagnostico': NO_APTO_SIN_METODO_ANTICONCEPTIVO,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_planificado': False,
        'embarazo_actual': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.NO_USA
    }
}

r6 = {
    'diagnostico': NO_APTO_CONDICION_FISICA_GRAVE,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_planificado': False,
        'embarazo_actual': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.GRAVE
    }
}


r7 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_planificado': False,
        'embarazo_actual': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.INTERMEDIO
    }
}

r8 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_planificado': False,
        'embarazo_actual': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.INTERMEDIO
    }
}

r9 = {
    'diagnostico': RECALL_NO_CONTROLADA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_planificado': False,
        'embarazo_actual': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlado': False
    }
}

r10 = {
    'diagnostico': RECALL_NO_CONTROLADA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_planificado': False,
        'embarazo_actual': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'examen_fisico': ExamenFisico.INTERMEDIO
    }
}

r11 = {
    'diagnostico': NO_APTO_CONDICION_FISICA_GRAVE,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_planificado': False,
        'embarazo_actual': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'examen_fisico': ExamenFisico.GRAVE,
        'controlado': True,
    }
}


r12 = {
    'diagnostico': NO_APTO_CONDICION_FISICA_GRAVE,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_planificado': False,
        'embarazo_actual': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'examen_fisico': ExamenFisico.GRAVE,
        'controlado': True,
    }
}

r13 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_planificado': False,
        'embarazo_actual': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'examen_fisico': ExamenFisico.INTERMEDIO,
        'controlado': True,
    }
}

r14 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_planificado': False,
        'embarazo_actual': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'examen_fisico': ExamenFisico.INTERMEDIO,
        'controlado': True,
    }
}

r15 = {
    'diagnostico': NO_APTO_CONDICION_RESPIRATORIA_GRAVE,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_planificado': False,
        'embarazo_actual': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.GRAVE,
    }
}


r16 = {
    'diagnostico': NO_APTO_CONDICION_RESPIRATORIA_GRAVE,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_planificado': False,
        'embarazo_actual': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.GRAVE,
    }
}


r17 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_planificado': False,
        'embarazo_actual': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.INTERMEDIO,
    }
}

r18 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_planificado': False,
        'embarazo_actual': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.INTERMEDIO,
    }
}


r19 = {
    'diagnostico': NO_APTO_CONDICION_CARDIACA_GRAVE,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlado': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.GRAVE,
    }
}


r20 = {
    'diagnostico': NO_APTO_CONDICION_CARDIACA_GRAVE,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlado': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.GRAVE,
    }
}


r21 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlado': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.INTERMEDIO,
    }
}

r22 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlado': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.INTERMEDIO,
    }
}


r23 = {
    'diagnostico': NO_APTO_CONDICION_CARDIACA_GRAVE,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.GRAVE,
    }
}


r24 = {
    'diagnostico': NO_APTO_CONDICION_CARDIACA_GRAVE,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.GRAVE,
    }
}


r25 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.INTERMEDIO,
    }
}


r26 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.INTERMEDIO,
    }
}


r27 = {
    'diagnostico': NO_APTO_CONDICION_CARDIACA_GRAVE,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.GRAVE,
    }
}


r28 = {
    'diagnostico': NO_APTO_CONDICION_CARDIACA_GRAVE,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.GRAVE,
    }
}


r29 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.INTERMEDIO,
    }
}

r30 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.INTERMEDIO,
    }
}

r31 = {
    'diagnostico': NO_APTO_PULSO_GRAVE,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.GRAVE,
    }
}

r32 = {
    'diagnostico': NO_APTO_PULSO_GRAVE,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.GRAVE,
    }
}

r33 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.INTERMEDIO,
    }
}

r34 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.INTERMEDIO,
    }
}


r35 = {
    'diagnostico': NO_APTO_PULSO_GRAVE,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlada': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.GRAVE,
    }
}

r36 = {
    'diagnostico': NO_APTO_PULSO_GRAVE,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlada': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.GRAVE,
    }
}

r37 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlada': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.INTERMEDIO,
    }
}

r38 = {
    'diagnostico': RECALL_CONDICION_MEJORA,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlada': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.INTERMEDIO,
    }
}

r39 = {
    'diagnostico': NO_APTO_PASADO_COVID,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.GRAVE,
        'covid': True,
    }
}

r40 = {
    'diagnostico': NO_APTO_PASADO_COVID,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'examen_fisico': ExamenFisico.NORMAL,
        'pulso': Pulso.NORMAL,
        'covid': True,
    }
}

r41 = {
    'diagnostico': NO_APTO_PASADO_COVID,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlada': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.NORMAL,
        'covid': True,
    }
}

r42 = {
    'diagnostico': NO_APTO_PASADO_COVID,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlada': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.NORMAL,
        'covid': True,
    }
}

r43 = {
    'diagnostico': NO_APTO_VACUNADO_COVID,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.NORMAL,
        'covid': False,
        'vacunacion': True,
    }
}

r44 = {
    'diagnostico': NO_APTO_VACUNADO_COVID,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.NORMAL,
        'covid': False,
        'vacunacion': True,
    }
}

r45 = {
    'diagnostico': NO_APTO_VACUNADO_ANTES,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlada': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.NORMAL,
        'covid': False,
        'vacunacion': True,
    }
}

r46 = {
    'diagnostico': NO_APTO_VACUNADO_ANTES,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlada': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.NORMAL,
        'covid': False,
        'vacunacion': True,
    }
}

r47 = {
    'diagnostico': NO_APTO_SISTEMA_INMUNOLOGICO,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.NORMAL,
        'covid': False,
        'vacunacion': False,
        'enfermedad_grave': True,
    }
}

r48 = {
    'diagnostico': NO_APTO_SISTEMA_INMUNOLOGICO,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.NORMAL,
        'covid': False,
        'vacunacion': False,
        'enfermedad_grave': True,
    }
}

r49 = {
    'diagnostico': NO_APTO_SISTEMA_INMUNOLOGICO,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlada': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.NORMAL,
        'covid': False,
        'vacunacion': False,
        'enfermedad_grave': True,
    }
}

r50 = {
    'diagnostico': NO_APTO_SISTEMA_INMUNOLOGICO,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlada': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.NORMAL,
        'covid': False,
        'vacunacion': False,
        'enfermedad_grave': True,
    }
}

r51 = {
    'diagnostico': APTO_PARTICIPAR,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.NORMAL,
        'covid': False,
        'vacunacion': False,
        'enfermedad_grave': False,
    }
}

r52 = {
    'diagnostico': APTO_PARTICIPAR,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': False,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.NORMAL,
        'covid': False,
        'vacunacion': False,
        'enfermedad_grave': False,
    }
}

r53 = {
    'diagnostico': APTO_PARTICIPAR,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.MASCULINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlada': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.NORMAL,
        'covid': False,
        'vacunacion': False,
        'enfermedad_grave': False,
    }
}

r54 = {
    'diagnostico': APTO_PARTICIPAR,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_actual': False,
        'embarazo_planificado': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.OTROS,
        'enfermedad_patologica': True,
        'controlada': True,
        'examen_fisico': ExamenFisico.NORMAL,
        'auscultacion_respiratoria': AuscultacionRespiratoria.NORMAL,
        'auscultacion_cardiaca': AuscultacionCardiaca.NORMAL,
        'pulso': Pulso.NORMAL,
        'covid': False,
        'vacunacion': False,
        'enfermedad_grave': False,
    }
}

r55 = {
    'diagnostico': NO_APTO_PRESERVATIVO,
    'sintomas': {
        'edad': Edad.APTO,
        'sexo': Sexo.FEMENINO,
        'embarazo_planificado': False,
        'embarazo_actual': False,
        'metodo_anticonceptivo': MetodoAnticonceptivo.PRESERVATIVO
    }
}

class Paciente():
    def __init__(self):
        self.sintomas = {}

    def agregar_sintoma(self, key, value):
        if key in SINTOMAS:
            self.sintomas[key] = value


class ConocimientoMedico():

    def __init__(self):
        self.reglas = [r1, r2, r3, r4, r5, r55, r6, r7, r8, r9, r10, r11, r12, r13,
                       r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24,
                       r25, r26, r27, r28, r29, r30, r31, r32, r33, r34, r35,
                       r36, r37, r38, r39, r40, r41, r42, r43, r44, r45, r46,
                       r47, r48, r49, r50, r51, r52, r53, r54]
        self.sintomas = SINTOMAS
        self.diagnosticos = DIAGNOSTICOS

    def get_diagnose_for_rule(self, ruleidx):
        return self.reglas[ruleidx]['diagnostico']
