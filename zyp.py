import asyncio
import aiohttp
import time
class Renkler:
    ZYPKIRMIZI = '\033[91m'
    ZYPYESIL = '\033[92m'
    ZYPSARI = '\033[93m'
    ZYPMAVI = '\033[94m'
    ZYPMOR = '\033[95m'
    ZYPCYAN = '\033[96m'
    ZYPBEYAZ = '\033[97m'
    ZYPKALIN = '\033[1m'
    ZYPALTCIZGI = '\033[4m'
    ZYPSIFIRLA = '\033[0m'

MESAJ_GECIKME = 0.6  # mesaj silme işlemlerinin arasında bekleme süresi

async def mesajlari_sil(token, hedef_id):
    """
    Belirli bir kullanıcı ile olan DM'deki tüm mesajlarınızı siler
    
    Zypheriss tarafından yapılmıştır satılması yasaktır  discord : _zypheris
    """
    headers = {
        'Authorization': token,
        'User-Agent': 'Mozilla/5.0'
    }
    
    baslangic_zamani = time.time()
    silinen_mesaj = 0
    
    async with aiohttp.ClientSession(headers=headers) as oturum:
        try:
            print(f"\n{Renkler.ZYPCYAN}🔍 Token doğrulanıyor...{Renkler.ZYPSIFIRLA}")
            async with oturum.get('https://discord.com/api/v9/users/@me') as yanit:
                if yanit.status != 200:
                    print(f"\n{Renkler.ZYPKIRMIZI}{Renkler.ZYPKALIN}❌ Geçersiz token! Lütfen geçerli bir token girin.{Renkler.ZYPSIFIRLA}")
                    return
                    
                kullanici_bilgisi = await yanit.json()
                kullanici_id = kullanici_bilgisi['id']
                print(f"\n{Renkler.ZYPYESIL}⚡ {Renkler.ZYPKALIN}{kullanici_bilgisi['username']}{Renkler.ZYPSIFIRLA}{Renkler.ZYPYESIL} ile giriş yapıldı{Renkler.ZYPSIFIRLA}")
            
            print(f"\n{Renkler.ZYPMAVI}🔄 DM kanalı oluşturuluyor...{Renkler.ZYPSIFIRLA}")
            async with oturum.post('https://discord.com/api/v9/users/@me/channels', 
                                 json={'recipient_id': hedef_id}) as yanit:
                if yanit.status != 200:
                    print(f"\n{Renkler.ZYPKIRMIZI}❌ Kullanıcı ID'si bulunamadı veya DM kanalı oluşturulamadı: {yanit.status}{Renkler.ZYPSIFIRLA}")
                    return
                    
                kanal_bilgisi = await yanit.json()
                kanal_id = kanal_bilgisi['id']
            
            print(f"\n{Renkler.ZYPCYAN}🔍 {Renkler.ZYPKALIN}{hedef_id}{Renkler.ZYPSIFIRLA}{Renkler.ZYPCYAN} ID'li kullanıcı ile DM'ler taranıyor...{Renkler.ZYPSIFIRLA}")
            daha_fazla_mesaj = True
            son_id = None
            
            while daha_fazla_mesaj:
                url = f'https://discord.com/api/v9/channels/{kanal_id}/messages?limit=100'
                if son_id:
                    url += f'&before={son_id}'
                    
                async with oturum.get(url) as yanit:
                    if yanit.status != 200:
                        print(f"\n{Renkler.ZYPSARI}⚠️ Mesajlar alınamadı: {yanit.status}{Renkler.ZYPSIFIRLA}")
                        break
                        
                    mesajlar = await yanit.json()
                    
                if not mesajlar:
                    daha_fazla_mesaj = False
                    break 
                son_id = mesajlar[-1]['id']
                benim_mesajlarim = [msg for msg in mesajlar if msg['author']['id'] == kullanici_id]
                
                if not benim_mesajlarim:
                    continue
                
                print(f"\n{Renkler.ZYPMAVI}⏳ Mesajlar siliniyor...{Renkler.ZYPSIFIRLA}")
                
                for mesaj in benim_mesajlarim:
                    try:
                        async with oturum.delete(f'https://discord.com/api/v9/channels/{kanal_id}/messages/{mesaj["id"]}') as yanit:
                            if yanit.status == 204:
                                silinen_mesaj += 1
                                print(f"{Renkler.ZYPYESIL}✅ Silinen mesaj: {silinen_mesaj}{Renkler.ZYPSIFIRLA}", end='\r')
                            elif yanit.status == 429: 
                                yeniden_deneme = await yanit.json()
                                bekleme_suresi = yeniden_deneme.get('retry_after', 5)
                                print(f"\n{Renkler.ZYPSARI}⏱️ Hız sınırı aşıldı. {Renkler.ZYPKALIN}{bekleme_suresi}{Renkler.ZYPSIFIRLA}{Renkler.ZYPSARI} saniye bekleniyor...{Renkler.ZYPSIFIRLA}")
                                await asyncio.sleep(bekleme_suresi)
                                async with oturum.delete(f'https://discord.com/api/v9/channels/{kanal_id}/messages/{mesaj["id"]}') as tekrar_yanit:
                                    if tekrar_yanit.status == 204:
                                        silinen_mesaj += 1
                                        print(f"{Renkler.ZYPYESIL}✅ Silinen mesaj: {silinen_mesaj}{Renkler.ZYPSIFIRLA}", end='\r')
                            else:
                                print(f"\n{Renkler.ZYPSARI}⚠️ Mesaj silinemedi: {yanit.status}{Renkler.ZYPSIFIRLA}")
                                
                            await asyncio.sleep(MESAJ_GECIKME)
                    except Exception as hata:
                        print(f"\n{Renkler.ZYPKIRMIZI}⚠️ Hata: {str(hata)[:100]}...{Renkler.ZYPSIFIRLA}")
                        await asyncio.sleep(2)
            
            toplam_sure = time.time() - baslangic_zamani
            print(f"\n\n{Renkler.ZYPYESIL}{Renkler.ZYPKALIN}🎯 İşlem tamamlandı!{Renkler.ZYPSIFIRLA}")
            print(f"{Renkler.ZYPCYAN}• Toplam silinen mesaj: {Renkler.ZYPKALIN}{silinen_mesaj}{Renkler.ZYPSIFIRLA}")
            print(f"{Renkler.ZYPCYAN}• Toplam süre: {Renkler.ZYPKALIN}{toplam_sure:.1f}{Renkler.ZYPSIFIRLA}{Renkler.ZYPCYAN} saniye{Renkler.ZYPSIFIRLA}")
            if silinen_mesaj > 0:
                print(f"{Renkler.ZYPCYAN}• Ortalama hız: {Renkler.ZYPKALIN}{toplam_sure/silinen_mesaj:.1f}{Renkler.ZYPSIFIRLA}{Renkler.ZYPCYAN} saniye/mesaj{Renkler.ZYPSIFIRLA}")
            
        except Exception as hata:
            print(f"\n{Renkler.ZYPKIRMIZI}{Renkler.ZYPKALIN}❌ Kritik hata: {str(hata)[:200]}...{Renkler.ZYPSIFIRLA}")

async def main():
    banner = f"""
    {Renkler.ZYPCYAN}{Renkler.ZYPKALIN}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃                                            ┃
    ┃  {Renkler.ZYPMOR}🚀 DISCORD DM TEMİZLEYİCİ v1.1 {Renkler.ZYPCYAN}           ┃
    ┃                                            ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{Renkler.ZYPSIFIRLA}
    """
    print(banner)
    
    token = input(f"{Renkler.ZYPMAVI}Discord tokeninizi girin: {Renkler.ZYPSIFIRLA}").strip()
    hedef_id = input(f"{Renkler.ZYPMAVI}Hedef kullanıcı ID'sini girin: {Renkler.ZYPSIFIRLA}").strip()
    
    if not token or not hedef_id:
        print(f"{Renkler.ZYPKIRMIZI}Token ve kullanıcı ID'si gereklidir!{Renkler.ZYPSIFIRLA}")
        return
    
    print(f"\n{Renkler.ZYPYESIL}🔑 Token alındı. İşlem başlıyor...{Renkler.ZYPSIFIRLA}\n")
    
    await mesajlari_sil(token, hedef_id)
    print(f"\n{Renkler.ZYPYESIL}{Renkler.ZYPKALIN}🏁 İşlem tamamlandı!{Renkler.ZYPSIFIRLA}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n\n{Renkler.ZYPSARI}⚠️ İşlem kullanıcı tarafından durduruldu.{Renkler.ZYPSIFIRLA}")