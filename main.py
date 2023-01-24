import csv
import time
from telethon import TelegramClient
from db_operations import get_phones, post_sell, post_last_sell

list_id, list_phone = get_phones()

api_id = 1
api_hash = '1'

message = 'Добрый вечер! Мы - начинающий учебный центр "UNION OF FINANCE".  Каждый месяц мы разыгрываем 10 сертификатов на прохождение курса "Основы трейдинга и инвестиций" в нашей компании. С помощью программы "Random"  были выбраны 10 профилей-победителей. Вы в их числе, я Вас поздравляю! Ваш презент - это сертификат на курс по повышению финансовой грамотности, он даёт Вам право пройти обучение абсолютно бесплатно. Курс  носит индивидуальный характер  и проводится по принципу "от простого к сложному", в него включены такие темы, как: финансовое планирование, способы сохранения капитала, криптовалюта и разбор двух основных способов прогнозирования цен! Курс состоит из 8 индивидуальных занятий (1 занятие = 45 минут). Для Вас - все 8 занятий без оплаты! По окончании курса Вам выдается сертификат о прохождении данного курса. Если Вы заинтересованы, напишите, пожалуйста, контактный номер телефона, чтобы мы с Вами связались и всё рассказали подробнее.'


def open_csv(name: str):
    count = 0
    sender_count = 0
    with open(name, encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(r_file, delimiter=";")
        # Считывание данных из CSV файла
        for row in file_reader:
            if sender_count < len(list_phone) * 10:
                if len(row) != 0:
                    if row[1] != 'n/a' and row[4] == 'n/a':

                        client = TelegramClient(list_phone[sender_count % len(list_phone)], api_id, api_hash)

                        async def main(target_namer):
                            await client.send_message(target_namer, message)

                        with client:
                            try:
                                client.loop.run_until_complete(main(row[1]))
                                count += 1
                                print(list_phone[sender_count % len(list_phone)] + ':')
                                print('     ', count, "Сообщенипе отправлено: ", row[1])
                                post_sell(list_id[sender_count % len(list_phone)], row[1])
                            except Exception as e:
                                print(list_phone[sender_count % len(list_phone)] + ':')
                                print("     Увы и ах: ", row[1])
                                print(e)

                        if sender_count % len(list_phone) == len(list_phone) - 1:
                            time.sleep(301)

                        sender_count += 1
            else:
                print('Я ЗАКОНЧИЛ !!!\nЯ ЗАКОНЧИЛ !!!\nЯ ЗАКОНЧИЛ !!!\nЯ ЗАКОНЧИЛ !!!\n')
                post_last_sell(list_id)
                return 0


open_csv("F:/rabotasakha_members.csv")