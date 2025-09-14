from dataclasses import dataclass
import random

@dataclass
class SpanishTranslations:
    LANGUAGE_NAME = "🇪🇸 Español"
    LANGUAGE_CODE = "es"

    WRONG_VALUE_ERROR = "❌ ¡Ups! Valor inválido para {{ variable_name }}. ¡Intenta de nuevo! 🤷‍♀️"

    START_MSG = (
    "✨ **¡Hola, mago de archivos!** ✨\n\n"
    "Soy **Auto Rename Bot** 🪄, tu asistente mágico para renombrar archivos!\n\n"
    "🔥 **Por qué me amarás:**\n"
    "- Renombro archivos con ✨ brillo y precisión\n"
    "- Súper rápido ⚡ y seguro 🔒\n"
    "- ¡Soporta TODOS los tipos de archivo! 📂🎵🎬\n\n"
    "¡Solo envíame un archivo y hagamos magia! 🎩\n\n"
    "🚀 **Consejo Pro:** Usa /mode para el modo ninja de auto-renombrado (¡debes agregar /filters)!\n"
    "¿Necesitas ayuda? /help te respalda!\n\n"
    "🛸 **Desarrollado por** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "❗ ¡Renombrado cancelado! ¡Puf! ✨ (¡Próximamente actualizaciones!)"

    RENAME_NO_FILTER_MATCH = (
        "🔮 **¡Ups! ¡No hay coincidencia de filtros!**\n\n"
        "Intenté usar filtros pero no encontré nada 🎩🐇\n"
        "Gestiona tus filtros con /filters ✏️"
    )

    RENAME_FILTER_MATCH_USED = (
        "🎯 **¡Poder de filtros activado!**\n"
        "Usando filtros ya que no especificaste un nombre\n"
        "Ajústalos con /filters ⚙️"
    )

    RENAME_NOFLTR_NONAME = (
        "📝 **¡NO se encontraron filtros!**\n\n"
        "Por favor agrega /filters 🎨 para filtros de auto-renombrado."
    )

    RENAME_CANCEL = "❌ No, cancelemos esto ✌️"

    RENAMING_FILE = "🌀 **Transformación de archivo en progreso...**"

    DL_RENAMING_FILE = "📥 **Descargando tu tesoro digital...**"

    RENAME_ERRORED_REPORT = "💥 **¡Ay! ¡Algo se rompió!** Por favor reporta esto 🚨"

    RENAME_CANCEL_BY_USER = "🙅‍♂️ **¡Agitaste la varita de cancelar!** ✨"

    FLTR_ADD_LEFT_STR = "➕ Filtro agregado: `<code>{{ text_1 }}</code>` **a la IZQUIERDA**."
    FLTR_ADD_RIGHT_STR = (
        "➕ Filtro agregado: `<code>{{ text_1 }}</code>` **a la DERECHA**."
    )
    FLTR_RM_STR = "❌ Filtro eliminado: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = (
        "🔄 Filtro reemplazado: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."
    )

    CURRENT_FLTRS = "🎛️ **Tu Panel de Filtros:**"
    ADD_FLTR = "➕ Agregar Filtro"
    RM_FLTR = "❌ Eliminar Filtro"

    FILTERS_INTRO = (
        "🛠 **Guía de Filtros:**\n"
        "Hay 3 tipos de filtros:\n\n"
        "🔄 **Filtro de Reemplazo:** Reemplaza una palabra por otra.\n"
        "➕ **Filtro de Adición:** Agrega una palabra al inicio o final.\n"
        "❌ **Filtro de Eliminación:** Elimina una palabra del nombre de archivo."
    )

    ADD_REPLACE_FLTR = "➕ Agregar Filtro de Reemplazo"
    ADD_ADDITION_FLTR = "➕ Agregar Filtro de Adición"
    ADD_REMOVE_FLTR = "➕ Agregar Filtro de Eliminación"
    BACK = "🔙 Atrás"

    REPALCE_FILTER_INIT_MSG = "✍️ Envía el formato: `<code>que_reemplazar | reemplazo</code>` o /ignore para volver."

    NO_INPUT_FROM_USER = "🤷‍♂️ **Grillos...** ¡No se detectó entrada!"
    INPUT_IGNORE = "👍 **¡Ignorado!**"
    WRONG_INPUT_FORMAT = "🤦‍♂️ **¡Ups!** ¡Formato incorrecto! ¡Revisa el formato proporcionado e intenta de nuevo!"
    REPLACE_FILTER_SUCCESS = (
        "✅ **Filtro de reemplazo agregado:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ Ingresa el texto a agregar dentro de `<code>|</code>`\n"
        "Ejemplo: `<code>| texto a agregar |</code>`\n"
        "o /ignore para volver."
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ Filtro agregado: `<code>{{ text_1 }}</code>` **a la IZQUIERDA**."
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ Filtro agregado: `<code>{{ text_1 }}</code>` **a la DERECHA**."
    )

    ADDITION_LEFT = "🔄 Adición a la IZQUIERDA"
    ADDITION_RIGHT = "🔄 Adición a la DERECHA"

    ADDITION_POSITION_PROMPT = "🧙‍♂️ **¿Dónde quieres agregar el texto?**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ Ingresa el texto que quieres eliminar o /ignore para volver."
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **Filtro de eliminación agregado:** se eliminará `<code>{{ text_1 }}</code>`."
    )

    RENAME_THEMES_DOWNLOADING = [
        "🎩 ¡Descarga completa! Preparando magia...",
        "📦 ¡Archivo adquirido! Listo para hechicería de nombres...",
        "✨ ¡Descarga exitosa! ¡Comenzando encantamientos...",
        "⚡ ¡Datos asegurados! Motores de renombrado encendiendo...",
        "💾 ¡Archivo capturado! Preparando para glorioso renacimiento..."
    ]

    RENAME_THEMES_UPLOADING = [
        "🚀 **¡Despegue!** ¡Archivo renombrado lanzado!",
        "🎉 **¡Ta-dá!** ¡Tu archivo con nuevo nombre está listo!",
        "📤 ¡Subida completa! ¡Disfruta tu obra maestra!",
        "🌟 ¡Metamorfosis de archivo completa!",
        "🏁 ¡Carrera terminada! Tu archivo cruzó la línea de meta!"
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 **¡Abortar!** ¡Hechizo de descarga interrumpido!",
        "🚧 ¡Ups! ¡Detuviste el tren de descarga!",
        "🎭 ¡El espectáculo terminó antes de comenzar!",
        "📵 ¡Conexión de descarga terminada!",
        "👋 ¡Abandonaste la descarga! ¡Adiós!"
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "✋ **¡Espera!** ¡Subida detenida a mitad de vuelo!",
        "🚫 ¡Sin entrega hoy! ¡Subida cancelada!",
        "🌪️ ¡Tornado de subida disipado!",
        "📴 ¡Conexión perdida en el vacío!",
        "🤷‍♂️ ¡Cambiaste de opinión! ¡Subida abortada!"
    ]

    REPLY_TO_MEDIA = "📎 **¡Pssst!** ¡Responde `/rename` a un archivo!"

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "💥 **¡Kaboom!** ¡Hechizo de renombrado falló!"

    DOWNLOADING_THE_FILE = "📥 **Obteniendo tu archivo...**"
    UPLOADING_THE_FILE = "📤 **Lanzando:** `{{ new_file_name }}` 🚀"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Misión de Renombrado Iniciada**\n"
        "🆔 ID de Misión: `{{ uid }}`\n\n"
        "👤 **Agente:** @{{ username }}\n"
        "📛 **Nombre en Clave:** {{ name }}\n"
        "🪪 **ID:** `{{ user_id }}`\n"
        "📜 **Archivo:** `{{ file_name }}`\n\n"
        "`⚡ ¡Hiperimpulso activado!`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "📥 **Misión de Renombrado en Cola**\n\n"
        "👤 **Agente:** @{{ username }}\n"
        "📛 **Nombre en Clave:** {{ name }}\n"
        "🪪 **ID:** `{{ user_id }}`\n\n"
        "`⏳ Esperando despliegue...`"
    )

    CAPTION_FOOT_NOTE = (
        "💡 **Consejo Pro:** ¡Usa /setcaption para agregar estilo!\n"
        "✨ ¡Usa `/setcaption {file_name}` para auto-completar el nombre de archivo en el pie de foto!"
    )

    DELETE_CAPTION = "🗑️ Eliminar Pie de Foto"
    CLOSE = "🚪 Salir"

    CAPTION_CURRENT = "📝 **Pie de Foto Actual:** {{ caption }}"
    CAPTION_NOT_SET = "🫗 **¡Pie de foto vacío!** Tan solitario..."
    CAPTION_SET = "✅ **Nuevo Pie de Foto:** {{ caption }}"
    CAPTION_DELETED = "🗑️ **Pie de foto eliminado exitosamente.**"

    RENAME_ADDED_TO_QUEUE = (
        "📊 **Renombrado en Cola**\n"
        "🆔 **ID DC:** {{ dc_id }}\n"
        "📦 **ID Media:** {{ media_id }}\n\n"
        "`⏳ Paciencia, joven padawan...`"
    )

    RENAME_QUEUE_STATUS = (
        "📈 **Estadísticas de Cola:**\n"
        "📊 **Total de Tareas:** {{ total_tasks }}\n"
        "⚡ **Capacidad:** {{ queue_capacity }}\n"
        "⏳ **Procesando:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **¡Tu archivo está siendo encantado!**\n"
        "🆔 **ID de Tarea:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Tu lugar en la fila:** {{ task_number }}\n"
        "🆔 **ID de Tarea:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👢 **¡Has sido expulsado!** ¡No hay bot para ti!"
    USER_NOT_PARTICIPANT = (
        "🔒 **¡Alerta de Club Secreto!**\n\n"
        "¡Únete a nuestro canal para desbloquear la magia!\n\n"
        "`🦄 Solo unicornios más allá de este punto`"
    )
    
    JOIN_CHANNEL = "🔗 Unirse al Club Secreto"

    MODE_INITIAL_MSG = (
        "🎛️ **Selector de Modo de Salida:**\n\n"
        "1️⃣ **Mantener formato original**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Forzar modo documento**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **Modo media general**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "✨ **Estilo de Renombrado:**\n"
        "🅰️ **Renombrado por comando**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Auto-renombrado**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣ Modo OG"
    MODE_SET_1 = "2️⃣ Modo Documento"
    MODE_SET_2 = "3️⃣ Modo Media"
    COMMAND_MODE_SET_3 = "🅰️ Comando"
    COMMAND_MODE_SET_4 = "🅱️ Auto"

    THUMB_REPLY_TO_MEDIA = "🖼️ **Responde a una imagen** para establecer como miniatura"
    THUMB_SET_SUCCESS = "✅ **¡Miniatura establecida!**"
    THUMB_NOT_FOUND = "🕵️‍♂️ **¡No se detectó miniatura!**"
    THUMB_CLEARED = "🧹 **¡Miniatura eliminada!**"

    HELP_STR = (
        "📚 **Libro de Hechizos Mágicos:**\n"
        "`{{ startcmd }}` - ¡Verifica si estoy vivo! 💓\n"
        "`{{ renamecmd }}` - ¡Renombra archivos como un jefe! 🎩\n"
        "`{{ filterscmd }}` - ¡Personaliza tus filtros de renombrado! ✨\n"
        "`{{ setthumbcmd }}` - ¡Establece una miniatura permanente! 🖼️\n"
        "`{{ getthumbcmd }}` - ¡Mira la miniatura actual! 👀\n"
        "`{{ clrthumbcmd }}` - ¡Elimina miniatura! 🗑️\n"
        "`{{ modecmd }}` - Cambia modos de salida:\n"
        "   - 📝 Formato original\n"
        "   - 📂 Forzar documento\n"
        "   - 🎥 Modo media\n\n"
        "   Cambia estilos de renombrado:\n"
        "   - 🏷️ Basado en comando\n"
        "   - 🤖 Auto-renombrado (debe agregar /filters)\n\n"
        "`{{ queuecmd }}` - Revisa cola de renombrado 📊\n"
        "`{{ setcaptioncmd }}` - Establece pies de foto elegantes 🎨\n"
        "`{{ helpcmd }}` - ¡Este libro mágico! 📖\n"
        "`{{ pingcmd }}` - ¡Ping-pong! 🏓\n"
        "`{{ infocmd }}` - ¡Especificaciones del bot! 🤖\n"
        "`{{ profilecmd }}` - ¡Tus estadísticas! 📈\n"
        "`{{ statuscmd }}` - ¡Signos vitales del bot! 💓\n"
        "`{{ statscmd }}` - ¡Números globales! 🌍\n"
        "`{{ broadcastcmd }}` - ¡Mega-anuncio! 📢\n"
        "`{{ leaderboardcmd }}` - ¡Top usuarios! 🏆\n"
        "`{{ setlanguagecmd }}` - ¡Cambiar idioma! 🌐"
    )

    CURRENT_LOCALE = "🌍 **Tu idioma:** {{ user_locale }}"
