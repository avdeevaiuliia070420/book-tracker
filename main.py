import json
import os

DATA_FILE = 'books.json'

def load_books():
    """Загружает список книг из JSON-файла."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_books(books):
    """Сохраняет список книг в JSON-файл."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

# Заглушки – будут реализованы в соответствующих ветках
def add_book(books):
    print("\n--- Добавление новой книги ---")
    author = input("Автор: ").strip()
    title = input("Название: ").strip()
    
    # Проверка дубликата (закроет Issue #1)
    for book in books:
        if book['автор'].lower() == author.lower() and book['название'].lower() == title.lower():
            print("Ошибка: Такая книга уже существует в списке.")
            return
    
    # Валидация оценки
    while True:
        try:
            rating = int(input("Оценка (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Оценка должна быть целым числом от 1 до 5.")
        except ValueError:
            print("Пожалуйста, введите целое число.")
    
    date = input("Дата прочтения (ГГГГ-ММ-ДД): ").strip()
    
    new_book = {
        "автор": author,
        "название": title,
        "оценка": rating,
        "дата_прочтения": date
    }
    books.append(new_book)
    save_books(books)
    print("Книга успешно добавлена!")

def list_books(books):
    """Вывод всех книг с нумерацией."""
    if not books:
        print("\nСписок книг пуст.")
        return
    print("\n--- Все книги ---")
    for idx, book in enumerate(books, 1):
        print(f"{idx}. {book['автор']} - {book['название']} | Оценка: {book['оценка']} | Дата: {book['дата_прочтения']}")

def average_rating(books):
    """Расчёт и вывод средней оценки."""
    if not books:
        print("\nНет книг для расчёта средней оценки.")
        return
    avg = sum(book['оценка'] for book in books) / len(books)
    print(f"\nСредняя оценка: {avg:.2f}")

def author_stats(books):
    """Статистика: количество книг по каждому автору."""
    if not books:
        print("\nНет книг для статистики.")
        return
    stats = {}
    for book in books:
        author = book['автор']
        stats[author] = stats.get(author, 0) + 1
    print("\n--- Статистика по авторам ---")
    for author, count in stats.items():
        print(f"{author}: {count} книг(и)")

def delete_book(books):
    pass

def main():
    books = load_books()
    while True:
        print("\n=== Трекер прочитанных книг ===")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            list_books(books)
        elif choice == '3':
            average_rating(books)
        elif choice == '4':
            author_stats(books)
        elif choice == '5':
            delete_book(books)
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()