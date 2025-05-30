# Discord DM Temizleyici 🚀

## Açıklama
Bu araç, Discord'da belirli bir kullanıcı ile olan özel mesajlarınızı (DM) otomatik olarak temizlemenizi sağlayan güçlü bir Python scriptidir. Kullanıcı dostu arayüzü ve renkli konsol çıktıları ile kolay kullanım sağlar.

## Özellikler
- 🔒 Güvenli token doğrulama
- 🗑️ Seçilen kullanıcı ile olan tüm DM'leri temizleme
- ⚡ Hızlı ve verimli mesaj silme
- 🎨 Renkli konsol çıktıları
- ⏱️ Otomatik hız sınırı yönetimi
- 📊 Detaylı işlem istatistikleri

## Kurulum
1. Python'un en son sürümünün yüklü olduğundan emin olun
2. Gerekli kütüphaneleri yükleyin:
```bash
pip install aiohttp
```

## Kullanım
1. Scripti çalıştırın:
```bash
python zyp.py
```

2. İstenildiğinde Discord tokeninizi girin
3. Mesajlarını silmek istediğiniz kullanıcının ID'sini girin
4. Script otomatik olarak mesajları silmeye başlayacaktır

## Önemli Notlar
- ⚠️ Discord tokeninizi kimseyle paylaşmayın
- ⏳ Mesaj silme hızı Discord'un API limitlerini aşmayacak şekilde ayarlanmıştır değiştirmenizi önermem
- 🔄 Hız sınırına ulaşıldığında script otomatik olarak bekleyecektir bu süre Değişim görmektiredir
- 📝 İşlem sonunda detaylı bir rapor görüntülenecektir

## İstatistikler
Script işlem sonunda şu bilgileri gösterir:
- Toplam silinen mesaj sayısı
- İşlemin toplam süresi
- Mesaj başına ortalama silme hızı

## Hata Durumları
Script şu durumlarda hata mesajları gösterir:
- ❌ Geçersiz token
- ⚠️ Kullanıcı ID'si bulunamadığında
- ⏱️ Discord API hız sınırına ulaşıldığında
- ⚠️ Mesaj silme işlemi başarısız olduğunda

## Güvenlik
- Token güvenliği için gerekli önlemler alınmıştır
- Tüm HTTP istekleri güvenli bir şekilde yönetilir
- Hata durumları güvenli bir şekilde ele alınır

## Geliştirici
- Discord: _zypheris
- Not: Bu script Zypheriss tarafından geliştirilmiştir ve satılması yasaktır

## Lisans
Bu yazılım özel kullanım için tasarlanmıştır. Ticari kullanım ve yeniden dağıtım hakları saklıdır.
