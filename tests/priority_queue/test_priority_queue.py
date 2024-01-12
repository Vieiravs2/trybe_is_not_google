from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    data1 = {"qtd_linhas": 10}
    data2 = {"qtd_linhas": 3}
    data3 = {"qtd_linhas": 2}

    priority_queue.enqueue(data1)
    priority_queue.enqueue(data2)
    priority_queue.enqueue(data3)

    assert priority_queue.dequeue() == data2
    assert priority_queue.search(1) == data1

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(100)

    testQtd = dict()
    testQtd["qtd_linhas"] = 5
    print(testQtd)

    assert priority_queue.is_priority(testQtd) is False
