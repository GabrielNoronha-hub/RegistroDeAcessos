import os
import csv
import subprocess

def obter_informacoes_seguranca(caminho_da_pasta, arquivo_saida):
    try:
        with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Arquivo/Pasta', 'Informações de Segurança'])

            for pasta_atual, subpastas, arquivos in os.walk(caminho_da_pasta):
                for item in subpastas + arquivos:
                    caminho_completo = os.path.join(pasta_atual, item)

                    result = subprocess.check_output(['icacls', caminho_completo], shell=True).decode('cp1252')
                    csv_writer.writerow([caminho_completo, result])

    except FileNotFoundError:
        print(f"A pasta '{caminho_da_pasta}' não foi encontrada.")
    except PermissionError:
        print(f"Sem permissão para acessar '{caminho_da_pasta}'.")

caminho_da_pasta = "X:\\"
arquivo_saida = "informacoes_seguranca.csv"
obter_informacoes_seguranca(caminho_da_pasta, arquivo_saida)