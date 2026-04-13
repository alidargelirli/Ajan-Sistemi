from langchain_ollama import OllamaLLM

class ResearcherAgent:
    def __init__(self):
        # Temperature 0.2: Teknik detaylarda tutarlılık ve hafif bir yaratıcılık için
        self.model = OllamaLLM(model="llama3", temperature=0.2)
        self.name = "Researcher"

    def run(self, task):
        prompt = f"""
        GÖREV: Aşağıdaki konu hakkında teknik bir araştırma yap ve maddeler halinde raporla.
        KONU: "{task}"
        
        RAPOR FORMATI:
        1. Temel Gereksinimler (Örn: Veritabanı tabloları, veri tipleri)
        2. Teknik Mimari Önerisi (Örn: Kullanılacak kütüphaneler, bağlantı yapıları)
        3. Kritik Uyarılar (Örn: Güvenlik, performans, ölçeklenebilirlik)
        
        Lütfen yanıtı Türkçe olarak ver.
        """
        print(f"\n[{self.name}] Detaylı araştırma başlatıldı, lütfen bekleyin...")
        response = self.model.invoke(prompt)
        return response