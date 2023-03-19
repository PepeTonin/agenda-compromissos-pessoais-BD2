def selectQuery(data_inicial, hora_inicial, range_busca):
    select_script = f"""
    select * from agenda
    where
    if(dataInicio = "{data_inicial}", horaInicio >= "{hora_inicial}", "") or dataInicio > "{data_inicial}"
    limit {range_busca}
    """
    return select_script


def insertQuery(ref1, ref2, ref3, ref4, ref5, ref6):
    insert_script = f"""
    insert into agenda(compromisso, descricao, dataInicio, horaInicio, dataFim, horaFim)
    values ("{ref1}", "{ref2}", "{ref3}", "{ref4}", "{ref5}", "{ref6}")
    """
    return insert_script


def deleteQuery(id):
    delete_script = f"""
    delete from agenda where idItem = {id}
    """
    return delete_script


def selectBeforeDeleteQuery(id):
    select_deleted_script = f"""
    select * from agenda where idItem = {id}
    """
    return select_deleted_script
