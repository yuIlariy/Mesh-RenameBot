from dataclasses import dataclass
import random

@dataclass
class GermanTranslations:
    LANGUAGE_NAME = "🇩🇪 Deutsch"
    LANGUAGE_CODE = "de"

    WRONG_VALUE_ERROR = "❌ Oops! Ungültiger Wert für {{ variable_name }}. Versuche es erneut! 🤷‍♀️"

    START_MSG = (
    "✨ **Hallo dort, Datei-Zauberer!** ✨\n\n"
    "Ich bin **Auto Rename Bot** 🪄, dein magischer Dateiumbenennungs-Assistent!\n\n"
    "🔥 **Warum du mich lieben wirst:**\n"
    "- Benenne Dateien mit ✨ Glanz und Präzision um\n"
    "- Blitzschnell ⚡ und sicher 🔒\n"
    "- Unterstützt ALLE Dateitypen! 📂🎵🎬\n\n"
    "Schick mir einfach eine Datei und lass uns Magie wirken! 🎩\n\n"
    "🚀 **Pro-Tipp:** Verwende /mode für den Auto-Rename-Ninja-Modus (muss /filters hinzufügen)!\n"
    "Hilfe benötigt? /help hat deinen Rücken!\n\n"
    "🛸 **Unterstützt von** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "❗ Umbenennung abgebrochen! Puff! ✨ (Updates kommen bald!)"

    RENAME_NO_FILTER_MATCH = (
        "🔮 **Hoppla! Keine Filterübereinstimmung!**\n\n"
        "Habe Filter verwendet, aber nichts gefunden 🎩🐇\n"
        "Verwalte deine Filter mit /filters ✏️"
    )

    RENAME_FILTER_MATCH_USED = (
        "🎯 **Filterkraft aktiviert!**\n"
        "Verwende Filter, da du keinen Namen angegeben hast\n"
        "Passe sie mit /filters an ⚙️"
    )

    RENAME_NOFLTR_NONAME = (
        "📝 **KEINE Filter gefunden!**\n\n"
        "Bitte füge /filters 🎨 für automatische Umbenennungsfilter hinzu."
    )

    RENAME_CANCEL = "❌ Nein, lass uns das abbrechen ✌️"

    RENAMING_FILE = "🌀 **Dateiumwandlung läuft...**"

    DL_RENAMING_FILE = "📥 **Lade deinen digitalen Schatz herunter...**"

    RENAME_ERRORED_REPORT = "💥 **Huch! Etwas ist kaputt gegangen!** Bitte melde dies 🚨"

    RENAME_CANCEL_BY_USER = "🙅‍♂️ **Du hast den Abbrechen-Zauberstab geschwungen!** ✨"

    FLTR_ADD_LEFT_STR = "➕ Filter hinzugefügt: `<code>{{ text_1 }}</code>` **nach LINKS**."
    FLTR_ADD_RIGHT_STR = (
        "➕ Filter hinzugefügt: `<code>{{ text_1 }}</code>` **nach RECHTS**."
    )
    FLTR_RM_STR = "❌ Filter entfernt: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = (
        "🔄 Filter ersetzt: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."
    )

    CURRENT_FLTRS = "🎛️ **Dein Filter-Dashboard:**"
    ADD_FLTR = "➕ Filter hinzufügen"
    RM_FLTR = "❌ Filter entfernen"

    FILTERS_INTRO = (
        "🛠 **Filter-Anleitung:**\n"
        "Es gibt 3 Filtertypen:\n\n"
        "🔄 **Ersetzungsfilter:** Ersetze ein bestimmtes Wort durch ein anderes.\n"
        "➕ **Hinzufügungsfilter:** Füge ein Wort am Anfang oder Ende hinzu.\n"
        "❌ **Entfernungsfilter:** Entferne ein Wort aus dem Dateinamen."
    )

    ADD_REPLACE_FLTR = "➕ Ersetzungsfilter hinzufügen"
    ADD_ADDITION_FLTR = "➕ Hinzufügungsfilter hinzufügen"
    ADD_REMOVE_FLTR = "➕ Entfernungsfilter hinzufügen"
    BACK = "🔙 Zurück"

    REPALCE_FILTER_INIT_MSG = "✍️ Sende das Format: `<code>was_zu_ersetzen | ersatz</code>` oder /ignore um zurückzugehen."

    NO_INPUT_FROM_USER = "🤷‍♂️ **Grillenzirpen...** Keine Eingabe erkannt!"
    INPUT_IGNORE = "👍 **Ignoriert!**"
    WRONG_INPUT_FORMAT = "🤦‍♂️ **Hoppla!** Falsches Format! Überprüfe das bereitgestellte Format und versuche es erneut!"
    REPLACE_FILTER_SUCCESS = (
        "✅ **Ersetzungsfilter hinzugefügt:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ Gib den hinzuzufügenden Text innerhalb `<code>|</code>` ein\n"
        "Beispiel: `<code>| hinzuzufügender Text |</code>`\n"
        "oder /ignore um zurückzugehen."
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ Filter hinzugefügt: `<code>{{ text_1 }}</code>` **nach LINKS**."
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ Filter hinzugefügt: `<code>{{ text_1 }}</code>` **nach RECHTS**."
    )

    ADDITION_LEFT = "🔄 Hinzufügung nach LINKS"
    ADDITION_RIGHT = "🔄 Hinzufügung nach RECHTS"

    ADDITION_POSITION_PROMPT = "🧙‍♂️ **Wo möchtest du den Text hinzufügen?**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ Gib den zu entfernenden Text ein oder /ignore um zurückzugehen."
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **Entfernungsfilter hinzugefügt:** `<code>{{ text_1 }}</code>` wird entfernt."
    )

    RENAME_THEMES_DOWNLOADING = [
        "🎩 Download abgeschlossen! Bereite Magie vor...",
        "📦 Datei erhalten! Bereit für Namenszauber...",
        "✨ Download erfolgreich! Zauber beginnen...",
        "⚡ Daten gesichert! Umbenennungsmaschinen starten...",
        "💾 Datei erfasst! Bereit für glorreiche Wiedergeburt..."
    ]

    RENAME_THEMES_UPLOADING = [
        "🚀 **Start!** Umbenannte Datei gestartet!",
        "🎉 **Ta-da!** Deine neu benannte Datei ist fertig!",
        "📤 Upload abgeschlossen! Genieße dein Meisterwerk!",
        "🌟 Dateimetamorphose abgeschlossen!",
        "🏁 Rennen vorbei! Deine Datei hat die Ziellinie überquert!"
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 **Abbrechen!** Download-Zauber unterbrochen!",
        "🚧 Hoppla! Du hast den Download-Zug gestoppt!",
        "🎭 Die Show ist vorbei, bevor sie begann!",
        "📵 Download-Verbindung getrennt!",
        "👋 Du hast den Download verlassen! Auf Wiedersehen!"
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "✋ **Moment mal!** Upload mitten im Flug gestoppt!",
        "🚫 Keine Lieferung heute! Upload abgebrochen!",
        "🌪️ Upload-Tornado aufgelöst!",
        "📴 Verbindung im Nichts verloren!",
        "🤷‍♂️ Du hast deine Meinung geändert! Upload abgebrochen!"
    ]

    REPLY_TO_MEDIA = "📎 **Pssst!** Antworte `/rename` auf eine Datei!"

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "💥 **Kaboom!** Umbenennungszauber fehlgeschlagen!"

    DOWNLOADING_THE_FILE = "📥 **Hole deine Datei...**"
    UPLOADING_THE_FILE = "📤 **Starte:** `{{ new_file_name }}` 🚀"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Umbenennungsmission gestartet**\n"
        "🆔 Missions-ID: `{{ uid }}`\n\n"
        "👤 **Agent:** @{{ username }}\n"
        "📛 **Deckname:** {{ name }}\n"
        "🪪 **ID:** `{{ user_id }}`\n"
        "📜 **Datei:** `{{ file_name }}`\n\n"
        "`⚡ Hyperantrieb aktiviert!`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "📥 **Umbenennungsmission in Warteschlange**\n\n"
        "👤 **Agent:** @{{ username }}\n"
        "📛 **Deckname:** {{ name }}\n"
        "🪪 **ID:** `{{ user_id }}`\n\n"
        "`⏳ Warte auf Einsatz...`"
    )

    CAPTION_FOOT_NOTE = (
        "💡 **Pro-Tipp:** Verwende /setcaption für Flair!\n"
        "✨ Verwende `/setcaption {file_name}` um den Dateinamen automatisch in der Beschriftung auszufüllen!"
    )

    DELETE_CAPTION = "🗑️ Beschriftung löschen"
    CLOSE = "🚪 Beenden"

    CAPTION_CURRENT = "📝 **Aktuelle Beschriftung:** {{ caption }}"
    CAPTION_NOT_SET = "🫗 **Beschriftung leer!** So einsam..."
    CAPTION_SET = "✅ **Neue Beschriftung:** {{ caption }}"
    CAPTION_DELETED = "🗑️ **Beschriftung erfolgreich gelöscht.**"

    RENAME_ADDED_TO_QUEUE = (
        "📊 **Umbenennung in Warteschlange**\n"
        "🆔 **DC-ID:** {{ dc_id }}\n"
        "📦 **Medien-ID:** {{ media_id }}\n\n"
        "`⏳ Geduld, junger Padawan...`"
    )

    RENAME_QUEUE_STATUS = (
        "📈 **Warteschlangen-Status:**\n"
        "📊 **Gesamtaufgaben:** {{ total_tasks }}\n"
        "⚡ **Kapazität:** {{ queue_capacity }}\n"
        "⏳ **In Bearbeitung:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **Deine Datei wird verzaubert!**\n"
        "🆔 **Aufgaben-ID:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Dein Platz in der Reihe:** {{ task_number }}\n"
        "🆔 **Aufgaben-ID:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👢 **Du wurdest rausgeworfen!** Kein Bot für dich!"
    USER_NOT_PARTICIPANT = (
        "🔒 **Geheimer Club-Alarm!**\n\n"
        "Tritt unserem Kanal bei, um die Magie zu entfesseln!\n\n"
        "`🦄 Nur Einhörner hinter diesem Punkt`"
    )
    
    JOIN_CHANNEL = "🔗 Geheimem Club beitreten"

    MODE_INITIAL_MSG = (
        "🎛️ **Ausgabemodus-Auswahl:**\n\n"
        "1️⃣ **Originalformat beibehalten**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Dokumentenmodus erzwingen**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **Allgemeiner Medienmodus**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "✨ **Umbenennungsstil:**\n"
        "🅰️ **Befehlsumbenennung**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Auto-Umbenennung**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣ OG-Modus"
    MODE_SET_1 = "2️⃣ Dokumentenmodus"
    MODE_SET_2 = "3️⃣ Medienmodus"
    COMMAND_MODE_SET_3 = "🅰️ Befehl"
    COMMAND_MODE_SET_4 = "🅱️ Auto"

    THUMB_REPLY_TO_MEDIA = "🖼️ **Antworte auf ein Bild** um es als Miniaturbild festzulegen"
    THUMB_SET_SUCCESS = "✅ **Miniaturbild gespeichert!**"
    THUMB_NOT_FOUND = "🕵️‍♂️ **Kein Miniaturbild erkannt!**"
    THUMB_CLEARED = "🧹 **Miniaturbild weggefegt!**"

    HELP_STR = (
        "📚 **Zauberbuch:**\n"
        "`{{ startcmd }}` - Überprüfe ob ich lebe! 💓\n"
        "`{{ renamecmd }}` - Benenne Dateien um wie ein Boss! 🎩\n"
        "`{{ filterscmd }}` - Passe deine Umbenennungsfilter an! ✨\n"
        "`{{ setthumbcmd }}` - Setze ein permanentes Miniaturbild! 🖼️\n"
        "`{{ getthumbcmd }}` - Schau auf aktuelles Miniaturbild! 👀\n"
        "`{{ clrthumbcmd }}` - Lösche Miniaturbild! 🗑️\n"
        "`{{ modecmd }}` - Wechsle Ausgabemodi:\n"
        "   - 📝 Originalformat\n"
        "   - 📂 Dokument erzwingen\n"
        "   - 🎥 Medienmodus\n\n"
        "   Wechsle Umbenennungsstile:\n"
        "   - 🏷️ Befehlsbasiert\n"
        "   - 🤖 Auto-Umbenennung (muss /filters hinzufügen)\n\n"
        "`{{ queuecmd }}` - Überprüfe Umbenennungswarteschlange 📊\n"
        "`{{ setcaptioncmd }}` - Setze ausgefallene Beschriftungen 🎨\n"
        "`{{ helpcmd }}` - Dieses Zauberbuch! 📖\n"
        "`{{ pingcmd }}` - Ping-pong! 🏓\n"
        "`{{ infocmd }}` - Bot-Spezifikationen! 🤖\n"
        "`{{ profilecmd }}` - Deine Statistiken! 📈\n"
        "`{{ statuscmd }}` - Bot-Vitalwerte! 💓\n"
        "`{{ statscmd }}` - Globale Zahlen! 🌍\n"
        "`{{ broadcastcmd }}` - Mega-Ankündigung! 📢\n"
        "`{{ leaderboardcmd }}` - Top-Benutzer! 🏆\n"
        "`{{ setlanguagecmd }}` - Sprache ändern! 🌐"
    )

    CURRENT_LOCALE = "🌍 **Deine Sprache:** {{ user_locale }}"
