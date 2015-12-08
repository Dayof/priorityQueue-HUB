from django.db import models

#temos que ver o que tem nesse AGHU

class Doenca:
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120)
    CID_letra = models.CharField(max_length=1)  #letra do codigo da doenca
    CID_nro = models.FloatField()               #numero do codigo da doenca

class Prontuario:
    id = models.AutoField(primary_key=True)
    data_cadastro = models.DateTimeField('Data do Cadastro')
    nome = models.CharField(max_length=50)
    nome_mae = models.CharField(max_length=50)
    data_de_nascimento = models.DateTimeField('Data de Nascimento')
    idade = models.IntegerField();
    sexo = models.IntegerField(); #0: Null, 1:Mulher, 2: Homem
    nro_SUS = models.IntegerField()
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=15)
    cidade = models.CharField(max_length=30)
    UF = models.CharField(max_length=2)
    CEP = models.IntegerField()
    DDD = models.IntegerField(max_length=2)
    telefone = IntegerField.CharField(max_length=9)

class Clinica:
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80)

class Convenio
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    
class Medico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    CRM = models.IntegerField()
    telefone = models.CharField(max_length=18)
    email = models.CharField(max_length=40)
    
class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    id_prontuario = models.ForeignKey('id.Prontuario')
    id_clinica = models.ForeignKey('id.Clinica')  
    id_convenio = models.ForeignKey('id.Convenio') 
    id_cid_letra = models.ForeignKey('id.Doenca')
    id_cirurgiao = models.ForeignKey('id.Medico')
    data_pedido = models.DateTimeField('Data do Pedido')
    operacao = models.IntegerField()                    #0: null, 1: eletiva, 2: urgencia
    centro = models.IntegerField(max_length=1)          #0: null, 1: Centro Cirurgico Central, 2: Centro de Cirurgia Ambulatorial, 3: Centro Obstétrico
    local = models.CharField(max_length=30)             #Enf. /Leito ou Apt
    DDD = models.IntegerField(max_length=2)
    telefone_atual = IntegerField.CharField(max_length=9)
    diagnostico = models.TextField()                    #Diagnóstico Principal
    sintomatologia = models.IntegerField(max_length=1)  #0: Ausente, 1: Leve, 2: Moderada, 3: Intensa
    doenca_maligna = models.IntegerField(max_length=1)  #0: Ausente, 1: Suspeita, 2: Confirmada
    doencas_associadas = models.IntegerField(max_length=1)  #0: Ausente, 1: Hipertensão arterial, 2: Diabetes, 3: Desnutrição, 4:Hipertensão arterial + diabetes, 5: Hipertensão arterial + Desnutrião, 6: Diabets + Desnutrição, 7: Todas
    procedimento_proposto = models.TextField()
    porte_da_operacao = models.IntegerField(max_length=1)   #0: null, 1: Pequeno, 2: Médio, 3: Grande
    auxiliares = models.CharField(max_length=50)
    anestesia = models.IntegerField(max_length=1)           #0: null, 1: ACA, 2: Local, 3: Local com sedação, 4: Bloqueio, 5: Geral
    exames_trans-operatorios = models.IntegerField(max_length=1) #0: Ausente, 1: Histopatológico (congelação), 2: Radiológico, 3: Não se Aplica
    concentrado_de_hemacias = models.FloatField()
    plasma = models.FloatField()                    
    plaquetas = models.FloatField()
    crio_precipitado = models.FloatField()
    material = models.TextField()                       #Material de órtese ou prótese
    instrumentos = models.TextField()                   #Instrumento de órtese ou prótese
    observacoes = models.TextField()
    cirurgia realizada = models.BooleanField()

