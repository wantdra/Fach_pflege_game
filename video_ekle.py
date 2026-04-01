import os, re

VIDEO_DIR = "video"
INDEX_FILE = "index.html"

# video/ klasöründeki ilk video dosyasını bul
if not os.path.exists(VIDEO_DIR):
    print(f"HATA: '{VIDEO_DIR}' klasörü bulunamadı!")
    print(f"Lütfen bu scriptin yanına 'video' klasörü oluştur ve videoyu oraya koy.")
    input("Çıkmak için Enter'a bas...")
    exit()

video_file = None
for f in sorted(os.listdir(VIDEO_DIR)):
    if f.lower().endswith(('.mp4', '.webm', '.ogg', '.mov')):
        video_file = f
        break

if not video_file:
    print(f"HATA: 'video/' klasöründe hiç video dosyası bulunamadı!")
    print(f"Desteklenen formatlar: mp4, webm, ogg, mov")
    input("Çıkmak için Enter'a bas...")
    exit()

path = os.path.join(VIDEO_DIR, video_file)
size_mb = os.path.getsize(path) / (1024 * 1024)
print(f"  Bulundu: {video_file} ({size_mb:.1f} MB)")
print(f"  (Video embed edilmez — klasörden direkt oynatılır, index.html küçük kalır)")

print(f"\nindex.html güncelleniyor...")

with open(INDEX_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# Eski video bloğunu kaldır
html = re.sub(r'// EMBEDDED_VIDEO_START.*?// EMBEDDED_VIDEO_END\n', '', html, flags=re.DOTALL)

# Sadece dosya adını kaydet
video_js = f"""// EMBEDDED_VIDEO_START
window.PENGUQUIZ_VIDEO_FILE = "{video_file}";
// EMBEDDED_VIDEO_END
"""

html = html.replace('// ============================================================\n// DATA LAYER',
                     video_js + '// ============================================================\n// DATA LAYER')

with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

size_kb = os.path.getsize(INDEX_FILE) / 1024
print(f"✅ Tamamlandı! index.html güncellendi ({size_kb:.0f} KB)")
print(f"   Video: video/{video_file} — index.html ile aynı klasörde olduğu sürece çalışır.")
print(f"\nÖNEMLİ: index.html'i taşırsan 'video/' klasörünü de yanına taşı!")
input("\nÇıkmak için Enter'a bas...")
