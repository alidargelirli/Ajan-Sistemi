import sys
import os
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Ajanları içe aktar (Klasör isminin 'ajanlar' olduğundan emin oluyoruz)
from ajanlar.manager_agent import ManagerAgent
from ajanlar.researcher_agent import ResearcherAgent
from ajanlar.coder_agent import CoderAgent
from ajanlar.file_manager_agent import FileManagerAgent

class App:
    def __init__(self):
        try:
            self.manager = ManagerAgent()
            self.researcher = ResearcherAgent()
            self.coder = CoderAgent()
            self.file_mgr = FileManagerAgent()
        except Exception as e:
            print(f"Hata: {e}")
        
        self.setup_ui()

    def setup_ui(self):
        self.root = tk.Tk()
        self.root.title("AI Ajan Üssü - Görsel Panel")
        self.root.geometry("700x600")

        tk.Label(self.root, text="OTONOM AJAN SISTEMI", font=("Helvetica", 16, "bold")).pack(pady=10)
        
        self.input_label = tk.Label(self.root, text="Proje fikrinizi yazın:")
        self.input_label.pack()
        
        self.entry = tk.Entry(self.root, width=80)
        self.entry.pack(pady=10)

        self.run_btn = tk.Button(self.root, text="SÜRECİ BAŞLAT", command=self.process, bg="#2ecc71", fg="white", font=("Arial", 10, "bold"))
        self.run_btn.pack(pady=10)

        self.log_area = scrolledtext.ScrolledText(self.root, width=80, height=20)
        self.log_area.pack(pady=10)

    def log(self, text):
        self.log_area.insert(tk.END, text + "\n")
        self.log_area.see(tk.END)
        self.root.update()

    def process(self):
        user_input = self.entry.get()
        if not user_input: return
        
        self.log(f"\n>>> YENİ GÖREV: {user_input}")
        
        try:
            self.log("[Sistem] Manager analiz ediyor...")
            self.manager.run(user_input)
            
            self.log("[Sistem] Researcher araştırmaya başladı...")
            rapor = self.researcher.run(user_input)
            
            self.log("[Sistem] Coder kodları yazıyor...")
            kod = self.coder.run(rapor)
            
            self.log("[Sistem] File Manager dosyaları kaydediyor...")
            sonuc = self.file_mgr.run(kod, "tasarim_sonucu.py")
            
            self.log(f"\n{sonuc}")
            messagebox.showinfo("Başarılı", "Proje üretildi ve 'output_codes' klasörüne kaydedildi!")
        except Exception as e:
            self.log(f"HATA OLUŞTU: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
