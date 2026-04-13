import os

class FileManagerAgent:
    def __init__(self):
        self.name = "File Manager"
        self.output_dir = "output_codes"

    def run(self, content, filename="generated_code.py"):
        # Çıktı klasörü yoksa oluştur
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
        file_path = os.path.join(self.output_dir, filename)
        
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return f"\n[{self.name}] Başarılı! Kod şuraya kaydedildi: {file_path}"
        except Exception as e:
            return f"\n[{self.name}] Dosya yazma hatası: {e}"
