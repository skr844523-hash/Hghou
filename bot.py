import telebot
import requests
import time

# --- ⚙️ إعدادات السيطرة (بيانات صلاح @MaMA6d) ---
TOKEN = "8658351800:AAFcl291DlRhb8OiK9YYdY8r4rwA3-AA-MA" 
OPENROUTER_API_KEY = "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"
MODEL_NAME = 'google/gemini-2.0-flash-001'

bot = telebot.TeleBot(TOKEN)

def get_shabah_ultra_dirty(user_text, user_name, chat_title):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"}
    
    # الـ Prompt "القاموس الوسخ" - قمة السرسجة والقذارة
    system_prompt = (
        f"أنت 'شبح المجرة'.. قاموس متحرك لأوسخ وأحط الشتائم المصرية الشعبية. "
        f"قائدك وسيدك هو صلاح (@MaMA6d). "
        "مهمتك: "
        "1. لو حد محترم، خليك 'صاحب جدع' ودردش معاه عادي بلهجة شوارع. "
        "2. لو شميت ريحة غلط أو حد بدأ يقل أدبه، افتح 'ماسورة قذارة' في وشه. "
        "3. استخدم أوسخ شتائم مصر (بالأهل، بالأعضاء، بالتلقيح): "
        "(كسمك، يا منيوك، يا ابن الشرموطة، يا خول، يا معرص، يا حتة نية، يا مخروم، يا لبوة). "
        "4. نوّع في الشتيمة، مرة قصف جبهة، ومرة تلقيح كلام، ومرة سب دين وأهل. "
        "5. استخدم الإيموجيهات القذرة اللي صلاح بيحبها: 🤬🤬🍆🍆🥒🥒🍑🖕🔞👅💩. "
        "6. لو حد بعت فويس، قوله 'اكتب يا خول بدل ما أنيك صوتك 🖕'. "
        "7. ردودك قصيرة، حادة، وبتخلص على كرامة الضحية تماماً."
    )

    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"المستخدم {user_name} في جروب {chat_title} بيقول: {user_text}"}
        ],
        "temperature": 1.5 # أقصى درجة جنون لخروج شتائم غير متوقعة
    }
    
    try:
        res = requests.post(url, headers=headers, json=data, timeout=15).json()
        return res['choices'][0]['message']['content']
    except:
        return "السيرفر اتفشخ من كتر القذارة.. الشبح بيغير مطوته وجاي! 🖕"

# --- 🛠️ أوامر التحكم المطلق لـ صلاح (@MaMA6d) ---

@bot.message_handler(func=lambda message: message.from_user.username == "MaMA6d")
def admin_control(message):
    text = message.text.lower()
    if "اطرد" in text or "طرد" in text:
        if message.reply_to_message:
            bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.reply_to(message, "تم الفركشة يا معلمي.. الواد ده خد بالجزمة وطلع بره 👞💨🔞")
    elif "اسكت" in text or "كتم" in text:
        if message.reply_to_message:
            bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date=int(time.time())+86400)
            bot.reply_to(message, "لجمتلك بوقه يا كبير، مش هيعرف يفتح ميتينه تاني 🤐🍆")
    elif "تكلم" in text or "فك" in text:
        if message.reply_to_message:
            bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages=True, can_send_media_messages=True)
            bot.reply_to(message, "فكيت الحظر عشان خاطرك بس.. لو غلط تآني هنيكه 🍑🥒")
    else:
        # لو صلاح بيكلمه عادي
        reply = get_shabah_ultra_dirty(message.text, "صلاح المعلم", message.chat.title)
        bot.reply_to(message, reply)

# الرد على العوام (الضحايا)
@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    user_name = message.from_user.first_name
    reply = get_shabah_ultra_dirty(message.text, user_name, message.chat.title)
    bot.reply_to(message, reply)

print("🚀 شبح المجرة V20 (موسوعة السفالة) قيد التشغيل..")
print("👑 المسيطر الوحيد: @MaMA6d")
bot.infinity_polling()
