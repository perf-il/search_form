import re


def is_valid_email(email: str) -> bool:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return bool(re.fullmatch(regex, email))


def is_valid_phone(phone: str) -> bool:
    regex = re.compile(r'\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}')
    return bool(re.fullmatch(regex, phone))


def is_valid_date(date: str) -> bool:
    regex_1 = re.compile(r'[0-3][0-9]\.[0-1][1-9]\.[1-2]\d{3}')
    regex_2 = re.compile(r'[1-2]\d{3}-[0-1][1-9]-[0-3][0-9]')
    return bool(re.fullmatch(regex_1, date) or re.fullmatch(regex_2, date))


def find_field_type(value: str) -> str:
    if is_valid_email(value):
        return 'email'
    if is_valid_phone(value):
        return 'phone'
    if is_valid_date(value):
        return 'date'
    return 'text'


def search_form(data_request: dict, templates: list) -> str | None:

    for template in templates:
        for key, value in template.items():
            if key == "name":
                continue
            else:
                if key in data_request and find_field_type(data_request[key]) == value:
                    result = template["name"]
                else:
                    result = None
                    break
        if result:
            return result

