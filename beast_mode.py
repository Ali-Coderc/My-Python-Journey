# 🛡️ مشروع الحارس الشخصي لعلي
# الموقع: غليزان، الجزائر
# الهدف: الـ 25 دولار بالحلال + الانضباط النفسي

import webbrowser

def main():
    print("--- ⚔️ مرحباً بك في لوحة تحكم الوحش علي ⚔️ ---")
    print("1. 💻 افتح مشروعي على GitHub")
    print("2. 🕋 مواقيت الصلاة (الرزق)")
    print("3. 🚫 حظر الأفكار السلبية (الحماية)")
    
    choice = input("\nما هو قرارك الآن؟: ")
    
    if choice == '1':
        webbrowser.open("https://github.com/Ali-Coderc/My-Python-Journey")
    elif choice == '2':
        webbrowser.open("https://www.google.com/search?q=prayer+times+relizane")
    elif choice == '3':
        print("🛑 تذكر: أنت مبرمج، والمبرمج يسيطر على نظامه!")
        webbrowser.open("https://www.youtube.com/results?search_query=how+to+quit+bad+habits+for+men")

if __name__ == "__main__":
    main()
