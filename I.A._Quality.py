# coding=utf-8
import os

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class User():
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha


class Manipulador(object):
    def __init__(self):
        self.Stack: Gtk.Stack = Builder.get_object("stack")
        self.banco_dados = []

    def on_main_window_destroy(self, window):
        Gtk.main_quit()

    def on_botao_login_clicked(self, botao):
        nome = Builder.get_object("nome").get_text()
        senha = Builder.get_object("senha").get_text()
        self.login(nome, senha)

    def login(self, nome, senha):
        if nome == 'Elder' and senha == '1':
            self.mensagem('Bem-vindo', 'Usuário logado com sucesso!', 'emblem-dafault')
            self.Stack.set_visible_child_name("view_inicial")
            Window.props.icon_name = 'avatar-default'


        else:
            self.mensagem('Aviso', 'Nome ou Senha incorretos!', 'dialog-error')

    def mensagem(self, param, param1, param2):
        mensagem: Gtk.MessageDialog = Builder.get_object("mensagem")
        mensagem.props.text = param
        mensagem.props.secondary_text = param1
        mensagem.props.icon_name = param2
        mensagem.show_all()
        mensagem.run()
        mensagem.hide()

    def on_botao_sair_clicked(self, botao):
        self.Stack.set_visible_child_name("view_login")
        Window.props.icon_name = 'changes-prevent'

    def on_botao_analisar_clicked(self, botao):
        pass


Builder = Gtk.Builder()
Builder.add_from_file("I.A. Quality.glade")
Builder.connect_signals(Manipulador())
Window: Gtk.Window = Builder.get_object("main_window")
Window.show_all()
Gtk.main()
