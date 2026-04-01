import base64, os, json, re

FINALE_DIR = "finale"
INDEX_FILE = "index.html"

if not os.path.exists(FINALE_DIR):
    print(f"HATA: '{FINALE_DIR}' klasörü bulunamadı!")
    print(f"Lütfen bu scriptin yanına 'finale' klasörü oluştur ve şarkıyı oraya koy.")
    input("Çıkmak için Enter'a bas...")
    exit()

song_file = None
for f in sorted(os.listdir(FINALE_DIR)):
    if f.lower().endswith(('.mp3', '.wav', '.ogg', '.m4a')):
        song_file = f
        break

if not song_file:
    print(f"HATA: 'finale/' klasöründe ses dosyası bulunamadı!")
    print(f"Desteklenen formatlar: mp3, wav, ogg, m4a")
    input("Çıkmak için Enter'a bas...")
    exit()

path = os.path.join(FINALE_DIR, song_file)
size_mb = os.path.getsize(path) / (1024 * 1024)
print(f"  Yükleniyor: {song_file} ({size_mb:.1f} MB)...")

with open(path, 'rb') as file:
    b64 = base64.b64encode(file.read()).decode()
    ext = song_file.rsplit('.', 1)[1].lower()
    mime = {'mp3': 'audio/mpeg', 'wav': 'audio/wav', 'ogg': 'audio/ogg', 'm4a': 'audio/mp4'}.get(ext, 'audio/mpeg')
    song_data = {'name': song_file, 'dataUrl': f'data:{mime};base64,{b64}'}

print(f"\nindex.html güncelleniyor...")

with open(INDEX_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# Eski finale şarkı bloğunu kaldır
html = re.sub(r'// EMBEDDED_FINALE_SONG_START.*?// EMBEDDED_FINALE_SONG_END\n', '', html, flags=re.DOTALL)

# Yeni bloğu ekle
finale_js = f"""// EMBEDDED_FINALE_SONG_START
window.PENGUQUIZ_FINALE_SONG = {json.dumps(song_data, ensure_ascii=False)};
// EMBEDDED_FINALE_SONG_END
"""

html = html.replace('// ============================================================\n// DATA LAYER',
                     finale_js + '// ============================================================\n// DATA LAYER')

with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

size_kb = os.path.getsize(INDEX_FILE) / 1024
print(f"✅ Tamamlandı! index.html güncellendi ({size_kb:.0f} KB)")
print(f"   Finale şarkısı gömüldü: {song_file} ({size_mb:.1f} MB)")
input("\nÇıkmak için Enter'a bas...")
