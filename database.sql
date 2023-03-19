create database aulaIntegracaoSQLePY;
use aulaIntegracaoSQLePY;

create table agenda (
	idItem int not null auto_increment,
    compromisso varchar(100) not null,
    descricao mediumtext null,
    dataInicio date not null,
    horaInicio time not null,
    dataFim date null,
    horaFim time null,
    primary key(idItem)
);