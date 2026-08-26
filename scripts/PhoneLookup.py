import phonenumbers
from phonenumbers import geocoder, carrier, timezone, PhoneNumberType


class PhoneLookup:
    def __init__(self, raw_phone: str, default_region: str = None):
        self.raw_phone = raw_phone
        self.default_region = default_region
        self.parsed_num = None
        self.is_valid = False
        self.print_data()

    def print_data(self):
            data = self.lookup()
            for key, value in data.items():
                if isinstance(value, dict):
                    for key, value in value.items():
                        print(f"o+ \t\033[2m{key}\033[0m: {value}")
                print(f"+ {key}: {value}")


    def _parse(self) -> bool:
        """Parses and validates the input without throwing unhandled exceptions."""
        try:
            self.parsed_num = phonenumbers.parse(self.raw_phone, self.default_region)
            self.is_valid = phonenumbers.is_valid_number(self.parsed_num)
            return self.is_valid
        except phonenumbers.NumberParseException:
            self.is_valid = False
            return False

    def _get_line_type(self) -> str:
        """Determines if the number is Mobile, Fixed-line, VoIP, etc."""
        if not self.parsed_num:
            return "UNKNOWN"

        number_type = phonenumbers.number_type(self.parsed_num)
        mapping = {
            PhoneNumberType.MOBILE: "MOBILE",
            PhoneNumberType.FIXED_LINE: "FIXED_LINE",
            PhoneNumberType.FIXED_LINE_OR_MOBILE: "FIXED_LINE_OR_MOBILE",
            PhoneNumberType.TOLL_FREE: "TOLL_FREE",
            PhoneNumberType.PREMIUM_RATE: "PREMIUM_RATE",
            PhoneNumberType.SHARED_COST: "SHARED_COST",
            PhoneNumberType.VOIP: "VOIP",
            PhoneNumberType.PERSONAL_NUMBER: "PERSONAL_NUMBER",
            PhoneNumberType.PAGER: "PAGER",
            PhoneNumberType.UAN: "UAN",
            PhoneNumberType.VOICEMAIL: "VOICEMAIL"
        }
        return mapping.get(number_type, "UNKNOWN")

    def lookup(self) -> dict:
        """Executes full offline extraction and returns a clean dictionary."""
        if not self._parse():
            return {
                "status": "error",
                "raw_input": self.raw_phone,
                "message": "Invalid phone number format or non-existent country code"
            }

        # Format number variants for downstream dorking/OSINT tools
        e164 = phonenumbers.format_number(self.parsed_num, phonenumbers.PhoneNumberFormat.E164)
        national = phonenumbers.format_number(self.parsed_num, phonenumbers.PhoneNumberFormat.NATIONAL)
        international = phonenumbers.format_number(self.parsed_num, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

        # Extract offline metadata
        region_desc = geocoder.description_for_number(self.parsed_num, "en")
        carrier_name = carrier.name_for_number(self.parsed_num, "en")
        tz_list = timezone.time_zones_for_number(self.parsed_num)

        return {
            "status": "success",
            "is_valid": self.is_valid,
            "formats": {
                "e164": e164,
                "national": national,
                "international": international,
                "country_code": str(self.parsed_num.country_code),
                "national_number": str(self.parsed_num.national_number)
            },
            "meta": {
                "country_region": region_desc if region_desc else "Unknown",
                "original_carrier": carrier_name if carrier_name else "Unknown / Unassigned",
                "line_type": self._get_line_type(),
                "time_zones": list(tz_list) if tz_list else []
            }
        }