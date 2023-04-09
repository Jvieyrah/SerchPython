# from ting_file_management.priority_queue import PriorityQueue
# import pytest


# def test_basic_priority_queueing():
#     """Aqui irá sua implementação"""
#     queue = PriorityQueue()

#     with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
#         queue.search(12)

#         small_enought_to_be_a_priority = {
#             'nome_do_arquivo': 'test.txt',
#             'qtd_linhas': 4,
#             'linhas_do_arquivo': ['1', '2', '3', '4'],
#         }

#         too_big_to_be_a_priority = {
#             'nome_do_arquivo': 'test.txt',
#             'qtd_linhas': 6,
#             'linhas_do_arquivo': ['1', '2', '3', '4', '5', '6'],
#         }

#         queue.enqueue(too_big_to_be_a_priority)
#         queue.enqueue(small_enought_to_be_a_priority)

#         assert len(queue) == 2

#         item0 = queue.search(0)
#         assert item0['qtd_linhas'] == 4

#         item1 = queue.search(1)
#         assert item1['qtd_linhas'] == 6

#         queue.dequeue()
#         assert len(queue) == 1

#         item1 = queue.search(0)
#         assert item1['qtd_linhas'] == 6

# from ting_file_management.priority_queue import PriorityQueue
from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    queue = PriorityQueue()

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(50)

    priority = {
        "nome_do_arquivo": "teste.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["linha1", "linha2", "linha3"],
    }

    not_priority = {
        "nome_do_arquivo": "teste.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [
            "linha1",
            "linha2",
            "linha3",
            "linha4",
            "linha5",
            "linha6",
        ],
    }

    queue.enqueue(not_priority)
    queue.enqueue(priority)

    assert len(queue) == 2

    item = queue.search(0)
    assert item["qtd_linhas"] == 3

    item2 = queue.search(1)
    assert item2["qtd_linhas"] == 6

    queue.dequeue()
    assert len(queue) == 1

    item3 = queue.search(0)
    assert item3["qtd_linhas"] == 6
