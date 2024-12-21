#  from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
#  from src.processing import filter_by_state, sort_by_date

# Вывод функций
if __name__ == "__main__":
    #  print(get_mask_card_number("Visa Classic 6831982476737658"))
    #  print(get_mask_account("Счет 35383033474447895560"))
    print(mask_account_card("Visa Platinum 7000792289606361"))
    #  print(mask_account_card("Счет 64686473678894779589"))
    print(get_date("2024-03-11T02:26:18.671407"))
