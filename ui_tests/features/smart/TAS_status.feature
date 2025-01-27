# language: ru

#  ЗАПУСКАТЬ ТАК
#  behave -f allure_behave.formatter:AllureFormatter -o allure-results ./ui_tests/features/smart/TAS_status.feature

@allure.label.layer:UI
@regress @critical
@allure.label.issue:
@allure.label.layer:web
@allure.label.severity:critical
@allure.label.owner:aiklevts
@autoretry
Функционал: [TAS] Переход Задачи в разные статусы.


  @allure.label.owner:aiklevts
  @TAS_STATUS
  @157603
  @REGRESSION
  Сценарий: #157603 [Smart ITSM] Смена назначенного лица в задаче в статусе в "Ожидании" на текущего оператора
    Дано Перейти по ссылке на страницу 'Задачи'
    Тогда Пользователь проходит авторизацию
    Тогда Активна страница 'Задачи'
    Тогда Пользователь автоматически залогинен
    Тогда Активна консоль "Задачи"
    Тогда Кликнуть на чекбокс "Статус"
    Тогда Выбрать значение "В ожидании"
    Тогда Кликнуть в таблице на первый элемент "TAS"
    Тогда Карточка в статусе "В ожидании"
    Тогда Назначенное лицо "Другой оператор"
    Тогда Изменить назначенное лицо на "Текущий оператор"
    Тогда Карточка в статусе "В ожидании"
    Тогда Назначенное лицо "Текущий оператор"
