actions = [
    {
        "response": {
            "action": "/account/payment?money={money}&account={account_id}",
            "message": "открыта страница пополнения счёта"
        },
        "description": "Пополнить счёт на <количество> рублей",
        "requests": [
            "пополнить [счёт|баланс] на {money} [рублей|руб]",
            "[внести|положить] на счёт {money} [рублей|руб]",
            "[внести|положить] {money} [рублей|руб] на счёт"
        ],
    },
    {
        "response": {
            "action": "/account/accounts/id{account_id}/service?type=sms_notification&action=on",
            "message": "смс уведомлении подключены"
        },
        "description": "Подключить смс уведомления",
        "requests": [
            "[включить|подключить] смс уведомления"
        ]
    },
    {
        "response": {
            "action": "/account/accounts/id{account_id}/service?type=sms_notification&action=off",
            "message": "смс уведомлении отключены"
        },
        "description": "Отключить смс уведомления",
        "requests": [
            "[выключить|отключить] смс уведомления",
        ]
    },
    {
        "response": {
            "action": "/account/accounts/id{account_id}/service?type=auto_refill&action=on",
            "message": "автопоплнение подключено"
        },
        "description": "Подключить автопополнение",
        "requests": [
            "[включить|подключить] автопополнение",
        ]
    },
    {
        "response": {
            "action": "/account/accounts/id{account_id}/service?type=auto_refill&action=off",
            "message": "отключено автопополнение"
        },
        "description": "Отключить автопополнение",
        "requests": [
            "[выключить|отключить] автопополнение",
        ]
    },
    {
        "response": {
            "action": "/account/cards/",
            "message": "показан список карт"
        },
        "description": "Показать список карт",
        "requests": [
            "показать список карт",
            "показать карты",
            "список карт",
            "карты"
        ]
    },
    {
        "response": {
            "action": "/account/cards/id{number}",
            "message": "информация о карте показана"
        },
        "description": "Показать карту <номер карты>",
        "requests": [
            "показать карту {number}",
            "карта {number}"
        ]
    },
    {
        "response": {
            "action": "/account/accounts/",
            "message": "счета показаны"
        },
        "description": "Показать счета",
        "requests": [
            "показать список счетов",
            "показать счета",
            "список счетов",
            "счета"
        ]
    },
    {
        "response": {
            "action": "/account/accounts/id{number}",
            "message": "показана информация о счете"
        },
        "description": "Показать информацию о счете <номер счета>",
        "requests": [
            "показать счет {number}"
        ]
    },
    {
        "response": {
            "action": "/account/accounts/id{account_id}/service",
            "message": "услуги показаны"
        },
        "description": "Показать услуги",
        "requests": [
            "показать услуги"
        ]
    }
]
