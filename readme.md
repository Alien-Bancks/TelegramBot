# Telegram Bot - Gerenciador de Tarefas

## Descrição
Este é um bot para o Telegram que permite gerenciar tarefas de forma simples. O usuário pode cadastrar, listar, editar e excluir tarefas através de comandos intuitivos.

## Funcionalidades
- Adicionar uma nova tarefa
- Listar todas as tarefas cadastradas
- Editar uma tarefa existente
- Excluir uma tarefa

## Como Usar

1. **Iniciar o bot:**
   - Use o comando `/start` para iniciar a interação.

2. **Cadastrar uma tarefa:**
   - Digite `/nova` e informe a descrição da tarefa.

3. **Listar tarefas:**
   - Use `/listar` para visualizar todas as tarefas cadastradas.

4. **Editar uma tarefa:**
   - Digite `/editar <número>` e forneça a nova descrição.

5. **Excluir uma tarefa:**
   - Use `/deletar <número>` para remover uma tarefa da lista.

## Instalação e Execução

1. Clone o repositório:
   ```sh
   git clone https://github.com/Alien-Bancks/TelegramBot.git
   cd TelegramBot
   ```
2. Configure o arquivo `.env` com o token do bot do Telegram:
   ```sh
   BOT_TOKEN=seu_token
   ```
3. Execute o bot:
   ```sh
   python main.py
   ```

## Estrutura do Projeto
```
TelegramBot/
│-- main.py         # Código principal do bot
│-- .env           # Arquivo de configuração do token
│-- README.md      # Documentação do projeto
```

## Tecnologias Utilizadas
- Python
- python-telegram-bot
- dotenv
