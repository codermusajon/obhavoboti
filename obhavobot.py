from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
from bs4 import BeautifulSoup as BS

t = requests.get('https://obhavo.uz/tashkent')
html_t = BS(t.content, 'html.parser')
t_namlik = html_t.find_all('div',class_='col-1')[0]
t_osmon = html_t.find_all('div', class_='current-forecast-desc')[0].text.strip()
t_oy=html_t.find_all('div', class_='col-2')[0].text.strip()
t_mintaqa = html_t.find('div', class_='padd-block').find_all('h2')[0].text.strip()
t_degree=html_t.find_all('div',class_='current-forecast')[0].text.strip()

j = requests.get("https://obhavo.uz/jizzakh")
html_j = BS(j.content, 'html.parser')
j_namlik = html_j.find_all('div',class_='col-1')[0]
j_osmon = html_j.find_all('div', class_='current-forecast-desc')[0].text.strip()
j_oy=html_j.find_all('div', class_='col-2')[0].text.strip()
j_mintaqa = html_j.find('div', class_='padd-block').find_all('h2')[0].text.strip()
j_degree = html_j.find_all('div',class_='current-forecast')[0].text.strip()

a = requests.get("https://obhavo.uz/andijan")
html_a = BS(a.content, 'html.parser')
a_namlik = html_a.find_all('div',class_='col-1')[0]
a_osmon = html_a.find_all('div', class_='current-forecast-desc')[0].text.strip()
a_oy=html_a.find_all('div', class_='col-2')[0].text.strip()
a_mintaqa = html_a.find('div', class_='padd-block').find_all('h2')[0].text.strip()
a_degree = html_a.find_all('div',class_='current-forecast')[0].text.strip()

b = requests.get("https://obhavo.uz/bukhara")
html_b = BS(b.content, 'html.parser')
b_namlik = html_b.find_all('div',class_='col-1')[0]
b_osmon = html_b.find_all('div', class_='current-forecast-desc')[0].text.strip()
b_oy=html_b.find_all('div', class_='col-2')[0].text.strip()
b_mintaqa = html_b.find('div', class_='padd-block').find_all('h2')[0].text.strip()
b_degree = html_b.find_all('div',class_='current-forecast')[0].text.strip()

k = requests.get("https://obhavo.uz/karshi")
html_k = BS(k.content, 'html.parser')
k_namlik = html_k.find_all('div',class_='col-1')[0]
k_osmon = html_k.find_all('div', class_='current-forecast-desc')[0].text.strip()
k_oy=html_k.find_all('div', class_='col-2')[0].text.strip()
k_mintaqa = html_k.find('div', class_='padd-block').find_all('h2')[0].text.strip()
k_degree = html_k.find_all('div',class_='current-forecast')[0].text.strip()

nv = requests.get("https://obhavo.uz/navoi")
html_nv = BS(nv.content, 'html.parser')
nv_namlik = html_nv.find_all('div',class_='col-1')[0]
nv_osmon = html_nv.find_all('div', class_='current-forecast-desc')[0].text.strip()
nv_oy=html_nv.find_all('div', class_='col-2')[0].text.strip()
nv_mintaqa = html_nv.find('div', class_='padd-block').find_all('h2')[0].text.strip()
nv_degree = html_nv.find_all('div',class_='current-forecast')[0].text.strip()

na = requests.get("https://obhavo.uz/namangan")
html_na = BS(na.content, 'html.parser')
na_namlik = html_na.find_all('div',class_='col-1')[0]
na_osmon = html_na.find_all('div', class_='current-forecast-desc')[0].text.strip()
na_oy=html_na.find_all('div', class_='col-2')[0].text.strip()
na_mintaqa = html_na.find('div', class_='padd-block').find_all('h2')[0].text.strip()
na_degree = html_na.find_all('div',class_='current-forecast')[0].text.strip()

nu = requests.get("https://obhavo.uz/nukus")
html_nu = BS(nu.content, 'html.parser')
nu_namlik = html_nu.find_all('div',class_='col-1')[0]
nu_osmon = html_nu.find_all('div', class_='current-forecast-desc')[0].text.strip()
nu_oy=html_nu.find_all('div', class_='col-2')[0].text.strip()
nu_mintaqa = html_nu.find('div', class_='padd-block').find_all('h2')[0].text.strip()
nu_degree = html_nu.find_all('div',class_='current-forecast')[0].text.strip()

s = requests.get("https://obhavo.uz/samarkand")
html_s = BS(s.content, 'html.parser')
s_namlik = html_s.find_all('div',class_='col-1')[0]
s_osmon = html_s.find_all('div', class_='current-forecast-desc')[0].text.strip()
s_oy=html_s.find_all('div', class_='col-2')[0].text.strip()
s_mintaqa = html_s.find('div', class_='padd-block').find_all('h2')[0].text.strip()
s_degree = html_s.find_all('div',class_='current-forecast')[0].text.strip()

te = requests.get("https://obhavo.uz/termez")
html_te = BS(te.content, 'html.parser')
te_namlik = html_te.find_all('div',class_='col-1')[0]
te_osmon = html_te.find_all('div', class_='current-forecast-desc')[0].text.strip()
te_oy=html_te.find_all('div', class_='col-2')[0].text.strip()
te_mintaqa = html_te.find('div', class_='padd-block').find_all('h2')[0].text.strip()
te_degree = html_te.find_all('div',class_='current-forecast')[0].text.strip()

u = requests.get("https://obhavo.uz/urgench")
html_u = BS(u.content, 'html.parser')
u_namlik = html_u.find_all('div',class_='col-1')[0]
u_osmon = html_u.find_all('div', class_='current-forecast-desc')[0].text.strip()
u_oy=html_u.find_all('div', class_='col-2')[0].text.strip()
u_mintaqa = html_u.find('div', class_='padd-block').find_all('h2')[0].text.strip()
u_degree = html_u.find_all('div',class_='current-forecast')[0].text.strip()

f = requests.get("https://obhavo.uz/ferghana")
html_f = BS(f.content, 'html.parser')
f_namlik = html_f.find_all('div',class_='col-1')[0]
f_osmon = html_f.find_all('div', class_='current-forecast-desc')[0].text.strip()
f_oy=html_f.find_all('div', class_='col-2')[0].text.strip()
f_mintaqa = html_f.find('div', class_='padd-block').find_all('h2')[0].text.strip()
f_degree = html_f.find_all('div',class_='current-forecast')[0].text.strip()

kh = requests.get("https://obhavo.uz/khiva")
html_kh = BS(kh.content, 'html.parser')
kh_namlik = html_kh.find_all('div',class_='col-1')[0]
kh_osmon = html_kh.find_all('div', class_='current-forecast-desc')[0].text.strip()
kh_oy=html_kh.find_all('div', class_='col-2')[0].text.strip()
kh_mintaqa = html_kh.find('div', class_='padd-block').find_all('h2')[0].text.strip()
kh_degree = html_kh.find_all('div',class_='current-forecast')[0].text.strip()






def city():
    return [
        [InlineKeyboardButton("Toshkent", callback_data=f"01")],
        [InlineKeyboardButton("Jizzax", callback_data=f"02")],
        [InlineKeyboardButton("Andijon", callback_data=f"03")],
        [InlineKeyboardButton("Buxoro", callback_data=f"04")],
        [InlineKeyboardButton("Qarshi", callback_data=f"05")],
        [InlineKeyboardButton("Navoiy", callback_data=f"06")],
        [InlineKeyboardButton("Namangan", callback_data=f"07")],
        [InlineKeyboardButton("Nukus", callback_data=f"08")],
        [InlineKeyboardButton("Samarqand", callback_data=f"09")],
        [InlineKeyboardButton("Termiz", callback_data=f"10")],
        [InlineKeyboardButton("Urganch", callback_data=f"11")],
        [InlineKeyboardButton("Farg'ona", callback_data=f"12")],
        [InlineKeyboardButton("Xiva", callback_data=f"13")]


    ]


def back():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]


def inline_handlerlar(update, context):
    query = update.callback_query
    data = query.data.split("_")

    if data[0] == "01":
        query.message.edit_text(f"🌏Mintaqangiz:  {t_mintaqa} \n🌡{t_degree[:4]} \n🌡{t_degree[4:]} \n {t_osmon} \n {t_namlik.text} \n {t_oy} \n Manzilimiz: @hudud_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "02":
        query.message.edit_text(f"🌏Mintaqangiz:  {j_mintaqa} \n🌡{j_degree} \n {j_osmon} \n {j_namlik.text} \n {j_oy} \n Manzilimiz: @hudud_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "03":
        query.message.edit_text(f"🌏Mintaqangiz:  {a_mintaqa} \n {a_degree} \n {a_osmon} \n {a_namlik.text} \n {a_oy} \n Manzilimiz: @hudud_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "04":
        query.message.edit_text(f"🌏Mintaqangiz:  {b_mintaqa} \n {b_degree} \n {b_osmon} \n {b_namlik.text} \n {b_oy} \n Manzilimiz: @hudud_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "05":
        query.message.edit_text(f"🌏Mintaqangiz:  {k_mintaqa} \n {k_degree} \n {k_osmon} \n {k_namlik.text} \n {k_oy} \n Manzilimiz: @hudud_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "06":
        query.message.edit_text(f"🌏Mintaqangiz:  {nv_mintaqa} \n {nv_degree} \n {nv_osmon} \n {nv_namlik.text} \n {nv_oy} \n Manzilimiz: @hudud_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "07":
        query.message.edit_text(f"🌏Mintaqangiz:  {na_mintaqa} \n {na_degree} \n {na_osmon} \n {na_namlik.text} \n {na_oy} \n Manzilimiz: @hudud_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "08":
        query.message.edit_text(f"🌏Mintaqangiz:  {nu_mintaqa} \n {nu_degree} \n {nu_osmon} \n {nu_namlik.text} \n {nu_oy} \n Manzilimiz: @hudud_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "09":
        query.message.edit_text(f"🌏Mintaqangiz:  {s_mintaqa} \n {s_degree} \n {s_osmon} \n {s_namlik.text} \n {s_oy} \n Manzilimiz: @hudud_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "10":
        query.message.edit_text(f"🌏Mintaqangiz:  {te_mintaqa} \n {te_degree} \n {te_osmon} \n {te_namlik.text} \n {te_oy} \n Manzilimiz: @hudud_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "11":
        query.message.edit_text(f"🌏Mintaqangiz:  {u_mintaqa} \n {u_degree} \n {u_osmon} \n {u_namlik.text} \n {u_oy} \n Manzilimiz: @hudud_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "12":
        query.message.edit_text(f"🌏Mintaqangiz:  {f_mintaqa} \n {f_degree} \n {f_osmon} \n {f_namlik.text} \n {f_oy} \n Manzilimiz: @hudud_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "13":
        query.message.edit_text(f"🌏Mintaqangiz:  {kh_mintaqa} \n {kh_degree} \n {kh_osmon} \n {kh_namlik.text} \n {kh_oy} \n Manzilimiz: @hudud_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))


    elif data[0] == 'back1':
        query.message.edit_text(
            f"🌏Bu yerdan Shahar yoki viloyatni tanlang 👇",
            reply_markup=InlineKeyboardMarkup(city()))


def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"""Salom {user.first_name} 🖐🏼\n🌏Bu yerdan Shahar yoki viloyatni tanla 👇""",
                              reply_markup=InlineKeyboardMarkup(city()))


def main():
    Token = "5431969559:AAG4Re8He0Sypm0VxE1wmlLyMQl_peiZRDQ"
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_handlerlar))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

# Davomini o`zingiz mustaqil bajaring!!!
