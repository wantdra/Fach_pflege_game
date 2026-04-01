import base64, os, json, re

MUSIC_DIR = "music"
INDEX_FILE = "index.html"

# music/ klasöründeki tüm ses dosyalarını oku
songs = []
if not os.path.exists(MUSIC_DIR):
    print(f"HATA: '{MUSIC_DIR}' klasörü bulunamadı!")
    print(f"Lütfen bu scriptin yanına 'music' klasörü oluştur ve MP3'leri oraya koy.")
    input("Çıkmak için Enter'a bas...")
    exit()

for f in sorted(os.listdir(MUSIC_DIR)):
    if f.lower().endswith(('.mp3', '.wav', '.ogg', '.m4a')):
        path = os.path.join(MUSIC_DIR, f)
        size_mb = os.path.getsize(path) / (1024 * 1024)
        print(f"  Yükleniyor: {f} ({size_mb:.1f} MB)...")
        with open(path, 'rb') as file:
            b64 = base64.b64encode(file.read()).decode()
            ext = f.rsplit('.', 1)[1].lower()
            mime = {'mp3': 'audio/mpeg', 'wav': 'audio/wav', 'ogg': 'audio/ogg', 'm4a': 'audio/mp4'}.get(ext, 'audio/mpeg')
            songs.append({'name': f, 'dataUrl': f'data:{mime};base64,{b64}'})

if len(songs) == 0:
    print(f"HATA: 'music/' klasöründe hiç ses dosyası bulunamadı!")
    input("Çıkmak için Enter'a bas...")
    exit()

print(f"\n{len(songs)} şarkı bulundu. index.html güncelleniyor...")

# index.html'i oku
with open(INDEX_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# Eski şarkı bloğunu kaldır (varsa)
html = re.sub(r'// EMBEDDED_SONGS_START.*?// EMBEDDED_SONGS_END\n', '', html, flags=re.DOTALL)

# Yeni şarkı bloğunu ekle — DATA LAYER'dan önce
songs_js = f"""// EMBEDDED_SONGS_START
window.PENGUQUIZ_SONGS = {json.dumps(songs, ensure_ascii=False)};
// EMBEDDED_SONGS_END
"""

html = html.replace('// ============================================================\n// DATA LAYER',
                     songs_js + '// ============================================================\n// DATA LAYER')

with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

size_kb = os.path.getsize(INDEX_FILE) / 1024
print(f"✅ Tamamlandı! index.html güncellendi ({size_kb:.0f} KB)")
print(f"   {len(songs)} şarkı gömüldü.")
input("\nÇıkmak için Enter'a bas...")
