from dataclasses import dataclass
import random

@dataclass
class KenyanTranslations:
    LANGUAGE_NAME = "Kenyan (Sheng/Swahili/English)"
    LANGUAGE_CODE = "ke"

    WRONG_VALUE_ERROR = "❌ Weka sahii bro! {{ variable_name }} ni wrong."

    START_MSG = (
        "Niaje msee! 👋\n"
        "Mimi ni **Auto Rename Bot**, your personal file master.\n\n"
        "✨ **Vitu ziko poa:**\n"
        "- Rename files with custom names na extensions\n"
        "- Fast, safe na easy to use\n"
        "- Inasaidia almost all file types\n\n"
        "Just dm me a file nitakushow the process!\n\n"
        "Twaanza! Use /mode for auto rename, **Rename bila command**🚀\n"
        "Send /help for more deets.\n\n"
        "🚀 **By** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "⚠️ Rename imecancel. Tutafute soon."

    RENAME_NO_FILTER_MATCH = (
        "🚫 **HAKUNA FILTER ILIMATCH - RENAME IMECANCEL**\n\n"
        "🔍 Nimejaribu kutumia filters kwa sababu hukunipa jina.\n"
        "👻 Weka filters zako kwa /filters."
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ Nimetumia filters kwa sababu hukunipa jina.\n"
        "👻 Tafadhali weka filters zako kwa /filters."
    )

    RENAME_NOFLTR_NONAME = (
        "✍️ Weka jina mpya kwa hii format:\n"
        "```/rename my_new_filename.ext```\n"
        "au just tumia `/filters` kuweka rename filters."
    )

    RENAME_CANCEL = "❌ Acha tu hii rename."

    RENAMING_FILE = "🔄 Inabamba file... Subiri kidogo."

    DL_RENAMING_FILE = "📥 Inapakua file... Ngoja tu."

    RENAME_ERRORED_REPORT = "❗ Kuna shida kwa upakuaji. Report hii kitu."

    RENAME_CANCEL_BY_USER = "🚫 **User amecancel.**"

    FLTR_ADD_LEFT_STR = "➕ Filter imeongezwa: `<code>{{ text_1 }}</code>` **kwa LEFT**."
    FLTR_ADD_RIGHT_STR = "➕ Filter imeongezwa: `<code>{{ text_1 }}</code>` **kwa RIGHT**."
    FLTR_RM_STR = "❌ Filter imefutwa: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = "🔄 Filter imebadilishwa: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."

    CURRENT_FLTRS = "⚙️ **Filters zako za sasa:**"
    ADD_FLTR = "➕ Add Filter"
    RM_FLTR = "❌ Toa Filter"

    FILTERS_INTRO = (
        "🛠 **Mafunzo ya Filters:**\n"
        "Kuna aina tatu za filters:\n\n"
        "🔄 **Replace Filter:** Badilisha neno na lingine.\n"
        "➕ **Addition Filter:** Ongeza neno mwanzoni au mwisho.\n"
        "❌ **Remove Filter:** Futa neno kutoka kwa jina."
    )

    ADD_REPLACE_FLTR = "➕ Add Replace Filter"
    ADD_ADDITION_FLTR = "➕ Add Addition Filter"
    ADD_REMOVE_FLTR = "➕ Add Remove Filter"
    BACK = "🔙 Rudi"

    REPALCE_FILTER_INIT_MSG = "✍️ Tuma kwa format: `<code>original | replacement</code>` au `/ignore` kuacha."

    NO_INPUT_FROM_USER = "⚠️ Hujatoa chochote."
    INPUT_IGNORE = "✅ **Imeachwa.**"
    WRONG_INPUT_FORMAT = "❌ Format ni wrong. Angalia again."
    REPLACE_FILTER_SUCCESS = "✅ **Replace filter imeongezwa:**\n`'{{ text_1 }}'` → `'{{ text_2 }}'`"

    ADDITION_FILTER_INIT_MSG = (
        "✍️ Weka text unataka kuongeza kati ya `<code>|</code>`\n"
        "Mfano: `<code>| text unataka |</code>`\n"
        "au `/ignore` kuacha."
    )

    ADDITION_FILTER_SUCCESS_LEFT = "✅ Filter imeongezwa: `<code>{{ text_1 }}</code>` **kwa LEFT**."
    ADDITION_FILTER_SUCCESS_RIGHT = "✅ Filter imeongezwa: `<code>{{ text_1 }}</code>` **kwa RIGHT**."

    ADDITION_LEFT = "🔄 Ongeza LEFT"
    ADDITION_RIGHT = "🔄 Ongeza RIGHT"

    ADDITION_POSITION_PROMPT = "📍 **Unataka kuongeza wapi?**"

    REMOVE_FILTER_INIT_MSG = "✍️ Weka text unataka kufuta au `/ignore` kuacha."

    REMOVE_FILTER_SUCCESS = "✅ **Remove filter imeongezwa:** `<code>{{ text_1 }}</code>` itafutwa."

    RENAME_THEMES_DOWNLOADING = [
        "✅ Download imekamilika. Rename inafanyika...",
        "📦 File imepatikana! Tayari kubadilisha jina...",
        "🪄 Download imekwisha. Rename inaanza...",
        "🔧 Data imechukuliwa. Inabamba jina...",
        "💾 Imehifadhiwa. Inaprepare jina jipya...",
    ]

    RENAME_THEMES_UPLOADING = [
        "✅ Rename imekwisha! Upload done.",
        "🚀 File imebadilishwa jina kwa mafanikio.",
        "📤 Upload imekamilika. File yako iko tayari!",
        "🌟 Rename imekamilika. Imesafirishwa!",
        "📁 Kazi imekwisha. File imepanda jina jipya.",
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 Download imesimama. Rename imeachwa...",
        "🚫 Umeghairi. Download haikufanyika.",
        "❌ Kazi imesimama wakati wa download.",
        "📴 Rename imecancel wakati wa download.",
        "👋 User ameghairi. File haijafika.",
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "🛑 Upload imesimama. File haijatumwa.",
        "🚫 Rename imereverse. Upload imeghairiwa.",
        "❌ Imesimama kwa last stage. Rename haikufanyika.",
        "📴 Upload imeghairiwa. File haijabadilishwa.",
        "👋 User amesema 'hapana' wakati wa upload.",
    ]

    REPLY_TO_MEDIA = "📂 Reply `/rename` kwa media file."

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "❗ Kuna shida kwa rename."

    DOWNLOADING_THE_FILE = "📥 Inapakua file"
    UPLOADING_THE_FILE = "📤 Inatuma file: **{{ new_file_name }}**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Rename imeanza**\n"
        "🆔 Task ID: `{{ uid }}`\n\n"
        "👤 **Username:** @{{ username }}\n"
        "📛 **Name:** {{ name }}\n"
        "🆔 **User ID:** `<code>{{ user_id }}</code>`\n"
        "📂 **File Name:** `<code>{{ file_name }}</code>`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "✅ **Rename task imeongezwa**\n\n"
        "👤 **Username:** @{{ username }}\n"
        "📛 **Name:** {{ name }}\n"
        "🆔 **User ID:** `<code>{{ user_id }}</code>`"
    )

    CAPTION_FOOT_NOTE = (
        "☄️ **NOTE:** Weka caption kwa `/setcaption` na text yako.\n"
        "📂 Tumia `<code>{file_name}</code>` kuweka jina la file kwa caption."
    )

    DELETE_CAPTION = "🗑 Futa Caption"
    CLOSE = "❌ Funga"

    CAPTION_CURRENT = "📝 **Caption yako ya sasa:** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **Hakuna caption.**"
    CAPTION_SET = "✅ **Caption imesetiwa:** {{ caption }}"
    CAPTION_DELETED = "🗑 **Caption imefutwa.**"

    RENAME_ADDED_TO_QUEUE = (
        "📥 **Rename task imeongezwa kwenye foleni**\n"
        "🆔 **DC ID:** {{ dc_id }}\n"
        "👻 **Media ID:** {{ media_id }}"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **Hali ya foleni:**\n"
        "☄️ **Total tasks:** {{ total_tasks }}\n"
        "⚡ **Uwezo wa foleni:** {{ queue_capacity }}\n"
        "⏳ **Inafanyika sasa:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **Task yako inafanyika**\n"
        "🆔 **Task ID:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Task yako iko kwenye foleni:** {{ task_number }}\n"
        "🆔 **Task ID:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👻 **Umeondolewa. Huna ruhusa ya kutumia bot hii.**"
    USER_NOT_PARTICIPANT = "👻 **Jiunge kwenye chat kutumia bot hii.**"
    JOIN_CHANNEL = "🔗 Jiunge Channel"

    MODE_INITIAL_MSG = (
        "📂 **Hali ya file:**\n\n"
        "1️⃣ **Same format kama uliyotuma**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Force Document**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **Upload kama Media**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "👻 **Chagua mode:**\n"
        "🅰️ **Rename na command**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Rename bila command**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 Reply kwa picha kuweka thumbnail."
    THUMB_SET_SUCCESS = "✅ **Thumbnail imesetiwa.**"
    THUMB_NOT_FOUND = "⚠️ **Hakuna thumbnail.**"
    THUMB_CLEARED = "🗑 **Thumbnail imefutwa.**"

    HELP_STR = (
        "📖 **Bot Commands:**\n"
        "`{{ startcmd }}` - ✅ Angalia kama bot iko hai\n"
        "`{{ renamecmd }}` - ✍️ Reply kwa file na `/rename filename.ext` kubadilisha jina\n"
        "`{{ filterscmd }}` - ⚙️ Dhibiti filters zako\n"
        "`{{ setthumbcmd }}` - 📷 Weka thumbnail (reply kwa picha)\n"
        "`{{ getthumbcmd }}` - 📸 Angalia thumbnail yako\n"
        "`{{ clrthumbcmd }}` - ❌ Toa thumbnail\n"
        "`{{ modecmd }}` - 🔄 Badilisha mode:\n"
        "    - 📝 Same format kama uliyotuma\n"
        "    - 📂 Force Document\n"
        "    - 🎥 General Media\n\n"
        "    🔄 Badilisha rename mode:\n"
        "    - 🏷 Rename **na command**\n"
        "    - ✨ Rename **bila command/auto**\n\n"
        "`{{ queuecmd }}` - 📊 Angalia foleni\n"
        "`{{ setcaptioncmd }}` - 📝 Weka caption\n"
        "`{{ helpcmd }}` - 📖 Msaada huu\n"
        "`{{ pingcmd }}` - 🎈 Ping Bot\n"
        "`{{ infocmd }}` - 🧑‍💻 Bot info\n"
        "`{{ profilecmd }}` - ☄️ Stats zako\n"
        "`{{ statuscmd }}` - 🗿 Hali ya bot\n"
        "`{{ statscmd }}` - 👻 Global stats\n"
        "`{{ broadcastcmd }}` - ☄️ Broadcast\n"
        "`{{ leaderboardcmd }}` - 👻 Leaderboard\n"
        "`{{ setlanguagecmd }}` - 🌐 Badilisha lugha"
    )

    CURRENT_LOCALE = "🌐 **Lugha yako:** {{ user_locale }}"

