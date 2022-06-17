from selenium import webdriver
from time import sleep

#---------------------------[VARIÁVEIS/CONSTANTES]------------------------------
CAMINHO_WEBDRIVER = 'C:/Users/carlo/OneDrive/Área de Trabalho/chromedriver.exe'
LINK_DO_SITE = ''

USUARIO = ''
SENHA = ''

#------------------------------[CÓDIGO PRINCIPAL]--------------------------------

chrome = webdriver.Chrome(executable_path=CAMINHO_WEBDRIVER)

chrome.get(LINK_DO_SITE)

#Página de login
chrome.find_element_by_id('txtLogin').send_keys(USUARIO)
chrome.find_element_by_id('txtSenha').send_keys(SENHA)
chrome.find_element_by_id('loginbutton').click()

sleep(1)

#Mudar p/ o Iframe de seleção
chrome.switch_to.frame(0)

chrome.find_element_by_xpath('//*[@id="principal_links"]/a[1]').click()

wait = input('Pressione uma tecla p/ finalizar o chrome...')
chrome.quit()