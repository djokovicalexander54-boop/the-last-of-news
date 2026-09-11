import trafilatura
import json
import asyncio
from flask import Flask
import threading
import os
import cloudscraper
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
pdfmetrics.registerFont(TTFont("Vazir", "Vazirmatn-Bold.ttf"))
# قالب پی دی اف اقتصادی
doc_E = SimpleDocTemplate(
    "pdf_Economic.pdf",
    pagesize=A4,
    rightMargin=30,
    leftMargin=30,
    topMargin=30,
    bottomMargin=30
)
# قالب پی دی اف سیاسی
doc_P = SimpleDocTemplate(
    "pdf_Policy.pdf",
    pagesize=A4,
    rightMargin=30,
    leftMargin=30,
    topMargin=30,
    bottomMargin=30
)
# قالب پی دی اف نظامی
doc_M = SimpleDocTemplate(
    "pdf_Military.pdf",
    pagesize=A4,
    rightMargin=30,
    leftMargin=30,
    topMargin=30,
    bottomMargin=30
)
# قالب پی دی اف تکنولوژی
doc_T = SimpleDocTemplate(
    "pdf_Technology.pdf",
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
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=14,
    leading=18,
    alignment=0
)
scraper = cloudscraper.create_scraper(browser={'browser':'chrome', 'platform':'windows','desktop':True})
async def start_new_01():
    # economic
    with open("economic.txt", "r", encoding="utf-8") as file:
        i=1
        k=1
        while k==1:
            try:
                long_text_economic = ""
                for line in file:
                    oop = ["https://", line]
                    item = "".join(oop)
                    url = item.strip()
                    site_path = await asyncio.to_thread(scraper.get, url, timeout=10)
                    new_data = trafilatura.extract(
                        site_path.text,
                        output_format="json",
                        include_comments=False,
                        target_language='fa',
                    )
                    if new_data:
                        data_note = json.loads(new_data)
                        text = data_note.get('text')
                        long_text_economic+=f"{text}\n--------------------"
                        print(f'{i}-->economic', flush=True)
                        i+=1
                        if i==50:
                            k=2 
                            break
            except Exception as e:         
                continue
        story_01 = []
        lines = long_text_economic.split('\n')
        for line in lines:
            if line.strip():
                pdf_file = get_display(arabic_reshaper.reshape(line))
                story_01.append(Paragraph(pdf_file, farsi_style))
                story_01.append(Spacer(1, 8))
        doc_E.build(story_01)
    print("ok economic", flush=True)
    return "pdf_Economic.pdf"
async def start_new_02():
    # policy
    with open("policy.txt", "r", encoding="utf-8") as file:
        i=1
        k=1
        while k==1:
            try:
                long_text_policy = ""
                for line in file:
                    oop = ["https://", line]
                    item = "".join(oop)
                    url = item.strip()
                    site_path = await asyncio.to_thread(scraper.get, url, timeout=10)
                    new_data = trafilatura.extract(
                        site_path.text,
                        output_format="json",
                        include_comments=False,
                        target_language='fa',
                    )
                    if new_data:
                        data_note = json.loads(new_data)
                        text = data_note.get('text')
                        long_text_policy+=f"{text}\n--------------------"
                        print(f'{i}-->policy', flush=True)
                        i+=1
                        if i==50:
                            k=2 
                            break
            except Exception as e:            
                continue
        story_02 = []
        lines = long_text_policy.split('\n')
        for line in lines:
            if line.strip():
                pdf_file = get_display(arabic_reshaper.reshape(line))
                story_02.append(Paragraph(pdf_file, farsi_style))
                story_02.append(Spacer(1, 8))
        doc_P.build(story_02)
    print("ok policy", flush=True)
    return "pdf_Policy.pdf"
async def start_new_03():
    # military
    with open("military.txt", "r", encoding="utf-8") as file:
        i=1
        k=1
        while k==1:
            try:
                long_text_military = ""
                for line in file:
                    oop = ["https://", line]
                    item = "".join(oop)
                    url = item.strip()
                    site_path = await asyncio.to_thread(scraper.get, url, timeout=10)
                    new_data = trafilatura.extract(
                        site_path.text,
                        output_format="json",
                        include_comments=False,
                        target_language='fa',
                    )
                    if new_data:
                        data_note = json.loads(new_data)
                        text = data_note.get('text')
                        long_text_military+=f"{text}\n--------------------"
                        print(f'{i}-->military', flush=True)
                        i+=1
                        if i==50:
                            k=2 
                            break
            except Exception as e:            
                continue
        story_03 = []
        lines = long_text_military.split('\n')
        for line in lines:
            if line.strip():
                pdf_file = get_display(arabic_reshaper.reshape(line))
                story_03.append(Paragraph(pdf_file, farsi_style))
                story_03.append(Spacer(1, 8))
        doc_M.build(story_03)
    print("ok military", flush=True)
    return "pdf_Military.pdf"
async def start_new_04():
    # technology
    with open("technology.txt", "r", encoding="utf-8") as file:
        i=1
        k=1
        while k==1:
            try:
                long_text_technology = ""
                for line in file:
                    oop = ["https://", line]
                    item = "".join(oop)
                    url = item.strip()
                    site_path = await asyncio.to_thread(scraper.get, url, timeout=10)
                    new_data = trafilatura.extract(
                        site_path.text,
                        output_format="json",
                        include_comments=False,
                        target_language='fa',
                    )
                    if new_data:
                        data_note = json.loads(new_data)
                        text = data_note.get('text')
                        long_text_technology+=f"{text}\n--------------------"
                        print(f'{i}-->technology', flush=True)
                        i+=1
                        if i==50:
                            k=2 
                            break
            except Exception as e:            
                continue
        story = []
        lines = long_text_technology.split('\n')
        for line in lines:
            if line.strip():
                pdf_file = get_display(arabic_reshaper.reshape(line))
                story.append(Paragraph(pdf_file, farsi_style))
                story.append(Spacer(1, 8))
        doc_T.build(story)
    print("ok technology", flush=True)
    return "pdf_Technology.pdf"
async def run_help(func):
    if func == start_new_01:
        pdf_E = await func()
    elif func == start_new_02:
        pdf_P = await func()
    elif func == start_new_03:
        pdf_M = await func()
    elif func == start_new_04:
        pdf_T = await func()
    return [pdf_E ,pdf_P, pdf_M, pdf_T]
async def main():
    task=[
        asyncio.create_task(run_help(start_new_01)),
        asyncio.create_task(run_help(start_new_02)),
        asyncio.create_task(run_help(start_new_03)),
        asyncio.create_task(run_help(start_new_04))
    ]
    await asyncio.gather(*task)
asyncio.run(main())
app = Flask(__name__)
@app.route("/")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pdf = await run_help()
    await context.bot.send_message(chat_id=7737231906 ,text="در حال بررسی")
    if pdf:
        await context.bot.send_document(chat_id=7737231906 , document=open(pdf[0], "rb"), caption="اخبار اقتصادی و مالی")
        await context.bot.send_document(chat_id=7737231906 , document=open(pdf[1], "rb"), caption="اخبار سیاسی")
        await context.bot.send_document(chat_id=7737231906 , document=open(pdf[2], "rb"), caption="اخبار نظامی")
        await context.bot.send_document(chat_id=7737231906 , document=open(pdf[3], "rb"), caption="اخبار تکنولوژی")
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
