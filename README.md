# brcomarcas

Contém a lista de comarcas do Brasil e funções de busca.

## Instalação

Como o pacote deve ser privado, não está no Pypi. A instalação é feita a partir do link do repositório no Github executando o seguinte comando:

```
pip install git+https://github.com/iasmini/brcomarcas
```

## Como usar

Funções existentes:
* get_comarcas: lista todas as comarcas do Brasil.
* get_comarcas_by_uf: lista todas as comarcas de um estado específico.

```python
from brcomarcas import get_comarcas_by_uf

# lista todas as comarcas de um estado específico
get_comarcas_by_uf('ac')
>>> ['Acrelândia', 'Assis Brasil', 'Brasiléia', 'Bujari', 'Capixaba', 'Cruzeiro do Sul', 'Epitaciolândia', 'Feijó', 'Jordão', 'Mâncio Lima', 'Manoel Urbano', 'Marechal Thaumaturgo', 'Plácido de Castro', 'Porto Acre', 'Porto Walter', 'Rio Branco', 'Rodrigues Alves', 'Santa Rosa do Purus', 'Senador Guiomard', 'Sena Madureira', 'Tarauacá', 'Xapuri']
```
