import os
import time
from datetime import datetime
from view import terminal as view
from model.util import generate_id
from model.screen_deposit import model_titele
from model.data_manager import write_table_to_file, read_table_from_file
from model.validation_input import input_validation_email, input_validation_date, input_validation_confirmation, input_validation_subscription
from model.messages import model_messages
from model.validation_print import mistake_validation_subscription, mistake_validation_email
from email_validator import validate_email

from view.terminal import  print_general_results, print_message


def list_customers(command):
    """
    funkcja odpowiedzialan za wyświetlenie listy klientów oraz błedów w importowanych plikach
    """

    # jako, że fukncja jest uniwersalna a jej wyietlanie uzależnione jest od tego z jakiego pliku chcemy usyskać informacje 
    # dlatego zmodyfikowane zostały pierwotne założenia poprzez dodanie wymaganego parametru w funkcji

    if command == 1:
        file_name = "model/crm/crm.csv"
        HEADERS = ["id", "name", "email", "subscribed"]
    else:
        file_name = "model/crm/crm_del.csv"
        HEADERS = ["id", "name", "email", "subscribed", "Deletion date", "Reaon for deletion" ]

    #czytanie danych z pliku
    data_table = read_table_from_file(file_name, separator=';')

    print_general_results(data_table, HEADERS)
    view.print_error_message("Not implemented yet.")


def list_customers_mistakes():
    """
    funkcja odpowiedzialan za wyświetlenie błędów w danych klienta
    """
    file_name = "model/crm/crm.csv"
    HEADERS = ["id", "name", "email", "subscribed", "mistake in emial", "mistake in subscribed"]

    #czytanie danych z pliku
    data_table = read_table_from_file(file_name, separator=';')
    data_table_mistake =[]
    
    #towrzenie zmiannych do tabeli ostatecznej z walidacją 3 i 4 zmiennej tabeli pioerwotnej za pomocą funcki walidacyjnych
    for i, value in enumerate(data_table):
        data_table_mistake.append([value[0],value[1], value[2], value[3], mistake_validation_email(value[2]), mistake_validation_subscription(value[3])])

    print_general_results(data_table_mistake, HEADERS)


def add_customer():
    """
    funkcja odpowiedzialan za dodawanie nowgo klient
    """

    #plik z danymi
    file_name = "model/crm/crm.csv"

    #nagłówki wyświetlanej tabeli
    HEADERS = ["id", "name", "email", "subscribed"]

    #generowanie numeru ID z funkcji
    id = generate_id()

    name = None
    email = None
    subscribed = None

    #dana imienia, zwraca wartość zwalidowaną przez funkcje, następnie zamienia usuwa wszystkie zbędne spacje
    name = view.get_input(f'{model_messages["S8"]}').upper()
    name = (' '.join(name.split()))
    
    #zwraca zwalidoważ wartość adresu email
    email = input_validation_email()

    #zwraca zwalidoważ subscribe
    subscribed = input_validation_subscription()

    #utworzenie tabeli z danycmi - dla poprawności trzeb by to była lista w liście - inaczej problem z funkcją wydruku

    new_data = [[id,name,email,subscribed]]
    separator=';'

    #komunikat
    print_message(model_messages["S11"])

    #wydrukowanie na ukranie wyniku tego co się chce dodać
    print_general_results(new_data, HEADERS)

    #upewnienie się czy dane chcemy dodać
    answer = input_validation_confirmation()

    #w zależnopsći od decyzji
    if answer == "1":
        #dodaje dane dio tabeli
        with open(file_name, "a") as file:
            row = separator.join(new_data[0])
            file.write(row + "\n")    
        #komunikat o tym, że dane zostały dodane
        print_message(f'{model_messages["S6"]}')
        input("Press enter")
    else:
        print_message(f'{model_messages["S7"]}')
        input("Press enter")
        

def update_customer():
    """
    funkcja odpowiedzialan za uaktualnienie danych klienta
    tylko dane imienia, emaila lub decyzji o subskrypcji mogą być uaktualnione
    """
    dt = str(datetime.today())

    #lista danyuch biorących udział 
    file_name_crm = "model/crm/crm.csv"
    
    #utworzenie tablic z danymi z plkikó
    data_table_crm = read_table_from_file(file_name_crm, separator=';')
    
    #utworzenie list z wartości ID klienta z modułu crm
    list_of_customer = list([i[0] for i in data_table_crm])

    #nowe listy (klientów i usuwanego)
    new_customer_old =[]
    new_customer_new =[]
    new_customer_to_update =[]
    #nagłówki
    HEADERS = ["id", "name", "email", "subscribed"]

    #utworzenie tabeli z danycmi - dla poprawności trzeb by to była lista w liście - inaczej problem z funkcją wydruku
    
    status_delete = True
    updated_customer = view.get_input(f'{model_messages["S19"]}')
    if not updated_customer:
        status_delete = False
        view.print_message(f'{model_messages["S2"]}')
        input("Press enter")
    elif updated_customer not in list_of_customer:
        status_delete = False
        print_message(f'{model_messages["E14"]}')
        input("Press enter")
    else:
        for i in data_table_crm:
            if i[0] != updated_customer:
                new_customer_old.append(i)
            else:
                new_customer_to_update.append(i)
                print_message(f'\t{model_messages["S20"]}')
                print_general_results(new_customer_to_update, HEADERS)
                item =[]
                item.append(i[0])
                question_1 = view.get_input(f'{model_messages["S15"]}')
                if question_1 == "1":
                    name = view.get_input(f'{model_messages["S8"]}').upper()
                    name = (' '.join(name.split()))
                    item.append(name)
                else:
                    item.append(i[1])
                question_2 = view.get_input(f'{model_messages["S16"]}')
                if question_2 == "1":
                    email = input_validation_email()
                    item.append(email)
                else:
                    item.append(i[2])
                question_3 = view.get_input(f'{model_messages["S17"]}')
                if question_3 == "1":
                    subscribed = input_validation_subscription()
                    item.append(subscribed)
                else:
                    item.append(i[3])
                new_customer_new.append(item)
                new_customer_old.append(item)

    if status_delete == True:

        #tylko jeżeli wartość jest prawdziwa można dokonać usunięcia rekordu
        print_message(f'{model_messages["S18"]}')
        print_general_results(new_customer_new, HEADERS)

        #niezależni jednak od poprawności zadajemy jeszcze pytanie aby się upewnić, że operator chce usunąć daną
        answer = input_validation_confirmation()

        #w zależnopsći od jego decyzji tylko jeżeli potwierdzi 
        if answer == "1":
            #wykonanie polecenia zapisu danych klientów z pominięciem usuniętej
            write_table_to_file(file_name_crm, new_customer_old, separator=';')
            print_message(f'{model_messages["S21"]}')
            input("Press enter")

    view.print_error_message("Not implemented yet.")


def delete_customer():
    """
    funkcja odpowiedzialan za usuwania danych klienta
    sprawdzea czy w danych sprzedażowych nie było transakcji z klientem
    oraz czy wogóle takowy istnieje
    """
    dt = str(datetime.today())

    #lista danyuch biorących udział 
    file_name_crm = "model/crm/crm.csv"
    file_name_del = "model/crm/crm_del.csv"
    file_name_sales = "model/sales/sales.csv"

    #utworzenie tablic z danymi z plkikó
    data_table_crm = read_table_from_file(file_name_crm, separator=';')
    data_table_sales = read_table_from_file(file_name_sales, separator=';')

    #utworzenie list z wartości ID klienta z modułu sprzedaży
    list_of_customer_with_sales = list([i[1] for i in data_table_sales])

    #utworzenie list z wartości ID klienta z modułu crm
    list_of_customer = list([i[0] for i in data_table_crm])
    
    #nowe listy (klientów i usuwanego)
    new_customer_list =[]
    deleted_customer_list =[]

    #nagłówki
    HEADERS = ["id", "name", "email", "subscribed"]
    HEADERS_del = ["id", "name", "email", "subscribed", "Deletion date", "Reaon for deletion" ]

    
    status_delete = True
    delete_customer = view.get_input(f'{model_messages["S12"]}')
    if not delete_customer:
        status_delete = False
        view.print_message(f'{model_messages["S2"]}')
        input("Press enter")
    elif delete_customer in list_of_customer_with_sales:
        status_delete = False
        print_message(f'{model_messages["E13"]}')
        input("Press enter")
    elif delete_customer not in list_of_customer:
        status_delete = False
        print_message(f'{model_messages["E14"]}')
        input("Press enter")
    else:
        for i in data_table_crm:
            if delete_customer != i[0]:
                new_customer_list.append(i)
            else:
                items=[]
                for k in i:
                    items.append(k)
                items.append(dt)
                items.append("Deleted by operator")
                deleted_customer_list.append(items)
        status_delete = True
        
    if status_delete == True:
        #tylko jeżeli wartość jest prawdziwa można dokonać usunięcia rekordu
        print_message(f'{model_messages["S13"]}')
        print_general_results(deleted_customer_list, HEADERS_del)

        #niezależni jednak od poprawności zadajemy jeszcze pytanie aby się upewnić, że operator chce usunąć daną
        answer = input_validation_confirmation()

        #w zależnopsći od jego decyzji tylko jeżeli potwierdzi 
        if answer == "1":
            #wykonanie polecenia zapisu danych klientów z pominięciem usuniętej
            write_table_to_file(file_name_crm, new_customer_list, separator=';')
            separator=';'
            with open(file_name_del, "a") as file:
                for record in deleted_customer_list:
                    row = separator.join(record)
                    file.write(row + "\n")
            #komunikat o tym, że dane zostały dodane
            print_message(f'{model_messages["S14"]}')
            input("Press enter")

    view.print_error_message("Not implemented yet.")


def get_subscribed_emails():
    # ustalenie nazw nagłówków, które wystąpią w tym raporcie
    HEADERS = ["id", "name", "email", "subscribed"]
    
    file = "model/crm/crm.csv"

    #czytanie danych z pliku
    customer_list = read_table_from_file(file, separator=';')
    customer_list_with_subscpription = []

    for i in customer_list:
        if i[3] == "1":         #tylko te dane kótre w ostatnim polu mają 1 
            customer_list_with_subscpription.append(i)
    print_message(f'\t{model_messages["S22"]}')
    print_general_results(customer_list_with_subscpription, HEADERS)
    view.print_error_message("Not implemented yet.")


def get_subscribed_emails_valid():
    # ustalenie nazw nagłówków, które wystąpią w tym raporcie
    HEADERS = ["id", "name", "email", "subscribed"]
    
    file = "model/crm/crm.csv"

    #czytanie danych z pliku
    customer_list = read_table_from_file(file, separator=';')
    customer_list_with_subscpription = []

    for i in customer_list:
        if i[3] == "1":
            try:
                validate_email(i[2]) #sprawdzenie poprawnosci adresu email
                email_quality = 1
            except Exception:
                email_quality = 0
            if email_quality == 1:
                customer_list_with_subscpription.append(i)

    print_message(f'\t{model_messages["S23"]}')
    print_general_results(customer_list_with_subscpription, HEADERS)
    view.print_error_message("Not implemented yet.")


def get_no_subscribed_emails_valid():
    # ustalenie nazw nagłówków, które wystąpią w tym raporcie
    HEADERS = ["id", "name", "email", "subscribed"]
    
    file = "model/crm/crm.csv"

    #czytanie danych z pliku
    customer_list = read_table_from_file(file, separator=';')
    customer_list_with_subscpription = []

    for i in customer_list:
        if i[3] != "1":
            try:
                validate_email(i[2]) #sprawdzenie poprawnosci adresu email
                email_quality = 1
            except Exception:
                email_quality = 0
            if email_quality == 1:
                customer_list_with_subscpription.append(i)

    print_message(f'\t{model_messages["S23"]}')
    print_general_results(customer_list_with_subscpription, HEADERS)
    view.print_error_message("Not implemented yet.")
    

def run_operation(option):
    if option == 1:
        list_customers(1)
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 6:
        get_subscribed_emails_valid()
    elif option == 7:
        get_no_subscribed_emails_valid()
    elif option == 8:
        list_customers_mistakes()
    elif option == 9:
        list_customers(6)
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "List of customer with subscription",
               "List of customer with subscription and valid email",
               "List of customer without subscription but valid email",
               "List of mistakes",
               "Deleted customer's records"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        os.system("cls")
        print(model_titele)
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
