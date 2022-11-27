from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardBuilder,InlineKeyboardButton


def get_kb_questions() -> InlineKeyboardMarkup:
    try:
        with open("C:\\Project\\Python\\testAIESEC\\answers.txt", 'r', encoding='utf-8') as file:
            a = file.read().split('\n')
            number_of_questions = len(a)
    except:
        print("ошибка в чтении файла")

    kb = InlineKeyboardBuilder()  # создается клавиатура
    for i in range(number_of_questions):
        kb.add(InlineKeyboardButton(
            text=str(i + 1),
            callback_data=f'callback_{i + 1}'
        ))
    kb.adjust(3)
    return kb.as_markup()
