from dataclasses import dataclass
import random

@dataclass
class GermanTranslations:
    LANGUAGE_NAME = "🇩🇪 Deutsch"
    LANGUAGE_CODE = "de"

    WRONG_VALUE_ERROR = "❌ Ungültiger Wert für Variable {{ variable_name }} eingegeben."

    START_MSG = (
        "Hallo! 👋\n"
        "Ich bin der **Auto Rename Bot**, dein Helfer zum mühelosen Umbenennen von Dateien auf Telegram.\n\n"
        "✨ **Hauptfunktionen:**\n"
        "- Dateien mit benutzerdefinierten Namen und Endungen umbenennen.\n"
        "- Schnell, sicher und einfach zu bedienen.\n"
        "- Unterstützt eine Vielzahl von Dateitypen.\n\n"
        "Schick mir einfach eine Datei und ich führe dich durch den Umbenennungsprozess!\n\n"
        "Lass uns beginnen! Nutze /mode für den automatischen Modus, **Umbenennen ohne Befehl**🚀\n"
        "Sende /help für mehr Informationen.\n\n"
        "🚀 **Betrieben von** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "⚠️ Die Umbenennung wurde **abgebrochen**. Wird bald aktualisiert."

    RENAME_NO_FILTER_MATCH = (
        "🚫 **KEIN FILTER ENTSPRICHT - ABBRUCH DER UMBENENNUNG**\n\n"
        "🔍 Es werden Filter verwendet, da kein Name angegeben wurde.\n"
        "👻 Verwalte deine Filter mit /filters."
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ Filter werden verwendet, da kein Name angegeben wurde.\n"
        "👻 Verwalte deine Filter mit /filters."
    )

    RENAME_NOFLTR_NONAME = (
        "✍️ Gib den neuen Dateinamen im Format ein:\n"
        "```/rename mein_neuer_dateiname.erweiterung```\n"
        "oder verwende `/filters` um Umbenennungsfilter zu setzen."
    )

    RENAME_CANCEL = "❌ Umbenennung abbrechen."

    RENAMING_FILE = "🔄 Datei wird umbenannt... Bitte warten."

    DL_RENAMING_FILE = "📥 Datei wird heruntergeladen... Bitte warten."

    RENAME_ERRORED_REPORT = "❗ Beim Download ist ein Fehler aufgetreten. Bitte melde dieses Problem."

    RENAME_CANCEL_BY_USER = "🚫 **Vom Benutzer abgebrochen.**"

    FLTR_ADD_LEFT_STR = "➕ Filter hinzugefügt: `<code>{{ text_1 }}</code>` **links**."
    FLTR_ADD_RIGHT_STR = "➕ Filter hinzugefügt: `<code>{{ text_1 }}</code>` **rechts**."
    FLTR_RM_STR = "❌ Filter entfernt: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = "🔄 Filter ersetzt: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."

    CURRENT_FLTRS = "⚙️ **Aktive Filter:**"
    ADD_FLTR = "➕ Filter hinzufügen"
    RM_FLTR = "❌ Filter entfernen"

    FILTERS_INTRO = (
        "🛠 **Filter-Anleitung:**\n"
        "Es gibt 3 Filtertypen:\n\n"
        "🔄 **Ersetzungsfilter:** Ersetzt ein Wort durch ein anderes.\n"
        "➕ **Hinzufügefilter:** Fügt ein Wort am Anfang oder Ende ein.\n"
        "❌ **Entfernungsfilter:** Entfernt ein Wort aus dem Dateinamen."
    )

    ADD_REPLACE_FLTR = "➕ Ersetzungsfilter hinzufügen"
    ADD_ADDITION_FLTR = "➕ Hinzufügefilter hinzufügen"
    ADD_REMOVE_FLTR = "➕ Entfernungsfilter hinzufügen"
    BACK = "🔙 Zurück"

    REPALCE_FILTER_INIT_MSG = "✍️ Sende das Format: `<code>zu_ersetzendes_wort | ersatz</code>` oder `/ignore` zum Abbrechen."

    NO_INPUT_FROM_USER = "⚠️ Keine Eingabe erhalten."
    INPUT_IGNORE = "✅ **Ignoriert**."
    WRONG_INPUT_FORMAT = "❌ Ungültiges Format. Bitte überprüfe die Eingabe."
    REPLACE_FILTER_SUCCESS = "✅ **Ersetzungsfilter hinzugefügt:**\n`'{{ text_1 }}'` → `'{{ text_2 }}'`"

    ADDITION_FILTER_INIT_MSG = (
        "✍️ Gib den hinzuzufügenden Text innerhalb `<code>|</code>` ein\n"
        "Beispiel: `<code>| hinzuzufügender_text |</code>`\n"
        "oder `/ignore` zum Abbrechen."
    )

    ADDITION_FILTER_SUCCESS_LEFT = "✅ Filter hinzugefügt: `<code>{{ text_1 }}</code>` **links**."
    ADDITION_FILTER_SUCCESS_RIGHT = "✅ Filter hinzugefügt: `<code>{{ text_1 }}</code>` **rechts**."

    ADDITION_LEFT = "🔄 Links hinzufügen"
    ADDITION_RIGHT = "🔄 Rechts hinzufügen"

    ADDITION_POSITION_PROMPT = "📍 **Wo soll der Text hinzugefügt werden?**"

    REMOVE_FILTER_INIT_MSG = "✍️ Gib den zu entfernenden Text ein oder `/ignore` zum Abbrechen."

    REMOVE_FILTER_SUCCESS = "✅ **Entfernungsfilter hinzugefügt:** `<code>{{ text_1 }}</code>` wird entfernt."

    RENAME_THEMES_DOWNLOADING = [
        "✅ Download abgeschlossen. Starte Umbenennung...",
        "📦 Datei empfangen! Bereit für neuen Namen...",
        "🪄 Download fertig. ✨ Beginne Umbenennung...",
        "🔧 Daten empfangen. Umbenennung startet...",
        "💾 Gespeichert. Nun mit Stil umbenennen...",
    ]

    RENAME_THEMES_UPLOADING = [
        "✅ Umbenennung erfolgreich! Upload abgeschlossen.",
        "🚀 Datei erfolgreich umbenannt und gesendet.",
        "📤 Upload fertig. Deine umbenannte Datei ist online!",
        "🌟 Umbenennung abgeschlossen. Datei wurde versendet.",
        "📁 Aufgabe erledigt. Die Datei wurde umbenannt.",
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 Download abgebrochen. Umbenennung abgebrochen...",
        "🚫 Du hast den Download gestoppt.",
        "❌ Vorgang mitten im Download abgebrochen.",
        "📴 Umbenennung während des Downloads abgebrochen.",
        "👋 Nutzer hat den Download abgebrochen.",
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "🛑 Upload abgebrochen. Datei bleibt unverändert.",
        "🚫 Umbenennung rückgängig gemacht. Upload gestoppt.",
        "❌ Letzte Phase unterbrochen. Umbenennung abgebrochen.",
        "📴 Upload abgelehnt. Umbenannte Datei nicht gesendet.",
        "👋 Nutzer hat während des Uploads abgebrochen.",
    ]

    REPLY_TO_MEDIA = "📂 Antworte mit `/rename` auf eine Mediendatei."

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "❗ Fehler während der Umbenennung."

    DOWNLOADING_THE_FILE = "📥 Datei wird heruntergeladen"
    UPLOADING_THE_FILE = "📤 Datei wird hochgeladen: **{{ new_file_name }}**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Umbenennung gestartet**\n"
        "🆔 Aufgaben-ID: `{{ uid }}`\n\n"
        "👤 **Benutzername:** @{{ username }}\n"
        "📛 **Name:** {{ name }}\n"
        "🆔 **Nutzer-ID:** `<code>{{ user_id }}</code>`\n"
        "📂 **Dateiname:** `<code>{{ file_name }}</code>`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "✅ **Umbenennungsaufgabe hinzugefügt**\n\n"
        "👤 **Benutzername:** @{{ username }}\n"
        "📛 **Name:** {{ name }}\n"
        "🆔 **Nutzer-ID:** `<code>{{ user_id }}</code>`"
    )

    CAPTION_FOOT_NOTE = (
        "☄️ **HINWEIS:** Du kannst die Beschriftung mit `/setcaption` gefolgt von deinem Text setzen.\n"
        "📂 Verwende `<code>{file_name}</code>` um den Dateinamen dynamisch einzufügen."
    )

    DELETE_CAPTION = "🗑 Beschriftung löschen"
    CLOSE = "❌ Schließen"

    CAPTION_CURRENT = "📝 **Aktuelle Beschriftung:** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **Keine Beschriftung gesetzt.**"
    CAPTION_SET = "✅ **Beschriftung aktualisiert zu:** {{ caption }}"
    CAPTION_DELETED = "🗑 **Beschriftung erfolgreich gelöscht.**"

    RENAME_ADDED_TO_QUEUE = (
        "📥 **Umbenennung zur Warteschlange hinzugefügt**\n"
        "🆔 **DC-ID:** {{ dc_id }}\n"
        "👻 **Medien-ID:** {{ media_id }}"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **Warteschlangenstatus:**\n"
        "☄️ **Aufgaben in Warteschlange:** {{ total_tasks }}\n"
        "⚡ **Warteschlangenkapazität:** {{ queue_capacity }}\n"
        "⏳ **Aktuell in Bearbeitung:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **Deine Aufgabe wird bearbeitet**\n"
        "🆔 **Aufgaben-ID:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Deine Position in der Warteschlange:** {{ task_number }}\n"
        "🆔 **Aufgaben-ID:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👻 **Du wurdest entfernt. Du kannst diesen Bot nicht nutzen.**"
    USER_NOT_PARTICIPANT = "👻 **Trete dem erforderlichen Chat bei, um diesen Bot zu nutzen.**"
    JOIN_CHANNEL = "🔗 Updates-Kanal beitreten"

    MODE_INITIAL_MSG = (
        "📂 **Dateiausgabemodus:**\n\n"
        "1️⃣ **Gleiches Format wie gesendet**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Als Dokument erzwingen**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **Als allgemeines Medium hochladen**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "👻 **Wähle den Umbenennungsmodus:**\n"
        "🅰️ **Mit Befehl umbenennen**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Ohne Befehl umbenennen**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 Antworte auf ein Bild, um es als Thumbnail zu setzen."
    THUMB_SET_SUCCESS = "✅ **Thumbnail erfolgreich gesetzt.**"
    THUMB_NOT_FOUND = "⚠️ **Kein Thumbnail gefunden.**"
    THUMB_CLEARED = "🗑 **Thumbnail erfolgreich entfernt.**"

    HELP_STR = (
        "📖 **Bot-Befehle:**\n"
        "`{{ startcmd }}` - ✅ Prüft, ob der Bot läuft.\n"
        "`{{ renamecmd }}` - ✍️ Antworte auf eine Mediendatei mit `/rename dateiname.erweiterung` zum Umbenennen.\n"
        "`{{ filterscmd }}` - ⚙️ Filter verwalten.\n"
        "`{{ setthumbcmd }}` - 📷 Permanentes Thumbnail setzen (auf Bild antworten).\n"
        "`{{ getthumbcmd }}` - 📸 Aktuelles Thumbnail anzeigen.\n"
        "`{{ clrthumbcmd }}` - ❌ Thumbnail entfernen.\n"
        "`{{ modecmd }}` - 🔄 Wechsel zwischen 3 Ausgabemodi:\n"
        "    - 📝 Gleiches Format wie gesendet.\n"
        "    - 📂 Als Dokument erzwingen.\n"
        "    - 🎥 Allgemeines Medium (streamingfähig).\n\n"
        "    🔄 Wechsel zwischen Umbenennungsmodi:\n"
        "    - 🏷 **Mit Befehl** umbenennen.\n"
        "    - ✨ **Ohne Befehl/automatisch** umbenennen.\n\n"
        "`{{ queuecmd }}` - 📊 Warteschlangenstatus anzeigen.\n"
        "`{{ setcaptioncmd }}` - 📝 Beschriftung für umbenannte Dateien setzen.\n"
        "`{{ helpcmd }}` - 📖 Diese Hilfe anzeigen.\n"
        "`{{ pingcmd }}` - 🎈 Bot anpingen.\n"
        "`{{ infocmd }}` - � Bot-Info anzeigen.\n"
        "`{{ profilecmd }}` - ☄️ Deine Nutzungsstatistiken.\n"
        "`{{ statuscmd }}` - 🗿 Bot-Status.\n"
        "`{{ statscmd }}` - 👻 Globale Bot-Statistiken.\n"
        "`{{ broadcastcmd }}` - ☄️ Broadcast senden.\n"
        "`{{ leaderboardcmd }}` - 👻 Nutzer-Rangliste.\n"
        "`{{ setlanguagecmd }}` - 🌐 Sprache ändern."
    )

    CURRENT_LOCALE = "🌐 **Aktuelle Sprache:** {{ user_locale }}"


