from dataclasses import dataclass
import random

@dataclass
class IndonesianTranslations:
    LANGUAGE_NAME = "🇮🇩 Bahasa Indonesia"
    LANGUAGE_CODE = "id"

    WRONG_VALUE_ERROR = "❌ Nilai tidak valid dimasukkan untuk variabel {{ variable_name }}."

    START_MSG = (
        "Halo! 👋\n"
        "Saya **Auto Rename Bot**, asisten Anda untuk mengganti nama file di Telegram dengan mudah.\n\n"
        "✨ **Fitur Utama:**\n"
        "- Ganti nama file dengan nama dan ekstensi kustom.\n"
        "- Cepat, aman, dan mudah digunakan.\n"
        "- Mendukung berbagai jenis file.\n\n"
        "Cukup kirimkan saya file, dan saya akan memandu Anda melalui proses penggantian nama!\n\n"
        "Mari mulai! Gunakan /mode untuk mengaktifkan penggantian nama otomatis, **Ganti nama tanpa perintah**🚀\n"
        "Kirim /help untuk info lebih lanjut.\n\n"
        "🚀 **Diberdayakan oleh** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "⚠️ Penggantian nama telah **dibatalkan**. Akan segera diperbarui."

    RENAME_NO_FILTER_MATCH = (
        "🚫 **TIDAK ADA FILTER YANG COCOK - MEMBATALKAN PENGGANTIAN NAMA**\n\n"
        "🔍 Menggunakan filter untuk mengganti nama karena tidak ada nama yang ditentukan.\n"
        "👻 Kelola filter Anda dengan /filters."
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ Menggunakan filter untuk mengganti nama karena tidak ada nama yang ditentukan.\n"
        "👻 Kelola filter Anda dengan /filters."
    )

    RENAME_NOFLTR_NONAME = (
        "✍️ Masukkan nama file baru dalam format:\n"
        "```/rename nama_file_baru.ekstensi```\n"
        "atau gunakan `/filters` untuk mengatur filter penggantian nama."
    )

    RENAME_CANCEL = "❌ Batalkan penggantian nama ini."

    RENAMING_FILE = "🔄 Mengganti nama file... Harap tunggu."

    DL_RENAMING_FILE = "📥 Mengunduh file... Harap tunggu."

    RENAME_ERRORED_REPORT = "❗ Terjadi kesalahan saat mengunduh. Laporkan masalah ini."

    RENAME_CANCEL_BY_USER = "🚫 **Dibatalkan oleh pengguna.**"

    FLTR_ADD_LEFT_STR = "➕ Menambahkan Filter: `<code>{{ text_1 }}</code>` **ke KIRI**."
    FLTR_ADD_RIGHT_STR = "➕ Menambahkan Filter: `<code>{{ text_1 }}</code>` **ke KANAN**."
    FLTR_RM_STR = "❌ Menghapus Filter: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = "🔄 Mengganti Filter: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."

    CURRENT_FLTRS = "⚙️ **Filter Anda Saat Ini:**"
    ADD_FLTR = "➕ Tambah Filter"
    RM_FLTR = "❌ Hapus Filter"

    FILTERS_INTRO = (
        "🛠 **Panduan Filter:**\n"
        "Ada 3 jenis filter:\n\n"
        "🔄 **Filter Ganti:** Ganti kata tertentu dengan kata lain.\n"
        "➕ **Filter Tambah:** Tambahkan kata di awal atau akhir.\n"
        "❌ **Filter Hapus:** Hapus kata dari nama file."
    )

    ADD_REPLACE_FLTR = "➕ Tambah Filter Ganti"
    ADD_ADDITION_FLTR = "➕ Tambah Filter Tambah"
    ADD_REMOVE_FLTR = "➕ Tambah Filter Hapus"
    BACK = "🔙 Kembali"

    REPALCE_FILTER_INIT_MSG = "✍️ Kirim format: `<code>yang_diganti | pengganti</code>` atau `/ignore` untuk kembali."

    NO_INPUT_FROM_USER = "⚠️ Tidak ada input yang diterima dari Anda."
    INPUT_IGNORE = "✅ **Diabaikan**."
    WRONG_INPUT_FORMAT = "❌ Format tidak valid. Periksa format yang diberikan."
    REPLACE_FILTER_SUCCESS = "✅ **Filter ganti ditambahkan:**\n`'{{ text_1 }}'` → `'{{ text_2 }}'`"

    ADDITION_FILTER_INIT_MSG = (
        "✍️ Masukkan teks yang akan ditambahkan dalam `<code>|</code>`\n"
        "Contoh: `<code>| teks yang ditambahkan |</code>`\n"
        "atau `/ignore` untuk kembali."
    )

    ADDITION_FILTER_SUCCESS_LEFT = "✅ Menambahkan filter: `<code>{{ text_1 }}</code>` **ke KIRI**."
    ADDITION_FILTER_SUCCESS_RIGHT = "✅ Menambahkan filter: `<code>{{ text_1 }}</code>` **ke KANAN**."

    ADDITION_LEFT = "🔄 Tambah ke Kiri"
    ADDITION_RIGHT = "🔄 Tambah ke Kanan"

    ADDITION_POSITION_PROMPT = "📍 **Di mana Anda ingin menambahkan teks?**"

    REMOVE_FILTER_INIT_MSG = "✍️ Masukkan teks yang ingin dihapus atau `/ignore` untuk kembali."

    REMOVE_FILTER_SUCCESS = "✅ **Filter hapus ditambahkan:** `<code>{{ text_1 }}</code>` akan dihapus."

    RENAME_THEMES_DOWNLOADING = [
        "✅ Unduhan selesai. Memulai ajaib penggantian nama...",
        "📦 File diterima! Siap memberikan nama baru...",
        "🪄 Unduhan selesai. ✨ Mari mulai ritual penggantian nama...",
        "🔧 Data diperoleh. Mesin penggantian nama menyala...",
        "💾 Disimpan dan disegel. Sekarang ganti nama dengan gaya...",
    ]

    RENAME_THEMES_UPLOADING = [
        "✅ Semua telah diganti nama dan siap! Unggahan selesai.",
        "🚀 File berhasil diganti nama dan diluncurkan.",
        "📤 Unggahan selesai. Karya Anda dengan nama baru sudah live!",
        "🌟 Penggantian nama file selesai. Terkirim ke kosmos!",
        "📁 Tugas selesai. File naik dengan nama baru.",
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 Unduhan dihentikan. Mimpi penggantian nama memudar...",
        "🚫 Anda menghentikannya. Unduhan dibatalkan.",
        "❌ Operasi dibatalkan di tengah penerbangan. Tidak ada file yang diambil.",
        "📴 Penggantian nama dibatalkan selama pengunduhan. Misi dibatalkan.",
        "👋 Pengguna memilih keluar di tengah pengunduhan. Selamat tinggal, file.",
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "🛑 Unggahan dibatalkan. File tetap lokal dan tidak dicintai.",
        "🚫 Penggantian nama dibalikkan. Unggahan dihentikan.",
        "❌ Tahap akhir terganggu. Penggantian nama ditinggalkan.",
        "📴 Unggahan diveto. File yang diganti nama tidak kemana-mana.",
        "👋 Pengguna berkata 'tidak' selama pengunggahan. File pensiun.",
    ]

    REPLY_TO_MEDIA = "📂 Balas `/rename` ke file media."

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "❗ Proses penggantian nama mengalami kesalahan."

    DOWNLOADING_THE_FILE = "📥 Mengunduh file"
    UPLOADING_THE_FILE = "📤 Mengunggah file: **{{ new_file_name }}**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Eksekusi Dimulai untuk Tugas Penggantian Nama**\n"
        "🆔 ID Tugas: `{{ uid }}`\n\n"
        "👤 **Username:** @{{ username }}\n"
        "📛 **Nama:** {{ name }}\n"
        "🆔 **ID Pengguna:** `<code>{{ user_id }}</code>`\n"
        "📂 **Nama File:** `<code>{{ file_name }}</code>`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "✅ **Tugas Penggantian Nama Ditambahkan**\n\n"
        "👤 **Username:** @{{ username }}\n"
        "📛 **Nama:** {{ name }}\n"
        "🆔 **ID Pengguna:** `<code>{{ user_id }}</code>`"
    )

    CAPTION_FOOT_NOTE = (
        "☄️ **CATATAN:** Anda dapat mengatur caption menggunakan `/setcaption` diikuti dengan teks yang diinginkan.\n"
        "📂 Gunakan `<code>{file_name}</code>` untuk secara dinamis menyisipkan nama file yang diganti dalam caption."
    )

    DELETE_CAPTION = "🗑 Hapus Caption"
    CLOSE = "❌ Tutup"

    CAPTION_CURRENT = "📝 **Caption Anda Saat Ini:** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **Tidak ada caption yang diatur.**"
    CAPTION_SET = "✅ **Caption diperbarui menjadi:** {{ caption }}"
    CAPTION_DELETED = "🗑 **Caption berhasil dihapus.**"

    RENAME_ADDED_TO_QUEUE = (
        "📥 **Tugas Penggantian Nama Ditambahkan ke Antrian**\n"
        "🆔 **DC ID:** {{ dc_id }}\n"
        "👻 **Media ID:** {{ media_id }}"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **Status Antrian Penggantian Nama:**\n"
        "☄️ **Total Tugas dalam Antrian:** {{ total_tasks }}\n"
        "⚡ **Kapasitas Antrian:** {{ queue_capacity }}\n"
        "⏳ **Sedang Diproses:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **Tugas Anda Sedang Dieksekusi**\n"
        "🆔 **ID Tugas:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Posisi Tugas Anda dalam Antrian:** {{ task_number }}\n"
        "🆔 **ID Tugas:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👻 **Anda telah dikeluarkan dari obrolan. Anda tidak dapat menggunakan bot ini.**"
    USER_NOT_PARTICIPANT = "👻 **Bergabunglah dengan obrolan yang diperlukan untuk menggunakan bot ini.**"
    JOIN_CHANNEL = "🔗 Gabung Channel Update"

    MODE_INITIAL_MSG = (
        "📂 **Mode Output File:**\n\n"
        "1️⃣ **Format yang sama seperti dikirim.**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Paksa sebagai Dokumen.**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **Unggah sebagai Media Umum.**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "👻 **Pilih mode penggantian nama:**\n"
        "🅰️ **Ganti nama dengan perintah.**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Ganti nama tanpa perintah.**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 Balas ke gambar untuk mengaturnya sebagai thumbnail."
    THUMB_SET_SUCCESS = "✅ **Thumbnail berhasil diatur.**"
    THUMB_NOT_FOUND = "⚠️ **Thumbnail Tidak Ditemukan.**"
    THUMB_CLEARED = "🗑 **Thumbnail berhasil dihapus.**"

    HELP_STR = (
        "📖 **Perintah Bot:**\n"
        "`{{ startcmd }}` - ✅ Periksa apakah bot sedang berjalan.\n"
        "`{{ renamecmd }}` - ✍️ Balas ke file media dengan `/rename namafile.ekstensi` untuk mengganti namanya.\n"
        "`{{ filterscmd }}` - ⚙️ Kelola filter penggantian nama Anda.\n"
        "`{{ setthumbcmd }}` - 📷 Atur thumbnail permanen (balas ke gambar).\n"
        "`{{ getthumbcmd }}` - 📸 Dapatkan thumbnail yang saat ini diatur.\n"
        "`{{ clrthumbcmd }}` - ❌ Hapus thumbnail yang diatur.\n"
        "`{{ modecmd }}` - 🔄 Beralih antara 3 mode output:\n"
        "    - 📝 Format yang sama seperti dikirim.\n"
        "    - 📂 Paksa sebagai Dokumen.\n"
        "    - 🎥 Media Umum (video/audio yang dapat di-stream).\n\n"
        "    🔄 Beralih antara mode penggantian nama:\n"
        "    - 🏷 Ganti nama **dengan perintah**.\n"
        "    - ✨ Ganti nama **tanpa perintah/ganti nama otomatis**.\n\n"
        "`{{ queuecmd }}` - 📊 Lihat status antrian penggantian nama bot.\n"
        "`{{ setcaptioncmd }}` - 📝 Atur caption untuk file yang diganti nama.\n"
        "`{{ helpcmd }}` - 📖 Tampilkan pesan bantuan ini.\n"
        "`{{ pingcmd }}` - 🎈 Ping Bot.\n"
        "`{{ infocmd }}` - 🧑‍💻 Lihat info bot.\n"
        "`{{ profilecmd }}` - ☄️ Statistik penggunaan Anda.\n"
        "`{{ statuscmd }}` - 🗿 Status Bot.\n"
        "`{{ statscmd }}` - 👻 Statistik global bot.\n"
        "`{{ broadcastcmd }}` - ☄️ Buat siaran.\n"
        "`{{ leaderboardcmd }}` - 👻 Papan peringkat pengguna.\n"
        "`{{ setlanguagecmd }}` - 🌐 Ubah bahasa bot."
    )

    CURRENT_LOCALE = "🌐 **Bahasa Anda saat ini:** {{ user_locale }}"


