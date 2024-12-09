from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date


# Вывод функций
if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
