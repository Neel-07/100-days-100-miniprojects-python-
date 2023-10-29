import requests
from bs4 import BeautifulSoup

def main():
    print("Welcome to the Text-Based Web Browser!")
    while True:
        url = input("Enter the URL of the website you want to visit (or 'exit' to quit): ")
        if url.lower() == 'exit':
            print("Exiting the web browser. Goodbye!")
            break
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            print("\nTitle of the web page:")
            print(soup.title.string)
            print("\nPage content:")
            print(soup.get_text())
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
