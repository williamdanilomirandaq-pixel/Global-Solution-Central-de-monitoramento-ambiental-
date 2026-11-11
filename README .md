# Central de Monitoramento Ambiental

Disciplina: Computational Thinking for Engineering  
Curso: Engenharia de Computação — 1º ano  
Semestre: 2º semestre de 2026

## Integrantes

- William Danilo Miranda Quisbert — RM 571246
- Matheus Luiz dos Santos Cabral — RM 569560
- Mateus Pedro de Oliveira — RM 569570

## 1. Sobre o projeto

Nosso grupo escolheu monitorar o **entorno de uma escola fictícia em São Paulo — SP**, com educação infantil, ensino fundamental e ensino médio. O local está em uma região urbana, com comércios próximos e circulação de carros, ônibus e pedestres. Entre as pessoas que passam pelo local estão crianças, jovens, adultos e idosos.

### Atividades no local e necessidades dos usuários

Os alunos entram e saem da escola nos horários de aula. No recreio, eles ficam em uma área a céu aberto dentro da escola, expostos ao clima, ao ar e aos ruídos do entorno. Por isso, consideramos três necessidades:

- **Temperatura:** manter um ambiente confortável para as atividades ao ar livre.
- **PM2,5:** reduzir a exposição das crianças e dos jovens às partículas finas emitidas principalmente pelo tráfego de veículos, já que o entorno tem muitos carros e ônibus.
- **Ruído:** manter condições adequadas para a convivência e para a aprendizagem.

### Finalidade do monitoramento

A finalidade é identificar situações que demandem atenção em um espaço frequentado por crianças e jovens e organizar essas informações em um relatório simples, que ajude a comunidade escolar a perceber com que frequência as condições saem dos limites adotados.

### Objetivo da solução

Desenvolver, em Python, uma simulação de uma central de monitoramento ambiental. O usuário informa valores de temperatura, concentração de partículas finas PM2,5 e nível de ruído. O programa compara os dados com os critérios definidos, mostra alertas, calcula estatísticas e gera um relatório em formato `.txt`.

O programa utiliza dados digitados pelo usuário. Não há conexão com sensores físicos e os resultados não representam uma medição real do local.
 
## 2. Parâmetros e critérios adotados

| Parâmetro | Critério utilizado no programa | Período/unidade |
|---|---|---|
| Temperatura | mínimo de 18 °C e máximo de 30 °C | °C |
| PM2,5 | acima de 15 µg/m³ gera alerta | µg/m³, média de 24 horas |
| Ruído | acima de 50 dB gera alerta | dB, período diurno |

Valores exatamente iguais aos limites são considerados dentro da faixa.

### Justificativa dos critérios

- **Temperatura (18 °C a 30 °C):** faixa didática definida pelo grupo para a simulação. Não é apresentada como limite legal ou como faixa oficial universal de conforto térmico.
- **PM2,5 (15 µg/m³ em 24 horas):** valor-guia de 24 horas recomendado pela Organização Mundial da Saúde (OMS) nas Diretrizes Globais de Qualidade do Ar de 2021. A Resolução CONAMA nº 506/2024 também apresenta 15 µg/m³ como padrão final (PF) para PM2,5 em 24 horas. É importante esclarecer que, em novembro de 2026, a etapa intermediária PI-2 da resolução brasileira está em vigor e estabelece 50 µg/m³ para 24 horas; o padrão final PF ainda depende de data de entrada em vigor a ser definida. Nosso programa escolhe 15 µg/m³ como referência de saúde mais restritiva para a simulação, e não como afirmação de que esse seja o padrão legal brasileiro atualmente exigível.
- **Ruído (50 dB no período diurno):** o valor aparece na Tabela 3 da ABNT NBR 10151:2019 para "área estritamente residencial urbana ou de hospitais ou de escolas". Como o entorno descrito também possui comércio, a classificação acústica oficial depende do uso e ocupação predominantes da área e da avaliação técnica aplicável. Para a simulação, o grupo adotou 50 dB tomando a escola como referência de atenção. O programa não realiza avaliação acústica normativa.

**Observação sobre os períodos:** cada valor de PM2,5 digitado representa uma média de 24 horas, e não uma leitura instantânea, de forma que o valor simulado e o limite têm o mesmo período de referência. Os valores de ruído representam uma medição/avaliação do período diurno. O programa recebe números para fins didáticos e não verifica se a medição real respeitou esses períodos. Essas informações constam nos comentários do código, nas mensagens de entrada e no relatório gerado.

## 3. Como executar

1. Instale o Python 3, caso ainda não esteja instalado.
2. Baixe ou clone este repositório.
3. Abra a pasta do projeto no Visual Studio Code.
4. Abra o terminal integrado do VS Code.
5. Execute:

```
python central_monitoramento_ambiental.py
```

Se o comando `python` não funcionar no Windows, tente:

```
py central_monitoramento_ambiental.py
```

O programa usa recursos nativos do Python e não precisa instalar bibliotecas externas.

## 4. Como o programa funciona

1. Pergunta quantas leituras serão registradas.
2. Para cada leitura, solicita temperatura, PM2,5 e ruído, indicando o número da leitura e a unidade esperada. Valores não numéricos são recusados, e valores negativos de PM2,5 e ruído não são aceitos.
3. Armazena os valores em uma lista de dicionários, mantendo juntos os três dados de cada leitura.
4. Verifica cada parâmetro separadamente e mostra todos os alertas necessários.
5. Calcula média, maior e menor valor de cada parâmetro.
6. Conta as ocorrências críticas de cada parâmetro e as leituras que tiveram pelo menos uma condição crítica. Uma leitura com vários alertas conta uma única vez como crítica.
7. Calcula o percentual de leituras críticas e aplica a classificação definida no enunciado: **mais de 30%** gera estado geral de atenção; **até 30%**, incluindo exatamente 30%, fica dentro do critério didático.
8. Salva um relatório `.txt` e pergunta se o usuário deseja iniciar outra sequência. Se a resposta for sim, os dados e os contadores são reiniciados.

## 5. Organização das funções

- `calcular_estatisticas(valores)`: calcula média, máximo e mínimo de uma lista.
- `pedir_quantidade()`: solicita uma quantidade inteira maior que zero.
- `registrar_leituras()`: recebe e organiza os dados digitados.
- `analisar_leituras(leituras)`: verifica os limites e conta alertas.
- `gerar_resultados(...)`: calcula estatísticas, percentual e classificação.
- `salvar_relatorio(...)`: grava os resultados em um arquivo `.txt`.
- `iniciar_programa()`: controla a execução e permite iniciar novas análises.

## 6. Arquivos gerados e exemplo de saída

Ao final de cada sequência, o programa cria um arquivo com nome semelhante a:

```text
relatorio_monitoramento_1.txt
```

Se o usuário fizer outra sequência na mesma execução, será criado `relatorio_monitoramento_2.txt`, e assim por diante.

O relatório contém a identificação do ambiente, os limites, os períodos dos valores, os valores registrados, as estatísticas, as ocorrências críticas, o percentual, a classificação e as observações sobre a simulação.

Um **exemplo de relatório gerado pelo programa** está neste repositório no arquivo [`relatorio_monitoramento_1.txt`](relatorio_monitoramento_1.txt). Ele usa 10 leituras, com valores dentro dos limites, valores exatamente iguais aos limites e leituras com um ou mais alertas (4 leituras críticas, 40%).

## 7. Fontes de referência

- Organização Mundial da Saúde (OMS). *WHO global air quality guidelines: particulate matter (PM2.5 and PM10), ozone, nitrogen dioxide, sulfur dioxide and carbon monoxide*. 2021. https://www.who.int/publications/i/item/9789240034228
- Conselho Nacional do Meio Ambiente (CONAMA). Resolução nº 506, de 5 de julho de 2024. Padrões nacionais de qualidade do ar, Anexo I. https://conama.mma.gov.br/?id=827&option=com_sisconama&task=arquivo.download
- Ministério do Meio Ambiente e Mudança do Clima. Padrões de Qualidade do Ar. https://www.gov.br/mma/pt-br/assuntos/meio-ambiente-urbano-recursos-hidricos-qualidade-ambiental/qualidade-do-ar/padroes-de-qualidade-do-ar/padroes-de-qualidade-do-ar/
- ABNT. ABNT NBR 10151:2019. *Acústica — Medição e avaliação de níveis de pressão sonora em áreas habitadas — Aplicação de uso geral*. Tabela 3. https://normadedesempenho.com.br/wp-content/uploads/2022/10/NBR-10151.pdf
https://aecho.com.br/ruido_escolas
---

**Trabalho Global Solution — Computational Thinking for Engineering — 2º semestre de 2026.**
