from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = "mensagem" # coloque aqui a mensagem a ser enviada
        self.grupos_ou_pessoas = ["grupo1", 'grupo2'] # coloque aqui os titulos dos grupos e/ou nome de usuários do seu whatsapp
        self.class_name = "_3uMse" # coloque aqui a classe da barra de escrever mensagem exemplo: 
        self.xpath = "//span[@data-icon='send']" # coloque aqui o o caminho do botao de envair exemplo: //span[@data-icon='send']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo_ou_pessoa}']")
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(self.xpath)
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()