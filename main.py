import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, CallbackContext

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

user_tasks = {}

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(" *Bot de Tarefas*\n\nComandos disponíveis:\n"
                                    "/nova - Cadastrar nova tarefa\n"
                                    "/listar - Listar todas as tarefas\n"
                                    "/editar - Editar uma tarefa\n"
                                    "/deletar - Deletar uma tarefa",
                                    parse_mode='Markdown')

# cadastro
async def nova_tarefa(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_tasks.setdefault(user_id, [])

    if not context.args:
        await update.message.reply_text("Digite a tarefa assim: `/nova  Comprar pão`", parse_mode='Markdown')
        return

    tarefa = " ".join(context.args)
    user_tasks[user_id].append(tarefa)
    await update.message.reply_text(f" Tarefa adicionada: *{tarefa}*", parse_mode='Markdown')

# listar
async def listar_tarefas(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    tarefas = user_tasks.get(user_id, [])

    if not tarefas:
        await update.message.reply_text(" Você não tem tarefas cadastradas.")
        return

    lista = "\n".join([f"{i+1}. {tarefa}" for i, tarefa in enumerate(tarefas)])
    await update.message.reply_text(f" *Suas tarefas:*\n\n{lista}", parse_mode='Markdown')

# edicao
async def editar_tarefa(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    tarefas = user_tasks.get(user_id, [])

    if not tarefas:
        await update.message.reply_text(" Você não tem tarefas para editar.")
        return

    if len(context.args) < 2:
        await update.message.reply_text("Digite o comando assim: `/editar 1 Nova descrição`", parse_mode='Markdown')
        return

    try:
        num = int(context.args[0]) - 1
        nova_descricao = " ".join(context.args[1:])

        if num < 0 or num >= len(tarefas):
            raise ValueError

        tarefas[num] = nova_descricao
        await update.message.reply_text(f" Tarefa {num+1} editada para: *{nova_descricao}*", parse_mode='Markdown')
    except ValueError:
        await update.message.reply_text(" Número inválido. Veja suas tarefas com /listar.")

# deletar
async def deletar_tarefa(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    tarefas = user_tasks.get(user_id, [])

    if not tarefas:
        await update.message.reply_text(" Você não tem tarefas para deletar.")
        return

    if not context.args:
        await update.message.reply_text("Digite o comando assim: `/deletar 1`", parse_mode='Markdown')
        return

    try:
        num = int(context.args[0]) - 1

        if num < 0 or num >= len(tarefas):
            raise ValueError

        removida = tarefas.pop(num)
        await update.message.reply_text(f"🗑️ Tarefa removida: *{removida}*", parse_mode='Markdown')
    except ValueError:
        await update.message.reply_text(" Número inválido. Veja suas tarefas com /listar.")

# config
def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("nova", nova_tarefa))
    application.add_handler(CommandHandler("listar", listar_tarefas))
    application.add_handler(CommandHandler("editar", editar_tarefa))
    application.add_handler(CommandHandler("deletar", deletar_tarefa))

    application.run_polling()

if __name__ == "__main__":
    main()
