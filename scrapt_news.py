import trafilatura
import json
import asyncio
import requests
from flask import Flask
import threading
import os
async def start_new():
    with open("economic.txt", "r", encoding="utf-8") as file:
        i=1
        w=1
        long_text = ""
        for line in file:
            item = line.strip()
            if item.startswith("https://"):
                url = item.split('#')[0]
                url_new = url.strip()
                print(f"{w} = {url_new}", flush=True)
                W+=1
                k=1
                tt=1
                while k==1:
                        site_path = requests.get(url_new)
                        await asyncio.sleep(3)
                        if site_path.status_code == 200:
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
                                print(f'{i}.yes ---> {url_new}', flush=True)
                                i+=1
                                if i==123:
                                    print("yes gemini.. 123", flush=True)
                                    with open("persian.txt", "w", encoding="utf-8") as file:
                                        file.write(long_text)
                                k=2
                        else:
                            print(tt, flush=True)
                            tt+=1
                            if tt==5:
                                k=2
                            await asyncio.sleep(3)
app = Flask(__name__)
@app.route("/")
def home():
    return "running..."
def help():
    asyncio.run(start_new()) 
if __name__ == '__main__':
    threading.Thread(target=help).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(port=port, host='0.0.0.0')
