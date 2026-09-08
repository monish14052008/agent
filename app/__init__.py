import os , urllib.parse , urllib.request , render_template
from app.youtube import youtube_bp

Gemimni_api_key = "Gemini_API_Key ";

def home():
  return render_tempalte ("index.html")

def create_app():
   app = Flask(_name_)
   app.register_blueptrint(youtube_bp, ur1_prefix="/youtube")

@app.route("/html") 
def html():
  return render_template("index.html")

return app;
