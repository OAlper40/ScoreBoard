import tkinter as tk
from tkinter import colorchooser

skor_a = 0
skor_b = 0
takim_a = "Takım 1"
takim_b = "Takım 2"

renk_a = "#b22222"
renk_b = "#0055ff"

def buton_stil_ayarla(button, bg, fg="white", hover_bg=None):
    if hover_bg is None:
        hover_bg = bg
    button.config(
        bg=bg,
        fg=fg,
        activebackground=hover_bg,
        relief="flat",
        bd=0,
        padx=10,
        pady=5,
        font=("Arial", 12, "bold"),
        cursor="hand2"
    )
    button.bind("<Enter>", lambda e: button.config(bg=hover_bg))
    button.bind("<Leave>", lambda e: button.config(bg=bg))

def guncelle_skor(animasyonlu=False):
    label_a.config(text=takim_a, bg=renk_a)
    label_b.config(text=takim_b, bg=renk_b)
    skor_label.config(text=f"{skor_a} - {skor_b}")
    if animasyonlu:
        skor_animasyon()
    toplam_genislik = label_a.winfo_reqwidth() + skor_label.winfo_reqwidth() + label_b.winfo_reqwidth() + 60
    skor_pencere.geometry(f"{toplam_genislik}x90+400+100")

def takimlari_guncelle():
    global takim_a, takim_b
    a = entry_a.get().strip()
    b = entry_b.get().strip()
    if a: takim_a = a.upper()
    if b: takim_b = b.upper()
    guncelle_skor()

def skor_guncelle_a(event=None):
    global skor_a
    try: skor_a = max(0, int(skor_entry_a.get()))
    except: skor_a = 0
    skor_entry_a.delete(0, tk.END)
    skor_entry_a.insert(0, str(skor_a))
    guncelle_skor()

def skor_guncelle_b(event=None):
    global skor_b
    try: skor_b = max(0, int(skor_entry_b.get()))
    except: skor_b = 0
    skor_entry_b.delete(0, tk.END)
    skor_entry_b.insert(0, str(skor_b))
    guncelle_skor()

def artir_a():
    global skor_a
    skor_a += 1
    skor_entry_a.delete(0, tk.END)
    skor_entry_a.insert(0, str(skor_a))
    guncelle_skor(animasyonlu=True)

def artir_b():
    global skor_b
    skor_b += 1
    skor_entry_b.delete(0, tk.END)
    skor_entry_b.insert(0, str(skor_b))
    guncelle_skor(animasyonlu=True)

def renk_sec_a():
    global renk_a
    renk = colorchooser.askcolor(title="Takım A Rengi Seç")[1]
    if renk:
        renk_a = renk
        guncelle_skor()

def renk_sec_b():
    global renk_b
    renk = colorchooser.askcolor(title="Takım B Rengi Seç")[1]
    if renk:
        renk_b = renk
        guncelle_skor()

def sifirla():
    global skor_a, skor_b
    skor_a = skor_b = 0
    skor_entry_a.delete(0, tk.END)
    skor_entry_a.insert(0, "0")
    skor_entry_b.delete(0, tk.END)
    skor_entry_b.insert(0, "0")
    guncelle_skor()

def kapat():
    skor_pencere.destroy()
    kontrol.destroy()

def skor_animasyon():
    skor_label.config(bg="#ffff00", fg="black")  # Sarı yap
    def geri_don(step=0):
        if step > 10:
            skor_label.config(bg="#222222", fg="white")
            return
        renk_deger = 255 - int((step / 10) * 200)
        renk = f"#{renk_deger:02x}{renk_deger:02x}00"
        skor_label.config(bg=renk)
        skor_label.after(50, lambda: geri_don(step + 1))
    skor_label.after(300, lambda: geri_don())

def surukle_baslat(event):
    skor_pencere.x = event.x
    skor_pencere.y = event.y

def surukle(event):
    x = skor_pencere.winfo_pointerx() - skor_pencere.x
    y = skor_pencere.winfo_pointery() - skor_pencere.y
    skor_pencere.geometry(f"+{x}+{y}")

# Skor penceresi (normal pencere, borderlı)
skor_pencere = tk.Tk()
skor_pencere.title("ScoreBoard")
skor_pencere.geometry("500x90+400+100")
skor_pencere.attributes("-topmost", True)
# transparan özellik kaldırıldı, border kaldırılmadı

frame = tk.Frame(skor_pencere, bg="#222222", bd=3, relief="raised")
frame.pack(expand=True, fill="both", padx=5, pady=5)

label_a = tk.Label(frame, text=takim_a, font=("Arial", 20, "bold"), fg="white", bg=renk_a, padx=15, pady=10, width=15)
label_a.pack(side="left", padx=(10,5))

skor_label = tk.Label(frame, text="0 - 0", font=("Arial", 20, "bold"), fg="white", bg="#222222", padx=15)
skor_label.pack(side="left", padx=5)

label_b = tk.Label(frame, text=takim_b, font=("Arial", 20, "bold"), fg="white", bg=renk_b, padx=15, pady=10, width=15)
label_b.pack(side="left", padx=(5,10))

# Sürükleme için event bağlama
frame.bind("<Button-1>", surukle_baslat)
frame.bind("<B1-Motion>", surukle)

# Kontrol Paneli
kontrol = tk.Toplevel()
kontrol.title("Kontrol Paneli")
kontrol.geometry("400x480")

tk.Label(kontrol, text="Takım A:", font=("Arial", 12, "bold")).pack()
entry_a = tk.Entry(kontrol, font=("Arial", 12))
entry_a.pack()

tk.Label(kontrol, text="Takım B:", font=("Arial", 12, "bold")).pack()
entry_b = tk.Entry(kontrol, font=("Arial", 12))
entry_b.pack()

btn_guncelle = tk.Button(kontrol, text="Takımları Güncelle", command=takimlari_guncelle)
btn_guncelle.pack(pady=5, fill="x")
buton_stil_ayarla(btn_guncelle, "#0055ff", hover_bg="#003bb5")

skor_frame = tk.Frame(kontrol)
skor_frame.pack(pady=10)

frame_a = tk.Frame(skor_frame)
frame_a.pack(side="left", padx=10)
tk.Label(frame_a, text="A Skor:", font=("Arial", 12, "bold")).pack()
skor_entry_a = tk.Entry(frame_a, font=("Arial", 14), width=5)
skor_entry_a.pack()
skor_entry_a.insert(0, "0")
skor_entry_a.bind("<Return>", skor_guncelle_a)
btn_artir_a = tk.Button(frame_a, text="+1", command=artir_a)
btn_artir_a.pack(pady=2)
buton_stil_ayarla(btn_artir_a, "#44aa44", hover_bg="#2a882a")

frame_b = tk.Frame(skor_frame)
frame_b.pack(side="left", padx=10)
tk.Label(frame_b, text="B Skor:", font=("Arial", 12, "bold")).pack()
skor_entry_b = tk.Entry(frame_b, font=("Arial", 14), width=5)
skor_entry_b.pack()
skor_entry_b.insert(0, "0")
skor_entry_b.bind("<Return>", skor_guncelle_b)
btn_artir_b = tk.Button(frame_b, text="+1", command=artir_b)
btn_artir_b.pack(pady=2)
buton_stil_ayarla(btn_artir_b, "#44aa44", hover_bg="#2a882a")

btn_renk_a = tk.Button(kontrol, text="Takım A Rengi", command=renk_sec_a)
btn_renk_a.pack(fill="x")
buton_stil_ayarla(btn_renk_a, "#b22222", hover_bg="#7a1212")

btn_renk_b = tk.Button(kontrol, text="Takım B Rengi", command=renk_sec_b)
btn_renk_b.pack(fill="x")
buton_stil_ayarla(btn_renk_b, "#0055ff", hover_bg="#003bb5")

btn_sifirla = tk.Button(kontrol, text="Sıfırla", command=sifirla)
btn_sifirla.pack(fill="x")
buton_stil_ayarla(btn_sifirla, "#ffaa00", fg="black", hover_bg="#cc8800")

btn_kapat = tk.Button(kontrol, text="Kapat", command=kapat)
btn_kapat.pack(fill="x")
buton_stil_ayarla(btn_kapat, "#ff3333", hover_bg="#b52222")

guncelle_skor()
skor_pencere.mainloop()
