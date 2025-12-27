import flet as ft
import requests
from config import COLLEGIATE_DICTIONARY_KEY


def main(page: ft.Page):
    word_field = ft.TextField(hint_text="enter a word")
    response_label = ft.Text("no word selected", max_lines=10)
    search_button = ft.Button(icon=ft.Icons.SEARCH, content=ft.Text("Search the Collegiate dictionary"))

    # handler functions
    def search_word(e) -> requests.Response:
        word = word_field.value
        api_key = COLLEGIATE_DICTIONARY_KEY
        search_url = f"https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
        print(f"searching for: {word}")
        response = requests.get(url=search_url)
        # process the response
        if response.status_code == 200:
            try:
                body = response.json()
                print("Word found", response.status_code)
                definitions = [f"{item["fl"]} - {item['shortdef'][0]}" for item in body if len(item['shortdef']) > 0]
                print(definitions)
                text = f"Entries: {len(body)} \nDefinitions: \n- {'\n- '.join(definitions)}"
                response_label.value = text
            except requests.exceptions.JSONDecodeError:
                print("Word not found", response.status_code, response.text)
                response_label.value = f"Word not found \n{response.text}"
        else:
            print("Response is not 200", response.status_code)
            response_label.value = f"API request failed with status: {response.status_code}"

    # map the handlers
    search_button.on_click = search_word

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Column(
                controls=[word_field, search_button, response_label],
            )
        )
    )


ft.run(main)
