TRANSLATIONS = {
    'en': {
        'welcome_message': "👋 Welcome to YT Insta Downloader Bot!\n\n🌍 Choose your language:",
        'language_set': "🌟 Great! Language set to {lang}.\n\n🚀 What would you like to do?",
        'subscription_confirmed': "✅ Thank you for subscribing! You can now use the bot.",
        'subscription_required': "❌ You haven't subscribed yet. Please join the channel and try again.",
        'subscription_check_error': "❌ An error occurred. Please try again later.",
        'help_text': "🆘 Help:\n\n1. 🔗 Send a YouTube or Instagram link to download\n2. 🌍 Use /language to change the language\n3. 🔄 Use /start to restart the bot\n\n💡 Tip: You can use the buttons below for quick actions!",
        'processing_request': "⏳ Processing your request... Please wait.",
        'download_success': "✅ Downloaded with YT Insta Downloader bot",
        'download_failed': "❌ Sorry, couldn't download the media. Please check the link and try again.",
        'send_link': "🔗 Great! Please send me a YouTube or Instagram link to download.",
        'choose_language': "🌍 Choose your new language:",
        'download_button': "📥 Download",
        'help_button': "🆘 Help",
        'change_language_button': "🌍 Change Language",
        'download_more_button': "📥 Download more",
        'join_channel_button': "✅ Join Channel",
        'check_subscription_button': "🔄 Check Subscription"
    },
    'uz': {
        'welcome_message': "👋 YT Insta Downloader botiga xush kelibsiz!\n\n🌍 Tilni tanlang:",
        'language_set': "🌟 Ajoyib! Til {lang} ga o'zgartirildi.\n\n🚀 Nima qilishni xohlaysiz?",
        'subscription_confirmed': "✅ Obuna bo'lganingiz uchun rahmat! Endi botdan foydalanishingiz mumkin.",
        'subscription_required': "❌ Siz hali obuna bo'lmagansiz. Iltimos, kanalga qo'shiling va qaytadan urinib ko'ring.",
        'subscription_check_error': "❌ Xatolik yuz berdi. Iltimos, keyinroq qayta urinib ko'ring.",
        'help_text': "🆘 Yordam:\n\n1. 🔗 Yuklab olish uchun YouTube yoki Instagram havolasini yuboring\n2. 🌍 Tilni o'zgartirish uchun /language buyrug'idan foydalaning\n3. 🔄 Botni qayta ishga tushirish uchun /start buyrug'idan foydalaning\n\n💡 Maslahat: Tezkor harakatlar uchun quyidagi tugmalardan foydalanishingiz mumkin!",
        'processing_request': "⏳ So'rovingiz qayta ishlanmoqda... Iltimos, kuting.",
        'download_success': "✅ YT Insta Downloader bot yordamida yuklab olindi",
        'download_failed': "❌ Kechirasiz, media yuklab olinmadi. Iltimos, havolani tekshiring va qaytadan urinib ko'ring.",
        'send_link': "🔗 Ajoyib! Iltimos, menga YouTube yoki Instagram havolasini yuboring.",
        'choose_language': "🌍 Yangi tilni tanlang:",
        'download_button': "📥 Yuklab olish",
        'help_button': "🆘 Yordam",
        'change_language_button': "🌍 Tilni o'zgartirish",
        'download_more_button': "📥 Ko'proq yuklab olish",
        'join_channel_button': "✅ Kanalga qo'shilish",
        'check_subscription_button': "🔄 Obunani tekshirish"
    },
    'ru': {
        'welcome_message': "👋 Добро пожаловать в YT Insta Downloader Bot!\n\n🌍 Выберите язык:",
        'language_set': "🌟 Отлично! Язык установлен на {lang}.\n\n🚀 Что бы вы хотели сделать?",
        'subscription_confirmed': "✅ Спасибо за подписку! Теперь вы можете использовать бота.",
        'subscription_required': "❌ Вы еще не подписались. Пожалуйста, присоединитесь к каналу и попробуйте снова.",
        'subscription_check_error': "❌ Произошла ошибка. Пожалуйста, попробуйте позже.",
        'help_text': "🆘 Помощь:\n\n1. 🔗 Отправьте ссылку на YouTube или Instagram для скачивания\n2. 🌍 Используйте /language для смены языка\n3. 🔄 Используйте /start для перезапуска бота\n\n💡 Совет: Вы можете использовать кнопки ниже для быстрых действий!",
        'processing_request': "⏳ Обрабатываем ваш запрос... Пожалуйста, подождите.",
        'download_success': "✅ Скачано с помощью YT Insta Downloader bot",
        'download_failed': "❌ Извините, не удалось скачать медиа. Пожалуйста, проверьте ссылку и попробуйте снова.",
        'send_link': "🔗 Отлично! Пожалуйста, отправьте мне ссылку на YouTube или Instagram.",
        'choose_language': "🌍 Выберите новый язык:",
        'download_button': "📥 Скачать",
        'help_button': "🆘 Помощь",
        'change_language_button': "🌍 Изменить язык",
        'download_more_button': "📥 Скачать еще",
        'join_channel_button': "✅ Присоединиться к каналу",
        'check_subscription_button': "🔄 Проверить подписку"
    }
}

def get_text(key, lang='en'):
    return TRANSLATIONS.get(lang, TRANSLATIONS['en']).get(key, TRANSLATIONS['en'].get(key, key))