import requests
from config.settings import HOST, PORT


page = 'get_form'
url = f'http://{HOST}:{PORT}/{page}'

user_form = {
      "user_name": "ilia",
      "user_email": "ilia@example.com",
      "user_phone": "+7 999 999 99 99",
      "any_fields": "test",
}

order_form = {
      "customer": "Any Company",
      "customer_email": "example@example.com",
      "date_order": "2023-03-10",
      "order": "title"
    }

call_back_form = {
      "title": "title",
      "phone": "+7 111 111 99 99",
      "comment": "comment",
    }

delivery_form = {
      "customer": "ilia",
      "city": "moscow",
      "phone": "+7 499 123 12 12",
      "date_delivered": "12.12.2023",
      "date_received": "12.12.2024",
      "any_fields": "test",
}
review_form = {
      "user_name": "ilia",
      "user_email": "lia@example.com",
      "date_review": "20.11.2023",
      "content": "good job"
    }

not_exist_form = {
      "field_1": "name",
      "field_2": "example@example.com",
      "field_3": "+7 111 111 11 11",
      "field_4": "12.12.2023",
      "field_5": "2023-12-12"
}


def test_user_form():
    """Test GET and POST requests for UserForm."""
    get_response = requests.get(url, params=user_form)
    post_response = requests.post(url, data=user_form)
    assert get_response.status_code == 200
    assert post_response.status_code == 200
    assert get_response.json() == {"form_name": "UserForm"}
    assert post_response.json() == {"form_name": "UserForm"}


def test_order_form():
    """Test GET and POST requests for OrderForm."""
    get_response = requests.get(url, params=order_form)
    post_response = requests.post(url, data=order_form)
    assert get_response.status_code == 200
    assert post_response.status_code == 200
    assert get_response.json() == {"form_name": "OrderForm"}
    assert post_response.json() == {"form_name": "OrderForm"}


def test_call_back_form():
    """Test GET and POST requests for CallBackForm."""
    get_response = requests.get(url, params=call_back_form)
    post_response = requests.post(url, data=call_back_form)
    assert get_response.status_code == 200
    assert post_response.status_code == 200
    assert get_response.json() == {"form_name": "CallBackForm"}
    assert post_response.json() == {"form_name": "CallBackForm"}


def test_delivery_form():
    """Test GET and POST requests for DeliveryForm."""
    get_response = requests.get(url, params=delivery_form)
    post_response = requests.post(url, data=delivery_form)
    assert get_response.status_code == 200
    assert post_response.status_code == 200
    assert get_response.json() == {"form_name": "DeliveryForm"}
    assert post_response.json() == {"form_name": "DeliveryForm"}


def test_review_form():
    """Test GET and POST requests for ReviewForm."""
    get_response = requests.get(url, params=review_form)
    post_response = requests.post(url, data=review_form)
    assert get_response.status_code == 200
    assert post_response.status_code == 200
    assert get_response.json() == {"form_name": "ReviewForm"}
    assert post_response.json() == {"form_name": "ReviewForm"}


def test_not_existing_form():
    """Test GET and POST requests for no-existing form."""
    get_response = requests.get(url, params=not_exist_form)
    post_response = requests.post(url, data=not_exist_form)
    assert get_response.status_code == 200
    assert get_response.json() == {
        'field_1': 'text',
        'field_2': 'email',
        'field_3': 'phone',
        'field_4': 'date',
        'field_5': 'date'
    }
    assert post_response.status_code == 200
    assert post_response.json() == {
        'field_1': 'text',
        'field_2': 'email',
        'field_3': 'phone',
        'field_4': 'date',
        'field_5': 'date'
    }


def test_empty_request():
    """Test GET and POST requests without arguments."""
    get_response = requests.get(url)
    post_response = requests.post(url)
    assert get_response.status_code == 200
    assert get_response.json() == {}
    assert post_response.status_code == 200
    assert post_response.json() == {}
