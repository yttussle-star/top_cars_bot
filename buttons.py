from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


all_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Koenigsegg'), KeyboardButton(text='Bugatti')],
        [KeyboardButton(text='Ferrari'), KeyboardButton(text='Lamborghini')],
        [KeyboardButton(text='McLaren'), KeyboardButton(text='Dodge')],











    ],
    resize_keyboard=True
)



koenigsegg_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="CC8S"), KeyboardButton(text="CCR")],
        [KeyboardButton(text="CCX"), KeyboardButton(text="CCXR")],
        [KeyboardButton(text="One:1"), KeyboardButton(text="Agera R")],
        [KeyboardButton(text="Agera RS"), KeyboardButton(text="Agera Final Edition")],
        [KeyboardButton(text="Agera FE Thor"), KeyboardButton(text="Agera FE Vader")],
        [KeyboardButton(text="Regera"), KeyboardButton(text="Jesko Absolute")],
        [KeyboardButton(text="Gemera"), KeyboardButton(text="CC850")],
        [KeyboardButton(text="Jesko Attack")],
        [KeyboardButton(text="orqaga")],
    ],
    resize_keyboard=True
)

#---------------------------------------------------------


bugati_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Veyron"), KeyboardButton(text="Chiron")],
        [KeyboardButton(text="Divo"), KeyboardButton(text="Centodieci")],
        [KeyboardButton(text="La Voiture Noire"), KeyboardButton(text="Bolide")],
        [KeyboardButton(text="Mistral"), KeyboardButton(text="EB110")],
        [KeyboardButton(text="Type 57"), KeyboardButton(text="Type 41 Royale")],
        [KeyboardButton(text="Veyron Super Sport"), KeyboardButton(text="Chiron Super Sport 300+")],
        [KeyboardButton(text="Chiron Pur Sport"), KeyboardButton(text="Chiron Sport")],
        [KeyboardButton(text="Veyron Grand Sport"), KeyboardButton(text="Chiron Profilee")],
        [KeyboardButton(text="orqaga")],''
    ],
    resize_keyboard=True
)


ferrari_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="F8 Tributo"), KeyboardButton(text="SF90 Stradale")],
        [KeyboardButton(text="296 GTB"), KeyboardButton(text="Roma")],
        [KeyboardButton(text="Portofino M"), KeyboardButton(text="812 Superfast")],
        [KeyboardButton(text="812 GTS"), KeyboardButton(text="SF90 Spider")],
        [KeyboardButton(text="296 GTS"), KeyboardButton(text="F8 Spider")],
        [KeyboardButton(text="Monza SP1"), KeyboardButton(text="Monza SP2")],
        [KeyboardButton(text="LaFerrari"), KeyboardButton(text="LaFerrari Aperta")],
        [KeyboardButton(text="488 Pista"), KeyboardButton(text="488 GTB")],
        [KeyboardButton(text="458 Italia"), KeyboardButton(text="458 Spider")],
        [KeyboardButton(text="California T"), KeyboardButton(text="FF")],
        [KeyboardButton(text="GTC4Lusso"), KeyboardButton(text="599 GTO")],
        [KeyboardButton(text="Enzo"), KeyboardButton(text="F40")],
        [KeyboardButton(text="F50"), KeyboardButton(text="F430")],
        [KeyboardButton(text="360 Modena"), KeyboardButton(text="Testarossa")],
        [KeyboardButton(text="orqaga")],
    ],
    resize_keyboard=True
)



lamborghini_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Aventador"), KeyboardButton(text="Huracán")],
        [KeyboardButton(text="Urus"), KeyboardButton(text="Revuelto")],
        [KeyboardButton(text="Sián"), KeyboardButton(text="Countach")],
        [KeyboardButton(text="Diablo"), KeyboardButton(text="Murciélago")],
        [KeyboardButton(text="Gallardo"), KeyboardButton(text="Veneno")],
        [KeyboardButton(text="Centenario"), KeyboardButton(text="Reventón")],
        [KeyboardButton(text="Asterion"), KeyboardButton(text="Essenza SCV12")],
        [KeyboardButton(text="Huracán STO"), KeyboardButton(text="Huracán Evo")],
        [KeyboardButton(text="Aventador SVJ"), KeyboardButton(text="Aventador S")],
        [KeyboardButton(text="Huracán Tecnica"), KeyboardButton(text="Huracán Sterrato")],
        [KeyboardButton(text="Countach LPI 800-4"), KeyboardButton(text="Jalpa")],
        [KeyboardButton(text="LM002"), KeyboardButton(text="Miura")],
        [KeyboardButton(text="350 GT"), KeyboardButton(text="400 GT")],
        [KeyboardButton(text="Islero"), KeyboardButton(text="Espada")],
        [KeyboardButton(text="orqaga")],
    ],
    resize_keyboard=True
)




mclaren_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="720S"), KeyboardButton(text="765LT")],
        [KeyboardButton(text="Artura"), KeyboardButton(text="P1")],
        [KeyboardButton(text="Senna"), KeyboardButton(text="Speedtail")],
        [KeyboardButton(text="570S"), KeyboardButton(text="600LT")],
        [KeyboardButton(text="650S"), KeyboardButton(text="675LT")],
        [KeyboardButton(text="MP4-12C"), KeyboardButton(text="F1")],
        [KeyboardButton(text="Elva"), KeyboardButton(text="Sabre")],
        [KeyboardButton(text="GT"), KeyboardButton(text="750S")],
        [KeyboardButton(text="540C"), KeyboardButton(text="620R")],
        [KeyboardButton(text="12C Spider"), KeyboardButton(text="650S Spider")],
        [KeyboardButton(text="675LT Spider"), KeyboardButton(text="720S Spider")],
        [KeyboardButton(text="765LT Spider"), KeyboardButton(text="570S Spider")],
        [KeyboardButton(text="600LT Spider"), KeyboardButton(text="Artura Spider")],
        [KeyboardButton(text="P1 GTR"), KeyboardButton(text="Senna GTR")],
        [KeyboardButton(text="orqaga")],
    ],
    resize_keyboard=True
)





dodge_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Charger"), KeyboardButton(text="Challenger")],
        [KeyboardButton(text="Durango"), KeyboardButton(text="Hornet")],
        [KeyboardButton(text="Charger SRT Hellcat"), KeyboardButton(text="Challenger SRT Hellcat")],
        [KeyboardButton(text="Durango SRT Hellcat"), KeyboardButton(text="Charger Daytona")],
        [KeyboardButton(text="Challenger Demon"), KeyboardButton(text="Challenger Redeye")],
        [KeyboardButton(text="Charger Redeye"), KeyboardButton(text="Charger Scat Pack")],
        [KeyboardButton(text="Challenger Scat Pack"), KeyboardButton(text="Viper")],
        [KeyboardButton(text="Dart"), KeyboardButton(text="Journey")],
        [KeyboardButton(text="Caravan"), KeyboardButton(text="Grand Caravan")],
        [KeyboardButton(text="Nitro"), KeyboardButton(text="Caliber")],
        [KeyboardButton(text="Avenger"), KeyboardButton(text="Magnum")],
        [KeyboardButton(text="Neon"), KeyboardButton(text="Stealth")],
        [KeyboardButton(text="Shadow"), KeyboardButton(text="Spirit")],
        [KeyboardButton(text="Dakota"), KeyboardButton(text="Ramcharger")],
        [KeyboardButton(text="orqaga")],
    ],
    resize_keyboard=True
)




















