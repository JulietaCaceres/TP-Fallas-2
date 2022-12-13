from engine.responses import Edad, Sexo, MetodoAnticonceptivo,\
    ExamenFisico, AuscultacionRespiratoria,\
    AuscultacionCardiaca, Pulso
from engine.frames import VolunteerFrame, WomanVolunteerFrame, FrameTree
from engine.evaluations import *

v1 = WomanVolunteerFrame(embarazo_actual=True, evaluation=NO_APTO_DURANTE_EMBARAZO)
v2 = WomanVolunteerFrame(embarazo_planificado=True, evaluation=NO_APTO_PLANIFICA_EMBARAZO)
v3 = WomanVolunteerFrame(metodo_anticonceptivo=MetodoAnticonceptivo.NO_USA, evaluation=NO_APTO_SIN_METODO_ANTICONCEPTIVO)
v4 = WomanVolunteerFrame(metodo_anticonceptivo=MetodoAnticonceptivo.PRESERVATIVO, evaluation=RECALL_METODO_EFECTIVO)
v5 = VolunteerFrame(examen_fisico=ExamenFisico.GRAVE, evaluation=NO_APTO_CONDICION_FISICA_GRAVE)
v6 = VolunteerFrame(auscultacion_respiratoria=AuscultacionRespiratoria.GRAVE, evaluation=NO_APTO_CONDICION_RESPIRATORIA_GRAVE)
v7 = VolunteerFrame(auscultacion_cardiaca=AuscultacionCardiaca.GRAVE, evaluation=NO_APTO_CONDICION_CARDIACA_GRAVE)
v8 = VolunteerFrame(pulso=Pulso.GRAVE, evaluation=NO_APTO_PULSO_GRAVE)
v9 = VolunteerFrame(examen_fisico=ExamenFisico.INTERMEDIO, evaluation=RECALL_CONDICION_MEJORA)
v10 = VolunteerFrame(auscultacion_respiratoria=AuscultacionRespiratoria.INTERMEDIO, evaluation=RECALL_CONDICION_MEJORA)
v11 = VolunteerFrame(auscultacion_cardiaca=AuscultacionCardiaca.INTERMEDIO, evaluation=RECALL_CONDICION_MEJORA)
v12 = VolunteerFrame(pulso=Pulso.INTERMEDIO, evaluation=RECALL_CONDICION_MEJORA)
v13 = VolunteerFrame(covid=True, evaluation=NO_APTO_PASADO_COVID)
v14 = VolunteerFrame(vacunacion=True, evaluation=NO_APTO_VACUNADO_COVID)
v15= VolunteerFrame(enfermedad_grave=True, evaluation=NO_APTO_SISTEMA_INMUNOLOGICO)
v16 = VolunteerFrame(enfermedad_patologica=True, controlada=False, evaluation=RECALL_NO_CONTROLADA)

class InferenceEngine():

    def __init__(self):
        self.conocimiento = FrameTree(volunteer_instances=[v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16])
    def get_evaluation_for_volunteer(self, volunteer_data):
        result = self.conocimiento.eval(volunteer_data)
        print("resultado: ", result)
        return result
