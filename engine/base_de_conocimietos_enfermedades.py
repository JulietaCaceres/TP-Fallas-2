from responses import Edad

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


class Paciente():
    def __init__(self):
        self.sintomas = {}

    def agregar_sintoma(self, key, value):
        if key in SINTOMAS:
            self.sintomas[key] = value


class ConocimientoMedico():

    def __init__(self):
        self.reglas = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10]
        self.sintomas = SINTOMAS
        self.diagnosticos = DIAGNOSTICOS

    def get_diagnose_for_rule(self, ruleidx):
        return self.reglas[ruleidx]['diagnostico']
