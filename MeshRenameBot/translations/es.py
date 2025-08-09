from dataclasses import dataclass
import random

@dataclass
class SpanishTranslations:
    LANGUAGE_NAME = "🇪🇸 Español"
    LANGUAGE_CODE = "es"

    WRONG_VALUE_ERROR = "❌ Valor inválido ingresado para la variable {{ variable_name }}."

    START_MSG = (
    "¡Hola! 👋\n"
    "Soy el **Bot de Renombrado Automático**, tu asistente para renombrar archivos en Telegram fácilmente.\n\n"
    "✨ **Características principales:**\n"
    "- Renombra archivos con nombres y extensiones personalizadas.\n"
    "- Rápido, seguro y fácil de usar.\n"
    "- Soporta una amplia variedad de tipos de archivos.\n\n"
    "¡Simplemente envíame un archivo y te guiaré en el proceso de renombrado!\n\n"
    "¡Comencemos! Usa /mode para activar el renombrado automático, **Renombrar sin comando** 🚀\n"
    "Envía /help para más información.\n\n"
    "🚀 **Desarrollado por** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "⚠️ El renombrado ha sido **cancelado**. Se actualizará pronto."

    RENAME_NO_FILTER_MATCH = (
        "🚫 **NO COINCIDEN FILTROS - CANCELANDO RENOMBRADO**\n\n"
        "🔍 Usando filtros para renombrar ya que no se especificó un nombre.\n"
        "👻 Gestiona tus filtros con /filters."
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ Usando filtros para renombrar ya que no se especificó un nombre.\n"
        "👻 Gestiona tus filtros con /filters."
    )

    RENAME_NOFLTR_NONAME = (
        "✍️ Ingresa el nuevo nombre de archivo en formato:\n"
        "```/rename mi_nuevo_archivo.extensión```\n"
        "o usa `/filters` para configurar filtros de renombrado."
    )

    RENAME_CANCEL = "❌ Cancelar este renombrado."

    RENAMING_FILE = "🔄 Renombrando el archivo... Por favor espera."

    DL_RENAMING_FILE = "📥 Descargando el archivo... Por favor espera."

    RENAME_ERRORED_REPORT = "❗ El descarga encontró un error. Reporta este problema."

    RENAME_CANCEL_BY_USER = "🚫 **Cancelado por el usuario.**"

    FLTR_ADD_LEFT_STR = "➕ Filtro añadido: `<code>{{ text_1 }}</code>` **a la IZQUIERDA**."
    FLTR_ADD_RIGHT_STR = (
        "➕ Filtro de adición: `<code>{{ text_1 }}</code>` **a la DERECHA**."
    )
    FLTR_RM_STR = "❌ Eliminar filtro: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = (
        "🔄 Reemplazar filtro: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."
    )

    CURRENT_FLTRS = "⚙️ **Tus Filtros Actuales:**"
    ADD_FLTR = "➕ Añadir Filtro"
    RM_FLTR = "❌ Eliminar Filtro"

    FILTERS_INTRO = (
        "🛠 **Guía de Filtros:**\n"
        "Hay 3 tipos de filtros:\n\n"
        "🔄 **Filtro de Reemplazo:** Reemplaza una palabra por otra.\n"
        "➕ **Filtro de Adición:** Añade una palabra al inicio o final.\n"
        "❌ **Filtro de Eliminación:** Elimina una palabra del nombre de archivo."
    )

    ADD_REPLACE_FLTR = "➕ Añadir Filtro de Reemplazo"
    ADD_ADDITION_FLTR = "➕ Añadir Filtro de Adición"
    ADD_REMOVE_FLTR = "➕ Añadir Filtro de Eliminación"
    BACK = "🔙 Atrás"

    REPALCE_FILTER_INIT_MSG = "✍️ Envía el formato: `<code>que_reemplazar | reemplazo</code>` o `/ignore` para volver."

    NO_INPUT_FROM_USER = "⚠️ No se recibió entrada de tu parte."
    INPUT_IGNORE = "✅ **Ignorado**."
    WRONG_INPUT_FORMAT = "❌ Formato inválido. Revisa el formato proporcionado."
    REPLACE_FILTER_SUCCESS = (
        "✅ **Filtro de reemplazo añadido:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ Ingresa el texto a añadir dentro de `<code>|</code>`\n"
        "Ejemplo: `<code>| texto a añadir |</code>`\n"
        "o `/ignore` para volver."
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ Filtro añadido: `<code>{{ text_1 }}</code>` **a la IZQUIERDA**."
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ Filtro añadido: `<code>{{ text_1 }}</code>` **a la DERECHA**."
    )

    ADDITION_LEFT = "🔄 Adición a la IZQUIERDA"
    ADDITION_RIGHT = "🔄 Adición a la DERECHA"

    ADDITION_POSITION_PROMPT = "📍 **¿Dónde quieres añadir el texto?**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ Ingresa el texto que quieres eliminar o `/ignore` para volver."
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **Filtro de eliminación añadido:** se eliminará `<code>{{ text_1 }}</code>`."
    )

    RENAME_THEMES_DOWNLOADING = [
        "✅ Descarga completada. Iniciando magia de renombrado...",
        "📦 ¡Archivo obtenido! Listo para darle un nuevo nombre...",
        "🪄 Descarga finalizada. ✨ Que comience el ritual de renombrado...",
        "🔧 Datos adquiridos. Motor de renombrado en marcha...",
        "💾 Guardado y sellado. Ahora a renombrar con estilo...",
    ]

    RENAME_THEMES_UPLOADING = [
        "✅ ¡Todo renombrado y listo! Carga completada.",
        "🚀 Archivo renombrado exitosamente y lanzado.",
        "📤 Carga finalizada. ¡Tu obra maestra renombrada está en línea!",
        "🌟 Renombrado de archivo finalizado. ¡Entregado al cosmos!",
        "📁 Tarea completada. El archivo asciende renombrado.",
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 Descarga detenida. El sueño del renombrado se desvanece...",
        "🚫 Cortaste la corriente. Descarga abortada.",
        "❌ Operación cancelada a mitad del vuelo. No se obtuvo archivo.",
        "📴 Renombrado cancelado durante la descarga. Misión suspendida.",
        "👋 Usuario canceló durante la descarga. Adiós, archivo.",
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "🛑 Carga cancelada. El archivo se queda local y no querido.",
        "🚫 Rebrandeo revertido. Carga terminada.",
        "❌ Etapa final interrumpida. Renombrado abandonado.",
        "📴 Carga vetada. Archivo renombrado no va a ninguna parte.",
        "👋 Usuario dijo 'no' durante la carga. Archivo retirado.",
    ]

    REPLY_TO_MEDIA = "📂 Responde con `/rename` a un archivo multimedia."

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "❗ El proceso de renombrado encontró un error."

    DOWNLOADING_THE_FILE = "📥 Descargando el archivo"
    UPLOADING_THE_FILE = "📤 Subiendo el archivo: **{{ new_file_name }}**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Ejecución Iniciada para Tarea de Renombrado**\n"
        "🆔 ID de Tarea: `{{ uid }}`\n\n"
        "👤 **Usuario:** @{{ username }}\n"
        "📛 **Nombre:** {{ name }}\n"
        "🆔 **ID de Usuario:** `<code>{{ user_id }}</code>`\n"
        "📂 **Nombre de Archivo:** `<code>{{ file_name }}</code>`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "✅ **Tarea de Renombrado Añadida**\n\n"
        "👤 **Usuario:** @{{ username }}\n"
        "📛 **Nombre:** {{ name }}\n"
        "🆔 **ID de Usuario:** `<code>{{ user_id }}</code>`"
    )

    CAPTION_FOOT_NOTE = (
        "☄️ **NOTA:** Puedes configurar el pie de foto usando `/setcaption` seguido de tu texto deseado.\n"
        "📂 Usa `<code>{file_name}</code>` para insertar dinámicamente el nombre del archivo renombrado en el pie de foto."
    )

    DELETE_CAPTION = "🗑 Eliminar Pie de Foto"
    CLOSE = "❌ Cerrar"

    CAPTION_CURRENT = "📝 **Tu Pie de Foto Actual:** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **No hay pie de foto configurado.**"
    CAPTION_SET = "✅ **Pie de foto actualizado a:** {{ caption }}"
    CAPTION_DELETED = "🗑 **Pie de foto eliminado exitosamente.**"

    RENAME_ADDED_TO_QUEUE = (
        "📥 **Tarea de Renombrado Añadida a la Cola**\n"
        "🆔 **ID de DC:** {{ dc_id }}\n"
        "👻 **ID de Media:** {{ media_id }}"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **Estado de la Cola de Renombrado:**\n"
        "☄️ **Total de Tareas en Cola:** {{ total_tasks }}\n"
        "⚡ **Capacidad de Cola:** {{ queue_capacity }}\n"
        "⏳ **Procesando Actualmente:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **Tu Tarea se Está Ejecutando Actualmente**\n"
        "🆔 **ID de Tarea:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Posición de tu Tarea en Cola:** {{ task_number }}\n"
        "🆔 **ID de Tarea:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👻 **Has sido eliminado del chat. No puedes usar este bot.**"
    USER_NOT_PARTICIPANT = "👻 **Únete al chat requerido para usar este bot.**"
    JOIN_CHANNEL = "🔗 Unirse al Canal de Actualizaciones"

    MODE_INITIAL_MSG = (
        "📂 **Modo de Salida de Archivo:**\n\n"
        "1️⃣ **Mismo formato que el enviado**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Forzar como Documento**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **Subir como Media General**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "👻 **Selecciona el modo de renombrado:**\n"
        "🅰️ **Renombrar con comando**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Renombrar sin comando**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 Responde a una imagen para establecerla como miniatura."
    THUMB_SET_SUCCESS = "✅ **Miniatura configurada exitosamente.**"
    THUMB_NOT_FOUND = "⚠️ **No se encontró miniatura.**"
    THUMB_CLEARED = "🗑 **Miniatura eliminada exitosamente.**"

    HELP_STR = (
        "📖 **Comandos del Bot:**\n"
        "`{{ startcmd }}` - ✅ Verificar si el bot está funcionando.\n"
        "`{{ renamecmd }}` - ✍️ Responde a un archivo multimedia con `/rename nombre.extension` para renombrarlo.\n"
        "`{{ filterscmd }}` - ⚙️ Gestionar tus filtros de renombrado.\n"
        "`{{ setthumbcmd }}` - 📷 Configurar miniatura permanente (responde a una imagen).\n"
        "`{{ getthumbcmd }}` - 📸 Obtener la miniatura actual.\n"
        "`{{ clrthumbcmd }}` - ❌ Eliminar la miniatura configurada.\n"
        "`{{ modecmd }}` - 🔄 Cambiar entre 3 modos de salida:\n"
        "    - 📝 Mismo formato que el enviado.\n"
        "    - 📂 Documento forzado.\n"
        "    - 🎥 Media General (video/audio transmisible).\n\n"
        "    🔄 Cambiar entre modos de renombrado:\n"
        "    - 🏷 Renombrar **con comando**.\n"
        "    - ✨ Renombrar **sin comando/auto Renombrar**.\n\n"
        "`{{ queuecmd }}` - 📊 Ver estado de la cola de renombrado.\n"
        "`{{ setcaptioncmd }}` - 📝 Configurar pie de foto para archivos renombrados.\n"
        "`{{ helpcmd }}` - 📖 Mostrar este mensaje de ayuda.\n"
        "`{{ pingcmd }}` - 🎈Ping al Bot.\n"
        "`{{ infocmd }}` - 🧑‍💻 Ver información del bot.\n"
        "`{{ profilecmd }}` - ☄️ Tus estadísticas de uso.\n"
        "`{{ statuscmd }}` - 🗿 Estado del Bot.\n"
        "`{{ statscmd }}` - 👻 Estadísticas globales del bot.\n"
        "`{{ broadcastcmd }}` - ☄️Hacer un broadcast.\n"
        "`{{ leaderboardcmd }}` - 👻 Tabla de clasificación de usuarios.\n"
        "`{{ setlanguagecmd }}` - 🌐 Cambiar el idioma del bot."
    )

    CURRENT_LOCALE = "🌐 **Tu idioma actual:** {{ user_locale }}"


