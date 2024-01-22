person:
- pk
- name
- cpf
- is_active
- is_client
- is_staff
- created_at
- updated_at

product:
- pk
- name
- description
- value
- code

sell:
- pk
- fk_person
- fk_product
- quantity
- status
- total

#Adicionar função do SimpleAPI, para executar as funções do sistema!
#Validação de CPF.
#Validação de telefone.
#Calcular valor total de forma automática.