import email_validator
import requests
import os


class Color:
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    reset = "\033[0m"


class EmailLookup:
    def __init__(self, email) -> None:
        self.email = email
        self.hibp_api_key = os.getenv("HIBP_API_KEY") or input(">>> HaveiBeenPwned API-Key: ")
        self.color = Color()
        self.timeout = 10
        self.lookup()

    def lookup(self):
        try:
            # Validate email
            try:
                email_info = email_validator.validate_email(
                    self.email, check_deliverability=False
                )
                self.email = email_info.normalized
            except email_validator.EmailNotValidError:
                print(
                    f"[!] {self.color.red}{self.email}{self.color.reset} seems to be invalid."
                )
                return

            hibp_data = self.check_hibp()

            if not hibp_data:
                print(f"{self.color.green}[v] no breaches found!{self.color.reset}")
                return

            print(f"[v] {self.color.green}gathered-data{self.color.reset}:")
            for breach in hibp_data:
                print(
                    f"\t[{self.color.yellow}{breach['name']}{self.color.reset}] date: {breach['date']} | count: {breach['pwncount']:,} | leaked: {breach['types']}"
                )

        except Exception as e:
            print(
                f"[!] {self.color.red}unable to verify the given email{self.color.reset}"
            )
            print(f"[debug-error] {e}")

    def check_hibp(self) -> list:
        try:
            url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{self.email}"
            headers = {"hibp-api-key": self.hibp_api_key, "User-Agent": "007-TheBond"}
            params = {"truncateResponse": "false"}

            res = requests.get(
                url, headers=headers, params=params, timeout=self.timeout
            )

            if res.status_code == 404:
                return []

            res.raise_for_status()
            data = res.json()

            results = []
            for breach in data:
                results.append(
                    {
                        "name": breach["Title"],
                        "date": breach["BreachDate"],
                        "pwncount": breach["PwnCount"],
                        "types": ", ".join(breach["DataClasses"]),
                    }
                )

            return results

        except Exception as e:
            print(f"[debug-error] {e}")
            return []