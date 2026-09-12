import trafilatura
import json
import asyncio
import cloudscraper
from reportlab.lib.pagesizes import letter
import arabic_reshaper
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from bidi.algorithm import get_display
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from flask import Flask
import threading
import os
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
    with open("economic.txt", "r", encoding="utf-8") as file_EE:
        i=0
        long_text_economic = ""
        for line in file_EE:
            url = line
            print(f"{i}------> economic >>> {url}")
            if i==100:
                break
            else:
                m=1
                while m!=5:
                    try:
                        response = await asyncio.wait_for(asyncio.to_thread(scraper.get, url, timeout=(5,10)), timeout=10)
                        if response.status_code == 200:
                            new_data = trafilatura.extract(
                                response.text,
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
                            m=5
                        else:
                            m+=1
                    except Exception as e:
                        print(e)
                        await asyncio.sleep(5)
                        m+=1
                        continue
    print("ok economic", flush=True)
    return long_text_economic
async def start_new_02():
    # policy
    with open("policy.txt", "r", encoding="utf-8") as file_PP:
        i=0
        long_text_policy = ""
        for line in file_PP:
            url = line
            print(f"{i}------> policy >>> {url}")
            if i==100:
                break
            else:
                m=1
                while m!=5:
                    try:
                        response = await asyncio.wait_for(asyncio.to_thread(scraper.get, url, timeout=(5,10)), timeout=10)
                        if response.status_code == 200:
                            new_data = trafilatura.extract(
                                response.text,
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
                            m=5
                        else:
                            m+=1
                    except Exception as e:   
                        print(e)  
                        await asyncio.sleep(5)
                        m+=1       
                        continue
    print("ok policy", flush=True)
    return long_text_policy
async def start_new_03():
    # military
    with open("military.txt", "r", encoding="utf-8") as file_MM:
        i=0
        long_text_military = ""
        for line in file_MM:
            url = line
            print(f"{i}------> military >>> {url}")
            if i==100:
                break
            else:
                m=1
                while m!=5:
                    try:
                        response = await asyncio.wait_for(asyncio.to_thread(scraper.get, url, timeout=(5,10)), timeout=10)
                        if response.status_code == 200:
                            new_data = trafilatura.extract(
                                response.text,
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
                            m=5
                        else:
                            m+=1
                    except Exception as e:   
                        print(e) 
                        await asyncio.sleep(5)
                        m+=1        
                        continue
    print("ok military", flush=True)
    return long_text_military
async def start_new_04():
    # technology
    with open("technology.txt", "r", encoding="utf-8") as file_TT:
        i=0
        m=1
        long_text_technology = ""
        for line in file_TT:
            url = line
            print(f"{i}------> technology >>> {url}")
            if i==100:
                break
            else:
                m=1
                while m!=5:
                    try:
                        response = await asyncio.wait_for(asyncio.to_thread(scraper.get, url, timeout=(5,10)), timeout=10)
                        if response.status_code == 200:
                            new_data = trafilatura.extract(
                                response.text,
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
                                m=5
                        else:
                            m+=1
                    except Exception as e:  
                        print(e) 
                        await asyncio.sleep(5)
                        m+=1        
                        continue
    print("ok technology", flush=True)
    return long_text_technology
async def main():
    pdf_E, pdf_P, pdf_M, pdf_T = await asyncio.gather(
        start_new_01(),
        start_new_02(),
        start_new_03(),
        start_new_04()
    )
    story_01 = []
    lines = pdf_E.split('\n')
    for line in lines:
        if line:
            pdf_file = get_display(arabic_reshaper.reshape(line))
            story_01.append(Paragraph(pdf_file, farsi_style))
            story_01.append(Spacer(1, 8))
    doc_E.build(story_01)
    print("ok pdf economic", flush=True)
    story_02 = []
    lines = pdf_P.split('\n')
    for line in lines:
        if line:
            pdf_file = get_display(arabic_reshaper.reshape(line))
            story_02.append(Paragraph(pdf_file, farsi_style))
            story_02.append(Spacer(1, 8))
    doc_P.build(story_02)
    print("ok pdf policy", flush=True)
    story_03 = []
    lines = pdf_M.split('\n')
    for line in lines:
        if line:
            pdf_file = get_display(arabic_reshaper.reshape(line))
            story_03.append(Paragraph(pdf_file, farsi_style))
            story_03.append(Spacer(1, 8))
    doc_M.build(story_03)
    print("ok pdf military", flush=True)
    story_04 = []
    lines = pdf_T.split('\n')
    for line in lines:
        if line:
            pdf_file = get_display(arabic_reshaper.reshape(line))
            story_04.append(Paragraph(pdf_file, farsi_style))
            story_04.append(Spacer(1, 8))
    doc_T.build(story_04)
    print("ok pdf technology", flush=True)
app = Flask(__name__)
@app.route("/")
def help():
    return "running..."
def kk():
    asyncio.run(main())
if __name__=='__main__':
    threading.Thread(target=kk, daemon=True).start()
    port = int(os.environ.get('PORT', 10000))
    app.run(port=port, host='0.0.0.0')
