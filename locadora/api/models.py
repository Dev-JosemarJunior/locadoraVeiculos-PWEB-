from django.db import models


class Pessoa(models.Model):
    """
    Representa uma pessoa no sistema de locação, pode ser tanto usado
    para cadastro de Clientes quanto de Funcionários.
    """
    nome = models.CharField(max_length=200)
    cpf = models.IntegerField()
    rg = models.IntegerField()
    endereco_id = models.IntegerField()
    carteira_habilitacao = models.IntegerField()
    telefone = models.IntegerField()
    nacionalidade = models.CharField(max_length=30)
    naturalidade = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1)
    email = models.CharField(max_length=20)


class Endereco(models.Model):
    """
    Representa o Endereço de uma Pessoa ou Fornecedor.
    """
    logradouro = models.CharField(max_length=200)
    cep = models.IntegerField()
    complemento = models.CharField(max_length=200)
    bairro_id = models.IntegerField()


class Bairro(models.Model):
    nome = models.CharField(max_length=200)
    cidade_id = models.IntegerField()


class Cidade(models.Model):
    nome = models.CharField(max_length=200)
    estado_id = models.IntegerField()


class Estado(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=2)
    pais = models.CharField(max_length=200)


class Usuario(models.Model):
    """
    Representa um Usuário do sistemas. Cada usuário tem um prilegio associado a ele.
    1: CLIENTE
    2: FUNCIONÁRIO
    3: ADMIN
    """
    nome = models.CharField(max_length=20)
    senha = models.CharField(max_length=50)
    privilege = models.IntegerField()
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class Cliente(models.Model):
    """
    Representa um  Cliente no sitema da Locadora.
    O status representa a situação do cadastro do cliente,
    caso seu status seja 0 o cadastro ainda não foi aprovado,
    caso seja 1 o cadastro ja foi aprovado.
    """
    pessoa_id = models.IntegerField()
    usuario_id = models.IntegerField()
    status = models.IntegerField()


class Fornecedor(models.Model):
    """
    Representa um Fornecedor da empresa de locação.
    """
    nome = models.CharField(max_length=200)
    cnpj = models.IntegerField()
    endereco_id = models.IntegerField()
    telefone = models.IntegerField()
    email = models.CharField(max_length=20)


class Funcionario(models.Model):
    """
    Representa um Funcionario da empresa de locação.
    """
    pessoa_id = models.IntegerField()
    usuario_id = models.IntegerField()
    carteira_de_trabalho = models.IntegerField()
    cargo = models.CharField(max_length=20)
    salario = models.CharField(max_length=20)


class ClassificacaoVeiculo(models.Model):
    """
    Representa o tipo do veículo: utilitário,	 passeio,	 familiar,	 entre	 outros.
    """
    nome = models.IntegerField()


class Veiculo(models.Model):
    """
    Representa um Veiculo da empresa de locação.
    """
    classificacao_id = models.IntegerField()
    placa = models.CharField(max_length=20)
    cor = models.CharField(max_length=20)
    chassi = models.IntegerField()
    renavam = models.IntegerField()
    foto = models.CharField(max_length=20)
    cadeiras = models.IntegerField()
    assentos_elevacao = models.IntegerField()
    gps = models.CharField(max_length=20)
    quilometragem = models.IntegerField()
    nivel_combustivel = models.IntegerField()
    disponibilidade = models.IntegerField()
    valor = models.FloatField()


class Seguro(models.Model):
    nome = models.CharField(max_length=20)
    valor = models.FloatField()


class Reserva(models.Model):
    cliente_id = models.IntegerField()
    veiculo_id = models.IntegerField()
    seguro_id = models.IntegerField()
    periodo = models.IntegerField()
    created_at = models.DateTimeField()


class Locacao(models.Model):
    funcionario_id = models.IntegerField()
    reserva_id = models.IntegerField()
    created_at = models.DateTimeField()
    valor = models.FloatField()
