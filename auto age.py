import requests

TOKEN = "token"
text = "text"
post_id = "post_id"

headers = {
    'authorization': "Bearer " + TOKEN,
    'x-device-info': 'Yay 3.2.0 Web (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36)',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

for i in range(150):
        payload = {"text": text,"color": 0,"font_size": 0,"post_id": post_id}
        res = requests.post('https://api.yay.space/v1/posts/repost',headers=headers,data=payload)
        print(res,res.text)
