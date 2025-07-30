import requests
import json

token="""BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3ODUzNjE2MzMsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJqdWFuaXRvYWxjYWNob2ZhNTVAaG90bWFpbC5jb20ifQ.7UlljmzrEnvL5lt4G_3gT_D-Q013yjYuYNY3xX3OARiVmjzY2gmyjOCBvil1Gp4Aiz_1RYQX2Nqtf_x7DC4Wig"""
url = "https://api.estadisticasbcra.com/usd"

headers = {"Authorization":token}
res = requests.get(url,headers=headers)

USD = []

if res.status_code == 200:
    for valor in res.json():
        nuevo = {
            "dia" if key == "d" else "valor" if key == "v" else key: v
            for key, v in valor.items()
        }
        USD.append(nuevo)
    with open("dolar_oficial.json", mode="w",encoding="utf-8")as archivo:
        escribir = json.dump(USD,archivo,indent=2,ensure_ascii=False)
        
else:
    print(f"❌ Error: {res.status_code}")
    print(res.text)