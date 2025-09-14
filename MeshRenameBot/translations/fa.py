from dataclasses import dataclass
import random

@dataclass
class PersianTranslations:
    LANGUAGE_NAME = "🇮🇷 فارسی"
    LANGUAGE_CODE = "fa"

    WRONG_VALUE_ERROR = "❌ اوه! مقدار نامعتبر برای {{ variable_name }}. دوباره تلاش کن! 🤷‍♀️"

    START_MSG = (
    "✨ **سلام جادوگر فایل!** ✨\n\n"
    "من **ربات تغییر نام خودکار** 🪄 هستم، دستیار جادویی تو برای تغییر نام فایل‌ها!\n\n"
    "🔥 **چرا منو دوست خواهی داشت:**\n"
    "- تغییر نام فایل‌ها با ✨ درخشش و دقت\n"
    "- فوق العاده سریع ⚡ و امن 🔒\n"
    "- پشتیبانی از تمامی انواع فایل! 📂🎵🎬\n\n"
    "فقط یک فایل برام بفرست و بذار جادو کنیم! 🎩\n\n"
    "🚀 **نکته حرفه‌ای:** از /mode برای حالت نینجای تغییر نام خودکار استفاده کن (باید /filters اضافه کنی)!\n"
    "نیاز به کمک داری؟ /help پشتیبانته!\n\n"
    "🛸 **قدرت گرفته توسط** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "❗ تغییر نام لغو شد! پوف! ✨ (به‌زودی آپدیت‌ها می‌رسن!)"

    RENAME_NO_FILTER_MATCH = (
        "🔮 **اوه! هیچ تطابق فیلتری!**\n\n"
        "سعی کردم از فیلترها استفاده کنم اما چیزی پیدا نکردم 🎩🐇\n"
        "فیلترهای خودت رو با /filters مدیریت کن ✏️"
    )

    RENAME_FILTER_MATCH_USED = (
        "🎯 **قدرت فیلتر فعال شد!**\n"
        "از فیلترها استفاده می‌کنم چون نامی مشخص نکردی\n"
        "با /filters تنظیمشون کن ⚙️"
    )

    RENAME_NOFLTR_NONAME = (
        "📝 **هیچ فیلتری پیدا نشد!**\n\n"
        "لطفا /filters 🎨 رو برای فیلترهای انتخاب خودکار تغییر نام اضافه کن."
    )

    RENAME_CANCEL = "❌ نه، بیا این رو لغو کنیم ✌️"

    RENAMING_FILE = "🌀 **تبدیل فایل در حال انجام...**"

    DL_RENAMING_FILE = "📥 **در حال دانلود گنج دیجیتالت...**"

    RENAME_ERRORED_REPORT = "💥 **ای وای! یه چیزی خراب شد!** لطفا این رو گزارش بده 🚨"

    RENAME_CANCEL_BY_USER = "🙅‍♂️ **چوب جادوی لغو رو تکان دادی!** ✨"

    FLTR_ADD_LEFT_STR = "➕ فیلتر اضافه شد: `<code>{{ text_1 }}</code>` **به چپ**."
    FLTR_ADD_RIGHT_STR = (
        "➕ فیلتر اضافه شد: `<code>{{ text_1 }}</code>` **به راست**."
    )
    FLTR_RM_STR = "❌ فیلتر حذف شد: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = (
        "🔄 فیلتر جایگزین شد: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."
    )

    CURRENT_FLTRS = "🎛️ **داشبورد فیلترهای تو:**"
    ADD_FLTR = "➕ افزودن فیلتر"
    RM_FLTR = "❌ حذف فیلتر"

    FILTERS_INTRO = (
        "🛠 **راهنمای فیلترها:**\n"
        "۳ نوع فیلتر وجود داره:\n\n"
        "🔄 **فیلتر جایگزینی:** یک کلمه رو با دیگری جایگزین کن.\n"
        "➕ **فیلتر افزودن:** یک کلمه به ابتدا یا انتها اضافه کن.\n"
        "❌ **فیلتر حذف:** یک کلمه از نام فایل حذف کن."
    )

    ADD_REPLACE_FLTR = "➕ افزودن فیلتر جایگزینی"
    ADD_ADDITION_FLTR = "➕ افزودن فیلتر افزودن"
    ADD_REMOVE_FLTR = "➕ افزودن فیلتر حذف"
    BACK = "🔙 بازگشت"

    REPALCE_FILTER_INIT_MSG = "✍️ قالب رو ارسال کن: `<code>چه_چیزی_جایگزین_شود | جایگزین</code>` یا /ignore برای برگشت."

    NO_INPUT_FROM_USER = "🤷‍♂️ **جیرجیرک...** هیچ ورودی تشخیص داده نشد!"
    INPUT_IGNORE = "👍 **نادیده گرفته شد!**"
    WRONG_INPUT_FORMAT = "🤦‍♂️ **اوه!** فرمت اشتباه! قالب ارائه شده رو بررسی کن و دوباره تلاش کن!"
    REPLACE_FILTER_SUCCESS = (
        "✅ **فیلتر جایگزینی اضافه شد:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ متنی که می‌خوای اضافه کنی رو بین `<code>|</code>` وارد کن\n"
        "مثال: `<code>| متنی برای اضافه کردن |</code>`\n"
        "یا /ignore برای برگشت."
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ فیلتر اضافه شد: `<code>{{ text_1 }}</code>` **به چپ**."
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ فیلتر اضافه شد: `<code>{{ text_1 }}</code>` **به راست**."
    )

    ADDITION_LEFT = "🔄 افزودن به چپ"
    ADDITION_RIGHT = "🔄 افزودن به راست"

    ADDITION_POSITION_PROMPT = "🧙‍♂️ **کجا می‌خوای متن رو اضافه کنی؟**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ متنی که می‌خوای حذف کنی رو وارد کن یا /ignore برای برگشت."
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **فیلتر حذف اضافه شد:** `<code>{{ text_1 }}</code>` حذف خواهد شد."
    )

    RENAME_THEMES_DOWNLOADING = [
        "🎩 دانلود کامل! آماده‌سازی جادو...",
        "📦 فایل دریافت شد! آماده برای جادوی نام‌گذاری...",
        "✨ دانلود موفق! طلسم‌ها شروع می‌شه...",
        "⚡ داده‌ها امن شد! موتورهای تغییر نام روشن می‌شن...",
        "💾 فایل ضبط شد! آماده برای تولد مجدد باشکوه..."
    ]

    RENAME_THEMES_UPLOADING = [
        "🚀 **پرتاب!** فایل تغییر نام داده شده پرتاب شد!",
        "🎉 **تا-دا!** فایل با نام جدیدت آماده است!",
        "📤 آپلود کامل! از شاهکارت لذت ببر!",
        "🌟 دگردیسی فایل کامل شد!",
        "🏁 مسابقه تموم شد! فایل تو از خط پایان عبور کرد!"
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 **لغو!** طلسم دانلود قطع شد!",
        "🚧 اوه! قطار دانلود رو متوقف کردی!",
        "🎭 نمایش تموم شد قبل از شروع!",
        "📵 اتصال دانلود قطع شد!",
        "👋 دانلود رو رها کردی! خداحافظ!"
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "✋ **صبر کن!** آپلود وسط پرواز متوقف شد!",
        "🚫 هیچ تحویلی امروز! آپلود لغو شد!",
        "🌪️ tornado آپلود پراکنده شد!",
        "📴 اتصال در خلا گم شد!",
        "🤷‍♂️ نظرت رو عوض کردی! آپلود لغو شد!"
    ]

    REPLY_TO_MEDIA = "📎 **پیس!** به یک فایل `/rename` رو ریپلای کن!"

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "💥 **کابوم!** طلسم تغییر نام شکست خورد!"

    DOWNLOADING_THE_FILE = "📥 **در حال گرفتن فایل تو...**"
    UPLOADING_THE_FILE = "📤 **در حال پرتاب:** `{{ new_file_name }}` 🚀"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **ماموریت تغییر نام شروع شد**\n"
        "🆔 شناسه ماموریت: `{{ uid }}`\n\n"
        "👤 **عامل:** @{{ username }}\n"
        "📛 **نام رمز:** {{ name }}\n"
        "🪪 **شناسه:** `{{ user_id }}`\n"
        "📜 **فایل:** `{{ file_name }}`\n\n"
        "`⚡ هایپردرایو فعال شد!`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "📥 **ماموریت تغییر نام در صف**\n\n"
        "👤 **عامل:** @{{ username }}\n"
        "📛 **نام رمز:** {{ name }}\n"
        "🪪 **شناسه:** `{{ user_id }}`\n\n"
        "`⏳ در انتظار استقرار...`"
    )

    CAPTION_FOOT_NOTE = (
        "💡 **نکته حرفه‌ای:** از /setcaption برای افزودن ظرافت استفاده کن!\n"
        "✨ از `/setcaption {file_name}` برای پر کردن خودکار نام فایل در کپشن استفاده کن!"
    )

    DELETE_CAPTION = "🗑️ حذف کپشن"
    CLOSE = "🚪 خروج"

    CAPTION_CURRENT = "📝 **کپشن فعلی:** {{ caption }}"
    CAPTION_NOT_SET = "🫗 **کپشن خالیه!** خیلی تنها..."
    CAPTION_SET = "✅ **کپشن جدید:** {{ caption }}"
    CAPTION_DELETED = "🗑️ **کپشن با موفقیت حذف شد.**"

    RENAME_ADDED_TO_QUEUE = (
        "📊 **تغییر نام در صف**\n"
        "🆔 **شناسه DC:** {{ dc_id }}\n"
        "📦 **شناسه مدیا:** {{ media_id }}\n\n"
        "`⏳ صبر کن، پادوان جوان...`"
    )

    RENAME_QUEUE_STATUS = (
        "📈 **آمار صف:**\n"
        "📊 **کل تسک‌ها:** {{ total_tasks }}\n"
        "⚡ **ظرفیت:** {{ queue_capacity }}\n"
        "⏳ **در حال پردازش:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **فایل تو داره جادو میشه!**\n"
        "🆔 **شناسه تسک:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **جای تو در صف:** {{ task_number }}\n"
        "🆔 **شناسه تسک:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👢 **تو اخراج شدی!** هیچ رباتی برات نیست!"
    USER_NOT_PARTICIPANT = (
        "🔒 **هشدار کلاب مخفی!**\n\n"
        "برای باز کردن جادو به کانال ما بپیوند!\n\n"
        "`🦄 فقط اسب‌های شاخدار از این نقطه به بعد`"
    )
    
    JOIN_CHANNEL = "🔗 پیوستن به کلاب مخفی"

    MODE_INITIAL_MSG = (
        "🎛️ **انتخاب‌کننده حالت خروجی:**\n\n"
        "1️⃣ **حفظ فرمت اصلی**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **اجبار حالت سند**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **حالت مدیا عمومی**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "✨ **سبک تغییر نام:**\n"
        "🅰️ **تغییر نام با دستور**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **تغییر نام خودکار**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣ حالت OG"
    MODE_SET_1 = "2️⃣ حالت سند"
    MODE_SET_2 = "3️⃣ حالت مدیا"
    COMMAND_MODE_SET_3 = "🅰️ دستور"
    COMMAND_MODE_SET_4 = "🅱️ خودکار"

    THUMB_REPLY_TO_MEDIA = "🖼️ **به یک عکس ریپلای کن** تا به عنوان thumbnail تنظیم بشه"
    THUMB_SET_SUCCESS = "✅ **thumbnail قفل شد!**"
    THUMB_NOT_FOUND = "🕵️‍♂️ **هیچ thumbnailی detect نشد!**"
    THUMB_CLEARED = "🧹 **thumbnail پاک شد!**"

    HELP_STR = (
        "📚 **کتاب طلسم جادویی:**\n"
        "`{{ startcmd }}` - چک کن که زنده‌م! 💓\n"
        "`{{ renamecmd }}` - فایل‌ها رو مثل رئیس تغییر نام بده! 🎩\n"
        "`{{ filterscmd }}` - فیلترهای تغییر نامت رو سفارشی کن! ✨\n"
        "`{{ setthumbcmd }}` - یک thumbnail دائمی تنظیم کن! 🖼️\n"
        "`{{ getthumbcmd }}` - به thumbnail فعلی نگاه کن! 👀\n"
        "`{{ clrthumbcmd }}` - thumbnail رو پاک کن! 🗑️\n"
        "`{{ modecmd }}` - تغییر حالت‌های خروجی:\n"
        "   - 📝 فرمت اصلی\n"
        "   - 📂 اجبار سند\n"
        "   - 🎥 حالت مدیا\n\n"
        "   تغییر سبک‌های تغییر نام:\n"
        "   - 🏷️ مبتنی بر دستور\n"
        "   - 🤖 تغییر نام خودکار (باید /filters اضافه کنی)\n\n"
        "`{{ queuecmd }}` - صف تغییر نام رو چک کن 📊\n"
        "`{{ setcaptioncmd }}` - کپشن‌های فانتزی تنظیم کن 🎨\n"
        "`{{ helpcmd }}` - این کتاب جادویی! 📖\n"
        "`{{ pingcmd }}` - پینگ-پنگ! 🏓\n"
        "`{{ infocmd }}` - مشخصات ربات! 🤖\n"
        "`{{ profilecmd }}` - آمار تو! 📈\n"
        "`{{ statuscmd }}` - علائم حیاتی ربات! 💓\n"
        "`{{ statscmd }}` - آمار جهانی! 🌍\n"
        "`{{ broadcastcmd }}` - مگا-اعلان! 📢\n"
        "`{{ leaderboardcmd }}` - کاربران برتر! 🏆\n"
        "`{{ setlanguagecmd }}` - تغییر زبان! 🌐"
    )

    CURRENT_LOCALE = "🌍 **زبان تو:** {{ user_locale }}"
