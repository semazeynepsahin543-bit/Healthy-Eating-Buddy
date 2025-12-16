# 🍎 Çocuklar İçin Beslenme Koçu (Gemini API Destekli)

Bu proje, Google Gemini API'si kullanılarak geliştirilmiş, çocuklara ve gençlere yönelik interaktif bir beslenme öneri sisteminin mantık katmanını oluşturur. Belirtilen yaş grubuna, gıda tercihlerine ve bilgi ihtiyacına göre kişiselleştirilmiş, eğitici ve eğlenceli beslenme tavsiyeleri sunar.

## ✨ Özellikler

* **Yaş Grubuna Özgü Tonlama:** 6-12 yaş grubu için **eğlenceli** ve **bilimsel** bilgiler; 13-17 yaş grubu için **detaylı** ve **besin değerlerine odaklı** içerik üretimi.
* **Üç Farklı İstek Tipi:**
    1.  **Sağlıklı Alternatif:** Zararlı olabilecek bir besin yerine geçecek, sağlıklı ve eğlenceli alternatifler sunar.
    2.  **Sevmiyorum!:** Çocuğun sevmediği bir besin yerine, aynı besin grubundan/benzer değerde farklı alternatifler önerir.
    3.  **Bilgi Ver:** Belirtilen besin hakkında yaş grubuna uygun, merak uyandırıcı ve detaylı bilgiler sağlar.
* **Harici Bağımlılık:** Google'ın güçlü **Gemini 2.5 Flash** modeli ile yüksek kalitede, bağlamsal ve tutarlı yanıtlar üretir.

## 🚀 Kurulum

Bu projeyi yerel olarak çalıştırmak için aşağıdaki adımları izleyin.

### 1. Python Bağımlılıkları

Projenin çalışması için `google-genai` kütüphanesine ihtiyacınız var.

```bash
pip install google-genai
2. API AnahtarıGemini API'sini kullanabilmek için bir API anahtarına ihtiyacınız var. Anahtarınızı almak için Google AI Studio'yu ziyaret edin.⚠️ Önemli Not: API anahtarınızı asla doğrudan herkese açık bir kod deposuna yüklemeyin! Burada gösterilen kod sadece test amaçlıdır. Gerçek uygulamalarda os.environ veya gizli anahtar yönetimi sistemlerini kullanın.3. Kodu ÇalıştırmaProjenin ana dosyasını (örneğin nutrition_coach.py adını verdiyseniz) çalıştırın.Bashpython nutrition_coach.py
💻 Kullanım (Kod Detayı)Projenin kalbi olan get_recommendation fonksiyonunu kullanarak tavsiye alabilirsiniz.Fonksiyon İmzasıPythondef get_recommendation(besin_adi, yas_grubu, istek_tipi):
    # ... (kod detayları)
ParametrelerParametreAçıklamaKabul Edilen Değerlerbesin_adiHakkında bilgi veya alternatif istenen besinin adı.(Örn: "Cips", "Brokoli", "Elma")yas_grubuHedef kitlenin yaş aralığı."6-12 yaş" veya "13-17 yaş"istek_tipiKullanıcının talebinin türü."Sağlıklı Alternatif", "Sevmiyorum!", "Bilgi Ver"Örnek KullanımÖrnek 1: Sağlıklı Alternatif (6-12 yaş)Python# Cips yerine sağlıklı alternatif (6-12 yaş, eğlenceli ton)
sonuc = get_recommendation("Cips", "6-12 yaş", "Sağlıklı Alternatif")
print(sonuc)
Örnek 2: Sevmediği Besin İçin Alternatif (13-17 yaş)Python# Brokoli sevmeyen genç için alternatif (13-17 yaş, detaylı ton)
sonuc = get_recommendation("Brokoli", "13-17 yaş", "Sevmiyorum!")
print(sonuc)
Örnek 3: Bilgi İsteme (13-17 yaş)Python# Muz hakkında bilgi (13-17 yaş, detaylı ton)
sonuc = get_recommendation("Muz", "13-17 yaş", "Bilgi Ver")
print(sonuc)
🛠️ Kod YapısıProje, temel olarak tek bir dosya ve içinde tüm mantığı barındıran tek bir fonksiyon üzerine kurulmuştur.Temel Dosya: nutrition_coach.pyBu dosya şunları içerir:API Bağlantısı: genai.Client ile Gemini API'sine bağlantı kurma ve hata yönetimi.get_recommendation Fonksiyonu:İstek parametrelerine göre ton (tone) belirleme.İstek tipine göre Prompt (model girdisi) oluşturma.client.models.generate_content() ile Gemini API'den yanıt alma.Gelen yanıtı döndürme veya API hatasını yakalama.🤝 Katkıda BulunmaProjenin daha da gelişmesine katkıda bulunmak ister misiniz? Her türlü katkı, öneri veya geri bildirim değerlidir!Projenin çatallamasını yapın (Fork).Yeni bir özellik/düzeltme için dal oluşturun (git checkout -b ozellik/muhtesem-eklenti).Değişikliklerinizi yapın ve commit edin (git commit -m 'Ozellik: Yeni sebze alternatifleri eklendi').Dalı push edin (git push origin ozellik/muhtesem-eklenti).Bir Pull Request (Çekme İsteği) oluşturun.📄 LisansBu proje MIT Lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakınız.
