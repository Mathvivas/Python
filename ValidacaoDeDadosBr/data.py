from datetime import datetime, timedelta

class Datas:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        MESES = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
                 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
        mes_cadastro = self.momento_cadastro.month - 1
        return MESES[mes_cadastro]

    def dia_semana(self):
        tupla_semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
        semana = self.momento_cadastro.weekday()
        return tupla_semana[semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada

    def tempo_de_cadastro(self):
        tempo = (datetime.today() + timedelta(days=30, hours=18, minutes=57, seconds=34)) - self.momento_cadastro
        return tempo