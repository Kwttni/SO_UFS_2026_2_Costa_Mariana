# SO_UFS_2026_2_Costa_Mariana

Repositório da Atividade 1 de Sistemas Operacionais (2026.2). O projeto analisa processos, threads, chamadas de sistema e uso de recursos durante a execução local de um modelo de IA generativa.

## Aplicação e modelo

* **Trilha:** Trilha B - RAG textual (Ollama + ollama-local-rag)
* **Repositório base:** [cpepper96/ollama-local-rag](https://github.com/cpepper96/ollama-local-rag)
* **Modelo:** Meta-Llama-3.1-8B-Instruct
* **Formato:** GGUF
* **Quantização:** Q4_K_M
* **Tamanho:** aproximadamente 4,9 GB
* **Sistema:** Fedora Linux 44
* **Processador:** AMD Ryzen 5 5600GT (6 núcleos / 12 threads)
* **Memória:** 16 GB RAM
* **Instalação:** Nativa

## Instalação e configuração

O código original precisou de algumas alterações por causa de incompatibilidades entre versões das bibliotecas `unstructured` e `langchain`, além da instalação do `faiss-cpu`.

### 1. Clonar o repositório

```bash
git clone https://github.com/[seu-usuario]/SO_UFS_2026_2_Costa_Mariana.git
cd SO_UFS_2026_2_Costa_Mariana/codigo_aplicacao
```

### 2. Criar o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Instalar o Ollama e baixar o modelo

```bash
curl -fsSL https://ollama.com/install.sh | sh
time ollama pull llama3.1
```

## Execução

### Indexação da base

```bash
python3 create_database.py
```

Esse comando lê os arquivos `.md` da pasta `bases_de_conhecimento/` e cria o índice vetorial.

### Consulta ao RAG

```bash
python3 query_data.py "What is Amazon Bedrock?"
```

## Monitoramento

Foram usados comandos para acompanhar processos, threads, CPU, memória e chamadas de sistema.

### Processos e threads

```bash
ps -eo pid,ppid,stat,ni,pri,psr,pcpu,pmem,nlwp,comm --sort=-pcpu
```

Também foram utilizados:

```bash
htop
```

```bash
pstree -p
```

### Chamadas de sistema

Para a indexação:

```bash
strace -f -c -o strace_log.txt python3 create_database.py
```

Para acompanhar o `llama-server`:

```bash
sudo strace -f -c -p $(pgrep llama-server) -o llama_strace.txt
```

## Testes

Foram utilizadas quatro configurações para comparar o comportamento do sistema.

### C1 - Execução padrão

Foram utilizadas as bases originais:

* `bedrock-docs.md`
* `bedrock-kb.md`

Foram testadas perguntas curtas e longas.

### C2 - Concorrência

Foram abertas duas execuções ao mesmo tempo com a mesma pergunta.

O objetivo foi observar o uso de CPU, memória e o comportamento do sistema com duas requisições simultâneas.

### C3 - Base maior

Foram adicionadas cinco bases de conhecimento:

* Redes
* Sistemas Operacionais
* Banco de Dados
* Inteligência Artificial
* Segurança

Depois disso, o banco vetorial foi criado novamente e foram feitas consultas curtas e longas.

### C4 - Base maior + concorrência

Foi usado o mesmo conjunto maior de bases da C3, mas com duas consultas executadas ao mesmo tempo.

Nesse cenário foram observados o uso de recursos e problemas na recuperação do contexto.
