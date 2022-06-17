import logging

logging.basicConfig(filename = "C:/LOGS/teste_logging.log",
                    level = logging.DEBUG,
                    format = '%(asctime)s - %(levelname)s | %(message)s')
#logger.debug|info|warning|error|critical
logger = logging.getLogger()


logger.info('CÓDIGO FUNCIONANDO NORMALMENTE')

valor_usuario = input('Digite um valor diferente de 0...')

try:
    if int(valor_usuario) != 0:
        logger.info(f'Valor {valor_usuario} inserido com sucesso no log!')
        print(f'Valor {valor_usuario} inserido com sucesso no log!')
    else:
        logger.warning('Valor igual a 0 detectado!')
        print('Valor igual a 0 detectado!')
        
except Exception as e:
    logger.error(f'Exceção detectada --> {e}')
    print(f'Exceção detectada --> {e}')
    
    
