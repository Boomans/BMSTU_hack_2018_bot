actions = [
    {
        "response": {
            "action": "/account/accounts/id{account_id}/payment?money={money}",
            "message": "открыта страница пополнения счёта"
        },
        "requests": [
            "пополнить [счёт|баланс] на {money} [рублей|руб]",
            "[внести|положить] на счёт {money} [рублей|руб]",
            "[внести|положить] {money} [рублей|руб] на счёт"
        ],
        "description": "пополнить счёт на <количество> рублей"
    },
    {
        "response": {
            "action": "/account/accounts/id{account_id}/service?type=sms_notification&action=on",
            "message": "смс уведомлении подключены"
        },
        "requests": [
            "[включить|подключить] смс уведомления"
        ]
    },
    {
        "response": {
            "action": "/account/accounts/id{account_id}/service?type=sms_notification&action=off",
            "message": "смс уведомлении отключены"
        },
        "requests": [
            "[выключить|отключить] смс уведомления",
        ]
    },
    {
        "response": {
            "action": "/account/accounts/id{account_id}/service?type=auto_refill&action=on",
            "message": "смс уведомлении подключены"
        },
        "requests": [
            "[включить|подключить] автопополнение",
        ]
    },
    {
        "response": {
            "action": "/account/accounts/id{account_id}/service?type=auto_refill&action=off",
            "message": "смс уведомлении отключены"
        },
        "requests": [
            "[выключить|отключить] автопополнение",
        ]
    },
    {
        "response": {
            "action": "/account/cards/",
            "message": "смс уведомлении отключены"
        },
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
            "message": "смс уведомлении отключены"
        },
        "requests": [
            "показать карту {number}",
            "карта {number}"
        ]
    },
    {
        "response": {
            "action": "/account/accounts/",
            "message": "смс уведомлении отключены"
        },
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
            "message": "смс уведомлении отключены"
        },
        "requests": [
            "показать счет {number}"
        ]
    },
    {
        "response": {
            "action": "/account/accounts/id{account_id}/service",
            "message": "смс уведомлении отключены"
        },
        "requests": [
            "показать услуги"
        ]
    }
]