from pydantic import BaseModel


class ConsultarMarcas(BaseModel):
    codigoTabelaReferencia: int
    codigoTipoVeiculo: int
