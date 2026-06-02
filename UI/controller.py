import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        soglia = int(self._view._txtAnno.value)
        self._view._txt_result.controls.clear()

        self._model.crea_grafo(soglia)
        num_componenti = self._model.numero_componenti()
        elenco=self._model.crea_elenco()

        self._view._txt_result.controls.append(ft.Text(f"Grafo correttamente creato.\nIl grafo ha {num_componenti} componenti connesse\nDi seguito il dettaglio sui nodi:"))
        self._view._txt_result.controls.append(ft.Text(elenco))
        self._view.update_page()

    def handleRaggiungibili(self, e):
        self._view._txt_result.controls.clear()
        stato=str(self._view.txtPaese.value)

        elenco=self._model.get_raggiungibili(stato)
        self._view._txt_result.controls.append(ft.Text(elenco))
        self._view.update_page()

    def load_campi(self):
        country=self._model.getCountry()
        lista=[]
        for i in country:
            lista.append(i.StateNme)
        lista_ord=sorted(lista)
        self._view.set_campi(lista_ord)


