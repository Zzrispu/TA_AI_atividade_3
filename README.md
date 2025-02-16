# Atividade 3: Comparação de Métricas de Classificação e Regressão com Armazenamento em Banco de Dados
Esse documento é um relatório dos experimentos realizados durante essa atividade. O reletório se dará através da explicação dos arquivos presentes neste repositório.

## Código Fonte (main.ipynb)
Todos os passos pedidos na ativide estão presentes no notebook **main.ipynb**, com exceção do sistema para visualizar e comparar os resultados dos experimentos.

### 1. Preparando o Banco de Dados
O primeiro passo a dar neste documento é estabelecer a conecção com a DataBase, no meu caso, estou usando o PostgreSQL. Para estabelecer essa conecção utilizei a bibllioteca **psycopg2** (todas bibliotecas usadas estão listados no **requirements.txt** neste mesmo repositório).

As credenciais são carregadas por meio da biblioteca **python-dotenv**, caso tente reproduzir estes experimentos, altere os dados no .env para as suas credenciais.

Também crei funções para lidar com a DataBase, cada uma delas está listada desntro do notebook, há uma para salvar o modelo de machine learning, seu tipo (Classifier ou Regressor), e seus hiperparâmetros. Uma para salvar os dados de pré-processamento (Sampling Strategy e Split Method). Uma para salvar as Métricas (tanto para classifiers quanto para regressors). E uma para salvar os resultados finais.

### 2. Modelos e Métricas Utilizadas
Os seguintes modelos de Machine Learning foram utlizados:
* **Classificação**: RandomForestClassifier, DecisionTree
* **Regressão**: RandomForestRegressor, Linear Regression

As métricas utilizadas para avaliação dos modelos incluem:
* **Classificação**: Accuracy, Precision, Recall, F1-Score, ROC AUC
* **Regressão**: MSE, MAPE, MAE, R2

### 3. Pré-Processamento dos DataSet
Foram aplicadas as seguintes técnicas de pré-processamento antes do treinamento dos modelos:
* **Amostragem dos dados**: Undersampling, Oversampling, Stratified Sampling
* **Separação dos dados**: Hold-out e Cross-Validation
* **Normalização**: StandartScaler

Para fins de comparação, os modelos foram treinados usando uma versão dos dados normalizda, e outra não normalizada.

### 3. Treinamento e amazenamento dos resultados
A medida que os modelos são treinados, os resultados dos experimentos são automáticamente armazenados na DataBase, dentro do notebook é possível ter uma prévia dos resultados das métricas, abaixo estão alguns exemplos.

#### Classificação - Iris DataSet
![{4845CCC2-746E-437B-861F-29DD7CC10B98}](https://github.com/user-attachments/assets/60bbfd0d-dcbe-43b8-9e14-bb942bf18d25)

#### Regressão - Bonton Housing DataSet
![{B7D19E87-481B-42F7-BC54-2E0BD089A81A}](https://github.com/user-attachments/assets/94396748-3248-45da-b695-217049b56ef2)

## Interface Grafica para visualizar e comparar os resultados (consultaSQL.py)
Para criar essa interface um útilizei a biblioteca **streamlit**, ele permite criar uma página web e visualizar tabelas de forma fácil, para executar este arquivo é preciso usar o seguinte comando no terminal:

> ``streamlit run consultaSQL.py``

Pela inconveniência de ter que baixar e rodar a biblioteca, irei apresentar imagens de como a interface se parece:

### 1. Sem filtro de tipo
Quando entramos na interface, por padrão nos é apresentado uma tabela sem filtro de todos os experimentos presentes no Banco de Dados.
![{72CE871C-F4D2-4EDE-B23B-98DEDAA70140}](https://github.com/user-attachments/assets/e6971299-46a8-432b-9c50-7ca21a896d42)

Podemos clicar para deixar a tabela em tela cheia, assim podendo ver todos os experimentos.
![{1313B082-60B1-41FE-AF46-1C7ECEE00B47}](https://github.com/user-attachments/assets/daf5c7e9-c86a-45f5-9f56-a1f025f5ae7a)

Também é possível ordenar as colunas em crescente e decrescente para uma melhor organização.

### 2. Classificação
Quando a opção de filtrar por **Classificação** é selecionada somente os experimentos do tipo **classification** serão exibidas, mas além disso, graficos comparativos de cada métrica para cada DataSet aparecerão:
![{60BD89D6-EC91-4A59-9796-7EDEB3E15B80}](https://github.com/user-attachments/assets/92f34d7d-24e0-45fd-915f-601ab704116b)
![{E032EB2C-3042-4D88-9FA4-8C01208BAB05}](https://github.com/user-attachments/assets/d3ff4ef5-873c-4f9b-a724-8b4a7f475371)
![{AE07137F-C9A3-46B0-83B8-D21D61247A71}](https://github.com/user-attachments/assets/ea26e0e0-5a40-48ac-bc3e-370007354638)
![{182AB76C-C21B-4FB6-9DE2-EDF8BCBCD993}](https://github.com/user-attachments/assets/d1b60c39-e1c6-49e7-b8df-fdf686d74299)

### 3. Regressão
Quando a opção de filtrar por **Regressão** é selecionada somente os experimentos do tipo **regression** serão exibidas, mas além disso, graficos comparativos de cada métrica para cada DataSet aparecerão:
![{88A74D0B-266A-41AB-A171-3CB1B90116AE}](https://github.com/user-attachments/assets/c28fd3bd-30c3-47ed-a004-50ff4442c6b0)
![{DEE5D5A5-0C46-47D3-B43B-9392B435369F}](https://github.com/user-attachments/assets/40b5e4d6-856c-46e8-8349-8153240568b1)
![{83C5E247-616B-4332-A1DA-5F16D20F2CBC}](https://github.com/user-attachments/assets/aeac27d4-c37e-45a7-bbb9-5b6dbd3bf479)

## Conclusão
Com base nos resultados dos experimentos, é possivel observar que para modelos de Classificação, usando o *OverSampling* para amostragem e *Holdout* para separação de dados, os modelos treinados com dados normalizados apresentaram métricas maiores.
Na comparação entre os modelos de Regressão, usando **Holdout** como separação e sem utilizar de amostram, as métricas dos experimentos ficaram muito diferentes entre si, mas isso se deve a grande disparidade nos tamanhos dos datasets, o **California Housing DataSet** tem  20.640 samples, já o **Boston Housing DataSet** tem somente 506.

Por motivos de simplificação na hora de exibir e comparar os experimentos (e para poupar minha sanidade mental), não há uma variedade tão grande experimentos com diferentes amostragens e separadores salvos na DataBase, isso faria a quantidade de graficos necessários triplicar.
