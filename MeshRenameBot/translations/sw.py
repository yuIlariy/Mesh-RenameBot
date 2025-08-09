from dataclasses import dataclass
import random

@dataclass
class SwahiliTranslations:
    LANGUAGE_NAME = "Kiswahili"
    LANGUAGE_CODE = "sw"

    WRONG_VALUE_ERROR = "❌ Thamani batili kwa muundo {{ variable_name }}."

    START_MSG = (
        "Hujambo! 👋\n"
        "Mimi ni **Bot ya Kubadilisha Majina**, msaidizi wako wa kubadilisha majina ya faili kwa urahisi Telegram.\n\n"
        "✨ **Vipengele vya Msingi:**\n"
        "- Badilisha majina ya faili na viambatisho vipya\n"
        "- Haraka, salama na rahisi kutumia\n"
        - Inasaidia aina nyingi za faili\n\n"
        "Tuma faili kwangu nami nitakuongoza katika mchakato!\n\n"
        "Tuanze! Tumia /mode kuwezesha kubadilisha jina kiotomatiki\n"
        "Tuma /help kujifunza zaidi.\n\n"
        "🚀 **Imetengenezwa na** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "⚠️ Ubadilishaji jina **umeghairiwa**. Itasasishwa hivi karibuni."

    RENAME_NO_FILTER_MATCH = (
        "🚫 **HAKUNA KICHUJIO KILINGANA - KUGHARIMI KUBADILISHA JINA**\n\n"
        "🔍 Tumia michujo ikiwa hakuna jina maalum\n"
        "👻 Dhibiti michujo yako kwa /filters."
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ Tumia michujo ikiwa hakuna jina maalum\n"
        "👻 Dhibiti michujo yako kwa /filters."
    )

    RENAME_NOFLTR_NONAME = (
        "✍️ Weka jina jipya kwa umbizo:\n"
        "```/rename jina_jipya.kiambatisho```\n"
        "au tumia `/filters` kuweka michujo ya kubadilisha jina."
    )

    RENAME_CANCEL = "❌ Ghairi ubadilishaji huu."

    RENAMING_FILE = "🔄 Inabadilisha jina la faili... Subiri kidogo."

    DL_RENAMING_FILE = "📥 Inapakua faili... Subiri kidogo."

    RENAME_ERRORED_REPORT = "❗ Kuna hitilafu katika upakuaji. Ripoti tatizo hili."

    RENAME_CANCEL_BY_USER = "🚫 **Imeghairiwa na mtumiaji.**"

    FLTR_ADD_LEFT_STR = "➕ Chujio cha kushoto: `<code>{{ text_1 }}</code>`."
    FLTR_ADD_RIGHT_STR = "➕ Chujio cha kulia: `<code>{{ text_1 }}</code>`."
    FLTR_RM_STR = "❌ Ondoa chujio: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = "🔄 Badilisha chujio: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."

    CURRENT_FLTRS = "⚙️ **Michujo yako ya sasa:**"
    ADD_FLTR = "➕ Ongeza chujio"
    RM_FLTR = "❌ Ondoa chujio"

    FILTERS_INTRO = (
        "🛠 **Mwongozo wa Michujo:**\n"
        "Kuna aina 3 za michujo:\n\n"
        "🔄 **Badilisha:** Badilisha neno kwa lingine\n"
        "➕ **Ongeza:** Ongeza neno mwanzoni au mwisho\n"
        "❌ **Ondoa:** Toa neno kutoka kwa jina la faili"
    )

    ADD_REPLACE_FLTR = "➕ Ongeza chujio cha kubadilisha"
    ADD_ADDITION_FLTR = "➕ Ongeza chujio cha kuongeza"
    ADD_REMOVE_FLTR = "➕ Ongeza chujio cha kuondoa"
    BACK = "🔙 Rudi"

    REPALCE_FILTER_INIT_MSG = "✍️ Tuma umbizo: `<code>kubadilisha | badala</code>` au `/ignore` kurudi."

    NO_INPUT_FROM_USER = "⚠️ Hakuna maelezo yaliyopokelewa."
    INPUT_IGNORE = "✅ **Imepuuzwa**."
    WRONG_INPUT_FORMAT = "❌ Umbizo batili. Angalia umbizo."
    REPLACE_FILTER_SUCCESS = "✅ **Chujio cha kubadilisha kimeongezwa:**\n`'{{ text_1 }}'` → `'{{ text_2 }}'`"

    ADDITION_FILTER_INIT_MSG = (
        "✍️ Weka maandishi ya kuongeza kati ya `<code>|</code>`\n"
        "Mfano: `<code>| maandishi |</code>`\n"
        "au `/ignore` kurudi."
    )

    ADDITION_FILTER_SUCCESS_LEFT = "✅ Chujio kimeongezwa: `<code>{{ text_1 }}</code>` **kushoto**."
    ADDITION_FILTER_SUCCESS_RIGHT = "✅ Chujio kimeongezwa: `<code>{{ text_1 }}</code>` **kulia**."

    ADDITION_LEFT = "🔄 Ongeza kushoto"
    ADDITION_RIGHT = "🔄 Ongeza kulia"

    ADDITION_POSITION_PROMPT = "📍 **Unataka kuongeza wapi?**"

    REMOVE_FILTER_INIT_MSG = "✍️ Weka maandishi ya kuondoa au `/ignore` kurudi."

    REMOVE_FILTER_SUCCESS = "✅ **Chujio cha kuondoa kimeongezwa:** `<code>{{ text_1 }}</code>` itaondolewa."

    RENAME_THEMES_DOWNLOADING = [
        "✅ Upakuaji umekamilika. Anza kubadilisha jina...",
        "📦 Faili imepakuliwa! Tayari kubadilisha jina...",
        "🪄 Upakuaji umekamilika. Anza mchakato...",
        "🔧 Data imepakuliwa. Inabadilisha jina...",
        "💾 Imehifadhiwa. Inajiandaa kwa jina jipya...",
    ]

    RENAME_THEMES_UPLOADING = [
        "✅ Jina limebadilishwa! Upakiaji umekamilika.",
        "🚀 Faili limebadilishwa jina kwa mafanikio.",
        "📤 Upakiaji umekamilika. Faili yako iko tayari!",
        "🌟 Jina limebadilishwa. Imewasilishwa!",
        "📁 Kazi imekamilika. Faili imebadilishwa jina.",
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 Upakuaji umeghairiwa. Imesitishwa...",
        "🚫 Umeghairi. Upakuaji umeghairiwa.",
        "❌ Imesitishwa wakati wa upakuaji.",
        "📴 Ubadilishaji jina umeghairiwa.",
        "👋 Mtumiaji ameghairi wakati wa upakuaji.",
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "🛑 Upakiaji umeghairiwa. Faili haijatumwa.",
        "🚫 Jina limeghairiwa. Upakiaji umeghairiwa.",
        "❌ Imesitishwa katika hatua ya mwisho.",
        "📴 Upakiaji umeghairiwa. Faili haijabadilishwa.",
        "👋 Mtumiaji ameghairi wakati wa upakiaji.",
    ]

    REPLY_TO_MEDIA = "📂 Reply `/rename` kwa faili ya media."

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "❗ Kuna hitilafu katika kubadilisha jina."

    DOWNLOADING_THE_FILE = "📥 Inapakua faili"
    UPLOADING_THE_FILE = "📤 Inatuma faili: **{{ new_file_name }}**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Mchakato umeanza**\n"
        "🆔 Kitambulisho: `{{ uid }}`\n\n"
        "👤 **Mtumiaji:** @{{ username }}\n"
        "📛 **Jina:** {{ name }}\n"
        "🆔 **ID:** `<code>{{ user_id }}</code>`\n"
        "📂 **Faili:** `<code>{{ file_name }}</code>`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "✅ **Kazi imeongezwa**\n\n"
        "👤 **Mtumiaji:** @{{ username }}\n"
        "📛 **Jina:** {{ name }}\n"
        "🆔 **ID:** `<code>{{ user_id }}</code>`"
    )

    CAPTION_FOOT_NOTE = (
        "☄️ **Kumbuka:** Weka maelezo kwa `/setcaption` na maandishi yako.\n"
        "📂 Tumia `<code>{file_name}</code>` kuweka jina la faili."
    )

    DELETE_CAPTION = "🗑 Futa maelezo"
    CLOSE = "❌ Funga"

    CAPTION_CURRENT = "📝 **Maelezo yako:** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **Hakuna maelezo.**"
    CAPTION_SET = "✅ **Maelezo yamesasishwa:** {{ caption }}"
    CAPTION_DELETED = "🗑 **Maelezo yamefutwa.**"

    RENAME_ADDED_TO_QUEUE = (
        "📥 **Kazi imeongezwa kwenye foleni**\n"
        "🆔 **DC ID:** {{ dc_id }}\n"
        "👻 **Media ID:** {{ media_id }}"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **Hali ya foleni:**\n"
        "☄️ **Kazi zote:** {{ total_tasks }}\n"
        "⚡ **Uwezo:** {{ queue_capacity }}\n"
        "⏳ **Inachakata sasa:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **Kazi yako inafanyika**\n"
        "🆔 **Kitambulisho:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Nafasi yako kwenye foleni:** {{ task_number }}\n"
        "🆔 **Kitambulisho:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👻 **Umeondolewa. Hauwezi kutumia bot hii.**"
    USER_NOT_PARTICIPANT = "👻 **Jiunge na mazungumzo ili kutumia bot hii.**"
    JOIN_CHANNEL = "🔗 Jiunge na idhaa"

    MODE_INITIAL_MSG = (
        "📂 **Hali ya faili:**\n\n"
        "1️⃣ **Umbizo sawa na lililotumwa**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Lazima kuwa hati**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **Tuma kama media**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "👻 **Chagua hali:**\n"
        "🅰️ **Badilisha jina kwa amri**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Badilisha jina bila amri**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 Reply kwa picha kuweka kama kibao."
    THUMB_SET_SUCCESS = "✅ **Kibao kimewekwa.**"
    THUMB_NOT_FOUND = "⚠️ **Hakuna kibao.**"
    THUMB_CLEARED = "🗑 **Kibao kimefutwa.**"

    HELP_STR = (
        "📖 **Amri za Bot:**\n"
        "`{{ startcmd }}` - ✅ Angalia ikiwa bot iko hai\n"
        "`{{ renamecmd }}` - ✍️ Badilisha jina la faili\n"
        "`{{ filterscmd }}` - ⚙️ Dhibiti michujo\n"
        "`{{ setthumbcmd }}` - 📷 Weka kibao\n"
        "`{{ getthumbcmd }}` - 📸 Angalia kibao\n"
        "`{{ clrthumbcmd }}` - ❌ Ondoa kibao\n"
        "`{{ modecmd }}` - 🔄 Hali za utoaji:\n"
        "    - 📝 Umbizo asili\n"
        "    - 📂 Hati\n"
        "    - 🎥 Media\n\n"
        "    🔄 Hali za kubadilisha jina:\n"
        "    - 🏷 Kwa amri\n"
        "    - ✨ Bila amri\n\n"
        "`{{ queuecmd }}` - 📊 Angalia foleni\n"
        "`{{ setcaptioncmd }}` - 📝 Weka maelezo\n"
        "`{{ helpcmd }}` - 📖 Msaada\n"
        "`{{ pingcmd }}` - 🎈 Ping\n"
        "`{{ infocmd }}` - 🧑‍💻 Maelezo\n"
        "`{{ profilecmd }}` - ☄️ Takwimu zako\n"
        "`{{ statuscmd }}` - 🗿 Hali\n"
        "`{{ statscmd }}` - 👻 Takwimu za jumla\n"
        "`{{ broadcastcmd }}` - ☄️ Tangaza\n"
        "`{{ leaderboardcmd }}` - 👻 Ubao wa kiongozi\n"
        "`{{ setlanguagecmd }}` - 🌐 Badilisha lugha"
    )

    CURRENT_LOCALE = "🌐 **Lugha yako:** {{ user_locale }}"


