import json
import requests

from .model_fipe import ConsultarMarcas


class Fipe:
    codigo_tabela_referencia = "300"

    def __init__(
        self,
        codigo_tipo_veiculo: int = None,
        codigo_marca: int = None,
        codigo_modelo: int = None,
    ):
        self.codigo_tipo_veiculo = codigo_tipo_veiculo
        self.codigo_marca = codigo_marca
        self.codigo_modelo = codigo_modelo

    def consultar_marcas(self):
        try:
            response = requests.post(
                "https://veiculos.fipe.org.br/api/veiculos/ConsultarMarcas",
                data=ConsultarMarcas(
                    codigoTabelaReferencia=self.codigo_tabela_referencia,
                    codigoTipoVeiculo=self.codigo_tipo_veiculo,
                ).model_dump(),
            )
            print(response.text)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def buscar_modelo_pela_marca(self):
        pass

    def buscar_carros_modelos(self):
        pass

    def buscar_carro_dados_completos(self):
        pass
