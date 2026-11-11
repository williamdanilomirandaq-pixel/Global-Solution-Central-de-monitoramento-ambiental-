# Central de Monitoramento Ambiental da Comunidade
# Trabalho de Computational Thinking for Engineering - 2º semestre de 2026
# Grupo: William, Matheus Luiz e Mateus Pedro

# AMBIENTE ESCOLHIDO
# Entorno de uma escola fictícia em São Paulo - SP, com educação infantil,
# ensino fundamental e ensino médio. A região é urbana, com comércio e
# movimentação de carros, ônibus e pedestres. Os alunos entram e saem nos
# horários de aula e, no recreio, ficam em uma área a céu aberto dentro da escola.
#
# FINALIDADE DO MONITORAMENTO
# Identificar situações que demandem atenção em um espaço frequentado por
# crianças e jovens. Observamos temperatura (conforto nas atividades ao ar
# livre), partículas PM2,5 (qualidade do ar respirado) e ruído (condições
# adequadas para convivência e aprendizagem).

# LIMITES UTILIZADOS NA SIMULAÇÃO
# Temperatura: de 18 °C até 30 °C.
# Essa faixa foi definida pelo grupo como um critério didático de atenção.
# Não é um limite oficial universal para temperatura em áreas externas.
#
# PM2,5: máximo de 15 µg/m³, considerando a média de 24 horas.
# Referência: Diretrizes de qualidade do ar da OMS (2021) e valor-guia
# final (PF) apresentado na Resolução CONAMA nº 506/2024.
# Atenção: o valor de 15 µg/m³ é uma referência de saúde/guia final.
# A resolução brasileira prevê etapas intermediárias de implantação.
# PERÍODO DOS DADOS: cada valor de PM2,5 digitado representa a média de
# 24 horas da leitura. Assim, o valor simulado e o limite têm o mesmo período
# de referência e podem ser comparados.
#
# Ruído: máximo de 50 dB no período diurno.
# Referência: ABNT NBR 10151:2019, tabela 3, para áreas de escolas.
# A classificação exata depende do uso predominante e das regras locais.
# PERÍODO DOS DADOS: cada valor de ruído digitado representa o período diurno.
#
# Este programa é uma simulação didática. Não substitui medição técnica
# nem avaliação oficial das condições ambientais.

TEMP_MIN = 18
TEMP_MAX = 30
PM25_MAX = 15
RUIDO_MAX = 50


# Esta função calcula as três informações estatísticas de uma lista.
# Usamos a mesma função para temperatura, PM2,5 e ruído.
def calcular_estatisticas(valores):
    soma = 0

    for valor in valores:
        soma = soma + valor

    media = soma / len(valores)
    maior = max(valores)
    menor = min(valores)

    return media, maior, menor


# Aqui pedimos um número inteiro maior que zero para saber
# quantas leituras o usuário quer registrar.
def pedir_quantidade():
    while True:
        try:
            quantidade = int(input("Quantas leituras deseja registrar? "))

            if quantidade > 0:
                return quantidade
            else:
                print("Digite um número maior que zero.")

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


# Esta parte recebe os valores de cada leitura.
# Guardamos os três dados juntos em um dicionário dentro da lista.
# A lista é criada de novo a cada chamada, então uma nova análise
# nunca se mistura com a anterior.
def registrar_leituras():
    quantidade = pedir_quantidade()
    leituras = []

    for numero in range(1, quantidade + 1):
        print("\n--- Leitura", numero, "---")

        while True:
            try:
                temperatura = float(input("Leitura " + str(numero) + " - Temperatura (°C): "))
                break
            except ValueError:
                print("Digite um valor numérico para a temperatura.")

        while True:
            try:
                pm25 = float(input("Leitura " + str(numero) + " - Concentração de PM2,5 (µg/m³, média de 24 h): "))

                if pm25 >= 0:
                    break
                else:
                    print("A concentração não pode ser negativa.")
            except ValueError:
                print("Digite um valor numérico para o PM2,5.")

        while True:
            try:
                ruido = float(input("Leitura " + str(numero) + " - Nível de ruído (dB, período diurno): "))

                if ruido >= 0:
                    break
                else:
                    print("O nível de ruído não pode ser negativo.")
            except ValueError:
                print("Digite um valor numérico para o ruído.")

        leitura = {
            "numero": numero,
            "temperatura": temperatura,
            "pm25": pm25,
            "ruido": ruido
        }

        leituras.append(leitura)

    return leituras


# Nesta função conferimos cada parâmetro separadamente.
# Assim, uma mesma leitura pode apresentar mais de um alerta.
# Valores exatamente iguais aos limites ficam dentro da faixa.
def analisar_leituras(leituras):
    ocorrencias_temperatura = 0
    ocorrencias_pm25 = 0
    ocorrencias_ruido = 0
    leituras_criticas = 0

    for leitura in leituras:
        critica_na_leitura = False

        print("\nResultado da leitura", leitura["numero"], ":")

        if leitura["temperatura"] < TEMP_MIN or leitura["temperatura"] > TEMP_MAX:
            print("- Temperatura fora dos limites estabelecidos.")
            ocorrencias_temperatura = ocorrencias_temperatura + 1
            critica_na_leitura = True

        if leitura["pm25"] > PM25_MAX:
            print("- Concentração de PM2,5 acima do limite adotado.")
            ocorrencias_pm25 = ocorrencias_pm25 + 1
            critica_na_leitura = True

        if leitura["ruido"] > RUIDO_MAX:
            print("- Nível de ruído elevado em relação ao limite definido.")
            ocorrencias_ruido = ocorrencias_ruido + 1
            critica_na_leitura = True

        # Uma leitura com vários alertas conta só uma vez como crítica.
        if critica_na_leitura:
            leituras_criticas = leituras_criticas + 1
        else:
            print("Leitura dentro dos limites de referência estabelecidos.")

    return ocorrencias_temperatura, ocorrencias_pm25, ocorrencias_ruido, leituras_criticas


# Aqui juntamos os resultados, calculamos as médias e mostramos
# a classificação geral da sequência.
def gerar_resultados(leituras, ocorrencias_temperatura, ocorrencias_pm25,
                     ocorrencias_ruido, leituras_criticas):

    temperaturas = []
    valores_pm25 = []
    ruidos = []

    for leitura in leituras:
        temperaturas.append(leitura["temperatura"])
        valores_pm25.append(leitura["pm25"])
        ruidos.append(leitura["ruido"])

    media_temp, maior_temp, menor_temp = calcular_estatisticas(temperaturas)
    media_pm25, maior_pm25, menor_pm25 = calcular_estatisticas(valores_pm25)
    media_ruido, maior_ruido, menor_ruido = calcular_estatisticas(ruidos)

    total_leituras = len(leituras)
    percentual_critico = (leituras_criticas / total_leituras) * 100

    # Mais de 30% é atenção; exatamente 30% fica na segunda classificação.
    if percentual_critico > 30:
        classificacao = "Estado geral: condições ambientais de atenção, com frequência de ocorrências acima do critério estabelecido."
    else:
        classificacao = "Estado geral: frequência de ocorrências dentro do critério estabelecido para a simulação."

    print("\n -RESUMO DA ANÁLISE ")
    print("Total de leituras:", total_leituras)

    print("\nTemperatura:")
    print("Média:", round(media_temp, 2), "°C")
    print("Maior valor:", maior_temp, "°C")
    print("Menor valor:", menor_temp, "°C")

    print("\nPM2,5:")
    print("Média:", round(media_pm25, 2), "µg/m³")
    print("Maior valor:", maior_pm25, "µg/m³")
    print("Menor valor:", menor_pm25, "µg/m³")

    print("\nRuído:")
    print("Média aritmética simplificada:", round(media_ruido, 2), "dB")
    print("Maior valor:", maior_ruido, "dB")
    print("Menor valor:", menor_ruido, "dB")

    print("\nOcorrências críticas:")
    print("Temperatura:", ocorrencias_temperatura)
    print("PM2,5:", ocorrencias_pm25)
    print("Ruído:", ocorrencias_ruido)
    print("Leituras com pelo menos uma condição crítica:", leituras_criticas)
    print("Percentual de leituras críticas:", round(percentual_critico, 2), "%")

    print("\n" + classificacao)

    # Deixamos os resultados organizados para montar o relatório TXT.
    resultados = {
        "total_leituras": total_leituras,
        "media_temp": media_temp,
        "maior_temp": maior_temp,
        "menor_temp": menor_temp,
        "media_pm25": media_pm25,
        "maior_pm25": maior_pm25,
        "menor_pm25": menor_pm25,
        "media_ruido": media_ruido,
        "maior_ruido": maior_ruido,
        "menor_ruido": menor_ruido,
        "ocorrencias_temperatura": ocorrencias_temperatura,
        "ocorrencias_pm25": ocorrencias_pm25,
        "ocorrencias_ruido": ocorrencias_ruido,
        "leituras_criticas": leituras_criticas,
        "percentual_critico": percentual_critico,
        "classificacao": classificacao
    }

    return resultados


# O relatório guarda os dados principais para consulta depois da execução.
def salvar_relatorio(numero_sequencia, leituras, resultados):
    nome_arquivo = "relatorio_monitoramento_" + str(numero_sequencia) + ".txt"

    arquivo = open(nome_arquivo, "w", encoding="utf-8")

    arquivo.write("CENTRAL DE MONITORAMENTO AMBIENTAL DA COMUNIDADE\n")
    arquivo.write("Ambiente: entorno de uma escola fictícia em São Paulo - SP\n")
    arquivo.write("Contexto: região urbana com comércio, carros, ônibus e circulação de pedestres.\n")
    arquivo.write("Público que circula: crianças, jovens, adultos e idosos.\n\n")

    arquivo.write("LIMITES DE REFERÊNCIA UTILIZADOS\n")
    arquivo.write("Temperatura: mínimo de " + str(TEMP_MIN) + " °C e máximo de " + str(TEMP_MAX) + " °C (faixa didática definida pelo grupo).\n")
    arquivo.write("PM2,5: máximo de " + str(PM25_MAX) + " µg/m³, média de 24 horas (referência OMS 2021 / valor-guia final CONAMA 506/2024).\n")
    arquivo.write("Ruído: máximo de " + str(RUIDO_MAX) + " dB no período diurno (referência ABNT NBR 10151:2019 para áreas de escolas).\n")
    arquivo.write("Período dos valores simulados: cada valor de PM2,5 representa a média de 24 horas; cada valor de ruído representa o período diurno.\n\n")

    arquivo.write("QUANTIDADE DE LEITURAS: " + str(resultados["total_leituras"]) + "\n\n")

    arquivo.write("VALORES REGISTRADOS\n")
    for leitura in leituras:
        arquivo.write(
            "Leitura " + str(leitura["numero"]) +
            " - Temperatura: " + str(leitura["temperatura"]) + " °C" +
            " | PM2,5: " + str(leitura["pm25"]) + " µg/m³" +
            " | Ruído: " + str(leitura["ruido"]) + " dB\n"
        )

    arquivo.write("\nESTATÍSTICAS\n")
    arquivo.write("Temperatura - média: " + str(round(resultados["media_temp"], 2)) + " °C; maior: " + str(resultados["maior_temp"]) + " °C; menor: " + str(resultados["menor_temp"]) + " °C.\n")
    arquivo.write("PM2,5 - média: " + str(round(resultados["media_pm25"], 2)) + " µg/m³; maior: " + str(resultados["maior_pm25"]) + " µg/m³; menor: " + str(resultados["menor_pm25"]) + " µg/m³.\n")
    arquivo.write("Ruído - média aritmética simplificada: " + str(round(resultados["media_ruido"], 2)) + " dB; maior: " + str(resultados["maior_ruido"]) + " dB; menor: " + str(resultados["menor_ruido"]) + " dB.\n\n")

    arquivo.write("OCORRÊNCIAS CRÍTICAS\n")
    arquivo.write("Temperatura: " + str(resultados["ocorrencias_temperatura"]) + "\n")
    arquivo.write("PM2,5: " + str(resultados["ocorrencias_pm25"]) + "\n")
    arquivo.write("Ruído: " + str(resultados["ocorrencias_ruido"]) + "\n")
    arquivo.write("Leituras com pelo menos uma condição crítica: " + str(resultados["leituras_criticas"]) + "\n")
    arquivo.write("Percentual de leituras críticas: " + str(round(resultados["percentual_critico"], 2)) + "%\n\n")

    arquivo.write(resultados["classificacao"] + "\n\n")
    arquivo.write("Observação: este relatório apresenta uma simulação baseada nos critérios adotados pelo grupo. Não representa certificação de segurança ambiental nem substitui uma avaliação técnica do local.\n")
    arquivo.write("Nota: a média aritmética dos valores de ruído é uma estatística descritiva simplificada, não sendo nível sonoro equivalente nem avaliação de exposição acústica.\n")

    arquivo.close()

    print("\nRelatório salvo como:", nome_arquivo)


# Mantemos o programa funcionando para que seja possível fazer
# outra sequência sem precisar executar o arquivo novamente.
def iniciar_programa():
    continuar = "s"
    numero_sequencia = 1

    print("")
    print(" CENTRAL DE MONITORAMENTO AMBIENTAL")
    print(" Entorno de uma escola - São Paulo/SP")

    while continuar == "s":
        leituras = registrar_leituras()

        (ocorrencias_temperatura, ocorrencias_pm25,
         ocorrencias_ruido, leituras_criticas) = analisar_leituras(leituras)

        resultados = gerar_resultados(
            leituras,
            ocorrencias_temperatura,
            ocorrencias_pm25,
            ocorrencias_ruido,
            leituras_criticas
        )

        salvar_relatorio(numero_sequencia, leituras, resultados)
        numero_sequencia = numero_sequencia + 1

        continuar = input("\nDeseja realizar uma nova análise? (s/n): ").strip().lower()

        while continuar != "s" and continuar != "n":
            continuar = input("Digite apenas s para sim ou n para não: ").strip().lower()

    print("\nPrograma encerrado. Obrigado por utilizar a central!")


# Chamamos a função principal para iniciar o programa.
iniciar_programa()
