import sys
import os
sys.path.append(os.getcwd())

from agents.manager_agent import ManagerAgent
from agents.researcher_agent import ResearcherAgent
from agents.coder_agent import CoderAgent
from agents.file_manager_agent import FileManagerAgent

def main():
    print("\n" + "="*40)
    print("--- OTONOM AJAN SISTEMI V4 (FULL) ---")
    print("="*40)
    
    try:
        manager = ManagerAgent()
        researcher = ResearcherAgent()
        coder = CoderAgent()
        file_mgr = FileManagerAgent()
        print("[Sistem] Tüm birimler (Manager, Researcher, Coder, FileMgr) aktif.")
    except Exception as e:
        print(f"Sistem hatasi: {e}")
        return

    while True:
        user_input = input("\nYeni Proje/Talep (Cikis icin 'exit'): ")
        if user_input.lower() == 'exit': break
            
        print(f"\n[Sistem] Süreç başlatıldı...")
        analysis = manager.run(user_input)
        
        # 1. ADIM: ARAŞTIRMA
        rapor = researcher.run(user_input)
        print(f"\n>>> Teknik Araştırma Tamamlandı.")
        
        # 2. ADIM: KODLAMA
        print(f"[Sistem] Kodlar yazılıyor...")
        kod = coder.run(rapor)
        
        # 3. ADIM: DOSYALAMA
        print(f"[Sistem] Dosyalar oluşturuluyor...")
        kayit_mesaji = file_mgr.run(kod, "veritabani_modeli.py")
        
        print("\n" + "*"*30)
        print(kayit_mesaji)
        print("*"*30)
        print("\nİşlem başarıyla bitti. 'output_codes' klasörünü kontrol edin.")

if __name__ == "__main__":
    main()
