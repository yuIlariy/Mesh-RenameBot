from dataclasses import dataclass
import random

@dataclass
class IndonesianTranslations:
    LANGUAGE_NAME = "🇮🇩 Indonesia"
    LANGUAGE_CODE = "id"

    WRONG_VALUE_ERROR = "❌ Ups! Nilai tidak valid untuk {{ variable_name }}. Coba lagi! 🤷‍♀️"

    START_MSG = (
    "✨ **Hai penyihir file!** ✨\n\n"
    "Saya adalah **Auto Rename Bot** 🪄, asisten ajaibmu untuk mengganti nama file!\n\n"
    "🔥 **Mengapa kamu akan menyukai saya:**\n"
    "- Ganti nama file dengan ✨ kilau dan presisi\n"
    "- Super cepat ⚡ dan aman 🔒\n"
    "- Mendukung SEMUA jenis file! 📂🎵🎬\n\n"
    "Cukup kirimkan saya file dan mari kita buat keajaiban! 🎩\n\n"
    "🚀 **Tip Pro:** Gunakan /mode untuk mode ninja ganti nama otomatis (harus tambahkan /filters)!\n"
    "Butuh bantuan? /help siap membantu!\n\n"
    "🛸 **Didukung oleh** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "❗ Penggantian nama dibatalkan! Puf! ✨ (Pembaruan segera datang!)"

    RENAME_NO_FILTER_MATCH = (
        "🔮 **Ups! Tidak ada filter yang cocok!**\n\n"
        "Mencoba menggunakan filter tetapi tidak menemukan apa pun 🎩🐇\n"
        "Kelola filter Anda dengan /filters ✏️"
    )

    RENAME_FILTER_MATCH_USED = (
        "🎯 **Kekuatan filter diaktifkan!**\n"
        "Menggunakan filter karena Anda tidak menentukan nama\n"
        "Sesuaikan dengan /filters ⚙️"
    )

    RENAME_NOFLTR_NONAME = (
        "📝 **TIDAK ada filter ditemukan!**\n\n"
        "Silakan tambahkan /filters 🎨 untuk filter ganti nama otomatis."
    )

    RENAME_CANCEL = "❌ Tidak, batalkan saja ✌️"

    RENAMING_FILE = "🌀 **Transformasi file sedang berlangsung...**"

    DL_RENAMING_FILE = "📥 **Mengunduh harta digital Anda...**"

    RENAME_ERRORED_REPORT = "💥 **Aduh! Sesuatu rusak!** Tolong laporkan ini 🚨"

    RENAME_CANCEL_BY_USER = "🙅‍♂️ **Anda mengayunkan tongkat pembatalan!** ✨"

    FLTR_ADD_LEFT_STR = "➕ Filter ditambahkan: `<code>{{ text_1 }}</code>` **ke KIRI**."
    FLTR_ADD_RIGHT_STR = (
        "➕ Filter ditambahkan: `<code>{{ text_1 }}</code>` **ke KANAN**."
    )
    FLTR_RM_STR = "❌ Filter dihapus: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = (
        "🔄 Filter diganti: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."
    )

    CURRENT_FLTRS = "🎛️ **Dasbor Filter Anda:**"
    ADD_FLTR = "➕ Tambah Filter"
    RM_FLTR = "❌ Hapus Filter"

    FILTERS_INTRO = (
        "🛠 **Panduan Filter:**\n"
        "Ada 3 jenis filter:\n\n"
        "🔄 **Filter Pengganti:** Ganti kata tertentu dengan kata lain.\n"
        "➕ **Filter Penambahan:** Tambahkan kata di awal atau akhir.\n"
        "❌ **Filter Penghapusan:** Hapus kata dari nama file."
    )

    ADD_REPLACE_FLTR = "➕ Tambah Filter Pengganti"
    ADD_ADDITION_FLTR = "➕ Tambah Filter Penambahan"
    ADD_REMOVE_FLTR = "➕ Tambah Filter Penghapusan"
    BACK = "🔙 Kembali"

    REPALCE_FILTER_INIT_MSG = "✍️ Kirim format: `<code>apa_yang_diganti | pengganti</code>` atau /ignore untuk kembali."

    NO_INPUT_FROM_USER = "🤷‍♂️ **Jangkrik...** Tidak ada input yang terdeteksi!"
    INPUT_IGNORE = "👍 **Diabaikan!**"
    WRONG_INPUT_FORMAT = "🤦‍♂️ **Ups!** Format salah! Periksa format yang diberikan dan coba lagi!"
    REPLACE_FILTER_SUCCESS = (
        "✅ **Filter pengganti ditambahkan:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ Masukkan teks untuk ditambahkan di dalam `<code>|</code>`\n"
        "Contoh: `<code>| teks untuk ditambahkan |</code>`\n"
        "atau /ignore untuk kembali."
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ Filter ditambahkan: `<code>{{ text_1 }}</code>` **ke KIRI**."
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ Filter ditambahkan: `<code>{{ text_1 }}</code>` **ke KANAN**."
    )

    ADDITION_LEFT = "🔄 Penambahan ke KIRI"
    ADDITION_RIGHT = "🔄 Penambahan ke KANAN"

    ADDITION_POSITION_PROMPT = "🧙‍♂️ **Di mana Anda ingin menambahkan teks?**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ Masukkan teks yang ingin Anda hapus atau /ignore untuk kembali."
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **Filter penghapusan ditambahkan:** `<code>{{ text_1 }}</code>` akan dihapus."
    )

    RENAME_THEMES_DOWNLOADING = [
        "🎩 Unduhan selesai! Mempersiapkan keajaiban...",
        "📦 File diperoleh! Siap untuk sihir penamaan...",
        "✨ Unduhan berhasil! Mantra dimulai...",
        "⚡ Data diamankan! Mesin pengganti nama menyala...",
        "💾 File ditangkap! Siap untuk kelahiran kembali yang mulia..."
    ]

    RENAME_THEMES_UPLOADING = [
        "🚀 **Blast off!** File yang diganti nama diluncurkan!",
        "🎉 **Ta-da!** File dengan nama barumu sudah siap!",
        "📤 Unggahan selesai! Nikmati mahakaryamu!",
        "🌟 Metamorfosis file selesai!",
        "🏁 Balapan selesai! File Anda telah melewati garis finish!"
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 **Abort!** Mantra unduhan terganggu!",
        "🚧 Ups! Anda menghentikan kereta unduhan!",
        "🎭 Pertunjukan berakhir sebelum dimulai!",
        "📵 Koneksi unduhan dihentikan!",
        "👋 Anda meninggalkan unduhan! Selamat tinggal!"
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "✋ **Tunggu!** Unggahan berhenti di tengah penerbangan!",
        "🚫 Tidak ada pengiriman hari ini! Unggahan dibatalkan!",
        "🌪️ Tornado unggahan menghilang!",
        "📴 Koneksi hilang dalam kekosongan!",
        "🤷‍♂️ Anda berubah pikiran! Unggahan dibatalkan!"
    ]

    REPLY_TO_MEDIA = "📎 **Psst!** Balas `/rename` ke file!"

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "💥 **Kaboom!** Mantra penggantian nama gagal!"

    DOWNLOADING_THE_FILE = "📥 **Mengambil file Anda...**"
    UPLOADING_THE_FILE = "📤 **Meluncurkan:** `{{ new_file_name }}` 🚀"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Misi Penggantian Nama Dimulai**\n"
        "🆔 ID Misi: `{{ uid }}`\n\n"
        "👤 **Agen:** @{{ username }}\n"
        "📛 **Nama Kode:** {{ name }}\n"
        "🪪 **ID:** `{{ user_id }}`\n"
        "📜 **File:** `{{ file_name }}`\n\n"
        "`⚡ Hyperdrive diaktifkan!`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "📥 **Misi Penggantian Nama Antri**\n\n"
        "👤 **Agen:** @{{ username }}\n"
        "📛 **Nama Kode:** {{ name }}\n"
        "🪪 **ID:** `{{ user_id }}`\n\n"
        "`⏳ Menunggu penyebaran...`"
    )

    CAPTION_FOOT_NOTE = (
        "💡 **Tip Pro:** Gunakan /setcaption untuk menambah gaya!\n"
        "✨ Gunakan `/setcaption {file_name}` untuk mengisi otomatis nama file di keterangan!"
    )

    DELETE_CAPTION = "🗑️ Hapus Keterangan"
    CLOSE = "🚪 Keluar"

    CAPTION_CURRENT = "📝 **Keterangan Saat Ini:** {{ caption }}"
    CAPTION_NOT_SET = "🫗 **Keterangan kosong!** Sangat sepi..."
    CAPTION_SET = "✅ **Keterangan Baru:** {{ caption }}"
    CAPTION_DELETED = "🗑️ **Keterangan berhasil dihapus.**"

    RENAME_ADDED_TO_QUEUE = (
        "📊 **Penggantian Nama Antri**\n"
        "🆔 **ID DC:** {{ dc_id }}\n"
        "📦 **ID Media:** {{ media_id }}\n\n"
        "`⏳ Sabar, padawan muda...`"
    )

    RENAME_QUEUE_STATUS = (
        "📈 **Statistik Antrian:**\n"
        "📊 **Total Tugas:** {{ total_tasks }}\n"
        "⚡ **Kapasitas:** {{ queue_capacity }}\n"
        "⏳ **Sedang Diproses:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **File Anda sedang disihir!**\n"
        "🆔 **ID Tugas:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Posisi Anda dalam antrian:** {{ task_number }}\n"
        "🆔 **ID Tugas:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👢 **Anda telah diusir!** Tidak ada bot untuk Anda!"
    USER_NOT_PARTICIPANT = (
        "🔒 **Peringatan Klub Rahasia!**\n\n"
        "Bergabunglah dengan saluran kami untuk membuka keajaiban!\n\n"
        "`🦄 Hanya unicorn setelah titik ini`"
    )
    
    JOIN_CHANNEL = "🔗 Bergabung dengan Klub Rahasia"

    MODE_INITIAL_MSG = (
        "🎛️ **Pemilih Mode Keluaran:**\n\n"
        "1️⃣ **Pertahankan format asli**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Paksa mode dokumen**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **Mode media umum**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "✨ **Gaya Penggantian Nama:**\n"
        "🅰️ **Penggantian nama perintah**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Penggantian nama otomatis**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣ Mode OG"
    MODE_SET_1 = "2️⃣ Mode Dokumen"
    MODE_SET_2 = "3️⃣ Mode Media"
    COMMAND_MODE_SET_3 = "🅰️ Perintah"
    COMMAND_MODE_SET_4 = "🅱️ Otomatis"

    THUMB_REPLY_TO_MEDIA = "🖼️ **Balas ke gambar** untuk mengatur sebagai thumbnail"
    THUMB_SET_SUCCESS = "✅ **Thumbnail dikunci!**"
    THUMB_NOT_FOUND = "🕵️‍♂️ **Tidak ada thumbnail yang terdeteksi!**"
    THUMB_CLEARED = "🧹 **Thumbnail disapu bersih!**"

    HELP_STR = (
        "📚 **Buku Mantra Ajaib:**\n"
        "`{{ startcmd }}` - Periksa apakah saya masih hidup! 💓\n"
        "`{{ renamecmd }}` - Ganti nama file seperti bos! 🎩\n"
        "`{{ filterscmd }}` - Sesuaikan filter penggantian nama Anda! ✨\n"
        "`{{ setthumbcmd }}` - Atur thumbnail permanen! 🖼️\n"
        "`{{ getthumbcmd }}` - Lihat thumbnail saat ini! 👀\n"
        "`{{ clrthumbcmd }}` - Hapus thumbnail! 🗑️\n"
        "`{{ modecmd }}` - Ubah mode keluaran:\n"
        "   - 📝 Format asli\n"
        "   - 📂 Paksa dokumen\n"
        "   - 🎥 Mode media\n\n"
        "   Ubah gaya penggantian nama:\n"
        "   - 🏷️ Berbasis perintah\n"
        "   - 🤖 Penggantian nama otomatis (harus tambahkan /filters)\n\n"
        "`{{ queuecmd }}` - Periksa antrian penggantian nama 📊\n"
        "`{{ setcaptioncmd }}` - Atur keterangan mewah 🎨\n"
        "`{{ helpcmd }}` - Buku ajaib ini! 📖\n"
        "`{{ pingcmd }}` - Ping-pong! 🏓\n"
        "`{{ infocmd }}` - Spesifikasi bot! 🤖\n"
        "`{{ profilecmd }}` - Statistik Anda! 📈\n"
        "`{{ statuscmd }}` - Tanda vital bot! 💓\n"
        "`{{ statscmd }}` - Angka global! 🌍\n"
        "`{{ broadcastcmd }}` - Mega-pengumuman! 📢\n"
        "`{{ leaderboardcmd }}` - Pengguna teratas! 🏆\n"
        "`{{ setlanguagecmd }}` - Ubah bahasa! 🌐"
    )

    CURRENT_LOCALE = "🌍 **Bahasa Anda:** {{ user_locale }}"
