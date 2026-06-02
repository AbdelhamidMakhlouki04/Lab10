from database.DB_connect import DBConnect
from model.contiguity import Contiguity,Country


class DAO():
    @staticmethod
    def get_archi(anno):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
            SELECT c1.state1no,p1.StateNme AS nome1,c1.state2no,p2.StateNme AS nome2
            FROM contiguity c1
            JOIN country p1 ON c1.state1no = p1.CCode
            JOIN country p2 ON c1.state2no = p2.CCode
            WHERE year<=%s AND conttype=1
            """
            cursor.execute(query,(anno,))
            for row in cursor:
                result.append(Contiguity(
                    row["state1no"],row["nome1"],row["state2no"],row["nome2"]))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_country():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
            SELECT *
            FROM country
            """
            cursor.execute(query,)
            for row in cursor:
                result.append(Country(
                    row["StateAbb"], row["CCode"], row["StateNme"]))
            cursor.close()
            cnx.close()
        return result
