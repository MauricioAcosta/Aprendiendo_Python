#!/usr/bin/env python
# -*- coding: utf-8 -*
import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):

        contact = Contact(name, phone, email)

        self._contacts.append(contact)

        self._save()

        #print('name: {}, phone: {}, email: {}'.format(name,phone,email))

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):

        for index, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[index]
                self._save()
                break

    def search(self, name):

        for contact in self._contacts:
            if contact.name.lower() == name.lower():

                self._print_contact(contact)
                break
        else:
            self._not_found()

    def update(self, name, phone, email):
        pass


    def _save(self):

        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )

    def _print_contact(self, contact):

        print('---*------*------*------*------*------*---')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('---*------*------*------*------*------*---')

    def _not_found(self):
        print('*********')
        print('¡No encontrado!')
        print('*********')

def run():
    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)

        for index, row in enumerate(reader):
            if index==0:
                continue
            contact_book.add(row[0], row[1], row[2])
    while True:

        command = str(raw_input('''
            ¿Que deseas hacer?

            [a]ñador contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir

        '''))

        if command == 'a':
            print('añadiendo contacto')
            name = str(raw_input('Escribe el nombre del contacto: '))
            phone = str(raw_input('Escribe el telefono del contacto: '))
            email = str(raw_input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            print('actualizando contacto')
            name = str(raw_input('Escribe el nombre del contacto: '))
            phone = str(raw_input('Escribe el telefono del contacto: '))
            email = str(raw_input('Escribe el email del contacto: '))
            contact_book.update(name, phone, email)


        elif command == 'b':
            print('buscando contacto')
            name = str(raw_input('Escribe el nombre del contacto: '))
            contact_book.search(name)

        elif command == 'e':
            print('eliminando contacto')
            name = str(raw_input('Escribe el nombre del contacto: '))

            contact_book.delete(name)

        elif command == 'l':
            print('listando contactos')

            contact_book.show_all()

        elif command == 's':
            print('¡Hasta luego :D!')
            break
        else:
            print("Comando invalido.")


if __name__ == '__main__':
    print('B I E N V E N I D O S  A  LA  A G E N D A')
    run()
