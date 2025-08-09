from dataclasses import dataclass
import random

@dataclass
class PortugueseTranslations:
    LANGUAGE_NAME = "🇧🇷 Português"
    LANGUAGE_CODE = "pt"

    WRONG_VALUE_ERROR = "❌ Valor inválido para a variável {{ variable_name }}."

    START_MSG = (
        "Olá! 👋\n"
        "Sou o **Bot de Renomear Arquivos**, seu assistente para renomear arquivos no Telegram.\n\n"
        "✨ **Recursos principais:**\n"
        "- Renomear arquivos com nomes e extensões personalizados\n"
        "- Rápido, seguro e fácil de usar\n"
        "- Suporta diversos tipos de arquivos\n\n"
        "Envie-me um arquivo e eu guiarei você no processo de renomeação!\n\n"
        "Vamos começar! Use /mode para ativar renomeação automática\n"
        "Envie /help para mais informações.\n\n"
        "🚀 **Desenvolvido por** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "⚠️ Renomeação **cancelada**. Atualização em breve."

    RENAME_NO_FILTER_MATCH = (
        "🚫 **NENHUM FILTRO CORRESPONDENTE - RENOMEAÇÃO CANCELADA**\n\n"
        "🔍 Usando filtros pois nenhum nome foi especificado.\n"
        "👻 Gerencie filtros com /filters."
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ Usando filtros pois nenhum nome foi especificado.\n"
        "👻 Gerencie filtros com /filters."
    )

    RENAME_NOFLTR_NONAME = (
        "✍️ Digite o novo nome no formato:\n"
        "```/rename novo_nome.extensão```\n"
        "ou use `/filters` para configurar filtros."
    )

    RENAME_CANCEL = "❌ Cancelar renomeação."

    RENAMING_FILE = "🔄 Renomeando arquivo... Aguarde."

    DL_RENAMING_FILE = "📥 Baixando arquivo... Aguarde."

    RENAME_ERRORED_REPORT = "❗ Erro no download. Reporte este problema."

    RENAME_CANCEL_BY_USER = "🚫 **Cancelado pelo usuário.**"

    FLTR_ADD_LEFT_STR = "➕ Filtro adicionado: `<code>{{ text_1 }}</code>` à ESQUERDA."
    FLTR_ADD_RIGHT_STR = "➕ Filtro adicionado: `<code>{{ text_1 }}</code>` à DIREITA."
    FLTR_RM_STR = "❌ Remover filtro: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = "🔄 Substituir filtro: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."

    CURRENT_FLTRS = "⚙️ **Seus filtros atuais:**"
    ADD_FLTR = "➕ Adicionar filtro"
    RM_FLTR = "❌ Remover filtro"

    FILTERS_INTRO = (
        "🛠 **Guia de filtros:**\n"
        "Existem 3 tipos de filtros:\n\n"
        "🔄 **Substituir:** Troca uma palavra por outra.\n"
        "➕ **Adicionar:** Insere texto no início ou fim.\n"
        "❌ **Remover:** Elimina uma palavra do nome."
    )

    ADD_REPLACE_FLTR = "➕ Adicionar filtro de substituição"
    ADD_ADDITION_FLTR = "➕ Adicionar filtro de adição"
    ADD_REMOVE_FLTR = "➕ Adicionar filtro de remoção"
    BACK = "🔙 Voltar"

    REPALCE_FILTER_INIT_MSG = "✍️ Envie no formato: `<code>texto_original | substituto</code>` ou `/ignore` para cancelar."

    NO_INPUT_FROM_USER = "⚠️ Nenhuma entrada recebida."
    INPUT_IGNORE = "✅ **Ignorado**."
    WRONG_INPUT_FORMAT = "❌ Formato inválido. Verifique o formato."
    REPLACE_FILTER_SUCCESS = "✅ **Filtro adicionado:**\n`'{{ text_1 }}'` → `'{{ text_2 }}'`"

    ADDITION_FILTER_INIT_MSG = (
        "✍️ Digite o texto a adicionar entre `<code>|</code>`\n"
        "Exemplo: `<code>| texto |</code>`\n"
        "ou `/ignore` para cancelar."
    )

    ADDITION_FILTER_SUCCESS_LEFT = "✅ Filtro adicionado: `<code>{{ text_1 }}</code>` à ESQUERDA."
    ADDITION_FILTER_SUCCESS_RIGHT = "✅ Filtro adicionado: `<code>{{ text_1 }}</code>` à DIREITA."

    ADDITION_LEFT = "🔄 Adicionar à esquerda"
    ADDITION_RIGHT = "🔄 Adicionar à direita"

    ADDITION_POSITION_PROMPT = "📍 **Onde deseja adicionar o texto?**"

    REMOVE_FILTER_INIT_MSG = "✍️ Digite o texto a remover ou `/ignore` para cancelar."

    REMOVE_FILTER_SUCCESS = "✅ **Filtro adicionado:** `<code>{{ text_1 }}</code>` será removido."

    RENAME_THEMES_DOWNLOADING = [
        "✅ Download completo. Iniciando renomeação...",
        "📦 Arquivo recebido! Pronto para renomear...",
        "🪄 Download concluído. Iniciando processo...",
        "🔧 Dados obtidos. Preparando renomeação...",
        "💾 Salvo. Preparando novo nome...",
    ]

    RENAME_THEMES_UPLOADING = [
        "✅ Renomeação concluída! Upload finalizado.",
        "🚀 Arquivo renomeado com sucesso.",
        "📤 Upload completo. Seu arquivo está pronto!",
        "🌟 Arquivo renomeado e enviado!",
        "📁 Tarefa concluída. Arquivo renomeado.",
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 Download interrompido. Operação cancelada...",
        "🚫 Você cancelou. Download abortado.",
        "❌ Operação cancelada durante download.",
        "📴 Renomeação cancelada. Download interrompido.",
        "👋 Usuário cancelou durante download.",
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "🛑 Upload cancelado. Arquivo não enviado.",
        "🚫 Renomeação revertida. Upload cancelado.",
        "❌ Estágio final interrompido. Operação cancelada.",
        "📴 Upload cancelado. Arquivo não renomeado.",
        "👋 Usuário cancelou durante upload.",
    ]

    REPLY_TO_MEDIA = "📂 Responda `/rename` a um arquivo de mídia."

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "❗ Ocorreu um erro durante a renomeação."

    DOWNLOADING_THE_FILE = "📥 Baixando arquivo"
    UPLOADING_THE_FILE = "📤 Enviando arquivo: **{{ new_file_name }}**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Iniciando tarefa de renomeação**\n"
        "🆔 ID: `{{ uid }}`\n\n"
        "👤 **Usuário:** @{{ username }}\n"
        "📛 **Nome:** {{ name }}\n"
        "🆔 **ID:** `<code>{{ user_id }}</code>`\n"
        "📂 **Arquivo:** `<code>{{ file_name }}</code>`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "✅ **Tarefa adicionada**\n\n"
        "👤 **Usuário:** @{{ username }}\n"
        "📛 **Nome:** {{ name }}\n"
        "🆔 **ID:** `<code>{{ user_id }}</code>`"
    )

    CAPTION_FOOT_NOTE = (
        "☄️ **NOTA:** Defina legenda com `/setcaption` seguido do texto.\n"
        "📂 Use `<code>{file_name}</code>` para inserir o nome do arquivo."
    )

    DELETE_CAPTION = "🗑 Remover legenda"
    CLOSE = "❌ Fechar"

    CAPTION_CURRENT = "📝 **Legenda atual:** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **Nenhuma legenda definida.**"
    CAPTION_SET = "✅ **Legenda atualizada:** {{ caption }}"
    CAPTION_DELETED = "🗑 **Legenda removida.**"

    RENAME_ADDED_TO_QUEUE = (
        "📥 **Tarefa na fila**\n"
        "🆔 **DC ID:** {{ dc_id }}\n"
        "👻 **Mídia ID:** {{ media_id }}"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **Status da fila:**\n"
        "☄️ **Tarefas:** {{ total_tasks }}\n"
        "⚡ **Capacidade:** {{ queue_capacity }}\n"
        "⏳ **Processando:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **Sua tarefa está em execução**\n"
        "🆔 **ID:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Sua posição na fila:** {{ task_number }}\n"
        "🆔 **ID:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👻 **Você foi removido. Não pode usar este bot.**"
    USER_NOT_PARTICIPANT = "👻 **Junte-se ao chat para usar este bot.**"
    JOIN_CHANNEL = "🔗 Canal de atualizações"

    MODE_INITIAL_MSG = (
        "📂 **Modo de saída:**\n\n"
        "1️⃣ **Mesmo formato do original**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Forçar como documento**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **Enviar como mídia**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "👻 **Selecione o modo:**\n"
        "🅰️ **Renomear com comando**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Renomear automaticamente**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 Responda a uma imagem para definir como miniatura."
    THUMB_SET_SUCCESS = "✅ **Miniatura definida.**"
    THUMB_NOT_FOUND = "⚠️ **Nenhuma miniatura.**"
    THUMB_CLEARED = "🗑 **Miniatura removida.**"

    HELP_STR = (
        "📖 **Comandos:**\n"
        "`{{ startcmd }}` - ✅ Verificar status\n"
        "`{{ renamecmd }}` - ✍️ Renomear arquivos\n"
        "`{{ filterscmd }}` - ⚙️ Gerenciar filtros\n"
        "`{{ setthumbcmd }}` - 📷 Definir miniatura\n"
        "`{{ getthumbcmd }}` - 📸 Ver miniatura\n"
        "`{{ clrthumbcmd }}` - ❌ Remover miniatura\n"
        "`{{ modecmd }}` - 🔄 Modos de saída:\n"
        "    - 📝 Formato original\n"
        "    - 📂 Documento\n"
        "    - 🎥 Mídia\n\n"
        "    🔄 Modos de renomeação:\n"
        "    - 🏷 Com comando\n"
        "    - ✨ Automático\n\n"
        "`{{ queuecmd }}` - 📊 Fila de tarefas\n"
        "`{{ setcaptioncmd }}` - 📝 Definir legenda\n"
        "`{{ helpcmd }}` - 📖 Ajuda\n"
        "`{{ pingcmd }}` - 🎈 Ping\n"
        "`{{ infocmd }}` - 🧑‍💻 Informações\n"
        "`{{ profilecmd }}` - ☄️ Estatísticas\n"
        "`{{ statuscmd }}` - 🗿 Status\n"
        "`{{ statscmd }}` - 👻 Estatísticas globais\n"
        "`{{ broadcastcmd }}` - ☄️ Broadcast\n"
        "`{{ leaderboardcmd }}` - 👻 Ranking\n"
        "`{{ setlanguagecmd }}` - 🌐 Idioma"
    )

    CURRENT_LOCALE = "🌐 **Idioma atual:** {{ user_locale }}"


