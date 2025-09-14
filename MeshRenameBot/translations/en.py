from dataclasses import dataclass
import random

@dataclass
class EnglishTranslations:
    LANGUAGE_NAME = "🇬🇧 English"
    LANGUAGE_CODE = "en"

    WRONG_VALUE_ERROR = "❌ Oopsie! Invalid value for {{ variable_name }}. Try again! 🤷‍♀️"

    START_MSG = (
    "✨ **Hey there, file wizard!** ✨\n\n"
    "I'm **Auto Rename Bot** 🪄, your magical file-renaming assistant!\n\n"
    "🔥 **Why you'll love me:**\n"
    "- Rename files with ✨ sparkle and precision\n"
    "- Blazing fast ⚡ and secure 🔒\n"
    "- Supports ALL the file types! 📂🎵🎬\n\n"
    "Just send me a file and let's make magic happen! 🎩\n\n"
    "🚀 **Pro Tip:** Use /mode for auto-rename ninja mode(must add /filters)!\n"
    "Need help? /help has your back!\n\n"
    "🛸 **Powered by** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "❗ Rename cancelled! Poof! ✨ (Updates coming soon!)"

    RENAME_NO_FILTER_MATCH = (
        "🔮 **Whoops! No filter match!**\n\n"
        "Tried using filters but came up empty 🎩🐇\n"
        "Manage your filters with /filters ✏️"
    )

    RENAME_FILTER_MATCH_USED = (
        "🎯 **Filter power activated!**\n"
        "Using filters since you didn't specify a name\n"
        "Tweak them with /filters ⚙️"
    )

    RENAME_NOFLTR_NONAME = (
        "📝 **NO filters found!**\n\n"
        "Please add /filters 🎨 for Auto pick rename filters."
    )

    RENAME_CANCEL = "❌ Nah, let's cancel this ✌️"

    RENAMING_FILE = "🌀 **File transformation in progress...**"

    DL_RENAMING_FILE = "📥 **Downloading your digital treasure...**"

    RENAME_ERRORED_REPORT = "💥 **Yikes! Something broke!** Please report this 🚨"

    RENAME_CANCEL_BY_USER = "🙅‍♂️ **You waved the cancel wand!** ✨"

    FLTR_ADD_LEFT_STR = "➕ Added Filter: `<code>{{ text_1 }}</code>` **to the LEFT**."
    FLTR_ADD_RIGHT_STR = (
        "➕ Addition Filter: `<code>{{ text_1 }}</code>` **to the RIGHT**."
    )
    FLTR_RM_STR = "❌ Remove Filter: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = (
        "🔄 Replace Filter: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."
    )

    CURRENT_FLTRS = "🎛️ **Your Filter Dashboard:**"
    ADD_FLTR = "➕ Add Filter"
    RM_FLTR = "❌ Remove Filter"

    FILTERS_INTRO = (
        "🛠 **Filter Guide:**\n"
        "There are 3 types of filters:\n\n"
        "🔄 **Replace Filter:** Replace a given word with another.\n"
        "➕ **Addition Filter:** Add a word at the beginning or end.\n"
        "❌ **Remove Filter:** Remove a word from the filename."
    )

    ADD_REPLACE_FLTR = "➕ Add Replace Filter"
    ADD_ADDITION_FLTR = "➕ Add Addition Filter"
    ADD_REMOVE_FLTR = "➕ Add Remove Filter"
    BACK = "🔙 Back"

    REPALCE_FILTER_INIT_MSG = "✍️ Send the format: `<code>what_to_replace | replacement</code>` or /ignore to go back."

    NO_INPUT_FROM_USER = "🤷‍♂️ **Crickets...** No input detected!"
    INPUT_IGNORE = "👍 **Ignored!**"
    WRONG_INPUT_FORMAT = "🤦‍♂️ **Whoops!** Wrong format! Check the provided format & Try again!"
    REPLACE_FILTER_SUCCESS = (
        "✅ **Replace filter added:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ Enter the text to add within `<code>|</code>`\n"
        "Example: `<code>| text to add |</code>`\n"
        "or /ignore to go back."
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ Added filter: `<code>{{ text_1 }}</code>` **to LEFT**."
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ Added filter: `<code>{{ text_1 }}</code>` **to RIGHT**."
    )

    ADDITION_LEFT = "🔄 Addition to LEFT"
    ADDITION_RIGHT = "🔄 Addition to RIGHT"

    ADDITION_POSITION_PROMPT = "🧙‍♂️ **Where do you want to add the text?**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ Enter the text you want to remove or /ignore to go back."
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **Remove filter added:** `<code>{{ text_1 }}</code>` will be removed."
    )

    RENAME_THEMES_DOWNLOADING = [
        "🎩 Download complete! Preparing magic...",
        "📦 File acquired! Ready for naming sorcery...",
        "✨ Download successful! Incantations beginning...",
        "⚡ Data secured! Renaming engines firing up...",
        "💾 File captured! Preparing for glorious rebirth..."
    ]

    RENAME_THEMES_UPLOADING = [
        "🚀 **Blast off!** Renamed file launched!",
        "🎉 **Ta-da!** Your newly named file is ready!",
        "📤 Upload complete! Enjoy your masterpiece!",
        "🌟 File metamorphosis complete!",
        "🏁 Race over! Your file has crossed the finish line!"
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 **Abort!** Download spell interrupted!",
        "🚧 Whoops! You stopped the download train!",
        "🎭 The show's over before it began!",
        "📵 Download connection terminated!",
        "👋 You ghosted the download! Bye-bye!"
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "✋ **Hold up!** Upload stopped mid-flight!",
        "🚫 No delivery today! Upload cancelled!",
        "🌪️ Upload tornado dissipated!",
        "📴 Connection lost in the void!",
        "🤷‍♂️ You changed your mind! Upload aborted!"
    ]

    REPLY_TO_MEDIA = "📎 **Psst!** Reply `/rename` to a file!"

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "💥 **Kaboom!** Renaming spell failed!"

    DOWNLOADING_THE_FILE = "📥 **Fetching your file...**"
    UPLOADING_THE_FILE = "📤 **Launching:** `{{ new_file_name }}` 🚀"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Rename Mission Initiated**\n"
        "🆔 Mission ID: `{{ uid }}`\n\n"
        "👤 **Agent:** @{{ username }}\n"
        "📛 **Codename:** {{ name }}\n"
        "🪪 **ID:** `{{ user_id }}`\n"
        "📜 **File:** `{{ file_name }}`\n\n"
        "`⚡ Hyperdrive engaged!`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "📥 **Rename Mission Queued**\n\n"
        "👤 **Agent:** @{{ username }}\n"
        "📛 **Codename:** {{ name }}\n"
        "🪪 **ID:** `{{ user_id }}`\n\n"
        "`⏳ Awaiting deployment...`"
    )

    CAPTION_FOOT_NOTE = (
        "💡 **Pro Tip:** Use /setcaption to add flair!\n"
        "✨ Use `/setcaption {file_name}` to auto-fill the filename in the caption!"
    )

    DELETE_CAPTION = "🗑️ Yeet Caption"
    CLOSE = "🚪 Exit"

    CAPTION_CURRENT = "📝 **Current Caption:** {{ caption }}"
    CAPTION_NOT_SET = "🫗 **Caption empty!** So lonely..."
    CAPTION_SET = "✅ **New Caption:** {{ caption }}"
    CAPTION_DELETED = "🗑️ **Caption deleted successfully.**"

    RENAME_ADDED_TO_QUEUE = (
        "📊 **Rename in Queue**\n"
        "🆔 **DC ID:** {{ dc_id }}\n"
        "📦 **Media ID:** {{ media_id }}\n\n"
        "`⏳ Patience, young padawan...`"
    )

    RENAME_QUEUE_STATUS = (
        "📈 **Queue Stats:**\n"
        "📊 **Total Tasks:** {{ total_tasks }}\n"
        "⚡ **Capacity:** {{ queue_capacity }}\n"
        "⏳ **Processing:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **Your file is being MAGIC'D!**\n"
        "🆔 **Task ID:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Your place in line:** {{ task_number }}\n"
        "🆔 **Task ID:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👢 **You've been booted!** No bot for you!"
    USER_NOT_PARTICIPANT = (
        "🔒 **Secret Club Alert!**\n\n"
        "Join our channel to unlock the magic!\n\n"
        "`🦄 Unicorns only beyond this point`"
    )
    
    JOIN_CHANNEL = "🔗 Join Secret Club"

    MODE_INITIAL_MSG = (
        "🎛️ **Output Mode Selector:**\n\n"
        "1️⃣ **Keep original format**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Force Document mode**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **General Media mode**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "✨ **Rename Style:**\n"
        "🅰️ **Command rename**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Auto-rename**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣ OG Mode"
    MODE_SET_1 = "2️⃣ Doc Mode"
    MODE_SET_2 = "3️⃣ Media Mode"
    COMMAND_MODE_SET_3 = "🅰️ Command"
    COMMAND_MODE_SET_4 = "🅱️ Auto"

    THUMB_REPLY_TO_MEDIA = "🖼️ **Reply to an image** to set as thumbnail"
    THUMB_SET_SUCCESS = "✅ **Thumbnail locked in!**"
    THUMB_NOT_FOUND = "🕵️‍♂️ **No thumbnail detected!**"
    THUMB_CLEARED = "🧹 **Thumbnail swept away!**"

    HELP_STR = (
        "📚 **Magic Spellbook:**\n"
        "`{{ startcmd }}` - Check if I'm alive! 💓\n"
        "`{{ renamecmd }}` - Rename files like a boss! 🎩\n"
        "`{{ filterscmd }}` - Customize your renaming filters! ✨\n"
        "`{{ setthumbcmd }}` - Set a permanent thumbnail! 🖼️\n"
        "`{{ getthumbcmd }}` - Peek at current thumbnail! 👀\n"
        "`{{ clrthumbcmd }}` - Delete thumbnail! 🗑️\n"
        "`{{ modecmd }}` - Switch output modes:\n"
        "   - 📝 Original format\n"
        "   - 📂 Force document\n"
        "   - 🎥 Media mode\n\n"
        "   Switch rename styles:\n"
        "   - 🏷️ Command-based\n"
        "   - 🤖 Auto-rename(must add /filters)\n\n"
        "`{{ queuecmd }}` - Check rename queue 📊\n"
        "`{{ setcaptioncmd }}` - Set fancy captions 🎨\n"
        "`{{ helpcmd }}` - This magic book! 📖\n"
        "`{{ pingcmd }}` - Ping-pong! 🏓\n"
        "`{{ infocmd }}` - Bot specs! 🤖\n"
        "`{{ profilecmd }}` - Your stats! 📈\n"
        "`{{ statuscmd }}` - Bot vitals! 💓\n"
        "`{{ statscmd }}` - Global numbers! 🌍\n"
        "`{{ broadcastcmd }}` - Mega-announce! 📢\n"
        "`{{ leaderboardcmd }}` - Top users! 🏆\n"
        "`{{ setlanguagecmd }}` - Change language! 🌐"
    )

    CURRENT_LOCALE = "🌍 **Your language:** {{ user_locale }}"

