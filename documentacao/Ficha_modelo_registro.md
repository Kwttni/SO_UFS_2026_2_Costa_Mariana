# Registro e Ficha Técnica do Modelo

## Dados do modelo

* **Nome completo:** Mariana Silva Costa
* **Trilha:** Trilha B - RAG textual: Ollama + ollama-local-rag
* **Repositório:** [cpepper96/ollama-local-rag](https://github.com/cpepper96/ollama-local-rag)
* **Modelo:** Meta-Llama-3.1-8B-Instruct
* **Hugging Face:** https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct
* **Família:** Llama 3.1
* **Variante:** Instruct
* **Parâmetros:** 8,03 bilhões
* **Formato:** GGUF
* **Quantização:** Q4_K_M (4-bit)
* **Tamanho:** aproximadamente 4,9 GB
* **Janela de contexto:** 128k tokens
* **Licença:** Llama 3.1 Community License

## Justificativa

O modelo Llama-3.1-8B-Instruct foi escolhido por possuir 8 bilhões de parâmetros, ficando dentro do limite de 10 bilhões. Ele apresenta um bom desempenho para seguir instruções e possui uma janela de contexto grande, o que é bom para a Trilha B, já que será utilizado para trabalhar com documentos e recuperação de informações. O modelo será executado localmente pelo Ollama usando o formato GGUF e a quantização Q4_K_M. Essa configuração ajuda a diminuir o consumo de memória e processamento, mantendo uma boa qualidade nas respostas e facilitando a coleta das métricas de desempenho, como uso de CPU, RAM, processos e threads.
## Registro

* **Data:** 03/09/2026
* **Horário:**  16:49
