from dataclasses import dataclass
import random

@dataclass
class HindiTranslations:
    LANGUAGE_NAME = "🇮🇳 हिंदी"
    LANGUAGE_CODE = "hi"

    WRONG_VALUE_ERROR = "❌ अरे! {{ variable_name }} के लिए अमान्य मान। फिर से कोशिश करो! 🤷‍♀️"

    START_MSG = (
    "✨ **अरे फाइल जादूगर!** ✨\n\n"
    "मैं **ऑटो रीनाम बॉट** 🪄 हूं, आपका जादुई फाइल नाम बदलने वाला सहायक!\n\n"
    "🔥 **आप मुझे क्यों पसंद करेंगे:**\n"
    "- ✨ चमक और सटीकता के साथ फाइलों का नाम बदलें\n"
    "- बिजली की तेज ⚡ और सुरक्षित 🔒\n"
    "- सभी प्रकार की फाइलों को सपोर्ट करता है! 📂🎵🎬\n\n"
    "बस मुझे एक फाइल भेजो और चलो जादू करते हैं! 🎩\n\n"
    "🚀 **प्रो टिप:** ऑटो-रीनाम निंजा मोड के लिए /mode का उपयोग करें (/filters जोड़ना होगा)!\n"
    "मदद चाहिए? /help आपके साथ है!\n\n"
    "🛸 **द्वारा संचालित** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "❗ नाम बदलना रद्द! पूफ! ✨ (जल्द ही अपडेट आ रहे हैं!)"

    RENAME_NO_FILTER_MATCH = (
        "🔮 **उफ़! कोई फिल्टर मेल नहीं मिला!**\n\n"
        "फिल्टर का उपयोग करने की कोशिश की लेकिन कुछ नहीं मिला 🎩🐇\n"
        "/filters के साथ अपने फिल्टर प्रबंधित करें ✏️"
    )

    RENAME_FILTER_MATCH_USED = (
        "🎯 **फिल्टर शक्ति सक्रिय!**\n"
        "आपने कोई नाम निर्दिष्ट नहीं किया है इसलिए फिल्टर का उपयोग कर रहा हूं\n"
        "/filters के साथ उन्हें ट्विक करें ⚙️"
    )

    RENAME_NOFLTR_NONAME = (
        "📝 **कोई फिल्टर नहीं मिले!**\n\n"
        "कृपया ऑटो पिक रीनाम फिल्टर के लिए /filters 🎨 जोड़ें।"
    )

    RENAME_CANCEL = "❌ नहीं, इसे रद्द करते हैं ✌️"

    RENAMING_FILE = "🌀 **फाइल रूपांतरण प्रगति पर है...**"

    DL_RENAMING_FILE = "📥 **आपका डिजिटल खजाना डाउनलोड हो रहा है...**"

    RENAME_ERRORED_REPORT = "💥 **अरे! कुछ टूट गया!** कृपया इसे रिपोर्ट करें 🚨"

    RENAME_CANCEL_BY_USER = "🙅‍♂️ **आपने रद्दीकरण छड़ी लहराई!** ✨"

    FLTR_ADD_LEFT_STR = "➕ फिल्टर जोड़ा: `<code>{{ text_1 }}</code>` **बाईं ओर**।"
    FLTR_ADD_RIGHT_STR = (
        "➕ फिल्टर जोड़ा: `<code>{{ text_1 }}</code>` **दाईं ओर**।"
    )
    FLTR_RM_STR = "❌ फिल्टर हटाया: `<code>{{ text_1 }}</code>`।"
    FLTR_REPLACE_STR = (
        "🔄 फिल्टर बदला: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`।"
    )

    CURRENT_FLTRS = "🎛️ **आपका फिल्टर डैशबोर्ड:**"
    ADD_FLTR = "➕ फिल्टर जोड़ें"
    RM_FLTR = "❌ फिल्टर हटाएं"

    FILTERS_INTRO = (
        "🛠 **फिल्टर गाइड:**\n"
        "3 प्रकार के फिल्टर हैं:\n\n"
        "🔄 **प्रतिस्थापन फिल्टर:** एक दिए गए शब्द को दूसरे से बदलें।\n"
        "➕ **जोड़ फिल्टर:** शुरुआत या अंत में एक शब्द जोड़ें।\n"
        "❌ **हटाना फिल्टर:** फाइलनाम से एक शब्द हटाएं।"
    )

    ADD_REPLACE_FLTR = "➕ प्रतिस्थापन फिल्टर जोड़ें"
    ADD_ADDITION_FLTR = "➕ जोड़ फिल्टर जोड़ें"
    ADD_REMOVE_FLTR = "➕ हटाना फिल्टर जोड़ें"
    BACK = "🔙 वापस"

    REPALCE_FILTER_INIT_MSG = "✍️ प्रारूप भेजें: `<code>क्या_बदलना_है | प्रतिस्थापन</code>` या वापस जाने के लिए /ignore।"

    NO_INPUT_FROM_USER = "🤷‍♂️ **झींगुर...** कोई इनपुट का पता नहीं चला!"
    INPUT_IGNORE = "👍 **नजरअंदाज किया!**"
    WRONG_INPUT_FORMAT = "🤦‍♂️ **उफ़!** गलत प्रारूप! प्रदान किया गया प्रारूप जांचें और फिर से कोशिश करें!"
    REPLACE_FILTER_SUCCESS = (
        "✅ **प्रतिस्थापन फिल्टर जोड़ा:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ `<code>|</code>` के अंदर जोड़ने के लिए टेक्स्ट दर्ज करें\n"
        "उदाहरण: `<code>| जोड़ने के लिए टेक्स्ट |</code>`\n"
        "या वापस जाने के लिए /ignore।"
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ फिल्टर जोड़ा: `<code>{{ text_1 }}</code>` **बाईं ओर**।"
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ फिल्टर जोड़ा: `<code>{{ text_1 }}</code>` **दाईं ओर**।"
    )

    ADDITION_LEFT = "🔄 बाईं ओर जोड़"
    ADDITION_RIGHT = "🔄 दाईं ओर जोड़"

    ADDITION_POSITION_PROMPT = "🧙‍♂️ **आप टेक्स्ट कहां जोड़ना चाहते हैं?**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ वह टेक्स्ट दर्ज करें जिसे आप हटाना चाहते हैं या वापस जाने के लिए /ignore।"
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **हटाना फिल्टर जोड़ा:** `<code>{{ text_1 }}</code>` हटा दिया जाएगा।"
    )

    RENAME_THEMES_DOWNLOADING = [
        "🎩 डाउनलोड पूरा! जादू तैयार कर रहा हूं...",
        "📦 फाइल प्राप्त! नामकरण जादू के लिए तैयार...",
        "✨ डाउनलोड सफल! मंत्र शुरू हो रहे हैं...",
        "⚡ डेटा सुरक्षित! नाम बदलने वाले इंजन फायरिंग अप...",
        "💾 फाइल कैप्चर! शानदार पुनर्जन्म के लिए तैयार..."
    ]

    RENAME_THEMES_UPLOADING = [
        "🚀 **ब्लास्ट ऑफ!** नाम बदली गई फाइल लॉन्च!",
        "🎉 **ता-दा!** आपकी नई नामित फाइल तैयार है!",
        "📤 अपलोड पूरा! अपनी कृति का आनंद लें!",
        "🌟 फाइल रूपांतरण पूरा!",
        "🏁 रेस खत्म! आपकी फाइल फिनिश लाइन पार कर चुकी है!"
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 **अबॉर्ट!** डाउनलोड जादू बाधित!",
        "🚧 उफ़! आपने डाउनलोड ट्रेन रोक दी!",
        "🎭 शो शुरू होने से पहले ही खत्म!",
        "📵 डाउनलोड कनेक्शन समाप्त!",
        "👋 आपने डाउनलोड को छोड़ दिया! अलविदा!"
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "✋ **होल्ड अप!** अपलोड मिड-फ्लाइट रुका!",
        "🚫 आज कोई डिलीवरी नहीं! अपलोड रद्द!",
        "🌪️ अपलोड टोर्नेडो dissipated!",
        "📴 कनेक्शन शून्य में खो गया!",
        "🤷‍♂️ आपने अपना मन बदल लिया! अपलोड abort!"
    ]

    REPLY_TO_MEDIA = "📎 **प्स्स्ट!** एक फाइल को `/rename` का जवाब दें!"

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "💥 **कबूम!** नाम बदलने का जादू विफल!"

    DOWNLOADING_THE_FILE = "📥 **आपकी फाइल fetch हो रही है...**"
    UPLOADING_THE_FILE = "📤 **लॉन्चिंग:** `{{ new_file_name }}` 🚀"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **नाम बदलने का मिशन शुरू**\n"
        "🆔 मिशन आईडी: `{{ uid }}`\n\n"
        "👤 **एजेंट:** @{{ username }}\n"
        "📛 **कोडनेम:** {{ name }}\n"
        "🪪 **आईडी:** `{{ user_id }}`\n"
        "📜 **फाइल:** `{{ file_name }}`\n\n"
        "`⚡ हाइपरड्राइव enged!`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "📥 **नाम बदलने का मिशन कतारबद्ध**\n\n"
        "👤 **एजेंट:** @{{ username }}\n"
        "📛 **कोडनेम:** {{ name }}\n"
        "🪪 **आईडी:** `{{ user_id }}`\n\n"
        "`⏳ तैनाती की प्रतीक्षा...`"
    )

    CAPTION_FOOT_NOTE = (
        "💡 **प्रो टिप:** स्टाइल जोड़ने के लिए /setcaption का उपयोग करें!\n"
        "✨ कैप्शन में फाइलनाम को ऑटो-फिल करने के लिए `/setcaption {file_name}` का उपयोग करें!"
    )

    DELETE_CAPTION = "🗑️ कैप्शन हटाएं"
    CLOSE = "🚪 बाहर निकलें"

    CAPTION_CURRENT = "📝 **वर्तमान कैप्शन:** {{ caption }}"
    CAPTION_NOT_SET = "🫗 **कैप्शन खाली!** कितना अकेला..."
    CAPTION_SET = "✅ **नया कैप्शन:** {{ caption }}"
    CAPTION_DELETED = "🗑️ **कैप्शन सफलतापूर्वक हटाया गया।**"

    RENAME_ADDED_TO_QUEUE = (
        "📊 **कतार में नाम बदलना**\n"
        "🆔 **डीसी आईडी:** {{ dc_id }}\n"
        "📦 **मीडिया आईडी:** {{ media_id }}\n\n"
        "`⏳ धैर्य, युवा padawan...`"
    )

    RENAME_QUEUE_STATUS = (
        "📈 **कतार स्टेट्स:**\n"
        "📊 **कुल कार्य:** {{ total_tasks }}\n"
        "⚡ **क्षमता:** {{ queue_capacity }}\n"
        "⏳ **प्रोसेसिंग:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **आपकी फाइल जादू हो रही है!**\n"
        "🆔 **टास्क आईडी:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **लाइन में आपकी जगह:** {{ task_number }}\n"
        "🆔 **टास्क आईडी:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👢 **आपको बाहर निकाल दिया गया है!** आपके लिए कोई बॉट नहीं!"
    USER_NOT_PARTICIPANT = (
        "🔒 **सीक्रेट क्लब अलर्ट!**\n\n"
        "जादू अनलॉक करने के लिए हमारे चैनल से जुड़ें!\n\n"
        "`🦄 इस बिंदु के बाद केवल यूनिकॉर्न`"
    )
    
    JOIN_CHANNEL = "🔗 सीक्रेट क्लब में शामिल हों"

    MODE_INITIAL_MSG = (
        "🎛️ **आउटपुट मोड सेलेक्टर:**\n\n"
        "1️⃣ **मूल प्रारूप रखें**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **डॉक्युमेंट मोड फोर्स करें**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **जनरल मीडिया मोड**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "✨ **नाम बदलने की शैली:**\n"
        "🅰️ **कमांड नाम बदलना**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **ऑटो-नाम बदलना**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣ OG मोड"
    MODE_SET_1 = "2️⃣ डॉक मोड"
    MODE_SET_2 = "3️⃣ मीडिया मोड"
    COMMAND_MODE_SET_3 = "🅰️ कमांड"
    COMMAND_MODE_SET_4 = "🅱️ ऑटो"

    THUMB_REPLY_TO_MEDIA = "🖼️ **थंबनेल के रूप में सेट करने के लिए एक छवि का उत्तर दें**"
    THUMB_SET_SUCCESS = "✅ **थंबनेल लॉक इन!**"
    THUMB_NOT_FOUND = "🕵️‍♂️ **कोई थंबनेल का पता नहीं चला!**"
    THUMB_CLEARED = "🧹 **थंबनेल swept away!**"

    HELP_STR = (
        "📚 **जादू की जादू की किताब:**\n"
        "`{{ startcmd }}` - जांचें कि क्या मैं जीवित हूं! 💓\n"
        "`{{ renamecmd }}` - एक बॉस की तरह फाइलों का नाम बदलें! 🎩\n"
        "`{{ filterscmd }}` - अपने नाम बदलने वाले फिल्टर को अनुकूलित करें! ✨\n"
        "`{{ setthumbcmd }}` - एक स्थायी थंबनेल सेट करें! 🖼️\n"
        "`{{ getthumbcmd }}` - वर्तमान थंबनेल पर एक नज़र डालें! 👀\n"
        "`{{ clrthumbcmd }}` - थंबनेल हटाएं! 🗑️\n"
        "`{{ modecmd }}` - आउटपुट मोड स्विच करें:\n"
        "   - 📝 मूल प्रारूप\n"
        "   - 📂 दस्तावेज़ को मजबूर करें\n"
        "   - 🎥 मीडिया मोड\n\n"
        "   नाम बदलने की शैलियों को स्विच करें:\n"
        "   - 🏷️ कमांड-आधारित\n"
        "   - 🤖 ऑटो-नाम बदलना (/filters जोड़ना होगा)\n\n"
        "`{{ queuecmd }}` - नाम बदलने की कतार की जांच करें 📊\n"
        "`{{ setcaptioncmd }}` - फैंसी कैप्शन सेट करें 🎨\n"
        "`{{ helpcmd }}` - यह जादू की किताब! 📖\n"
        "`{{ pingcmd }}` - पिंग-पोंग! 🏓\n"
        "`{{ infocmd }}` - बॉट विशेषताएँ! 🤖\n"
        "`{{ profilecmd }}` - आपके आँकड़े! 📈\n"
        "`{{ statuscmd }}` - बॉट जीवन संकेत! 💓\n"
        "`{{ statscmd }}` - वैश्विक संख्याएँ! 🌍\n"
        "`{{ broadcastcmd }}` - मेगा-घोषणा! 📢\n"
        "`{{ leaderboardcmd }}` - शीर्ष उपयोगकर्ता! 🏆\n"
        "`{{ setlanguagecmd }}` - भाषा बदलें! 🌐"
    )

    CURRENT_LOCALE = "🌍 **आपकी भाषा:** {{ user_locale }}"
