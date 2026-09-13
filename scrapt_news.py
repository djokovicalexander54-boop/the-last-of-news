import trafilatura
import json
import asyncio
import cloudscraper
from flask import Flask
import threading
import os
scraper = cloudscraper.create_scraper(browser={'browser':'chrome', 'platform':'windows','desktop':True})
async def start_new_01():
    # economic
    with open("economic.txt", "r", encoding="utf-8") as file_EE:
        i=1
        long_text_economic = ""
        for line in file_EE:
            url = line.strip()
            if url.startswith("https://"):
                new_url = url.strip()
                print(f"{i} {new_url}")
                i+=1
                try:
                    response = await asyncio.wait_for(asyncio.to_thread(scraper.get, new_url, timeout=(5,10)), timeout=10)
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
                            long_text_economic+=f"{text} \n -------------------- \n"
                            print("ok this..")
                except Exception as e:
                    print(e)
    print("ok economic", flush=True)
    return long_text_economic
async def start_new_02():
    # policy
    with open("policy.txt", "r", encoding="utf-8") as file_PP:
        i=1
        long_text_policy = ""
        for line in file_PP:
            url = line.strip()
            if url.startswith("https://"):
                new_url = url.strip()
                print(f"{i} {new_url}")
                i+=1
                try:
                    response = await asyncio.wait_for(asyncio.to_thread(scraper.get, new_url, timeout=(5,10)), timeout=10)
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
                            print("ok this..")
                except Exception as e:   
                    print(e)  
    print("ok policy", flush=True)
    return long_text_policy
async def start_new_03():
    # military
    with open("military.txt", "r", encoding="utf-8") as file_MM:
        i=1
        long_text_military = ""
        for line in file_MM:
            url = line.strip()
            if url.startswith("https://"):
                new_url = url.strip()
                print(f"{i} {new_url}")
                i+=1
                try:
                    response = await asyncio.wait_for(asyncio.to_thread(scraper.get, new_url, timeout=(5,10)), timeout=10)
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
                            print("ok this..")
                except Exception as e:   
                    print(e) 
    print("ok military", flush=True)
    return long_text_military
async def start_new_04():
    # technology
    with open("technology.txt", "r", encoding="utf-8") as file_TT:
        i=1
        long_text_technology = ""
        for line in file_TT:
            url = line.strip()
            if url.startswith("https://"):
                new_url = url.strip()
                print(f"{i} {new_url}")
                i+=1
                try:
                    response = await asyncio.wait_for(asyncio.to_thread(scraper.get, new_url, timeout=(5,10)), timeout=10)
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
                            print(f"ok this..")
                except Exception as e:  
                    print(e) 
    print("ok technology", flush=True)
    return long_text_technology
async def main():
    pdf_E = await asyncio.gather(
        start_new_01()
    #    start_new_02(),
    #    start_new_03(),
    #    start_new_04()
    )
    with open("economic_news.txt", "w", encoding="utf-8") as file_E:
        file_E.write(pdf_E[0])
    print("ok pdf economic", flush=True)
    #with open("policy_news.txt", "w", encoding="utf-8") as file_P:
    #    file_P.write(pdf_P[0])
    #print("ok pdf policy", flush=True)
    #with open("military_news.txt", "w", encoding="utf-8") as file_M:
    #    file_M.write(pdf_M[0])
    #print("ok pdf military", flush=True)
    #with open("technology_news.txt", "w", encoding="utf-8") as file_T:
    #    file_T.write(pdf_T[0])
    #    print("ok pdf technology", flush=True)
app = Flask(__name__)
@app.route("/")
def home():
    return "running scrapt news..."
def starting():
    asyncio.run(main())
if __name__ == '__main__':
    threading.Thread(target=starting).start()
    port = int(os.environ("PORT", 8080))
    app.run(port=port, host='0.0.0.0')
