from langchain_ollama import OllamaLLM

class CoderAgent:
    def __init__(self):
        self.model = OllamaLLM(model="llama3", temperature=0)
        self.name = "Coder"

    def run(self, research_report):
        prompt = f"""
        GÖREV: Aşağıdaki teknik araştırma raporunu al ve bu yapıyı karşılayan profesyonel bir Python SQLAlchemy model kodu yaz.
        RAPOR: "{research_report}"
        
        SADECE Python kodunu ve kısa açıklamaları ver. Gereksiz metin ekleme.
        """
        print(f"\n[{self.name}] Kod mimarisi oluşturuluyor...")
        return self.model.invoke(prompt)
