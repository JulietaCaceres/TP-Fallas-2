from engine.responses import Sexo
class FrameTree:
    def __init__(self, volunteer_instances):
        self.volunteer_instances = volunteer_instances
        print("instances: ", volunteer_instances)

    def eval(self, volunteer_data):
        for volunteer_instance in self.volunteer_instances:
            if volunteer_instance.es(volunteer_data):
                print("volunteer_instance: ", volunteer_instance)
                return volunteer_instance.evaluation
        return "Apto para realizar la prueba"

class VolunteerFrame:
    def __init__(self, sex=Sexo.MASCULINO, enfermedad_patologica=None, controlada=None, examen_fisico=None, auscultacion_respiratoria=None,
                 auscultacion_cardiaca=None, pulso=None, covid=None, vacunacion=None, enfermedad_grave=None, evaluation=None):
        self.sex = sex
        self.enfermedad_patologica = enfermedad_patologica
        self.controlada = controlada
        self.examen_fisico = examen_fisico
        self.auscultacion_respiratoria = auscultacion_respiratoria
        self.auscultacion_cardiaca = auscultacion_cardiaca
        self.pulso = pulso
        self.covid = covid
        self.vacunacion = vacunacion
        self.enfermedad_grave = enfermedad_grave
        self.evaluation = evaluation


    def __repr__(self):
        return f"""
        sex = {self.sex}
        enfermedad_patologica = {self.enfermedad_patologica}
        controlada = {self.controlada}
        examen_fisico = {self.examen_fisico}
        auscultacion_respiratoria = {self.auscultacion_respiratoria}
        auscultacion_cardiaca = {self.auscultacion_cardiaca}
        pulso = {self.pulso}
        covid = {self.covid}
        vacunacion = {self.vacunacion}
        enfermedad_grave = {self.enfermedad_grave}
        evaluation = {self.evaluation}
        """

    def es(self, volunteer_data):
        return ((not self.enfermedad_grave) or self.enfermedad_grave == volunteer_data["enfermedad_grave"]) and \
                  ((not self.vacunacion) or self.vacunacion == volunteer_data["vacunacion"]) and \
                    ((not self.covid) or self.covid == volunteer_data["covid"]) and \
                        ((not self.pulso) or self.pulso == volunteer_data["pulso"]) and \
                            ((not self.auscultacion_cardiaca) or self.auscultacion_cardiaca == volunteer_data["auscultacion_cardiaca"]) and \
                                ((not self.auscultacion_respiratoria) or self.auscultacion_respiratoria == volunteer_data["auscultacion_respiratoria"]) and \
                                    ((not self.examen_fisico) or self.examen_fisico == volunteer_data["examen_fisico"]) and \
                                            ((not self.enfermedad_patologica) or (self.enfermedad_patologica == volunteer_data["enfermedad_patologica"] and  self.controlada == volunteer_data["controlada"]))



class WomanVolunteerFrame(VolunteerFrame):
    def __init__(self, sex=Sexo.FEMENINO, enfermedad_patologica=None, controlada=None, examen_fisico=None, auscultacion_respiratoria=None,
                 auscultacion_cardiaca=None, pulso=None, covid=None, vacunacion=None, enfermedad_grave=None, embarazo_actual=None, embarazo_planificado=None,
                 metodo_anticonceptivo=None, evaluation=None):

        super().__init__(sex, enfermedad_patologica, controlada, examen_fisico, auscultacion_respiratoria,
                         auscultacion_cardiaca, pulso, covid, vacunacion, enfermedad_grave, evaluation)
        self.embarazo_actual = embarazo_actual
        self.embarazo_planificado = embarazo_planificado
        self.metodo_anticonceptivo = metodo_anticonceptivo

    def es(self, volunteer_data):
        return (((not self.embarazo_actual) or (self.embarazo_actual == volunteer_data["embarazo_actual"])) \
               and ((not self.embarazo_planificado) or (self.embarazo_planificado == volunteer_data["embarazo_planificado"])) \
               and ((not self.metodo_anticonceptivo) or (self.metodo_anticonceptivo == volunteer_data["metodo_anticonceptivo"]))) \

    def __repr__(self):
        return f"""
        sex = {self.sex}
        enfermedad_patologica = {self.enfermedad_patologica}
        controlada = {self.controlada}
        examen_fisico = {self.examen_fisico}
        auscultacion_respiratoria = {self.auscultacion_respiratoria}
        auscultacion_cardiaca = {self.auscultacion_cardiaca}
        pulso = {self.pulso}
        covid = {self.covid}
        vacunacion = {self.vacunacion}
        enfermedad_grave = {self.enfermedad_grave}
        evaluation = {self.evaluation}
        embarazo_actual = {self.embarazo_actual}
        embarazo_planificado = {self.embarazo_planificado}
        metodo_anticonceptivo = {self.metodo_anticonceptivo}
        """