В MySQL-базе есть таблица преподавателей (teachers) с полями fio (ФИО учителя), id (идентификатор) и есть таблица учеников-участников соревнований (participants) с полями name (имя ученика), id (идентификатор), teacher_id (внешний ключ на преподавателя ученика) и result (занятое учеником место в соревновании — положительные числа, начиная с 1).

Как вы считаете, что выводится следующим запросом

SELECT fio from teachers
WHERE id IN (SELECT teacher_id FROM participants
    WHERE result < 4 AND teacher_id NOT IN (
        SELECT teacher_id FROM participants WHERE result > 3));


Можно ли этот запрос как-то улучшить? Предложите вариант.

'''
Этот запрос выводит ФИО преподавателей,
у которых ВСЕ ученики заняли места [1,2,3] .

SELECT DISTINCT t.fio
FROM teachers t
JOIN participants p ON t.id = p.teacher_id
GROUP BY t.id, t.fio
HAVING MAX(p.result) < 4;

оптимизируй
SELECT DISTINCT t.fio
FROM teachers t
INNER JOIN participants p1 ON t.id = p1.teacher_id AND p1.result < 4
LEFT JOIN participants p2 ON t.id = p2.teacher_id AND p2.result > 3
WHERE p2.teacher_id IS NULL;

'''


ФИО преподавателей, у которых все ученики заняли места только с 1-го по 3-е

'''

Как поступить, если каждую запись нужно удалять через индивидуальное для каждой записи время?

1) Как в MongoDB настроить автоудаление записей из коллекции старее суток? 

создаем индекс ttl

db.collection.createIndex(
  { "createdAt": 1 },  { expireAfterSeconds: 86400 } // 86400 секунд = 24 часа
)
При создании дока добавляем  createdAt
{
  "data": "your data",  
  createdAt: new Date(),
  ...
}

2) Как поступить, если каждую запись нужно удалять через индивидуальное для каждой записи время?

создаем индекс ttl

db.collection.createIndex({ "expiresAt": 1 }, { expireAfterSeconds: 0 })

добавляем в док время удаления

db.collection.insertOne({
    "data": "your data",
    "expiresAt": new Date(Date.now() + 2 * 60 * 60 * 1000)  // 2 часа
})

db.collection.insertOne({
    "data": "other data",
    "expiresAt": new Date(Date.now() + 48* 60 * 60 * 1000)  // 48 часов 
})
'''



collection.create_index("expiresAt", expireAfterSeconds=0)

# Insert with custom expiration
def insert_with_ttl(data, hours_to_live=1):
    expiry_date = datetime.utcnow() + timedelta(hours=hours_to_live)
    document = {
        "data": data,
        "expiresAt": expiry_date
    }
    collection.insert_one(document)

# Usage examples
insert_with_ttl("expires in 2 hours", 2)
insert_with_ttl("expires in 1 day", 24)

'''
Покупатель выбирает товары и добавляет их в корзину.
Продавец проверяет наличие товаров на складе и остатки по каждому товару.
Продавец подтверждает (или не подтверждает заказ) и отправляет покупателю информацию о предоплате (или альтернативные варианты или заказ по наличию).
Покупатель подтверждает получение информации о предоплате и переводит деньги продавцу.
Продавец обрабатывает платёж и отправляет покупателю подтверждение оплаты и информацию о статусе заказа.
Если товары отсутствуют на складе, продавец отправляет покупателю сообщение об этом и предлагает альтернативные варианты или возможность заказать товар позже.


'''