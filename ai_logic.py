from google import genai

# BURAYA SADECE API ANAHTARINIZI YAPIŞTIRIN!
API_KEY = "AIzaSyB7kxCql4ZJWpje3LrpoPDDiP1pKiRDI4g" 

try:
    # İstemciyi başlatırken anahtarı kullanıyoruz
    client = genai.Client(api_key=API_KEY)
    MODEL = "gemini-2.5-flash"
    print("Mantık Katmanı: Gemini İstemcisi Başlatıldı.")
except Exception as e:
    client = None
    print(f"HATA: Gemini İstemcisi Başlatılamadı! {e}")

# --- TEK BİR ANA FONKSİYON KALACAK ---
def get_recommendation(besin_adi, yas_grubu, istek_tipi):
    if not client:
        return "API bağlantısı yok. Lütfen API anahtarınızı kontrol edin."

    # Yaş Grubuna Göre Ton Belirleme
    if yas_grubu == "6-12 yaş":
        ton = "eğlenceli, iki kısa paragraf halinde, biraz daha bilimsel bilgi vererek"
    else: # 13-17 yaş
        ton = "daha detaylı, besin değerlerine odaklanarak ve gençlerin ilgisini çekecek şekilde"

    # İstek Tipine Göre Prompt Oluşturma
    if istek_tipi == "Sağlıklı Alternatif":
        prompt = (
            f"Sen bir beslenme koçusun. {yas_grubu} grubundaki bir çocuk '{besin_adi}' (zararlı besin) hakkında sağlıklı bir alternatif istiyor. "
            f"Lütfen önerini {ton} hazırla. Önerin {besin_adi}'nin yerine geçebilecek, eğlenceli ve sağlıklı bir atıştırmalık olsun."
        )
    elif istek_tipi == "Sevmiyorum!":
        prompt = (
            f"Sen bir beslenme koçusun. {yas_grubu} grubundaki bir çocuk sevmediği besin olan '{besin_adi}' için alternatif istiyor. "
            f"Lütfen önerini {ton} hazırla. '{besin_adi}' ile aynı besin grubundan/benzer değerde, çocukların sevebileceği 1-2 farklı alternatif sun."
        )
    else: # Bilgi Ver
        prompt = (
            f"Sen bir beslenme uzmanısısın. {yas_grubu} grubundaki bir çocuk '{besin_adi}' hakkında bilgi istiyor. "
            f"Bilgiyi {ton} ve merak uyandırıcı bir şekilde açıkla."
        )
        
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Gemini'den yanıt alınamadı. Hata: {e}"