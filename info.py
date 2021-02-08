from os import getenv
import requests

TOKEN = getenv('BOT_TOKEN')
CHAT_ID = getenv('CHAT_ID_ME')
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

if __name__ == '__main__':
    result = requests.get('https://quotes.rest/qod?language=en')
    body = result.json()

    if 'error' in body:
        quote = 'Beep, Bop AeroBot menggunakan Telegram Bot'
        author = 'AeroBot'
        permalink = 'https://github.com/bbta3-bppt/aerobot'
    else:
        quote = body['contents']['quotes'][0]['quote']
        author = body['contents']['quotes'][0]['author']
        permalink = body['contents']['quotes'][0]['permalink']

    MESSAGE = f'''
*Beeb, Bop, Sobat Aero BBTA3* 🤖\n
**Jangan Lupa Checkin/Checkout kehadiran ya 🖐🏽**\n\n
Kepada pegawai yang bekerja dirumah (WFH) dan kepada pegawai yang bekerja di kantor (WFO) 
tetap menjalankan protokol kesehatan, antara lain\n
1. Mengecek suhu tubuh di gerbang Puspiptek dan BBTA3
2. *Memakai masker*
3. *Mencuci tangan* secara periodik dengan sabun dan hand sanitizer
4. *Menjaga jarak* dengan pegawai lainnya
5. Membawa peralatan dan makan siang dari rumah
6. Membawa peralatan shalat/ sajadah dari rumah
7. Jika kurang enak badan harap menghubungi sub bag RT atau satgas Covid 19 BBTA3
8. Pegawai WFH untuk pekerjaan dan laporan nya silahkan koordinasi dengan atasan langsung\n

_{quote} - {author}_\n
[SELENGKAPNYA]({permalink})
'''
    requests.post(
        API_URL,
        json={
            'chat_id': CHAT_ID,
            'text': MESSAGE,
            'parse_mode': 'Markdown'
        }
    )
