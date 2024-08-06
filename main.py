import sys
import webbrowser

from PySide6.QtCore import QRect
from PySide6.QtGui import QIntValidator, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow

from app_design import Ui_CurrencyConventer
from connections import collect_data, check_internet


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CurrencyConventer()
        self.ui.setupUi(self)

        self.internet_connection = False
        if check_internet():
            self.internet_connection = True

        self.currencies = {"usd", "kzt", "uah", "cny", "rub", "kgs", "pln"}
        self.rates_to_usd = self.get_rates()

        self.convert_text = self.ui.Convert_Text
        self.currency_line_top = self.ui.Currency_Line_Top
        self.currency_box_top = self.ui.Currency_Box_Top
        self.currency_line_bottom = self.ui.Currency_Line_Bottom
        self.currency_box_bottom = self.ui.Currency_Box_Bottom
        self.review_button = self.ui.Review_Button
        self.internet_status_image = self.ui.Internet_Status_Image
        self.internet_status_text = self.ui.Internet_Status
        self.internet_note = self.ui.Internet_Note

        self.apply_settings()  # Настройка и применение функционала
        self.search_signals()  # Отлов изменений

    def apply_settings(self):
        if not self.internet_connection:  # Оповещение о интернет соединении
            self.internet_status_image.setPixmap(QPixmap(":/icons/icons/wifi_off.svg"))
            self.internet_status_text.setGeometry(QRect(285, 550, 135, 15))
            self.internet_status_text.setText("connection not available")
            self.internet_note.setVisible(True)

        for currency in self.currencies:  # Наполнение валютами
            self.currency_box_top.addItem(currency.upper())
            self.currency_box_bottom.addItem(currency.upper())

        self.currency_box_top.setCurrentText("USD")
        self.currency_box_bottom.setCurrentText("RUB")

        self.currency_line_top.setPlaceholderText("enter numbers")
        self.currency_line_top.setMaxLength(15)
        self.currency_line_bottom.setPlaceholderText("fill me up daddy >_<")
        self.currency_line_bottom.setReadOnly(True)

        int_validator = QIntValidator()  # Запрет на ввод всякой параши кроме моих любимых чисел
        self.currency_line_top.setValidator(int_validator)

        self.convert_text.setText(f"1 USD equals to {self.rates_to_usd["rub"]} RUB ")

    def search_signals(self):
        self.currency_line_top.textEdited.connect(self.perform_operation)
        self.currency_box_top.currentTextChanged.connect(self.perform_operation)
        self.currency_box_bottom.currentTextChanged.connect(self.perform_operation)

        self.review_button.clicked.connect(self.get_review)

    def get_rates(self):
        data = {}
        if self.internet_connection:  # Проверка интернета, и получение данных
            data = collect_data(currencies=self.currencies)

            with open("rates.txt", "w") as rates_file:  # Создание файла хранения курса, при доступе к интернету
                for key, value in data.items():
                    rates_file.write(f"{key} = {value}\n")
        else:
            try:  # Попытка получения из файла rates.txt
                with open("rates.txt", "r") as rates_file:
                    for line in rates_file:
                        key, value = line.strip().split(" = ")
                        data[key] = float(value)
            except FileNotFoundError:  # Ошибка файла
                raise ConnectionError("Не установлено соеденение с интернетом, а так-же с файлом rates.txt")

        return data

    def calculate_exchange_rate(self, from_currency, to_currency):  # Получение курса относительно доллара
        if from_currency == "usd" and to_currency == "usd":
            return 1
        if from_currency == "usd":
            return self.rates_to_usd.get(to_currency)
        elif to_currency == "usd":
            return self.rates_to_usd.get(from_currency)
        else:
            return self.rates_to_usd.get(to_currency) / self.rates_to_usd.get(from_currency)

    def perform_operation(self):  # Основная функция взаимодействия интерфейса
        first_currency = self.currency_box_top.currentText().lower()
        second_currency = self.currency_box_bottom.currentText().lower()
        user_input = self.currency_line_top.displayText()
        user_input = user_input.replace(" ", "")

        rate = self.calculate_exchange_rate(first_currency, second_currency)
        self.convert_text.setText(f"1 {first_currency.upper()} equals to {round(rate, 2)} {second_currency.upper()}")

        if len(user_input) == 0:
            self.currency_line_bottom.setText("")
            return False
        if user_input == "-":
            return False
        int_number = int(user_input)
        if int_number <= 0:
            self.currency_line_bottom.setText(user_input)
            return False

        if first_currency == second_currency:
            self.currency_line_bottom.setText(user_input)
            return False

        result = int_number*rate

        result = round(result, 2)
        self.currency_line_bottom.setText(str(result))

    @staticmethod
    def get_review():  # Открытие браузера
        url = "https://forms.gle/dxqSnL2tKuT9JXbt8"
        webbrowser.open(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()

    sys.exit(app.exec())
