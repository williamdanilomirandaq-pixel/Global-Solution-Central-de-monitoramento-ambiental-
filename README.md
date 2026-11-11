
# Central de Monitoramento Ambiental

## Sobre o projeto

Esse projeto foi desenvolvido como parte de um trabalho da faculdade. A ideia é criar um programa em Python que simula o monitoramento ambiental no entorno de uma escola.

Escolhemos esse ambiente porque é um local com circulação de pessoas, carros e ônibus, além de comércios próximos.

## Integrantes

- William Danilo Miranda Quisbert — RM 571246
- Matheus Luiz dos Santos Cabral — RM 569560
- Mateus Pedro de Oliveira — RM 569570

## O que o programa faz?

O programa recebe informações de três fatores ambientais:

- Temperatura (°C);
- Partículas PM2,5 (µg/m³);
- Ruído (dB).

Depois de receber os valores, ele verifica se estão dentro dos limites que escolhemos para a simulação. Também mostra os alertas, calcula algumas estatísticas e gera um relatório em arquivo TXT.

## Como executar

Para executar o programa, é necessário ter o Python instalado.

1. Baixe os arquivos do repositório.
2. Abra a pasta no VS Code.
3. Abra o arquivo `central_monitoramento_ambiental.py`.
4. Execute o código.

## Relatório de exemplo

O arquivo `relatorio_monitoramento_10_leituras.txt` mostra um exemplo de resultado do programa, usando 10 rodadas de leitura.

## Sobre os limites utilizados

Os valores foram escolhidos com base em referências sobre qualidade do ar e ruído, além de um critério definido pelo grupo para temperatura.

É importante lembrar que o programa é uma simulação feita para o trabalho. Ele não realiza medições reais do ambiente.

## Fontes consultadas

- OMS — Diretrizes de qualidade do ar: https://www.who.int/publications/i/item/9789240034228
- CONAMA — Resolução nº 506/2024: https://conama.mma.gov.br/?id=827&option=com_sisconama&task=arquivo.download
- Ministério do Meio Ambiente — Padrões de qualidade do ar: https://www.gov.br/mma/pt-br/assuntos/meio-ambiente-urbano-recursos-hidricos-qualidade-ambiental/qualidade-do-ar/padroes-de-qualidade-do-ar/padroes-de-qualidade-do-ar/
- ABNT NBR 10151:2019 — Avaliação de ruído: https://normadedesempenho.com.br/wp-content/uploads/2022/10/NBR-10151.pdf
- AECHO — Ruído nas escolas: https://aecho.com.br/ruido_escolas
