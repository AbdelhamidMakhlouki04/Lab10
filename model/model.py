import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo=None

    def crea_grafo(self,soglia):
        archi=DAO.get_archi(soglia)
        country=DAO.get_country()
        grafo=nx.Graph()
        for i in country:
            grafo.add_node(i.StateNme)
        for i in archi:
            grafo.add_edge(i.nome1,i.nome2)

        self.grafo=grafo
        return grafo

    def crea_elenco(self):
        elenco=""
        grafo_ordinato = sorted(self.grafo.nodes())

        for nodo in grafo_ordinato:
            vicini=list(self.grafo.neighbors(nodo))
            grado=self.grafo.degree(nodo)

            elenco += f"{nodo} -- {grado} -- {vicini}\n"
        return elenco

    def numero_componenti(self):
        return nx.number_connected_components(self.grafo)

    def getCountry(self):
        return DAO.get_country()

    def get_raggiungibili(self,stato):
        raggiungibili= list(nx.node_connected_component(self.grafo,stato))
        elenco=""
        for i in raggiungibili:
            elenco += f"{i}\n"
        return elenco

