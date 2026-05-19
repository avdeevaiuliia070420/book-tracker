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
    pass

def list_books(books):
    pass

def average_rating(books):
    pass

def author_stats(books):
    pass

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