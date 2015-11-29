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
    rec_med_aux = models.BooleanField() #Receber� M�dico Auxiliar
    med_aux = models.CharField(max_length=50) #Nome do m�dico auxiliar se a op��o a cima for igual a sim
    equipe_aux =  models.BooleanField() #Outra equipe m�dica participar� da cirurgia
    CID = models.IntegerField() #???

    
class Cirurgia(models.Model):
    diagnostico = models.TextField() #Diagn�stico Principal
    sintomatologia = models.IntegerField() #0: Ausente, 1: Leve, 2: Moderada, 3: Intensa
    doenca_maligna = models.IntegerField() #0: Ausente, 1: Suspeita, 2: Confirmada
    doencas_associadas = models.IntegerField() #0: Ausente, 1: Hipertens�o arterial, 2: Diabetes, 3: Desnutri��o, 4:Hipertens�o arterial + diabetes, 5: Hipertens�o arterial + Desnutri�o, 6: Diabets + Desnutri��o, 7: Todas
    anestesia = models.IntegerField() #0: N�o se aplica, 1: ACA, 2: Local, 3: Local com seda��o, 4: Bloqueio, 5: Geral
    porte_da_operacao = models.IntegerField() #0: Pequeno, 1: M�dio, 2: Grande
    exames_trans-operatorios = models.IntegerField() #0: Ausente, 1: Histopatol�gico, 2: Radiol�gico
    concentrado_de_hemacias = models.FloatField()
    plasma = models.FloatField()
    plaquetas = models.FloatField()
    crio_precipitado = models.FloatField()
    instrumentos_especificos = models.FloatField()
    observacoes = models.TextField()
    cirurgia realizada = models.BooleanField()

  
