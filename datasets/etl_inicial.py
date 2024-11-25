import pandas as pd

path_arq_orig = "Instalacao_Origem.csv"
path_arq_dest = "Instalacao_Destino.csv"

arq_sep = ";"

pais_ua = "UCRANIA"
pais_rus = "RUSSIA"
porto_santos = "Santos"

ano_min = 2018
ano_max = 2023

# Portos de origem e destino:
df_orig = pd.read_csv(path_arq_orig, sep=arq_sep, usecols=["Origem", "Origem Nome", "CDBigramaOrigem"])
df_dest = pd.read_csv(path_arq_dest, sep=arq_sep, usecols=["Destino", "Nome Destino", "CDBigramaDestino"])

#
# Ucrânia ou Rússia de Santos
#
def santos_importacao():
    df_carga_mestre = pd.DataFrame()  # Contera todos os anos
    print("Importações de Santos de Ucrânia e Rússia!")
    path_file = "df_rus_ua_psantos.csv"

    dtype_dict = pd.read_pickle("aux_carga_dtypes.pkl").to_dict()

    cod_santos = df_dest[(df_dest["Nome Destino"] == porto_santos)]["Destino"]

    # Arquivos de carga
    for ano in range(ano_min, ano_max + 1):
        path_arq_carg = f"datasets/{ano}Carga.csv"
        df_carga = pd.read_csv(path_arq_carg, sep=arq_sep, decimal=",", dtype=dtype_dict)
        print(f"Dados brutos de {ano} carregados!")
        # Adição da coluna de ano para cada ano correspondente
        df_carga["Ano"] = ano

        #
        # Destino e Origem
        #
        # Destino == Código de Santos
        df_carga = df_carga[df_carga["Destino"] == cod_santos.iloc[0]]
        df_carga = df_carga.merge(df_orig.loc[:, ["CDBigramaOrigem", "Origem"]], how="left", on="Origem")
        
        df_carga["Origem"] = df_carga["CDBigramaOrigem"]
        df_carga.drop("CDBigramaOrigem", axis=1, inplace=True)

        # Ucrânia ou Rússia
        df_carga = df_carga[(df_carga["Origem"] == "UA") | (df_carga["Origem"] == "RU")]

        # Retira-se cargas vazias
        df_carga = df_carga[df_carga["ConteinerEstado"] != "Vazio"]

        # Filtra para Ucrânia ou Rússia e Santos
        df_carga_mestre = pd.concat([df_carga_mestre, df_carga], ignore_index=True)
        # print(df_carga_mestre)

    # Exporta para arquivo .csv
    df_carga_mestre.to_csv(path_file, index=False)
    print(f"Arquivo {path_file} criado!")


santos_importacao()