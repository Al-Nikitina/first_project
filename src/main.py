def print_author():
    from dotenv import load_dotenv
    import os
    load_dotenv(dotenv_path="C:\\Users\\Admin\\Desktop\\Яндекс Практикум\\Виртуальное окружение\\first-project\\.env")
    author=os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")
print_author()
