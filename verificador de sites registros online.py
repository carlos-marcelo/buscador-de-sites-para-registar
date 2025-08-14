from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import os

EDGE_DRIVER_PATH = "C:\\WebDriver\\msedgedriver.exe"

# 100 palavras que remetem à IA
palavras_ia = [
    "iaemchatgpt", "iaemrobotica", "iaemdiagnostico", "iaeminteligencia", "iaemeducacao",
    "iaemavaliacao", "iaemformacao", "iaemplataforma", "iaemtreinamento", "iaemconsultoria",
    "iaemsaude", "iaemfinancas", "iaemengenharia", "iaemjuridico", "iaemmarketing",
    "iaemlogistica", "iaemindustria", "iaemprojetos", "iaemprocessos", "iaempessoas",
    "iaemdados", "iaemgovernanca", "iaemautomacao", "iaemseguranca", "iaemcomunicacao",
    "iaemdesign", "iaemsoftware", "iaemhardware", "iaemtransporte", "iaemservicos",
    "iaemvendas", "iaematendimento", "iaemmetaverso", "iaemrealidadeaumentada", "iaemrealidadevirtual",
    "iaemnlp", "iaemvision", "iaemaudio", "iaemmultimodal", "iaemdashboards",
    "iaemkpi", "iaemokr", "iaemlean", "iaemscrum", "iaemagile",
    "iaemframeworks", "iaemmodelospreditivos", "iaemclassificacao", "iaemregressao", "iaemclustering",
    "iaemrecomendacao", "iaemtransferlearning", "iaemtransformers", "iaembert", "iaemgpt",
    "iaemllm", "iaemopenai", "iaemtensorflow", "iaempytorch", "iaemmlops",
    "iaemcloud", "iaemaws", "iaemazure", "iaemgcp", "iaemdatabricks",
    "iaemdataops", "iaemdataquality", "iaemethics", "iaemtransparency", "iaemexplainability",
    "iaemtrust", "iaemresponsible", "iaemgreen", "iaemsustainable", "iaeminclusive",
    "iaemhumaninloop", "iaemedge", "iaemtinyml", "iaemquantum", "iaemneuromorphic",
    "iaemsyntheticdata", "iaemmodeldrift", "iaemcontinuallearning", "iaemgenerative", "iaemconversational",
    "iaemreasoning", "iaemcognitive", "iaememotion", "iaembehavior", "iaempersonalization",
    "iaemadaptive", "iaemautonomous", "iaemagents", "iaemsmartcities", "iaemsmarthealth",
    "iaemsmartagriculture", "iaemsmartindustry", "iaemsmarteducation", "iaemsmarttransport", "iaemsmartenergy"
]

dominios_ia = [f"{palavra}.com.br" for palavra in palavras_ia]

caminho_saida = "C:\\Users\\marce\\OneDrive\\Área de Trabalho"
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
arquivo_final = os.path.join(caminho_saida, f"dominios_ia_{timestamp}.txt")

service = Service(EDGE_DRIVER_PATH)
options = webdriver.EdgeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--log-level=3")

driver = webdriver.Edge(service=service, options=options)

resultados = []

def verificar_disponibilidade(driver, texto_alvo, timeout=3):
    for _ in range(int(timeout / 0.3)):
        texto_pagina = driver.find_element(By.TAG_NAME, "body").text.lower()
        if texto_alvo.lower() in texto_pagina:
            return "DISPONÍVEL"
        time.sleep(0.3)
    return "INDISPONÍVEL"

for i, dominio in enumerate(dominios_ia, start=1):
    try:
        url = f"https://registro.br/busca-dominio?fqdn={dominio}"
        driver.get(url)

        print(f"[{i}/{len(dominios_ia)}] 🔍 Verificando: {dominio}")
        status = verificar_disponibilidade(driver, "Domínio disponível para registro.")
        print(f"📌 {dominio} → {status}")
        resultados.append((dominio, status))

    except Exception as e:
        print(f"⚠️ Erro ao verificar {dominio}: {e}")
        resultados.append((dominio, "ERRO"))

driver.quit()

with open(arquivo_final, "w", encoding="utf-8") as f:
    f.write(f"{'DOMÍNIO'.ljust(35)} | STATUS\n")
    f.write(f"{'-'*35} | {'-'*10}\n")
    for dominio, status in resultados:
        f.write(f"{dominio.ljust(35)} | {status}\n")

print("\n✅ Verificação concluída!")
print(f"📄 Resultados salvos em: {arquivo_final}")


