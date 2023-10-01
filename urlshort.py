import string
import random

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.chars = string.ascii_letters + string.digits
        self.base_url = "https://short.ly/"

    def generate_short_url(self):
        return ''.join(random.choice(self.chars) for _ in range(6))

    def shorten_url(self, original_url):
        if original_url in self.url_map:
            return self.url_map[original_url]
        else:
            short_url = self.base_url + self.generate_short_url()
            self.url_map[original_url] = short_url
            return short_url

if __name__ == "__main__":
    url_shortener = URLShortener()

    while True:
        print("URL Shortener Menu:")
        print("1. Shorten URL")
        print("2. Resolve URL")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            original_url = input("Enter the original URL: ")
            short_url = url_shortener.shorten_url(original_url)
            print(f"Shortened URL: {short_url}")

        elif choice == "2":
            short_url = input("Enter the shortened URL: ")
            original_url = url_shortener.resolve_url(short_url)
            if original_url:
                print(f"Original URL: {original_url}")
            else:
                print("URL not found.")

        elif choice == "3":
            print("Exiting the URL Shortener. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option (1, 2, or 3).")