# Declaração de Uso Crítico de IA Generativa

As IAs foram usadas como apoio durante o desenvolvimento da atividade e do relatório. As respostas foram conferidas por meio de testes práticos e documentação.

## Ferramentas utilizadas

* ChatGPT (OpenAI)
* Gemini (Google)

## Como as IAs foram usadas

As IAs foram utilizadas para:

1. Revisar a escrita do relatório.
2. Criar os arquivos md's com base no documeto técnico e demais informações.
2. Criar um checklist dos requisitos da atividade.
3. Ajudar a entender erros do terminal e possíveis soluções.
4. Explicar siglas e informações dos comandos de monitoramento, como as colunas do `ps`.
5. Criar bases de conhecimento sintéticas para os testes C3 e C4.
6. Sugerir perguntas curtas e longas para testar o RAG.

## 5 prompts utilizados

1. *"Gere 5 bases de conhecimento em md com a mesma estrutura das bases bedrock-docs.md e bedrock-kb.md anexadas."*

2. *"Crie uma tabela para validar os seguintes requisitos para 12 execuções mensuráveis, cobrindo as três configurações, ao menos dois tamanhos de entrada ou carga e pelo menos duas repetições por cenário."*

3. *"Me dê ideias de entradas de testes."*

4. *"Além do htop e strace, há outro comando que posso usar para verificar os requisitos solicitados?"*

5. *"Me explique o que cada sigla significa: PID PPID STAT NI PRI PSR %CPU %MEM NLWP COMMAND."*

## Sugestões utilizadas ou rejeitadas

### Sugestões aprovadas

Foram utilizadas as cinco bases de conhecimento geradas pela IA sobre:

* Redes
* Sistemas Operacionais
* Inteligência Artificial
* Banco de Dados
* Segurança

Essas bases foram usadas nos testes das configurações C3 e C4.

### Sugestões corrigidas

A tabela criada pela IA para organizar os requisitos e métricas foi ajustada manualmente para ficar de acordo com os testes realmente realizados.

### Sugestões rejeitadas

Algumas sugestões de código usando `langchain.chains` foram rejeitadas porque utilizavam formas antigas de importação e não funcionavam com as versões atuais das bibliotecas.

## Erros encontrados

Durante a configuração foram encontrados erros como:

```text
ERROR: No matching distribution found for unstructured==0.13.2
```

e:

```text
ModuleNotFoundError
```

relacionado ao `langchain`.

As primeiras soluções sugeridas pela IA não resolveram completamente o problema.

## Como os problemas foram resolvidos

A correção foi feita manualmente nos arquivos:

* `create_database.py`
* `query_data.py`

O código foi atualizado para utilizar a sintaxe atual do LCEL do LangChain.

Também foi necessária a instalação do pacote:

```bash
pip install faiss-cpu
```

## Como as respostas foram verificadas

As sugestões da IA não foram utilizadas sem verificação. Foram realizados testes no ambiente utilizado na atividade e consultas à documentação.

Foram utilizadas como referência:

* API Reference do LangChain: https://reference.langchain.com/
* Issue sobre a obsolescência dos métodos: https://github.com/langchain-ai/langchain-community/issues/674
* Repositório original do projeto: https://github.com/cpepper96/ollama-local-rag

Além disso, o código corrigido foi executado na máquina utilizada nos experimentos para verificar se as alterações funcionavam.
