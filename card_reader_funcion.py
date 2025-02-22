# -*- coding: utf-8 -*-

import keyboard
import numbers
import csv


class Verify:
    def __init__(self):
        self.answer = None
        self.IDs = []
        self.ID = None
        self.characters = []

    def colect_IDs(self):
        self.IDs = []
        with open("ID's.csv", 'r') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            for linha in leitor_csv:
                self.IDs.append(linha[1])

    def convert_to_characters(self):
        while True:
            evento = keyboard.read_event(suppress=True)
            if evento.event_type == keyboard.KEY_DOWN:
                if evento.name == "enter":
                    break
                elif evento.name == "esc":
                    self.characters = "esc"
                    break
                else:
                    self.characters += evento.name

    def count_verify(self):
        self.convert_to_characters()
        self.ID = ""
        for number in self.characters:
            if self.characters == "esc":
                self.ID = "Esc"
                break
            elif isinstance(number, numbers.Number):
                self.ID = "Error reading!"
                break
            else:
                self.ID = f"{self.ID}{number}"

        if self.ID == "Error reading!":
            self.answer = False
        else:
            if self.ID in self.IDs:
                self.answer = True
            else:
                self.answer = False
        if self.ID == "Esc":
            self.answer = "Esc"

    def verify(self, IDs=None):
        if not IDs:
            self.colect_IDs()
        else:
            self.IDs = IDs
        self.count_verify()
        return self.answer
