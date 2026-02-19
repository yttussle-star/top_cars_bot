from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
import logging
from buttons import all_keyboard, koenigsegg_keyboard, bugati_keyboard, ferrari_keyboard, lamborghini_keyboard, \
    mclaren_keyboard, dodge_keyboard


from data import TOKEN



bot = Bot(TOKEN)
dp = Dispatcher()

router = Router()

@router.message(Command('start'))
async def start_function(message:Message):
    await message.answer(text=f"Salom, {message.from_user.first_name} bu bot mashinalar modellari va ular haqida malumot beradgan bot", reply_markup=all_keyboard)


@dp.message(lambda m: m.text == "Koenigsegg")
async def open1_menu(message: Message):
    await message.answer(
        "Koenigsegg — bu Shvetsiyada joylashgan mashhur superkar va giperkarlar ishlab chiqaruvchi avtomobil kompaniyasidir. Ushbu kompaniya 1994-yilda shved muhandisi va avtomobil ishqibozi Christian von Koenigsegg tomonidan tashkil etilgan. Uning asosiy maqsadi dunyodagi eng tez, eng ilg‘or va texnologik jihatdan mukammal sport avtomobillarni yaratish bo‘lgan. Kompaniya Shvetsiyaning Ängelholm shahrida joylashgan bo‘lib, u yerda barcha Koenigsegg avtomobillari qo‘lda yig‘iladi. Dastlabki yillarda kompaniya faqat prototiplar ustida ishlagan, real ishlab chiqarish esa 2000-yillarning boshida boshlangan. 2002-yilda Koenigsegg CC8S modeli yo‘llarda harakatlanish uchun rasmiy ruxsat olib, kompaniyaning birinchi seriyali avtomobili sifatida tarixga kirgan. Shundan so‘ng Koenigsegg CCX, Agera, Regera, Jesko va Gemera kabi mashhur modellarni ishlab chiqardi. Koenigsegg avtomobillari juda kam miqdorda ishlab chiqariladi, bu esa ularni noyob va qimmat qiladi. Kompaniya o‘zining dvigatellari, transmissiyasi va aerodinamik texnologiyalarini mustaqil ravishda ishlab chiqishi bilan ham mashhur. Bugungi kunda Koenigsegg dunyodagi eng tez va eng innovatsion avtomobillarni ishlab chiqaruvchi kompaniyalardan biri hisoblanadi va ko‘plab tezlik rekordlariga ega.",
        reply_markup=koenigsegg_keyboard
    )

@dp.message(lambda m: m.text == "Bugatti")
async def open2_menu(message: Message):
    await message.answer(
        "Bugatti — bu dunyodagi eng mashhur va nufuzli giperkar ishlab chiqaruvchi avtomobil kompaniyalaridan biridir. Ushbu kompaniya 1909-yilda italiyalik muhandis va dizayner Ettore Bugatti tomonidan tashkil etilgan. Dastlab Bugatti Fransiyaning Molsheim shahrida faoliyat boshlagan va qisqa vaqt ichida hashamat, tezlik hamda muhandislik mukammalligi bilan mashhur bo‘lib ketgan. Bugatti ilk yillarda sport va poyga avtomobillarini ishlab chiqargan bo‘lsa, keyinchalik hashamatli avtomobillar bilan ham tanila boshlagan. Ikkinchi jahon urushi davridan so‘ng kompaniya faoliyati susaygan va uzoq vaqt ishlab chiqarish to‘xtab qolgan. Bugatti brendi 1990-yillarda qayta tiklandi, ammo zamonaviy Bugatti davri 1998-yilda Volkswagen Group kompaniyani sotib olganidan keyin boshlandi. Shundan so‘ng Bugatti yuqori texnologiyali giperkarlar ishlab chiqarishga e’tibor qaratdi. 2005-yilda Bugatti Veyron modeli taqdim etilib, u dunyodagi eng tez va eng kuchli seriyali avtomobillardan biri sifatida tarixga kirdi. Keyinchalik Chiron, Divo, Bolide va Mistral kabi modellar ishlab chiqildi. Bugatti avtomobillari juda cheklangan miqdorda, qo‘lda yig‘iladi va yuqori darajadagi hashamat hamda texnologiyalarni o‘zida mujassam etadi. Bugungi kunda Bugatti nomi tezlik, hashamat va muhandislik san’atining eng yuqori cho‘qqisini ifodalaydi.",
        reply_markup=bugati_keyboard
    )


@dp.message(lambda m: m.text == "Ferrari")
async def open3_menu(message: Message):
    await message.answer(
        "Ferrari — bu Italiyada tashkil topgan va butun dunyoga mashhur bo‘lgan sport hamda superkarlar ishlab chiqaruvchi avtomobil kompaniyasidir. Ushbu kompaniya 1939-yilda italiyalik poygachi va muhandis Enzo Ferrari tomonidan tashkil etilgan. Dastlab kompaniya Auto Avio Costruzioni nomi ostida faoliyat yuritgan bo‘lib, birinchi avtomobili 1940-yilda ishlab chiqarilgan. Ikkinchi jahon urushidan so‘ng, 1947-yilda Ferrari nomi rasman paydo bo‘ldi va aynan shu yildan boshlab Ferrari brendi ostida avtomobillar ishlab chiqarila boshlandi. Kompaniyaning bosh qarorgohi Italiyaning Maranello shahrida joylashgan. Ferrari avvalo poyga avtomobillari, ayniqsa Formula 1 musobaqalari bilan mashhur bo‘lib, u yerda eng muvaffaqiyatli jamoalardan biri hisoblanadi. Poygalardagi tajriba keyinchalik yo‘l uchun mo‘ljallangan sport avtomobillarini yaratishda katta rol o‘ynadi. Ferrari avtomobillari yuqori tezlik, kuchli dvigatellar va o‘ziga xos dizayn bilan ajralib turadi. Kompaniya ishlab chiqarishni har doim cheklangan miqdorda olib boradi, bu esa Ferrari mashinalarini qimmat va noyob qiladi. Bugungi kunda Ferrari sport avtomobillari tezlik, sifat va prestij ramzi sifatida butun dunyoda tan olingan.",
        reply_markup=ferrari_keyboard
    )


@dp.message(lambda m: m.text == "Lamborghini")
async def open4_menu(message: Message):
    await message.answer(
        "Lamborghini — bu Italiyada tashkil topgan va hashamatli superkarlar ishlab chiqarishi bilan mashhur bo‘lgan avtomobil kompaniyasidir. Ushbu kompaniya 1963-yilda italiyalik tadbirkor Ferruccio Lamborghini tomonidan asos solingan. Ferruccio Lamborghini dastlab traktorlar ishlab chiqarish bilan shug‘ullangan va keyinchalik sport avtomobillar bozoriga kirishga qaror qilgan. Kompaniyaning bosh qarorgohi Italiyaning Sant’Agata Bolognese shahrida joylashgan. Lamborghini tashkil topganidan so‘ng qisqa vaqt ichida o‘zining kuchli dvigatellari va noodatiy dizayni bilan mashhurlikka erishdi. Kompaniyaning ilk modellari 1960-yillarning o‘rtalarida ishlab chiqarila boshlagan bo‘lib, Lamborghini 350 GT ilk muhim avtomobillardan biri hisoblanadi. Keyinchalik Miura modeli Lamborghini’ni butun dunyoga tanitdi va u tarixdagi ilk haqiqiy superkarlardan biri sifatida e’tirof etiladi. Lamborghini avtomobillari agressiv dizayn, kuchli V10 va V12 dvigatellari bilan ajralib turadi. Kompaniya ko‘p yillar davomida turli egalar qo‘l ostida faoliyat yuritgan va hozirgi kunda Volkswagen Group tarkibidagi Audi kompaniyasiga tegishli. Lamborghini avtomobillari cheklangan miqdorda ishlab chiqariladi va ular tezlik, hashamat hamda o‘ziga xos uslub ramzi hisoblanadi. Bugungi kunda Lamborghini dunyodagi eng mashhur superkar brendlaridan biri sifatida tanilgan.",
        reply_markup=lamborghini_keyboard
    )




@dp.message(lambda m: m.text == "Mclaren")
async def open5_menu(message: Message):
    await message.answer(
        "McLaren — bu Britaniyada tashkil topgan va dunyoga mashhur bo‘lgan sport va superkarlar ishlab chiqaruvchi avtomobil kompaniyasidir. Ushbu kompaniya 1963-yilda britaniyalik poygachi va muhandis Bruce McLaren tomonidan asos solingan. Dastlab kompaniya Formula 1 poyga jamoasi sifatida faoliyat boshlagan va tez orada poyga avtomobillarini yaratish bilan mashhur bo‘lgan. McLaren kompaniyasi bosh qarorgohi Buyuk Britaniyaning Woking shahrida joylashgan. Kompaniya ilk yo‘l avtomobilini 1992-yilda — McLaren F1 modelini ishlab chiqdi. F1 modeli o‘z vaqtida dunyodagi eng tez va eng ilg‘or avtomobillardan biri bo‘lib, u muhandislik va dizayn sohasida inqilobiy yangiliklar kiritdi. Shundan so‘ng McLaren MP4-12C, 650S, P1, 720S va Artura kabi superkarlar ishlab chiqarildi. McLaren avtomobillari yuqori tezlik, eng so‘nggi aerodinamik va texnologik yechimlar bilan ajralib turadi. Kompaniya ishlab chiqarishni cheklangan miqdorda amalga oshiradi, bu esa ularning avtomobillarini noyob va qimmat qiladi. Bugungi kunda McLaren nafaqat Formula 1 poygalarida, balki yo‘l uchun mo‘ljallangan superkarlar bozorida ham dunyodagi eng nufuzli brendlardan biri sifatida tanilgan.",
        reply_markup=mclaren_keyboard
    )





@dp.message(lambda m: m.text == "Dodge")
async def open6_menu(message: Message):
    await message.answer(
        "Dodge — bu Amerika Qo‘shma Shtatlarida tashkil topgan va mashhur avtomobil ishlab chiqaruvchi kompaniya hisoblanadi. Ushbu kompaniya 1900-yillarning boshlarida, aniqrog‘i 1900-yilda ikki aka-uka John va Horace Dodge tomonidan tashkil etilgan. Dastlab Dodge kompaniyasi turli avtomobil qismlari va motorlar ishlab chiqarish bilan shug‘ullangan, ammo tez orada ular o‘z avtomobillarini yaratishga qaror qilgan. 1914-yilda kompaniya birinchi Dodge avtomobilini ishlab chiqarib, bozorda o‘z o‘rnini topdi. Dodge avtomobillari dastlab mustahkamligi va ishonchliligi bilan mashhur bo‘lgan, shu sababli ularni ko‘plab yo‘l va transport ishlarida ishlatishgan. Keyinchalik Dodge sport, hashamatli va yengil avtomobillarni ham ishlab chiqarishni boshladi, jumladan Charger, Challenger va Durango kabi mashhur modellar paydo bo‘ldi. Bugungi kunda Dodge kompaniyasi Stellantis (ilgari Fiat Chrysler) guruhiga tegishli bo‘lib, ularning avtomobillari yuqori tezlik, kuchli dvigatellar va mustahkam dizayn bilan ajralib turadi. Dodge brendi Amerikaning avtomobil sanoatida uzoq tarixga ega bo‘lib, ishonchlilik va kuchli performans ramzi sifatida tanilgan.",
        reply_markup=dodge_keyboard
    )



@router.message(F.text == 'orqaga')
async def start_command(message: Message):
    await message.answer(text=f"Menu", reply_markup=all_keyboard)




@router.message(F.text)
async def car1_photo_handler(message: Message):
    text=message.text
    if text == "CC8S":
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIBW2l8dFeOEiC7yyOhAAHljAkMeECNOwACSA9rG1FH4EtLKWRY0UQzQQEAAwIAA3kAAzgE",
            caption="Koenigsegg CC8S"
        )

    elif text == "CCR":
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIBa2mAKDy_IBajYoXYYI8HzM174qy2AALnC2sbpHoBSAMbvEeibzz5AQADAgADeQADOAQ",
            caption="Koenigsegg CCR"
        )

    elif text == "CCX":
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIBbWmAMZScygvwouDYdP0xmJCBksXuAAIMDGsbpHoBSJ-apX8NTU5yAQADAgADeQADOAQ",
            caption="Koenigsegg CCX"
        )

    elif text == "CCXR":
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIBb2mAMepvxezl4UFuFoPHd733uhKRAAINDGsbpHoBSOP_BXOVnEQbAQADAgADeQADOAQ",
            caption="Koenigsegg CCXR"
        )

    elif text == "One:1":
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIBcmmAMtYWQrHlVYZ-OKg1_USZaavzAAIRDGsbpHoBSKz7F5fG1q_bAQADAgADeQADOAQ",
            caption="Koenigsegg One:1"
        )

    elif text == "Agera R":
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIBdGmAM1kWh3CX9V0OGkwjedxMjpY4AAITDGsbpHoBSI20dZdmzUcMAQADAgADeQADOAQ",
            caption="Koenigsegg Agera R"
        )

    elif text == "Agera RS":
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIBdmmAM8FKMAGThuppWjL-SBjk6rBjAAIUDGsbpHoBSHhdj0XFpuUSAQADAgADeQADOAQ",
            caption="Koenigsegg Agera RS"
        )

    elif text == "Agera Final Edition":
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIBeGmANAb9GH3oyqBG_mjahG2jpDK5AAIYDGsbpHoBSKXV-0V-ujmhAQADAgADeAADOAQ",
            caption="Koenigsegg Agera Final Edition"
        )

    elif text == "Agera FE Thor":
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIBemmANEMvITFHFjaeWdWxhShLVSQPAAIeDGsbpHoBSHd6nChM5J7PAQADAgADeQADOAQ",
            caption="Koenigsegg Agera FE Thor"
        )

    elif text == "Agera FE Vader":
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIBfGmANK4r265yXwTa_qfe0Lslj6_HAAIiDGsbpHoBSPQ_Jj2uAdlYAQADAgADeAADOAQ",
            caption="Koenigsegg Agera FE Vader"
        )

    elif text == "Regera":
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIBfmmANPOP9d07Gd3oFieAAUJd0IXqAAIlDGsbpHoBSEN52gkNtMpvAQADAgADbQADOAQ",
            caption="Koenigsegg Regera"
        )

    elif text == "Jesko Absolute":
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIBgmmANXhM-xW2LEurvIArMgkFJcqjAAInDGsbpHoBSHJXI2Y1zLgFAQADAgADbQADOAQ",
            caption="Koenigsegg Jesko Absolut"
        )

    elif text == "Jesko Attack":
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIBgGmANUWPOcSedBiuhgtJFi7UTkbyAAImDGsbpHoBSL4vgpyxXEFIAQADAgADeAADOAQ",
            caption="Koenigsegg Jesko Attack"
        )

    elif text == "Gemera":
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIBhGmANaT59VMKRfAtyN7OF83PW8rJAAIoDGsbpHoBSKgv6jRNDS9DAQADAgADeQADOAQ",
            caption="Koenigsegg Gemera"
        )

    elif text == "CC850":
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIBhmmANd1XMJ2nYDhcv2Z10AWkb0o7AAIuDGsbpHoBSDxfRdBfwjj7AQADAgADeQADOAQ",
            caption="Koenigsegg CC850"
        )





@router.message(F.text)
async def car2_photo_handler(message: Message):
    text=message.text
    if text == "Veyron":
        await message.answer_photo(
            photo="BURGA_VEYRON_PHOTO_FILE_ID",
            caption="Bugatti Veyron\n\n8.0L W16 quad-turbo engine\n1200 HP\n415 km/h top speed"
        )

    elif text == "Chiron":
        await message.answer_photo(
            photo="BURGA_CHIRON_PHOTO_FILE_ID",
            caption="Bugatti Chiron\n\n8.0L W16 quad-turbo engine\n1500 HP\n420 km/h top speed"
        )

    elif text == "Divo":
        await message.answer_photo(
            photo="BURGA_DIVO_PHOTO_FILE_ID",
            caption="Bugatti Divo\n\n8.0L W16 quad-turbo engine\n1500 HP\nLimited to 40 units\n380 km/h top speed"
        )

    elif text == "Centodieci":
        await message.answer_photo(
            photo="BURGA_CENTODIECI_PHOTO_FILE_ID",
            caption="Bugatti Centodieci\n\n8.0L W16 quad-turbo engine\n1600 HP\nLimited to 10 units\n380 km/h top speed"
        )

    elif text == "La Voiture Noire":
        await message.answer_photo(
            photo="BURGA_LA_VOITURE_NOIRE_PHOTO_FILE_ID",
            caption="Bugatti La Voiture Noire\n\n8.0L W16 quad-turbo engine\n1500 HP\nOne-off model\n$18.7 million price"
        )

    elif text == "Bolide":
        await message.answer_photo(
            photo="BURGA_BOLIDE_PHOTO_FILE_ID",
            caption="Bugatti Bolide\n\n8.0L W16 quad-turbo engine\n1825 HP\nTrack-only hypercar\n0-100 km/h in 2.17s"
        )

    elif text == "Mistral":
        await message.answer_photo(
            photo="BURGA_MISTRAL_PHOTO_FILE_ID",
            caption="Bugatti Mistral\n\n8.0L W16 engine\n1600 HP\nRoadster version\nLast W16 roadster"
        )

    elif text == "EB110":
        await message.answer_photo(
            photo="BURGA_EB110_PHOTO_FILE_ID",
            caption="Bugatti EB110\n\n3.5L V12 quad-turbo engine\n560 HP\n1990s supercar\n343 km/h top speed"
        )

    elif text == "Type 57":
        await message.answer_photo(
            photo="BURGA_TYPE57_PHOTO_FILE_ID",
            caption="Bugatti Type 57\n\n3.3L Straight-8 engine\n1934-1940 classic\nOne of the most beautiful cars ever made"
        )

    elif text == "Type 41 Royale":
        await message.answer_photo(
            photo="BURGA_TYPE41_ROYALE_PHOTO_FILE_ID",
            caption="Bugatti Type 41 Royale\n\n12.7L Straight-8 engine\nLuxury car from 1927-1933\nOnly 6 units produced"
        )

    elif text == "Veyron Super Sport":
        await message.answer_photo(
            photo="BURGA_VEYRON_SUPER_SPORT_PHOTO_FILE_ID",
            caption="Bugatti Veyron Super Sport\n\n8.0L W16 quad-turbo engine\n1200 HP\nWorld record: 431 km/h (2010)\nLimited to 30 units"
        )

    elif text == "Chiron Super Sport 300+":
        await message.answer_photo(
            photo="BURGA_CHIRON_SS300_PHOTO_FILE_ID",
            caption="Bugatti Chiron Super Sport 300+\n\n8.0L W16 quad-turbo engine\n1600 HP\nFirst car over 300 mph (482.8 km/h)\nLimited edition"
        )

    elif text == "Chiron Pur Sport":
        await message.answer_photo(
            photo="BURGA_CHIRON_PUR_SPORT_PHOTO_FILE_ID",
            caption="Bugatti Chiron Pur Sport\n\n8.0L W16 quad-turbo engine\n1500 HP\nFocus on agility and handling\n60 units produced"
        )

    elif text == "Chiron Sport":
        await message.answer_photo(
            photo="BURGA_CHIRON_SPORT_PHOTO_FILE_ID",
            caption="Bugatti Chiron Sport\n\n8.0L W16 quad-turbo engine\n1500 HP\nWeight reduced by 18 kg\nEnhanced handling"
        )

    elif text == "Veyron Grand Sport":
        await message.answer_photo(
            photo="BURGA_VEYRON_GRAND_SPORT_PHOTO_FILE_ID",
            caption="Bugatti Veyron Grand Sport\n\n8.0L W16 quad-turbo engine\n1200 HP\nConvertible version of Veyron\n360 km/h top speed"
        )

    elif text == "Chiron Profilee":
        await message.answer_photo(
            photo="BURGA_CHIRON_PROFILEE_PHOTO_FILE_ID",
            caption="Bugatti Chiron Profilee\n\n8.0L W16 quad-turbo engine\n1600 HP\nOne-off unique model\nLast new Chiron variant"
        )



























async def main():
    dp.include_router(router)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())








# import asyncio
# import logging
#
# from aiogram import Bot, Dispatcher, Router, F
# from aiogram.types import Message
#
# TOKEN = "8450344529:AAG8yC2DjL8gsopSoD_lFg-jRexovMRY5Oc"
# bot = Bot(TOKEN)
# dp = Dispatcher()
#
# router = Router()
#
# @router.message(F.photo)
# async def start_func(message: Message):
#     await message.answer(message.photo[-1].file_id)
#
# @router.message(F.text == '/photo')
# async def photo_func(message: Message):
#     await message.answer_photo(photo='AgACAgIAAxkBAAO-aXxHs8fYpIi1d5y2oNYg9AGrkG0AAhMRaxu6YeFLYprqYLJd74oBAAMCAAN4AAM4BA')
#
# async def main():
#     dp.include_router(router)
#     logging.basicConfig(level=logging.INFO)
#     await dp.start_polling(bot)
#
# if __name__ == '__main__':
#     asyncio.run(main())
#

































# 8450344529:AAG8yC2DjL8gsopSoD_lFg-jRexovMRY5Oc