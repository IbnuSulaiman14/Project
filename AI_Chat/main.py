import google.generativeai as genai
import os
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
file_env = os.path.join(current_dir,".env")

load_dotenv(file_env)

def tanya_ai(input_user):
    try:
        API_key = os.getenv("GOOGLE_API_KEY")
        
        if not API_key:
            return "API KEY tidak ditemukan"

        genai.configure(api_key=API_key)

        instruksi_khusus = """
        Kamu adalah peramal nasib, tarot, dan zodiak.
        Karaktermu: Misterius, mistis, lucu, penuh teka-teki, dan bijaksana.
        Jika user bertanya nasib, berpura-puralah kamu sedang mengambil SATU KARTU TAROT secara acak (misal: The Fool, The Lovers, Death, dll) lalu jelaskan artinya.
        Hubungkan nasib user dengan posisi bintang/zodiak.
        Kalau user jomblo, kasih semangat atau mantra lucu.
        Kalau user punya pacar, kasih ramalan apakah dia setia atau tidak (ngarang saja yang lucu).
        """

        model = genai.GenerativeModel(
            "gemini-2.5-flash",
            system_instruction=instruksi_khusus
        )
        
        response = model.generate_content(input_user)
        return response.text
    
    except Exception as e:
        return f"Ada Error nih : {e}"