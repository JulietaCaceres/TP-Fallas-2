from engine.responses import Edad, Sexo, MetodoAnticonceptivo,\
    ExamenFisico, AuscultacionRespiratoria,\
    AuscultacionCardiaca, Pulso
from engine.frames import VolunteerFrame, WomanVolunteerFrame, FrameTree
from engine.evaluations import *

f0 = VolunteerFrame(edad=Edad.MENOR, evaluation=NO_APTO_MENOR_EDAD)
f1 = VolunteerFrame(edad=Edad.MAYOR, evaluation=NO_APTO_MAYOR_EDAD)
f2 = WomanVolunteerFrame(embarazo_actual=True, evaluation=NO_APTO_DURANTE_EMBARAZO)
f3 = WomanVolunteerFrame(embarazo_planificado=True, evaluation=NO_APTO_PLANIFICA_EMBARAZO)
f4 = WomanVolunteerFrame(metodo_anticonceptivo=MetodoAnticonceptivo.NO_USA, evaluation=NO_APTO_SIN_METODO_ANTICONCEPTIVO)
f5 = WomanVolunteerFrame(metodo_anticonceptivo=MetodoAnticonceptivo.PRESERVATIVO, evaluation=RECALL_METODO_EFECTIVO)
f6 = VolunteerFrame(examen_fisico=ExamenFisico.GRAVE, evaluation=NO_APTO_CONDICION_FISICA_GRAVE)
f7 = VolunteerFrame(auscultacion_respiratoria=AuscultacionRespiratoria.GRAVE, evaluation=NO_APTO_CONDICION_RESPIRATORIA_GRAVE)
f8 = VolunteerFrame(auscultacion_cardiaca=AuscultacionCardiaca.GRAVE, evaluation=NO_APTO_CONDICION_CARDIACA_GRAVE)
f9 = VolunteerFrame(pulso=Pulso.GRAVE, evaluation=NO_APTO_PULSO_GRAVE)
f10 = VolunteerFrame(examen_fisico=ExamenFisico.INTERMEDIO, evaluation=RECALL_CONDICION_MEJORA)
f11 = VolunteerFrame(auscultacion_respiratoria=AuscultacionRespiratoria.INTERMEDIO, evaluation=RECALL_CONDICION_MEJORA)
f12 = VolunteerFrame(auscultacion_cardiaca=AuscultacionCardiaca.INTERMEDIO, evaluation=RECALL_CONDICION_MEJORA)
f13 = VolunteerFrame(pulso=Pulso.INTERMEDIO, evaluation=RECALL_CONDICION_MEJORA)
f14 = VolunteerFrame(covid=True, evaluation=NO_APTO_PASADO_COVID)
f15 = VolunteerFrame(vacunacion=True, evaluation=NO_APTO_VACUNADO_COVID)
f16= VolunteerFrame(enfermedad_grave=True, evaluation=NO_APTO_SISTEMA_INMUNOLOGICO)
f17 = VolunteerFrame(enfermedad_patologica=True, controlada=False, evaluation=RECALL_NO_CONTROLADA)

class InferenceEngine():

    def __init__(self):
        self.conocimiento = FrameTree(volunteer_instances=[f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17])

    def get_evaluation_for_volunteer(self, volunteer_data):
        result = self.conocimiento.eval(volunteer_data)
        print("resultado: ", result)
        return result
