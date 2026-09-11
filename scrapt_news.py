import trafilatura
import json
import asyncio
import requests
from flask import Flask
import threading
import os
from telegram import Update
from telegram.ext import Application, ContextTypes, CommandHandler
from telegram import Bot
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import arabic_reshaper
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from bidi.algorithm import get_display
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
TOKEN = "8992200652:AAFiA72fUw_u6KO1MsVFk5d9UIAendpssWw"
bot = Bot(TOKEN)
async def start_new():
    pdfmetrics.registerFont(TTFont("Vazir", "Vazirmatn-Bold.ttf"))
    doc = SimpleDocTemplate(
        "pdf_d.pdf",
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )
    styles = getSampleStyleSheet()
    farsi_style = ParagraphStyle(
        'Farsistyle',
        parent=styles['Normal'],
        fontName='Vazir',
        fontSize=14,
        leading=18,
        alignment=2
    )
    english_style = ParagraphStyle(
        'EnglishStyle',
        parent=styles("Normal"),
        fontName="Helvetica",
        fontSize=14,
        leading=18,
        alignment=0
    )
    with open("news_sites.txt", "r", encoding="utf-8") as file:
        i=1
        try:
            long_text = ""
            for line in file:
                item = line.strip()
                if item.startswith("https://"):
                    url = item.split('#')[0]
                    url_new = url.strip()
                    site_path = requests.get(url_new)
                    new_data = trafilatura.extract(
                        site_path.text,
                        output_format="json",
                        include_comments=False,
                        target_language='fa',
                    )
                    if new_data:
                        data_note = json.loads(new_data)
                        text = data_note.get('text')
                        long_text+=f"{text}\n--------------------"
                        print(f'{i}.yes', flush=True)
                        i+=1
                        if i==123:
                            break
        except Exception as e:            
            print("yes gemini..", flush=True)
    story = []
    lines = long_text.split('\n')
    for line in lines:
        if line.strip():
            pdf_file = get_display(arabic_reshaper.reshape(line))
            story.append(Paragraph(pdf_file, farsi_style))
            story.append(Spacer(1, 8))
    doc.build(story)
    return "pdf_d.pdf"
app = Flask(__name__)
@app.route("/")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pdf = await start_new()
    await context.bot.send_message(chat_id=7737231906 ,text="در حال بررسی")
    if pdf:
        await context.bot.send_document(chat_id=7737231906 , document=open(pdf, "rb"), caption="آخرین اخبار")
    else:
        await context.bot.send_message(chat_id=7737231906 ,text=f"خالیه..{pdf}")
def run_port():
    port = int(os.environ.get("PORT", 10000))
    app.run(port=port, host='0.0.0.0')
if __name__=='__main__':
    threading.Thread(target=run_port, daemon=False).start()
    app1 = Application.builder().token(TOKEN).build()
    app1.add_handler(CommandHandler("start", start))
    app1.run_polling()