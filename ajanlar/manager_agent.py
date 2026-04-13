from langchain_ollama import OllamaLLM
import json

class ManagerAgent:
    def __init__(self):
        self.model = OllamaLLM(model="llama3", temperature=0)
        self.name = "Manager"

    def run(self, user_input: str):
        prompt = f"""
        GÖREV: Kullanıcı talebini analiz et ve SADECE JSON formatında yanıt ver.
        TALEP: "{user_input}"
        FORMAT:
        {{
          "analiz": "talep özeti",
          "guven_skoru": 0.98,
          "sonraki_adim": "researcher"
        }}
        """
        response = self.model.invoke(prompt)
        try:
            return json.loads(response)
        except:
            return {"error": "JSON_DECODE_FAILURE", "guven_skoru": 0.0}
