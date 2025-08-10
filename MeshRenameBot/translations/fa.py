from dataclasses import dataclass
import random

@dataclass
class PersianTranslations:
    LANGUAGE_NAME = "🇮🇷 فارسی"
    LANGUAGE_CODE = "fa"

    WRONG_VALUE_ERROR = "❌ مقدار نامعتبر برای متغیر {{ variable_name }} وارد شده است."

    START_MSG = (
        "سلام! 👋\n"
        "من **ربات تغییر نام خودکار** هستم، دستیار شما برای تغییر نام فایل‌ها در تلگرام.\n\n"
        "✨ **ویژگی‌های کلیدی:**\n"
        "- تغییر نام فایل‌ها با نام و پسوند دلخواه\n"
        "- سریع، امن و آسان برای استفاده\n"
        "- پشتیبانی از انواع فایل‌ها\n\n"
        "کافیست یک فایل برای من بفرستید، من شما را در فرآیند تغییر نام راهنمایی می‌کنم!\n\n"
        "بیایید شروع کنیم! از /mode برای فعال‌سازی تغییر نام خودکار استفاده کنید، **تغییر نام بدون دستور**🚀\n"
        "برای اطلاعات بیشتر /help را بفرستید.\n\n"
        "🚀 **قدرت گرفته توسط** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "⚠️ تغییر نام **لغو شد**. به زودی به‌روزرسانی می‌شود."

    RENAME_NO_FILTER_MATCH = (
        "🚫 **هیچ فیلتری مطابقت نداشت - لغو تغییر نام**\n\n"
        "🔍 از فیلترها برای تغییر نام استفاده می‌شود چون نامی مشخص نشده است.\n"
        "👻 فیلترهای خود را با /filters مدیریت کنید."
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ از فیلترها برای تغییر نام استفاده می‌شود چون نامی مشخص نشده است.\n"
        "👻 فیلترهای خود را با /filters مدیریت کنید."
    )

    RENAME_NOFLTR_NONAME = (
        "✍️ نام جدید فایل را به این فرمت وارد کنید:\n"
        "```/rename نام_جدید_فایل.پسوند```\n"
        "یا از `/filters` برای تنظیم فیلترهای تغییر نام استفاده کنید."
    )

    RENAME_CANCEL = "❌ لغو این تغییر نام."

    RENAMING_FILE = "🔄 در حال تغییر نام فایل... لطفا صبر کنید."

    DL_RENAMING_FILE = "📥 در حال دانلود فایل... لطفا صبر کنید."

    RENAME_ERRORED_REPORT = "❗ خطایی در دانلود رخ داد. این مشکل را گزارش دهید."

    RENAME_CANCEL_BY_USER = "🚫 **توسط کاربر لغو شد.**"

    FLTR_ADD_LEFT_STR = "➕ فیلتر اضافه شد: `<code>{{ text_1 }}</code>` **به چپ**."
    FLTR_ADD_RIGHT_STR = "➕ فیلتر اضافه شد: `<code>{{ text_1 }}</code>` **به راست**."
    FLTR_RM_STR = "❌ فیلتر حذف شد: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = "🔄 فیلتر جایگزین شد: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."

    CURRENT_FLTRS = "⚙️ **فیلترهای فعلی شما:**"
    ADD_FLTR = "➕ افزودن فیلتر"
    RM_FLTR = "❌ حذف فیلتر"

    FILTERS_INTRO = (
        "🛠 **راهنمای فیلترها:**\n"
        "سه نوع فیلتر وجود دارد:\n\n"
        "🔄 **فیلتر جایگزینی:** جایگزینی یک کلمه با کلمه دیگر\n"
        "➕ **فیلتر افزودنی:** افزودن کلمه در ابتدا یا انتها\n"
        "❌ **فیلتر حذفی:** حذف یک کلمه از نام فایل"
    )

    ADD_REPLACE_FLTR = "➕ افزودن فیلتر جایگزینی"
    ADD_ADDITION_FLTR = "➕ افزودن فیلتر افزودنی"
    ADD_REMOVE_FLTR = "➕ افزودن فیلتر حذفی"
    BACK = "🔙 بازگشت"

    REPALCE_FILTER_INIT_MSG = "✍️ فرمت را ارسال کنید: `<code>چه_چیزی_جایگزین_شود | جایگزین</code>` یا `/ignore` برای بازگشت."

    NO_INPUT_FROM_USER = "⚠️ هیچ ورودی از شما دریافت نشد."
    INPUT_IGNORE = "✅ **نادیده گرفته شد**."
    WRONG_INPUT_FORMAT = "❌ فرمت نامعتبر. فرمت ارائه شده را بررسی کنید."
    REPLACE_FILTER_SUCCESS = "✅ **فیلتر جایگزینی اضافه شد:**\n`'{{ text_1 }}'` → `'{{ text_2 }}'`"

    ADDITION_FILTER_INIT_MSG = (
        "✍️ متنی که می‌خواهید اضافه کنید را در `<code>|</code>` وارد کنید\n"
        "مثال: `<code>| متنی برای اضافه کردن |</code>`\n"
        "یا `/ignore` برای بازگشت."
    )

    ADDITION_FILTER_SUCCESS_LEFT = "✅ فیلتر اضافه شد: `<code>{{ text_1 }}</code>` **به چپ**."
    ADDITION_FILTER_SUCCESS_RIGHT = "✅ فیلتر اضافه شد: `<code>{{ text_1 }}</code>` **به راست**."

    ADDITION_LEFT = "🔄 افزودن به چپ"
    ADDITION_RIGHT = "🔄 افزودن به راست"

    ADDITION_POSITION_PROMPT = "📍 **می‌خواهید متن را کجا اضافه کنید؟**"

    REMOVE_FILTER_INIT_MSG = "✍️ متنی که می‌خواهید حذف شود را وارد کنید یا `/ignore` برای بازگشت."

    REMOVE_FILTER_SUCCESS = "✅ **فیلتر حذفی اضافه شد:** `<code>{{ text_1 }}</code>` حذف خواهد شد."

    RENAME_THEMES_DOWNLOADING = [
        "✅ دانلود کامل شد. شروع جادوی تغییر نام...",
        "📦 فایل دریافت شد! آماده اعطای نام جدید...",
        "🪄 دانلود انجام شد. ✨ بیایید مراسم تغییر نام را شروع کنیم...",
        "🔧 داده دریافت شد. موتور تغییر نام روشن می‌شود...",
        "💾 ذخیره و مهر و موم شد. حالا با استایل تغییر نام دهید...",
    ]

    RENAME_THEMES_UPLOADING = [
        "✅ همه تغییر نام داده شدند! آپلود کامل شد.",
        "🚀 فایل با موفقیت تغییر نام داده و ارسال شد.",
        "📤 آپلود انجام شد. شاهکار تغییر نام یافته شما زنده است!",
        "🌟 تغییر نام فایل نهایی شد. به کیهان تحویل داده شد!",
        "📁 کار تکمیل شد. فایل با نام جدید صعود کرد.",
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 دانلود متوقف شد. رویای تغییر نام محو می‌شود...",
        "🚫 شما متوقفش کردید. دانلغو شد.",
        "❌ عملیات در میانه راه لغو شد. هیچ فایلی دریافت نشد.",
        "📴 تغییر نام در حین دانلود لغو شد. ماموریت لغو شد.",
        "👋 کاربر در میانه دانلغو انصراف داد. خداحافظ فایل.",
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "🛑 آپلغو شد. فایل محلی و دوست‌نداشتنی می‌ماند.",
        "🚫 تغییر نام معکوس شد. آپلود متوقف شد.",
        "❌ مرحله نهایی مختل شد. تغییر نام رها شد.",
        "📴 آپلغو وتو شد. فایل تغییر نام یافته به جایی نمی‌رود.",
        "👋 کاربر گفت 'نه' در حین آپلود. فایل بازنشسته شد.",
    ]

    REPLY_TO_MEDIA = "📂 با `/rename` به یک فایل رسانه پاسخ دهید."

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "❗ خطایی در فرآیند تغییر نام رخ داد."

    DOWNLOADING_THE_FILE = "📥 در حال دانلود فایل"
    UPLOADING_THE_FILE = "📤 در حال آپلود فایل: **{{ new_file_name }}**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **شروع اجرا برای کار تغییر نام**\n"
        "🆔 شناسه کار: `{{ uid }}`\n\n"
        "👤 **نام کاربری:** @{{ username }}\n"
        "📛 **نام:** {{ name }}\n"
        "🆔 **شناسه کاربر:** `<code>{{ user_id }}</code>`\n"
        "📂 **نام فایل:** `<code>{{ file_name }}</code>`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "✅ **کار تغییر نام اضافه شد**\n\n"
        "👤 **نام کاربری:** @{{ username }}\n"
        "📛 **نام:** {{ name }}\n"
        "🆔 **شناسه کاربر:** `<code>{{ user_id }}</code>`"
    )

    CAPTION_FOOT_NOTE = (
        "☄️ **توجه:** می‌توانید کپشن را با `/setcaption` و متن دلخواه تنظیم کنید.\n"
        "📂 از `<code>{file_name}</code>` برای درج پویای نام فایل در کپشن استفاده کنید."
    )

    DELETE_CAPTION = "🗑 حذف کپشن"
    CLOSE = "❌ بستن"

    CAPTION_CURRENT = "📝 **کپشن فعلی شما:** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **کپشنی تنظیم نشده است.**"
    CAPTION_SET = "✅ **کپشن به این به‌روزرسانی شد:** {{ caption }}"
    CAPTION_DELETED = "🗑 **کپشن با موفقیت حذف شد.**"

    RENAME_ADDED_TO_QUEUE = (
        "📥 **کار تغییر نام به صف اضافه شد**\n"
        "🆔 **شناسه DC:** {{ dc_id }}\n"
        "👻 **شناسه رسانه:** {{ media_id }}"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **وضعیت صف تغییر نام:**\n"
        "☄️ **کل کارها در صف:** {{ total_tasks }}\n"
        "⚡ **ظرفیت صف:** {{ queue_capacity }}\n"
        "⏳ **در حال پردازش:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **کار شما در حال اجراست**\n"
        "🆔 **شناسه کار:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **موقعیت کار شما در صف:** {{ task_number }}\n"
        "🆔 **شناسه کار:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👻 **شما از چت حذف شده‌اید. نمی‌توانید از این ربات استفاده کنید.**"
    USER_NOT_PARTICIPANT = "👻 **برای استفاده از این ربات باید در چت مورد نظر عضو شوید.**"
    JOIN_CHANNEL = "🔗 عضویت در کانال به‌روزرسانی‌ها"

    MODE_INITIAL_MSG = (
        "📂 **حالت خروجی فایل:**\n\n"
        "1️⃣ **همان فرمتی که ارسال شده**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **اجبار به سند**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **آپلود به عنوان رسانه عمومی**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "👻 **حالت تغییر نام را انتخاب کنید:**\n"
        "🅰️ **تغییر نام با دستور**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **تغییر نام بدون دستور**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 به یک تصویر پاسخ دهید تا به عنوان تصویر کوچک تنظیم شود."
    THUMB_SET_SUCCESS = "✅ **تصویر کوچک با موفقیت تنظیم شد.**"
    THUMB_NOT_FOUND = "⚠️ **تصویر کوچکی یافت نشد.**"
    THUMB_CLEARED = "🗑 **تصویر کوچک با موفقیت حذف شد.**"

    HELP_STR = (
        "📖 **دستورات ربات:**\n"
        "`{{ startcmd }}` - ✅ بررسی وضعیت ربات\n"
        "`{{ renamecmd }}` - ✍️ پاسخ به فایل رسانه با `/rename نام فایل.پسوند` برای تغییر نام\n"
        "`{{ filterscmd }}` - ⚙️ مدیریت فیلترهای تغییر نام\n"
        "`{{ setthumbcmd }}` - 📷 تنظیم تصویر کوچک دائمی (پاسخ به تصویر)\n"
        "`{{ getthumbcmd }}` - 📸 دریافت تصویر کوچک فعلی\n"
        "`{{ clrthumbcmd }}` - ❌ حذف تصویر کوچک تنظیم شده\n"
        "`{{ modecmd }}` - 🔄 تغییر بین 3 حالت خروجی:\n"
        "    - 📝 همان فرمتی که ارسال شده\n"
        "    - 📂 اجبار به سند\n"
        "    - 🎥 رسانه عمومی (ویدیو/صوت قابل پخش)\n\n"
        "    🔄 تغییر بین حالت‌های تغییر نام:\n"
        "    - 🏷 تغییر نام **با دستور**\n"
        "    - ✨ تغییر نام **بدون دستور/تغییر نام خودکار**\n\n"
        "`{{ queuecmd }}` - 📊 مشاهده وضعیت صف تغییر نام ربات\n"
        "`{{ setcaptioncmd }}` - 📝 تنظیم کپشن برای فایل‌های تغییر نام یافته\n"
        "`{{ helpcmd }}` - 📖 نمایش این پیام راهنما\n"
        "`{{ pingcmd }}` - 🎈 پینگ ربات\n"
        "`{{ infocmd }}` - � اطلاعات ربات\n"
        "`{{ profilecmd }}` - ☄️ آمار استفاده شما\n"
        "`{{ statuscmd }}` - 🗿 وضعیت ربات\n"
        "`{{ statscmd }}` - 👻 آمار جهانی ربات\n"
        "`{{ broadcastcmd }}` - ☄️ ارسال پیام همگانی\n"
        "`{{ leaderboardcmd }}` - 👻 جدول رده‌بندی کاربران\n"
        "`{{ setlanguagecmd }}` - 🌐 تغییر زبان ربات"
    )

    CURRENT_LOCALE = "🌐 **زبان فعلی شما:** {{ user_locale }}"


