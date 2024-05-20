import json
from datetime import datetime

def obter_dados_paciente():
    dados_paciente = {}
    nome_completo = input("Digite o nome completo do paciente: ")
    nome_completo = ' '.join(word.capitalize() for word in nome_completo.split())
    dados_paciente['Nome completo'] = nome_completo
    cpf = input("Digite o CPF do paciente: ")
    cpf = ''.join(filter(str.isdigit, cpf))
    cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    dados_paciente['CPF'] = cpf
    dados_paciente['Data_de_nascimento'] = input("Digite a data de nascimento do paciente (dd/mm/aaaa): ")
    dados_paciente['Idade'] = calcular_idade(dados_paciente['Data_de_nascimento'])
    dados_paciente['Sexo'] = input("Digite o sexo do paciente (M/F):").upper()
    dados_paciente['Email'] = input("Digite o email do paciente: ")
    celular = input("Digite o número de celular do paciente: ")
    celular = ''.join(filter(str.isdigit, celular))
    celular = f"({celular[:2]}) {celular[2:7]}-{celular[7:]}"
    dados_paciente['Celular'] = celular
    return dados_paciente

def calcular_idade(Data_de_nascimento):
    hoje = datetime.today()
    data_nasc = datetime.strptime(Data_de_nascimento, "%d/%m/%Y")
    Idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
    return Idade

def menu_procedimentos():
    print("\nEscolha o procedimento que você precisa fazer:")
    print("1. Hemograma")
    print("2. Tomografia")
    print("3. Ressonância Magnética")
    print("4. Eletrocardiograma")
    print("5. Sair")

def obter_explicacao_procedimento(procedimento):
    explicacoes = {
        "1": "Um hemograma é um exame de sangue que avalia os componentes do sangue, como glóbulos vermelhos (que transportam oxigênio),"
             "\nglóbulos brancos (que combatem infecções) e plaquetas (que ajudam na coagulação). É um procedimento que permite analisar "
             "\ndiversos aspectos da saúde por meio da análise do sangue, é usado para diagnosticar anemias,"
             "\ninfecções, distúrbios da coagulação e problemas imunológicos.",
        "2": "A tomografia computadorizada, é um exame médico que utiliza raios-X para criar imagens detalhadas do interior do corpo."
             "\nEla produz imagens do corpo, que permitem aos médicos visualizar estruturas como ossos, tecidos moles e órgãos. Essas"
             "\nimagens são geradas através de um processo computadorizado que combina várias imagens de raios-X tiradas de diferentes"
             "\nângulos. A tomografia é amplamente utilizada para diagnosticar uma variedade de condições médicas, desde lesões"
             "\ntraumáticas até câncer, e é uma ferramenta valiosa na avaliação de muitos tipos de doenças e lesões.",
        "3": "A ressonância magnética (RM) é um exame de imagem que utiliza campos magnéticos e ondas de rádio para gerar imagens"
             "\ndetalhadas do interior do corpo. Diferente da tomografia computadorizada (TC), a RM não utiliza radiação ionizante."
             "\nEm vez disso, ela produz imagens de alta resolução dos tecidos moles, como músculos, ligamentos e órgãos internos."
             "\nA ressonância magnética é frequentemente usada para diagnosticar uma variedade de condições, incluindo lesões"
             "\nmusculoesqueléticas, doenças neurológicas e problemas vasculares, oferecendo informações valiosas para os médicos no"
             "\nplanejamento de tratamentos e procedimentos cirúrgicos.",
        "4": "Um eletrocardiograma (ECG) é um exame médico que registra a atividade elétrica do coração ao longo do tempo. Ele é"
             "\nrealizado colocando eletrodos na pele do paciente, geralmente no peito, braços e pernas, que captam os sinais elétricos"
             "\ndo coração. Esses sinais são então registrados em um gráfico chamado de traçado, que mostra a atividade elétrica do"
             "\ncoração em forma de ondas. O ECG é usado para diagnosticar problemas cardíacos, como arritmias, doenças das artérias"
             "\ncoronárias e outros distúrbios do ritmo cardíaco."
    }
    return explicacoes.get(procedimento, "Procedimento não reconhecido.")

def main():
    pacientes = []
    while True:
        print("\n--- Cadastro de Paciente ---")
        paciente = obter_dados_paciente()
        paciente_data = {
            "Nome completo": paciente['Nome completo'],
            "CPF": paciente['CPF'],
            "Data_de_nascimento": paciente['Data_de_nascimento'],
            "Idade": paciente['Idade'],
            "Sexo": paciente['Sexo'],
            "Email": paciente['Email'],
            "Celular": paciente['Celular'],
            "Procedimento": {}
        }
        while True:
            menu_procedimentos()
            procedimento = input("Escolha o procedimento desejado (1-5): ")
            if procedimento == '5':
                break
            explicacao = obter_explicacao_procedimento(procedimento)
            paciente_data["Procedimento"] = {
                "Nome do procedimento": f"Procedimento {procedimento}",
                "Explicação do procedimento": explicacao
            }
        pacientes.append(paciente_data)
        continuar = input("\nDeseja cadastrar outro paciente? (S/N): ").upper()
        if continuar != 'S':
            break
    with open('pacientes.json', 'w') as json_file:
        json.dump(pacientes, json_file, indent=4)
    print("\n--- Lista de Pacientes Cadastrados ---")
    for idx, paciente in enumerate(pacientes, start=1):
        print(f"\nPaciente {idx}:")
        for chave, valor in paciente.items():
            if chave == "Procedimento":
                print(f"{chave.capitalize()}:")
                for p_chave, p_valor in valor.items():
                    print(f"  {p_chave}: {p_valor}")
            else:
                print(f"{chave.capitalize()}: {valor}")

if __name__ == "__main__":
    main()
