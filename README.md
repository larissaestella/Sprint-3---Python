# Sprint 3 - Python
            Jeferson Gabriel de Mendonça | 553149 
            Joseh Gabriel Trimboli Agra | 553094
            Larissa Estella Gonçalves dos Santos | 552695
            Lucas Masaki Nagahama | 553084 
            Victor Henrique Vilares Rodrigues | 554175
    
# Cadastro de Pacientes
Este é um script Python para gerenciar o cadastro de pacientes e os procedimentos médicos. Ele coleta informações pessoais dos pacientes, calcula suas idades, fornece explicações sobre procedimentos médicos e envia mensagens de WhatsApp com os detalhes do procedimento escolhido. Os dados dos pacientes são armazenados em um arquivo externo JSON.

## Funcionalidades

### 1. Coleta de Dados do Paciente
A função `obter_dados_paciente` coleta informações pessoais dos pacientes:
- Nome completo
- CPF
- Data de nascimento
- Sexo
- Email
- Número de celular

O CPF é formatado corretamente e o número de celular é limpo de caracteres não numéricos.

### 2. Cálculo da Idade
A função `calcular_idade` calcula a idade do paciente com base na data de nascimento fornecida.

### 3. Menu de Procedimentos
A função `menu_procedimentos` exibe um menu com os seguintes procedimentos médicos:
- Hemograma
- Tomografia
- Ressonância Magnética
- Eletrocardiograma

### 4. Explicação dos Procedimentos
A função `obter_explicacao_procedimento` retorna uma descrição detalhada do procedimento selecionado.

### 5. Envio de Mensagens via WhatsApp
A função `enviar_whatsapp` utiliza a biblioteca `pywhatkit` para enviar mensagens de WhatsApp contendo informações sobre o procedimento escolhido para o número de celular do paciente.

### 6. Limpeza de Número
A função `limpar_numero` remove todos os caracteres não numéricos do número de celular.

### 7. Execução Principal
A função `main` gerencia o fluxo principal do programa:
- Coleta dados dos pacientes e os armazena em um dicionário.
- Permite a seleção e explicação de procedimentos.
- Envia as informações do procedimento via WhatsApp.
- Armazena os dados dos pacientes em um arquivo `pacientes.json`.
- Exibe uma lista dos pacientes cadastrados ao final.

## Execução do Script
Para executar o script, certifique-se de que todas as bibliotecas necessárias estejam instaladas (`json`, `datetime`, `pywhatkit`, `re`) e execute o arquivo. O script solicitará os dados do paciente e permitirá a escolha de procedimentos, enviando informações detalhadas via WhatsApp e armazenando tudo em um arquivo JSON.

## Requisitos
- Python 3
- Biblioteca `pywhatkit`
- Conexão com a internet para enviar mensagens via WhatsApp

## Como Executar
1. Instale as dependências necessárias:
  ```bash
  pip install pywhatkit
  ```
2. Execute o script:
  ```bash
  python nome_do_arquivo.py
  ```

## Observações
- Certifique-se de ter o WhatsApp Web configurado e logado no navegador.
- O envio de mensagens via WhatsApp está configurado para ser enviado imediatamente (0 minutos de atraso). Ajuste conforme necessário na função `enviar_whatsapp`.

## Contato
Para mais informações, entre em contato com o desenvolvedor do script.