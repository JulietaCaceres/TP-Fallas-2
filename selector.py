from experta import *
from responses import *
from typing import Optional


class Voluntarie(Fact):
    def __init__(self,
                edad: Optional[Edad] = None,
                sexo: Optional[Sexo] = None,
                embarazo_actual: Optional[bool] = None,
                embarazo_planificado: Optional[bool] = None,
                metodo_anticonceptivo: Optional[MetodoAnticonceptivo] = None,
                examen_fisico: Optional[ExamenFisico] = None,
                enfermedad_patologica: Optional[bool] = None,
                controlada: Optional[bool] = None,
                auscultacion_respiratoria : Optional[AuscultacionRespiratoria] = None,
                auscultacion_cardiaca: Optional[AuscultacionCardiaca] = None,
                pulso: Optional[Pulso] = None,
                covid: Optional[Pulso] = None,
                vacunacion: Optional[Pulso] = None,
                enfermedad_grave: Optional[Pulso] = None,
                ):
        attrs = dict(edad=edad, sexo=sexo, embarazo_actual=embarazo_actual, embarazo_planificado=embarazo_planificado,
                     metodo_anticonceptivo=metodo_anticonceptivo, enfermedad_patologica=enfermedad_patologica,
                     controlada=controlada, examen_fisico=examen_fisico, auscultacion_respiratoria=auscultacion_respiratoria,
                     auscultacion_cardiaca=auscultacion_cardiaca, pulso=pulso, covid=covid, vacunacion=vacunacion, enfermedad_grave=enfermedad_grave )
        super().__init__(**{k:v for k,v in attrs.items() if v is not None})


class Selector(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.response = "No se puede determinar la enfermedad con los datos de entrada"

    @Rule(Voluntarie(edad=Edad.MENOR
                     )
          )
    def R1_No_Apto_edad_menor(self):
        self.response = "NO APTO: No puede realizar prueba si es menor de edad"

    @Rule(Voluntarie(edad=Edad.MAYOR
                     )
          )
    def R1_No_Apto_edad_mayor(self):
        self.response = "NO APTO: No puede realizar prueba si es mayor de edad"


    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                     embarazo_actual=True
                     )
          )
    def R1_No_Apto(self):
        self.response = "NO APTO: No puede realizar prueba durante el embarazo"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                     embarazo_actual=False,
                     embarazo_planificado=True
                     )
          )
    def R2_No_Apto(self):
        self.response = "NO APTO: No puede realizar la prueba si esta planificando un embarazo."

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                     embarazo_actual=False,
                     embarazo_planificado=False,
                     metodo_anticonceptivo=MetodoAnticonceptivo.NO_USA
                     )
          )
    def R3_No_Apto(self):
        self.response = "NO APTO: No puede realizar la prueba si no usa métodos anticonceptivos."

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                     embarazo_actual=False,
                     embarazo_planificado=False,
                     metodo_anticonceptivo=MetodoAnticonceptivo.PRESERVATIVO
                     )
          )
    def R4_Recall(self):
        self.response = "RECALL: Si incorpora otro metodo mas efectivo, se le llamara a futuro."


    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.GRAVE
                    )
          )
    def R5_Recall(self):
        self.response = "NO APTO: Condición física grave"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.GRAVE
                    )
          )
    def R6_Recall(self):
        self.response = "NO APTO: Condición física grave"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.INTERMEDIO
                    )
        )
    def R7_Recall(self):
        self.response = "RECALL: Si su condición mejora se le volverá a llamar"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                     embarazo_actual=False,
                     embarazo_planificado=False,
                     metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                     enfermedad_patologica=False,
                     examen_fisico=ExamenFisico.INTERMEDIO
                     )
          )
    def R8_Recall(self):
        self.response = "RECALL: Si su condición mejora se le volverá a llamar"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=False
                    )
          )
    def R9_Recall(self):
        self.response = "RECALL: No puede realizar la prueba si tiene una enfermedad o patología no controlada."

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=False
                    )
          )
    def R10_Recall(self):
        self.response = "RECALL: No puede realizar la prueba si tiene una enfermedad o patología no controlada"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                     embarazo_actual=False,
                     embarazo_planificado=False,
                     metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                     enfermedad_patologica=True,
                     controlada=True,
                     examen_fisico=ExamenFisico.GRAVE
                     )
          )
    def R11_Recall(self):
        self.response = "NO APTO: Condición física grave"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                     embarazo_actual=False,
                     embarazo_planificado=False,
                     metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                     enfermedad_patologica=True,
                     controlada=True,
                     examen_fisico=ExamenFisico.GRAVE
                     )
          )
    def R12_Recall(self):
        self.response = "NO APTO: Condición física grave"


    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.INTERMEDIO
                    )
        )
    def R13_Recall(self):
        self.response = "RECALL: Si su condición mejora se le volverá a llamar"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.INTERMEDIO
                    )
          )
    def R14_Recall(self):
        self.response = "RECALL: Si su condición mejora se le volverá a llamar"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.GRAVE
                    )
        )
    def R15_Recall(self):
        self.response = "NO APTO: Condición respiratoria grave"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.GRAVE
                    )
        )
    def R16_Recall(self):
        self.response = "NO APTO: Condición respiratoria grave"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.INTERMEDIO
                    )
        )
    def R17_Recall(self):
        self.response = "RECALL: Si su condición mejora se le volverá a llamar"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.INTERMEDIO
                    )
        )
    def R18_Recall(self):
        self.response = "RECALL: Si su condición mejora se le volverá a llamar" 

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.GRAVE
                    )
          )
    def R19_Recall(self):
        self.response = "NO APTO: Condición respiratoria grave"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.GRAVE
                    )
          )
    def R20_Recall(self):
        self.response = "NO APTO: Condición respiratoria grave"


    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.INTERMEDIO
                    )
          )
    def R21_Recall(self):
        self.response = "RECALL: Si su condición mejora se le volverá a llamar"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.INTERMEDIO
                    )
          )
    def R22_Recall(self):
        self.response = "RECALL: Si su condición mejora se le volverá a llamar"


    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.GRAVE
                    )
        )
    def R23_Recall(self):
        self.response = "NO APTO: Condición cardiaca grave"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.GRAVE
                    )
        )
    def R24_Recall(self):
        self.response = "NO APTO: Condición cardiaca grave"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.INTERMEDIO
                    )
        )
    def R25_Recall(self):
        self.response = "RECALL9: Si su condición mejora se le volverá a llamar"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.INTERMEDIO
                    )
        )
    def R26_Recall(self):
        self.response = "RECALL: Si su condición mejora se le volverá a llamar"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.GRAVE
                    )
          )
    def R27_Recall(self):
        self.response = "NO APTO: Condición cardíaca grave"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.GRAVE
                    )
          )
    def R28_Recall(self):
        self.response = "NO APTO: Condición cardíaca grave"


    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.INTERMEDIO
                    )
          )
    def R29_Recall(self):
        self.response = "RECALL: Si su condición mejora se le volverá a llamar"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.INTERMEDIO
                    )
          )
    def R30_Recall(self):
        self.response = "RECALL: Si su condición mejora se le volverá a llamar"


    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.GRAVE
                    )
        )
    def R31_Recall(self):
        self.response = "NO APTO: Pulso grave"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.GRAVE
                    )
        )
    def R32_Recall(self):
        self.response = "NO APTO: Pulso grave"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.INTERMEDIO
                    )
        )
    def R33_Recall(self):
        self.response = "RECALL: Si su condición mejora se le volverá a llamar"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.INTERMEDIO
                    )
        )
    def R34_Recall(self):
        self.response = "RECALL: Si su condición mejora se le volverá a llamar"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.GRAVE
                    )
          )
    def R35_Recall(self):
        self.response = "NO APTO: Pulso grave"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.GRAVE
                    )
          )
    def R36_Recall(self):
        self.response = "NO APTO: Pulso grave"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.INTERMEDIO
                    )
          )
    def R37_Recall(self):
        self.response = "RECALL: Si su condición mejora se le volverá a llamar"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.INTERMEDIO
                    )
          )
    def R38_Recall(self):
        self.response = "RECALL: Si su condición mejora se le volverá a llamar"

# covid: no enfermedad covid si

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=True
                    )
        )
    def R39_Recall(self):
        self.response = "NO APTO: No se puede realizar el estudio si ya tuvo COVID"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=True
                    )
        )
    def R40_Recall(self):
        self.response = "NO APTO: No se puede realizar el estudio si ya tuvo COVID"

# covid: si enfermedad covid si

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=True
                    )
          )
    def R41_Recall(self):
        self.response = "NO APTO: No se puede realizar el estudio si ya tuvo COVID"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=True
                    )
          )
    def R42_Recall(self):
        self.response = "NO APTO: No se puede realizar el estudio si ya tuvo COVID"

# vacunacion: no enfermedad vac si

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=False,
                    vacunacion=True
                    )
        )
    def R43_Recall(self):
        self.response = "NO APTO: No puede participar del estudio si ya tiene una vacuna"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=False,
                    vacunacion=True
                    )
        )
    def R44_Recall(self):
        self.response = "NO APTO: No puede participar del estudio si ya tiene una vacuna"


    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=False,
                    vacunacion=True
                    )
          )
    def R45_Recall(self):
        self.response = "NO APTO: Fue vacunade anteriormente"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=False,
                    vacunacion=True
                    )
          )
    def R46_Recall(self):
        self.response = "NO APTO: Fue vacunade anteriormente"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=False,
                    vacunacion=False,
                    enfermedad_grave=True
                    )
        )
    def R47_Recall(self):
        self.response = "NO APTO: Tiene enfermedad grave que compromete al sistema inmunológico"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=False,
                    vacunacion=False,
                    enfermedad_grave=True
                    )
        )
    def R48_Recall(self):
        self.response = "NO APTO: Tiene enfermedad grave que compromete al sistema inmunológico"

# enfermedad grave: si enf grave si

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=False,
                    vacunacion=False,
                    enfermedad_grave=True
                    )
          )
    def R49_Recall(self):
        self.response = "NO APTO: Tiene enfermedad grave que compromete al sistema inmunológico"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=False,
                    vacunacion=False,
                    enfermedad_grave=True
                    )
          )
    def R50_Recall(self):
        self.response = "NO APTO: Tiene enfermedad grave que compromete al sistema inmunológico"

#aptos finales

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=False,
                    vacunacion=False,
                    enfermedad_grave=False
                    )
        )
    def R51_Recall(self):
        self.response = "APTO: Puede participar en el estudio"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=False,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=False,
                    vacunacion=False,
                    enfermedad_grave=False
                    )
        )
    def R52_Recall(self):
        self.response = "APTO: Puede participar en el estudio"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.MASCULINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=False,
                    vacunacion=False,
                    enfermedad_grave=False
                    )
          )
    def R53_Recall(self):
        self.response = "APTO: Puede participar en el estudio"

    @Rule(Voluntarie(edad=Edad.APTO, sexo=Sexo.FEMENINO,
                    embarazo_actual=False,
                    embarazo_planificado=False,
                    metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                    enfermedad_patologica=True,
                    controlada=True,
                    examen_fisico=ExamenFisico.NORMAL,
                    auscultacion_respiratoria=AuscultacionRespiratoria.NORMAL,
                    auscultacion_cardiaca=AuscultacionCardiaca.NORMAL,
                    pulso=Pulso.NORMAL,
                    covid=False,
                    vacunacion=False,
                    enfermedad_grave=False
                    )
          )
    def R54_Recall(self):
        self.response = "APTO: Puede participar en el estudio"