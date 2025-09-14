from dataclasses import dataclass
import random

@dataclass
class PortugueseTranslations:
    LANGUAGE_NAME = "🇵🇹 Português"
    LANGUAGE_CODE = "pt"

    WRONG_VALUE_ERROR = "❌ Oops! Valor inválido para {{ variable_name }}. Tente novamente! 🤷‍♀️"

    START_MSG = (
    "✨ **Olá, mágico de arquivos!** ✨\n\n"
    "Eu sou o **Bot de Renomeação Automática** 🪄, seu assistente mágico para renomear arquivos!\n\n"
    "🔥 **Por que você vai me amar:**\n"
    "- Renomeie arquivos com ✨ brilho e precisão\n"
    "- Super rápido ⚡ e seguro 🔒\n"
    "- Suporta TODOS os tipos de arquivo! 📂🎵🎬\n\n"
    "Apenas me envie um arquivo e vamos fazer mágica! 🎩\n\n"
    "🚀 **Dica Pro:** Use /mode para o modo ninja de renomeação automática (deve adicionar /filters)!\n"
    "Precisa de ajuda? /help tem você coberto!\n\n"
    "🛸 **Desenvolvido por** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "❗ Renomeação cancelada! Puf! ✨ (Atualizações em breve!)"

    RENAME_NO_FILTER_MATCH = (
        "🔮 **Ops! Nenhum filtro corresponde!**\n\n"
        "Tentei usar filtros mas não encontrei nada 🎩🐇\n"
        "Gerencie seus filtros com /filters ✏️"
    )

    RENAME_FILTER_MATCH_USED = (
        "🎯 **Poder do filtro ativado!**\n"
        "Usando filtros já que você não especificou um nome\n"
        "Ajuste-os com /filters ⚙️"
    )

    RENAME_NOFLTR_NONAME = (
        "📝 **NENHUM filtro encontrado!**\n\n"
        "Por favor adicione /filters 🎨 para filtros de renomeação automática."
    )

    RENAME_CANCEL = "❌ Não, vamos cancelar isso ✌️"

    RENAMING_FILE = "🌀 **Transformação de arquivo em andamento...**"

    DL_RENAMING_FILE = "📥 **Baixando seu tesouro digital...**"

    RENAME_ERRORED_REPORT = "💥 **Eita! Algo quebrou!** Por favor reporte isso 🚨"

    RENAME_CANCEL_BY_USER = "🙅‍♂️ **Você acenou a varinha de cancelamento!** ✨"

    FLTR_ADD_LEFT_STR = "➕ Filtro adicionado: `<code>{{ text_1 }}</code>` **à ESQUERDA**."
    FLTR_ADD_RIGHT_STR = (
        "➕ Filtro adicionado: `<code>{{ text_1 }}</code>` **à DIREITA**."
    )
    FLTR_RM_STR = "❌ Filtro removido: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = (
        "🔄 Filtro substituído: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."
    )

    CURRENT_FLTRS = "🎛️ **Seu Painel de Filtros:**"
    ADD_FLTR = "➕ Adicionar Filtro"
    RM_FLTR = "❌ Remover Filtro"

    FILTERS_INTRO = (
        "🛠 **Guia de Filtros:**\n"
        "Existem 3 tipos de filtros:\n\n"
        "🔄 **Filtro de Substituição:** Substitui uma palavra por outra.\n"
        "➕ **Filtro de Adição:** Adiciona uma palavra no início ou final.\n"
        "❌ **Filtro de Remoção:** Remove uma palavra do nome do arquivo."
    )

    ADD_REPLACE_FLTR = "➕ Adicionar Filtro de Substituição"
    ADD_ADDITION_FLTR = "➕ Adicionar Filtro de Adição"
    ADD_REMOVE_FLTR = "➕ Adicionar Filtro de Remoção"
    BACK = "🔙 Voltar"

    REPALCE_FILTER_INIT_MSG = "✍️ Envie o formato: `<code>o_que_substituir | substituição</code>` ou /ignore para voltar."

    NO_INPUT_FROM_USER = "🤷‍♂️ **Grilos...** Nenhuma entrada detectada!"
    INPUT_IGNORE = "👍 **Ignorado!**"
    WRONG_INPUT_FORMAT = "🤦‍♂️ **Ops!** Formato errado! Verifique o formato fornecido e tente novamente!"
    REPLACE_FILTER_SUCCESS = (
        "✅ **Filtro de substituição adicionado:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ Digite o texto a adicionar dentro de `<code>|</code>`\n"
        "Exemplo: `<code>| texto para adicionar |</code>`\n"
        "ou /ignore para voltar."
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ Filtro adicionado: `<code>{{ text_1 }}</code>` **à ESQUERDA**."
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ Filtro adicionado: `<code>{{ text_1 }}</code>` **à DIREITA**."
    )

    ADDITION_LEFT = "🔄 Adição à ESQUERDA"
    ADDITION_RIGHT = "🔄 Adição à DIREITA"

    ADDITION_POSITION_PROMPT = "🧙‍♂️ **Onde você quer adicionar o texto?**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ Digite o texto que deseja remover ou /ignore para voltar."
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **Filtro de remoção adicionado:** `<code>{{ text_1 }}</code>` será removido."
    )

    RENAME_THEMES_DOWNLOADING = [
        "🎩 Download completo! Preparando mágica...",
        "📦 Arquivo adquirido! Pronto para feitiçaria de nomeação...",
        "✨ Download bem-sucedido! Encantamentos começando...",
        "⚡ Dados seguros! Motores de renomeação ligando...",
        "💾 Arquivo capturado! Pronto para renascimento glorioso..."
    ]

    RENAME_THEMES_UPLOADING = [
        "🚀 **Decolagem!** Arquivo renomeado lançado!",
        "🎉 **Tá-dá!** Seu arquivo com novo nome está pronto!",
        "📤 Upload completo! Aproveite sua obra-prima!",
        "🌟 Metamorfose de arquivo completa!",
        "🏁 Corrida terminada! Seu arquivo cruzou a linha de chegada!"
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 **Abortar!** Feitiço de download interrompido!",
        "🚧 Ops! Você parou o trem de download!",
        "🎭 O show acabou antes de começar!",
        "📵 Conexão de download terminada!",
        "👋 Você abandonou o download! Tchau!"
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "✋ **Espere!** Upload parado no meio do voo!",
        "🚫 Entrega cancelada hoje! Upload cancelado!",
        "🌪️ Tornado de upload dissipado!",
        "📴 Conexão perdida no vácuo!",
        "🤷‍♂️ Você mudou de ideia! Upload abortado!"
    ]

    REPLY_TO_MEDIA = "📎 **Pssst!** Responda `/rename` a um arquivo!"

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "💥 **Kaboom!** Feitiço de renomeação falhou!"

    DOWNLOADING_THE_FILE = "📥 **Buscando seu arquivo...**"
    UPLOADING_THE_FILE = "📤 **Lançando:** `{{ new_file_name }}` 🚀"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Missão de Renomeação Iniciada**\n"
        "🆔 ID da Missão: `{{ uid }}`\n\n"
        "👤 **Agente:** @{{ username }}\n"
        "📛 **Codinome:** {{ name }}\n"
        "🪪 **ID:** `{{ user_id }}`\n"
        "📜 **Arquivo:** `{{ file_name }}`\n\n"
        "`⚡ Hyperdrive engatado!`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "📥 **Missão de Renomeação na Fila**\n\n"
        "👤 **Agente:** @{{ username }}\n"
        "📛 **Codinome:** {{ name }}\n"
        "🪪 **ID:** `{{ user_id }}`\n\n"
        "`⏳ Aguardando implantação...`"
    )

    CAPTION_FOOT_NOTE = (
        "💡 **Dica Pro:** Use /setcaption para adicionar estilo!\n"
        "✨ Use `/setcaption {file_name}` para preencher automaticamente o nome do arquivo na legenda!"
    )

    DELETE_CAPTION = "🗑️ Excluir Legenda"
    CLOSE = "🚪 Sair"

    CAPTION_CURRENT = "📝 **Legenda Atual:** {{ caption }}"
    CAPTION_NOT_SET = "🫗 **Legenda vazia!** Tão solitária..."
    CAPTION_SET = "✅ **Nova Legenda:** {{ caption }}"
    CAPTION_DELETED = "🗑️ **Legenda excluída com sucesso.**"

    RENAME_ADDED_TO_QUEUE = (
        "📊 **Renomeação na Fila**\n"
        "🆔 **ID DC:** {{ dc_id }}\n"
        "📦 **ID Mídia:** {{ media_id }}\n\n"
        "`⏳ Paciência, jovem padawan...`"
    )

    RENAME_QUEUE_STATUS = (
        "📈 **Status da Fila:**\n"
        "📊 **Total de Tarefas:** {{ total_tasks }}\n"
        "⚡ **Capacidade:** {{ queue_capacity }}\n"
        "⏳ **Processando:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **Seu arquivo está sendo enfeitiçado!**\n"
        "🆔 **ID da Tarefa:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Sua posição na fila:** {{ task_number }}\n"
        "🆔 **ID da Tarefa:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👢 **Você foi expulso!** Nenhum bot para você!"
    USER_NOT_PARTICIPANT = (
        "🔒 **Alerta de Clube Secreto!**\n\n"
        "Junte-se ao nosso canal para desbloquear a mágica!\n\n"
        "`🦄 Apenas unicórnios além deste ponto`"
    )
    
    JOIN_CHANNEL = "🔗 Entrar no Clube Secreto"

    MODE_INITIAL_MSG = (
        "🎛️ **Seletor de Modo de Saída:**\n\n"
        "1️⃣ **Manter formato original**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Forçar modo documento**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **Modo de mídia geral**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "✨ **Estilo de Renomeação:**\n"
        "🅰️ **Renomeação por comando**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Renomeação automática**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣ Modo OG"
    MODE_SET_1 = "2️⃣ Modo Documento"
    MODE_SET_2 = "3️⃣ Modo Mídia"
    COMMAND_MODE_SET_3 = "🅰️ Comando"
    COMMAND_MODE_SET_4 = "🅱️ Auto"

    THUMB_REPLY_TO_MEDIA = "🖼️ **Responda a uma imagem** para definir como miniatura"
    THUMB_SET_SUCCESS = "✅ **Miniatura bloqueada!**"
    THUMB_NOT_FOUND = "🕵️‍♂️ **Nenhuma miniatura detectada!**"
    THUMB_CLEARED = "🧹 **Miniatura varrida!**"

    HELP_STR = (
        "📚 **Livro de Feitiços Mágicos:**\n"
        "`{{ startcmd }}` - Verifique se estou vivo! 💓\n"
        "`{{ renamecmd }}` - Renomeie arquivos como um chefe! 🎩\n"
        "`{{ filterscmd }}` - Personalize seus filtros de renomeação! ✨\n"
        "`{{ setthumbcmd }}` - Defina uma miniatura permanente! 🖼️\n"
        "`{{ getthumbcmd }}` - Dê uma olhada na miniatura atual! 👀\n"
        "`{{ clrthumbcmd }}` - Exclua miniatura! 🗑️\n"
        "`{{ modecmd }}` - Alterar modos de saída:\n"
        "   - 📝 Formato original\n"
        "   - 📂 Forçar documento\n"
        "   - 🎥 Modo mídia\n\n"
        "   Alterar estilos de renomeação:\n"
        "   - 🏷️ Baseado em comando\n"
        "   - 🤖 Renomeação automática (deve adicionar /filters)\n\n"
        "`{{ queuecmd }}` - Verifique a fila de renomeação 📊\n"
        "`{{ setcaptioncmd }}` - Defina legendas chiques 🎨\n"
        "`{{ helpcmd }}` - Este livro mágico! 📖\n"
        "`{{ pingcmd }}` - Ping-pong! 🏓\n"
        "`{{ infocmd }}` - Especificações do bot! 🤖\n"
        "`{{ profilecmd }}` - Suas estatísticas! 📈\n"
        "`{{ statuscmd }}` - Sinais vitais do bot! 💓\n"
        "`{{ statscmd }}` - Números globais! 🌍\n"
        "`{{ broadcastcmd }}` - Mega-anúncio! 📢\n"
        "`{{ leaderboardcmd }}` - Melhores usuários! 🏆\n"
        "`{{ setlanguagecmd }}` - Alterar idioma! 🌐"
    )

    CURRENT_LOCALE = "🌍 **Seu idioma:** {{ user_locale }}"
