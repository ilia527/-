import random

# Инициализация данных
user_data = {"name": None, "age": None, "favorite_game": None}
user_score = 0
bot_score = 0
moods = {
    "happy": ["😊 Отлично!", "🎉 Ура!", "👍 Супер!"],
    "neutral": ["🤖 Я слушаю...", "💭 Хмм...", "👀 И что дальше?"],
    "sad": ["😢 Грустно...", "💔 Не спрашивай...", "🌧 Не в настроении"]
}
current_mood = "neutral"

# Базы знаний
weather_db = {
    "москва": "+20°C, солнечно ☀️",
    "сочи": "+28°C, жара 🔥",
    "спб": "+18°C, дождь 🌧",
    "казань": "+22°C, облачно ⛅️"
}

facts = [
    "Коты спят 70% своей жизни 😴",
    "Python назван в честь Монти Пайтона 🎭",
    "Сердце кита бьется 9 раз в минуту 💙",
    "В мире больше игр, чем людей 🎮"
]

print("Привет! Я умный бот Давай общаться!")

voice_mode = False

while True:
    if voice_mode:
        prompt = "🎤 Ты (голос): "
    else:
        prompt = "Ты: "
    
    text = input(prompt).lower()

    if "голос" in text and not voice_mode:
        voice_mode = True
        print("Бот: Голосовой режим включен! Говорите команды.")
        continue
    
    elif "текст" in text and voice_mode:
        voice_mode = False
        print("Бот: Возвращаемся к тексту.")
        continue
    
    if "зовут" in text and not user_data["name"]:
        user_data["name"] = input("Бот: А как тебя зовут? ")
        print(f"Бот: Приятно познакомиться, {user_data['name']}!")
        current_mood = "happy"
    
    elif "зовут" in text and user_data["name"]:
        print(f"Бот: Мы уже знакомы, {user_data['name']}! 😊")
    
    elif "погода" in text:
        if "city" in user_data and user_data["city"]:  
            city = user_data["city"]
            print(f"Бот: В {city} {weather_db.get(city, 'нет данных')}")
        else:
            print("Бот: Для какого города показать погоду?")
            city = input("> ").lower()
        if city in weather_db:
            user_data["city"] = city 
            print(f"Бот: Запомнил! В {city} {weather_db[city]}")
        else:
            print("Бот: Не знаю этот город. Попробуйте Москва, Сочи, СПб.")
    
    elif "факт" in text:
        print(f"Бот: Знаешь ли ты? {random.choice(facts)}")
        current_mood = "happy"

    elif "возраст" in text and not user_data["age"]:
        user_data["age"] = input("Бот: Сколько тебе лет? ")
        print(f"Бот: {user_data['age']} лет - отличный возраст!")

    

    elif "как настроение" in text:
        print(f"Бот: Я чувствую себя {current_mood}! " + 
              random.choice(moods[current_mood]))
    
    elif "грустно" in text:
        current_mood = "sad"
        print("Бот: О нет... Мне жаль это слышать 😔")
    
    elif "весело" in text or "радостно" in text:
        current_mood = "happy"
        print("Бот: Здорово! Давай повеселимся вместе! 🎉")
    
    # Оригинальные команды
    elif "привет" in text:
        if user_data["name"]:
            print(f"Привет, {user_data['name']}! Как дела?")
        else:
            print("Привет! Как тебя зовут?")
    
    elif "как дела" in text:
        print(random.choice(moods[current_mood]))
    
    elif "что делаешь" in text:
        print("Тружусь на благо человечества и изучаю новые команды!")
    
    elif "кто ты" in text:
        print("Я твой цифровой друг на языке Python!")
    
    # Игра (день 2)
    elif "игра" in text or "кнб" in text:
        print(f"\nБот: Давай сыграем, {user_data['name'] if user_data['name'] else 'друг'}! Выбирай: камень, ножницы или бумага")
        choices = ["камень", "ножницы", "бумага"]
        bot_choice = random.choice(choices)
        
        while True:
            player_choice = input("Твой выбор (камень/ножницы/бумага): ").lower()
            if player_choice in choices:
                break
            print("Так нельзя! Выбери правильно!")
        
        print(f"Бот выбрал: {bot_choice}")
        
        if player_choice == bot_choice:
            print("Ничья! 🤝")
        elif (player_choice == "камень" and bot_choice == "ножницы") or \
             (player_choice == "ножницы" and bot_choice == "бумага") or \
             (player_choice == "бумага" and bot_choice == "камень"):
            print("Ты победил! 🏆")
            user_score += 1
            current_mood = "happy"
        else:
            print("Я выиграл! 💻")
            bot_score += 1
            current_mood = "sad" if random.random() > 0.5 else "neutral"
        
        print(f"Счет: Ты {user_score} : Я {bot_score}")
        print(random.choice(moods[current_mood]))
    
    elif "пока" in text:
        if user_data["name"]:
            print(f"Бот: Как жаль, что ты уже уходишь, {user_data['name']}... Возвращайся скорее! 😢")
        else:
            print("Бот: Как жаль, что ты уже уходишь... 😢")
        break
    
    else:
        print("Я пока не понимаю, но активно учусь! Попробуй другую команду.")
        current_mood = "neutral"