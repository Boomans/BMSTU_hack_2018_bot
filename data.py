actions = [
    {
        "response": {
            "redirect": "/account/card/payment&money={money}",
            "message": "открыта страница пополнения счёта"
        },
        "requests": [
            "пополнить счёт на {money} рублей",
            "пополнить баланс на {money} рублей",
            "внести на счёт {money} рублей",
            "внести {money} рублей на счёт",
            "положить на счёт {money} рублей",
            "положить {money} рублей на счёт",
        ]
    },
    {
        "response": {
            "redirect": "/account/card/sms_notification&action=on",
            "message": "смс уведомлении подключены"
        },
        "requests": [
            "Включить смс уведомления",
            "Подключить смс уведомления"
        ]
    },
    {
        "response": {
            "redirect": "/account/card/sms_notification&action=off",
            "message": "смс уведомлении отключены"
        },
        "requests": [
            "Выключить смс уведомления",
            "Отключить смс уведомления"
        ]
    }
]