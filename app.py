   # --- TIKLAMA MANTIĞI FONKSİYONU ---
def besin_butonuna_tikla(besin_adi):
    try: 
        besin_entry.delete(0, 'end')
        besin_entry.insert(0, besin_adi)
    except NameError:
        pass 

# --- ARAYÜZ VE MANTIK FONKSİYONU ---
def analiz_et_butonu_tiklandi():
    besin = besin_entry.get().lower() 
    istek_tipi = radio_var.get()
    yas_grubu = yas_var.get()
    
    if not besin or not istek_tipi or not yas_grubu:
        messagebox.showwarning("Eksik Giriş", "Lütfen Besin Adı, Yaş Grubu ve İstek Tipini seçin.")
        return

    sonuc_text.configure(text="🤖 Yapay zeka analiz ediyor, lütfen bekleyin...") 
    root.update()

    sonuc = generate_recommendation(besin, yas_grubu, istek_tipi)
    
    sonuc_text.configure(text=sonuc, wraplength=400, justify="left") 


# --- CUSTOMTKINTER ARAYÜZ KURULUMU (Pembe Tema) ---

ctk.set_appearance_mode("Light") 
ctk.set_default_color_theme("green") 

root = ctk.CTk() 
root.title("🍏 Sağlıklı Beslenme Arkadaşı (6-17 Yaş)")
root.configure(fg_color="#FADADD") # Açık pembe arka plan
root.geometry("900x700") 

# Ana Çerçeve (Beyaz/Açık Gri İç Kutu)
main_frame = ctk.CTkFrame(master=root, corner_radius=20, fg_color="#FFFFFF")
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Görsel Başlık
ctk.CTkLabel(master=main_frame, text="✏️", font=("Arial", 60), text_color="#FF69B4").pack(pady=10)

# Besin Adı Giriş
ctk.CTkLabel(master=main_frame, text="Öğrenmek İstediğiniz Besinin Adı:", font=("Arial", 16, "bold")).pack(pady=10)

besin_entry = ctk.CTkEntry(master=main_frame, width=300, height=30, corner_radius=10, font=("Arial", 14))
besin_entry.pack(pady=5)
besin_entry.insert(0, "Cips") 

# Yaş Grubu Seçimi
ctk.CTkLabel(master=main_frame, text="Yaş Grubu:", font=("Arial", 16, "bold")).pack(pady=10)
yas_var = ctk.StringVar(value="6-12 yaş")
yas_gruplari = ["6-12 yaş", "13-17 yaş"]

yas_frame = ctk.CTkFrame(master=main_frame, fg_color="transparent") 
yas_frame.pack()
for yas in yas_gruplari:
    ctk.CTkRadioButton(master=yas_frame, text=yas, variable=yas_var, value=yas, 
                       border_color="#FF69B4", hover_color="#FF69B4", fg_color="#FF69B4",
                       font=("Arial", 14)).pack(side="left", padx=10, pady=5)


# İstek Tipi Seçimi
ctk.CTkLabel(master=main_frame, text="Ne Öğrenmek İstersin?", font=("Arial", 16, "bold")).pack(pady=15)
radio_var = ctk.StringVar(value="Sağlıklı Alternatif") 

pembe_renk = "#FF69B4" 
ctk.CTkRadioButton(master=main_frame, text="⭐ Sağlıklı Alternatif", variable=radio_var, value="Sağlıklı Alternatif", font=("Arial", 14), 
                   border_color=pembe_renk, hover_color=pembe_renk, fg_color=pembe_renk).pack(anchor="w", padx=40, pady=5)
ctk.CTkRadioButton(master=main_frame, text="💔 Sevmiyorum! (Alternatif)", variable=radio_var, value="Sevmiyorum!", font=("Arial", 14), 
                   border_color=pembe_renk, hover_color=pembe_renk, fg_color=pembe_renk).pack(anchor="w", padx=40, pady=5)
ctk.CTkRadioButton(master=main_frame, text="📖 Bilgi Ver", variable=radio_var, value="Bilgi Ver", font=("Arial", 14), 
                   border_color=pembe_renk, hover_color=pembe_renk, fg_color=pembe_renk).pack(anchor="w", padx=40, pady=5)

# Analiz Et Butonu (Canlı Pembe Tonu)
analiz_button = ctk.CTkButton(master=main_frame, text="✨ Analiz Et", command=analiz_et_butonu_tiklandi,
                            fg_color="#FF69B4", hover_color="#E05599", 
                            font=("Arial", 16, "bold"), height=45, corner_radius=15)
analiz_button.pack(pady=30, ipadx=20, ipady=10)

# Sonuç Alanı
ctk.CTkLabel(master=main_frame, text="--- Yapay Zeka Yanıtı ---", font=("Arial", 16, "bold")).pack(pady=10)

# !!! YENİ: KAYDIRILABİLİR ÇERÇEVE OLUŞTURUYORUZ !!!
scroll_frame = ctk.CTkScrollableFrame(master=main_frame, 
                                        label_text="Gemini'den Öneri", 
                                        width=400, 
                                        height=250, 
                                        corner_radius=10)
scroll_frame.pack(pady=10, padx=20, fill="x", expand=True)

# !!! Sonuç Metnini bu yeni çerçeve içine yerleştiriyoruz !!!
sonuc_text = ctk.CTkLabel(master=scroll_frame, text="Burada önerileriniz görünecektir.", 
                        fg_color="#F8F8F8", text_color="black", 
                        corner_radius=10, padx=15, pady=15, 
                        wraplength=380,
                        justify="left",
                        font=("Arial", 14))
sonuc_text.pack(fill="x", expand=True) 

root.mainloop()