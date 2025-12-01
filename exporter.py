import  requests 
import  json
import  time
from prometheus_client import start_http_server, Gauge


url_numero_pessoas = "http://api.open-notify.org/astros.json"

def pega_numero_astronautas():
    try:
        """
        Pegar o número de astronautas que estão no espaco!
        """
        response = requests.get(url_numero_pessoas)
        data = response.json()
        return data['number']
    except Exception as e:
        print("Tivemos problemas para acessar a URL")
        raise e

def atualiza_metricas():
    try:
        """
        Atualiza as metricas com o numero de astronautas no espaco!
        """
        numero_pessoas = Gauge ('numero_de_astronautas', 'Numero de astronautas no espaco')
        while True:
            numero_pessoas.set(pega_numero_astronautas())
            time.sleep(10)
            print("O numero de astronautas nesse momento é %s" % pega_numero_astronautas())
    except Exception as e:
        print("Tivemos problemas ao atualizar as méticas!")
        raise e
    
def inicia_exporter():
    try:
        """
        Inicia o http server
        """
    
        start_http_server(8899)
        return True
    except Exception as e:
        print("Tivemos problemas em iniciar o http server!")
        raise e

def main():
    """
    Funcao principal que ira chamar as demais.
    """
    try:
        inicia_exporter()
        print("HTTP Server iniciado")
        atualiza_metricas()
    except Exception as e:
        print("Tivemos um problema na inicializacão do nosso exporter")
        exit(1)

if __name__ == '__main__':
    main()
    exit(0)