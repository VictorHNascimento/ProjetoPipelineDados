import json
import csv

class Dados:

    def __init__(self, dados):
        self.dados = dados
        self.nome_colunas = self.__Recebe_Colunas()
        self.qtde_linhas = self.__Tamanho_Dados()

    def __Leitura_JSON(path):
        with open(path, 'r') as file:
            dados_json = json.load(file)

        return dados_json

    def __Leitura_CSV(path):
        dados_csv = []
        with open(path, 'r') as file:
            spanreader =  csv.DictReader(file, delimiter=',')
            for row in spanreader:
                dados_csv.append(row)
        return dados_csv

    @classmethod
    def Leitura_Dados(cls, path, tipo_dado):
        dados = []
        if tipo_dado == '.csv':
            dados = cls.__Leitura_CSV(path)

        elif tipo_dado == '.json':
            dados = cls.__Leitura_JSON(path)

        return cls(dados)

    def __Recebe_Colunas(self):
        return list(self.dados[-1].keys())

    def Renomeia_Colunas(self, key_mapping):
        dados_novos = []

        for old in self.dados:
            dict_temp = {}
            for key, value in old.items():
                dict_temp[key_mapping[key]] = value
            dados_novos.append(dict_temp)

        self.dados = dados_novos
        self.nome_colunas = self.__Recebe_Colunas()

    def __Tamanho_Dados(self):
        return len(self.dados)

    def Unificacao_Dados(dadosA, dadosB):
        dados_unificados = []
        dados_unificados.extend(dadosA.dados)
        dados_unificados.extend(dadosB.dados)
        return Dados(dados_unificados)

    def __Tabelando_Dados(self):
        dados_tabela =  [self.nome_colunas]

        for row in self.dados:
            l = []
            for c in self.nome_colunas:
                l.append(row.get(c, 'Indisponivel'))
            dados_tabela.append(l)
        return dados_tabela

    def Salvando_Dados(self, path):
        try:
            dados_tabela = self.__Tabelando_Dados()
            with open(path, 'w') as file:
                writer= csv.writer(file)
                writer.writerows(dados_tabela)
            print('Salvo com sucesso!')
            print(f'Caminho do Arquivo: {path}')
        except:
            print('Ocorreu um erro ao salvar o arquivo')
