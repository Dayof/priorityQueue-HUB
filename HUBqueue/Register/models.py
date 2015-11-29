from django.db import models

class Paciente(models.Model):
    nro_pedido = models.IntegerField() #ver se vai usar AutoField
    data_cadastro = models.DateTimeField('Data do Cadastro')
    data_cirurgia = models.DateTimeField('Data da Cirurgia')
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=18)
    idade = models.IntegerField();
    sexo = models.IntegerField(); #0: Mulher, 1: Homem
    data_de_nascimento = models.DateTimeField('Data de Nascimento')
    nro_SUS = models.IntegerField()
    nome_mae = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=15)
    cidade = models.CharField(max_length=30)
    UF = models.CharField(max_length=2)
    clinica = models.CharField(max_length=30)
    convenio = models.CharField(max_length=15)
    CID = models.IntegerField() #???

class Medico(models.Model):
    nome = models.CharField(max_length=50)
    CRM = models.IntegerField()
    telefone = models.CharField(max_length=18)
    email = models.CharField(max_length=40)
    rec_med_aux = models.BooleanField() #Receberá Médico Auxiliar
    med_aux = models.CharField(max_length=50) #Nome do médico auxiliar se a opção a cima for igual a sim
    equipe_aux =  models.BooleanField() #Outra equipe médica participará da cirurgia
    CID = models.IntegerField() #???

    
class Cirurgia(models.Model):
    diagnostico = models.TextField() #Diagnóstico Principal
    sintomatologia = models.IntegerField() #0: Ausente, 1: Leve, 2: Moderada, 3: Intensa
    doenca_maligna = models.IntegerField() #0: Ausente, 1: Suspeita, 2: Confirmada
    doencas_associadas = models.IntegerField() #0: Ausente, 1: Hipertensão arterial, 2: Diabetes, 3: Desnutrição, 4:Hipertensão arterial + diabetes, 5: Hipertensão arterial + Desnutrião, 6: Diabets + Desnutrição, 7: Todas
    anestesia = models.IntegerField() #0: Não se aplica, 1: ACA, 2: Local, 3: Local com sedação, 4: Bloqueio, 5: Geral
    porte_da_operacao = models.IntegerField() #0: Pequeno, 1: Médio, 2: Grande
    exames_trans-operatorios = models.IntegerField() #0: Ausente, 1: Histopatológico, 2: Radiológico
    concentrado_de_hemacias = models.FloatField()
    plasma = models.FloatField()
    plaquetas = models.FloatField()
    crio_precipitado = models.FloatField()
    instrumentos_especificos = models.FloatField()
    observacoes = models.TextField()
    cirurgia realizada = models.BooleanField()

  
