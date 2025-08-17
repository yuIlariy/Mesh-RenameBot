from dataclasses import dataclass
import random

@dataclass
class EnglishTranslations:
    LANGUAGE_NAME = "🇬🇧 English"
    LANGUAGE_CODE = "en"

    WRONG_VALUE_ERROR = "❌ Invalid value entered for {{ variable_name }} variable."

    START_MSG = (
    "Hello there! 👋\n"
    "I’m **Auto Rename Bot**, your go-to assistant for effortlessly renaming files on Telegram.\n\n"
    "✨ **Key Features:**\n"
    "- Rename files with custom names and extensions.\n"
    "- Fast, secure, and easy to use.\n"
    "- Supports a wide range of file types.\n\n"
    "Simply send me a file, and I’ll guide you through the renaming process!\n\n"
    "Let’s get started! Use /mode to enable auto rename, **Rename without command**🚀\n"
    "Send /help to learn more.\n\n"
    "🚀 **Powered by** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "⚠️ The rename has been **canceled**. Will be updated soon."

    RENAME_NO_FILTER_MATCH = (
        "‼️ **NO FILTER MATCHED - ABORTING RENAME**\n\n"
        "🔍 Using filters to rename as no name was specified.\n"
        "📜 Manage your filters using /filters."
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ Using filters to rename as no name was specified.\n"
        "📜 Manage your filters using /filters."
    )

    RENAME_NOFLTR_NONAME = (
        "📝 Enter the new file name in format:\n"
        "```/rename my_new_filename.extension```\n"
        "or use `/filters` to set rename filters."
    )

    RENAME_CANCEL = "❌ Cancel this rename."

    RENAMING_FILE = "🔄 Renaming the file... Please wait."

    DL_RENAMING_FILE = "📥 Downloading the file... Please wait."

    RENAME_ERRORED_REPORT = "❗ The download encountered an error. Report this issue."

    RENAME_CANCEL_BY_USER = "❗ **Canceled by the user.**"

    FLTR_ADD_LEFT_STR = "➕ Added Filter: `<code>{{ text_1 }}</code>` **to the LEFT**."
    FLTR_ADD_RIGHT_STR = (
        "➕ Addition Filter: `<code>{{ text_1 }}</code>` **to the RIGHT**."
    )
    FLTR_RM_STR = "❌ Remove Filter: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = (
        "🔄 Replace Filter: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."
    )

    CURRENT_FLTRS = "⚙️ **Your Current Filters:**"
    ADD_FLTR = "➕ Add Filter"
    RM_FLTR = "❌ Remove Filter"

    FILTERS_INTRO = (
        "🗒️ **Filter Guide:**\n"
        "There are 3 types of filters:\n\n"
        "🔄 **Replace Filter:** Replace a given word with another.\n"
        "➕ **Addition Filter:** Add a word at the beginning or end.\n"
        "❌ **Remove Filter:** Remove a word from the filename."
    )

    ADD_REPLACE_FLTR = "➕ Add Replace Filter"
    ADD_ADDITION_FLTR = "➕ Add Addition Filter"
    ADD_REMOVE_FLTR = "➕ Add Remove Filter"
    BACK = "🔙 Back"

    REPALCE_FILTER_INIT_MSG = "🖌️ Send the format: `<code>what_to_replace | replacement</code>` or `/ignore` to go back."

    NO_INPUT_FROM_USER = "⚠️ No input received from you."
    INPUT_IGNORE = "✅ **Ignored**."
    WRONG_INPUT_FORMAT = "❌ Invalid format. Check the provided format."
    REPLACE_FILTER_SUCCESS = (
        "✅ **Replace filter added:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "🖌️ Enter the text to add within `<code>|</code>`\n"
        "Example: `<code>| text to add |</code>`\n"
        "or `/ignore` to go back."
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ Added filter: `<code>{{ text_1 }}</code>` **to LEFT**."
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ Added filter: `<code>{{ text_1 }}</code>` **to RIGHT**."
    )

    ADDITION_LEFT = "🔄 Addition to LEFT"
    ADDITION_RIGHT = "🔄 Addition to RIGHT"

    ADDITION_POSITION_PROMPT = "📑 **Where do you want to add the text?**"

    REMOVE_FILTER_INIT_MSG = (
        "🖌️ Enter the text you want to remove or `/ignore` to go back."
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **Remove filter added:** `<code>{{ text_1 }}</code>` will be removed."
    )

    RENAME_THEMES_DOWNLOADING = [
        "✅ Download complete. Initiating rename magic...",
        "📦 File fetched! Ready to bless it with a new name...",
        "🪄 Download done. ✨ Let the rename ritual begin...",
        "🔧 Data acquired. Renaming engine revving up...",
        "💾 Saved and sealed. Now to rename with style...",
    ]

    RENAME_THEMES_UPLOADING = [
        "✅ All renamed and ready! Upload complete.",
        "🚀 File successfully rebranded and launched.",
        "📤 Upload done. Your renamed masterpiece is live!",
        "🌟 File rename finalized. Delivered to the cosmos!",
        "📁 Task complete. The file ascends renamed.",
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 Download halted. The rename dream fades...",
        "❗ You pulled the plug. Download aborted.",
        "❌ Operation scrapped mid-flight. No file fetched.",
        "📴 Rename canceled during download. Mission scrubbed.",
        "👋 User opted out mid-download. Peace out, file.",
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "🛑 Upload canceled. File stays local and unloved.",
        "❗ Rebrand reversed. Upload terminated.",
        "❌ Final stage interrupted. Rename abandoned.",
        "📴 Upload vetoed. Renamed file goes nowhere.",
        "👋 User said 'nope' during upload. File retired.",
    ]

    REPLY_TO_MEDIA = "📂 Reply `/rename` to a media file."

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "❗ Rename process encountered an error."

    DOWNLOADING_THE_FILE = "📥 Downloading the file"
    UPLOADING_THE_FILE = "📤 Uploading the file: **{{ new_file_name }}**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Rename Task Execution Started**\n"
        "🆔 Task ID: `{{ uid }}`\n\n"
        "👤 **User:** @{{ username }}\n"
        "📛 **Name:** {{ name }}\n"
        "📑 **User ID:** `<code>{{ user_id }}</code>`\n"
        "🪆 **File Name:** `<code>{{ file_name }}</code>`\n\n"
        "`🐳 FastWhale engine engaged.`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "📋 **Rename Task Registered**\n\n"
        "👤 **User:** @{{ username }}\n"
        "📛 **Name:** {{ name }}\n"
        "🆔 **User ID:** `<code>{{ user_id }}</code>`\n\n"
        "`🗳️ Queued for processing.`"
    )

    CAPTION_FOOT_NOTE = (
        "☄️ **NOTE:** You can set the caption using `/setcaption` followed by your desired text.\n"
        "📂 Use `<code>{file_name}</code>` to dynamically insert the renamed file name in the caption."
    )

    DELETE_CAPTION = "🗑 Delete Caption"
    CLOSE = "❌ Close"

    CAPTION_CURRENT = "📝 **Your Current Caption:** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **No caption set.**"
    CAPTION_SET = "✅ **Caption updated to:** {{ caption }}"
    CAPTION_DELETED = "🗑 **Caption deleted successfully.**"

    RENAME_ADDED_TO_QUEUE = (
        "🏷️ **Task Queued for Rename**\n"
        "🆔 **DC ID:** {{ dc_id }}\n"
        "🪆 **Media ID:** {{ media_id }}\n\n"
        "`🌀 Awaiting execution...`"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **Rename Queue Status:**\n"
        "☄️ **Total Tasks in Queue:** {{ total_tasks }}\n"
        "⚡ **Queue Capacity:** {{ queue_capacity }}\n"
        "⏳ **Currently Processing:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **Your Task is Currently Executing**\n"
        "🆔 **Task ID:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Your Task Position in Queue:** {{ task_number }}\n"
        "🆔 **Task ID:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "🌋 **You have been removed from the chat. You cannot use this bot.**"
    USER_NOT_PARTICIPANT = (
        "🖌️ **Access Denied**\n\n"
        "📜 To use this bot, please join the updates channel first.\n\n"
        "`🐋 FastWhale bots swim only with the pod.`"
    )
    
    JOIN_CHANNEL = "🔗 Join Updates Channel"

    MODE_INITIAL_MSG = (
        "📂 **File Output Mode:**\n\n"
        "1️⃣ **Same format as sent.**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Force to Document.**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **Upload as General Media.**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "🖌️ **Select the renaming mode:**\n"
        "🅰️ **Rename with command.**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Rename without command.**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 Reply to an image to set it as a thumbnail."
    THUMB_SET_SUCCESS = "✅ **Thumbnail set successfully.**"
    THUMB_NOT_FOUND = "⚠️ **No Thumbnail Found.**"
    THUMB_CLEARED = "🗑 **Thumbnail cleared successfully.**"

    HELP_STR = (
        "📖 **Bot Commands:**\n"
        "`{{ startcmd }}` - ✅ Check if the bot is running.\n"
        "`{{ renamecmd }}` - 🖌️ Reply to a media file with `/rename filename.extension` to rename it.\n"
        "`{{ filterscmd }}` - ⚙️ Manage your rename filters.\n"
        "`{{ setthumbcmd }}` - 📷 Set a permanent thumbnail (reply to an image).\n"
        "`{{ getthumbcmd }}` - 📸 Get the currently set thumbnail.\n"
        "`{{ clrthumbcmd }}` - ❌ Remove the set thumbnail.\n"
        "`{{ modecmd }}` - 🔄 Switch between 3 output modes:\n"
        "    - 📝 Same format as sent.\n"
        "    - 📂 Forced Document.\n"
        "    - 🎥 General Media (streamable video/audio).\n\n"
        "    🔄 Switch between renaming modes:\n"
        "    - 🏷 Rename **with command**.\n"
        "    - ✨ Rename **without command/auto Rename**.\n\n"
        "`{{ queuecmd }}` - 📊 View the bot's rename queue status.\n"
        "`{{ setcaptioncmd }}` - 📝 Set a caption for the renamed files.\n"
        "`{{ helpcmd }}` - 📖 Show this help message.\n"
        "`{{ pingcmd }}` - 🎈Ping Bot.\n"
        "`{{ infocmd }}` - 🧑‍💻 View bot info.\n"
        "`{{ profilecmd }}` - ☄️ Your usage stats.\n"
        "`{{ statuscmd }}` - 🗿 Bot Status.\n"
        "`{{ statscmd }}` - 👻 Global bot stats.\n"
        "`{{ broadcastcmd }}` - ☄️Make it go broadcast.\n"
        "`{{ leaderboardcmd }}` - 👻 Users leaderboard.\n"
        "`{{ setlanguagecmd }}` - 🌐 Change the bot's language."
    )

    CURRENT_LOCALE = "🌐 **Your current language:** {{ user_locale }}"

