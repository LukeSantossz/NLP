NLP with Transformers (O'Reilly)

O que isso faz?
Este repositório explora a implementação prática de tarefas essenciais de Processamento de Linguagem Natural (NLP) utilizando modelos de aprendizagem profunda.

Classificação de Texto: Categorização automática de sequências de texto.

Reconhecimento de Entidades Nomeadas (NER): Identificação de entidades como nomes de pessoas, organizações e localizações.

Question Answering: Capacidade de extrair respostas diretas a partir de um contexto de texto específico.

O que é?
É um conjunto de scripts de estudo e exercícios práticos em Python, focados na utilização da arquitetura Transformers para resolver problemas de processamento de texto.

Quais tecnologias são usadas?
Python: Linguagem de programação principal.

Hugging Face Transformers: Framework para o carregamento e execução de pipelines de modelos pré-treinados.

Pandas: Biblioteca para a manipulação de dados e visualização de resultados em tabelas.

PyTorch: Framework de aprendizagem profunda utilizado como backend para os modelos.

Qual é a ambição do projeto?
O projeto faz parte de um plano de desenvolvimento individual para a transição de carreira para a área de Dados e Inteligência Artificial. O objetivo é dominar as ferramentas do estado da arte em NLP e construir uma base técnica sólida em Machine Learning e Deep Learning através de exercícios práticos da literatura técnica.

Qual é o estágio do projeto?
Estado: Em desenvolvimento (Trabalho em curso).

Concluído: Estudo e codificação dos exemplos iniciais do Capítulo 1 ("Hello Transformers").

Pendente: Implementação dos tópicos de arquitetura interna de Transformers, ajuste fino de modelos (fine-tuning) e processamento de grandes volumes de dados de texto previstos nos capítulos seguintes.

Existem alguns problemas conhecidos ou coisas que não são feitas corretamente?
No ficheiro chapterOne.py, as secções de código estão comentadas para permitir que cada tarefa de NLP seja testada individualmente sem sobrecarregar a memória com múltiplos modelos em simultâneo.

A execução inicial de cada pipeline exige o download automático de modelos pesados, o que requer uma ligação estável à internet e espaço em disco.

Atualmente, o código utiliza apenas as configurações padrão das pipelines, sem otimização de hiperparâmetros ou seleção de modelos específicos para línguas que não o inglês.