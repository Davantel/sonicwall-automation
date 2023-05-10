# sonicwall-automation

Este é um script Python que usa a biblioteca Selenium para automatizar a extração de informações de um sistema web e baixar arquivos PDF. O script se conecta a um determinado URL usando o webdriver do Chrome e realiza o login no sistema usando credenciais pré-definidas. Ele então navega pelas diferentes páginas do sistema usando comandos XPath para selecionar elementos específicos, fazendo uso de funções da biblioteca Selenium como "switch_to.frame" e "find_element". 

Em seguida, ele seleciona a data anterior ao dia atual, clicando em diferentes elementos da página para selecionar o intervalo correto. Por fim, o script faz o download de um arquivo PDF clicando em um botão e executa uma série de comandos em um loop para baixar PDFs de várias páginas. O script também lida com exceções e imprime uma mensagem caso não haja vírus na página analisada.

Este projeto é de código aberto e os usuários são incentivados a contribuir com sugestões, correções e melhorias. O código está disponível no GitHub e é distribuído sob a licença MIT, o que significa que pode ser usado livremente por qualquer pessoa, inclusive para fins comerciais.
