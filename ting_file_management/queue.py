from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._queue = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return self.size()

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if self.size() == 0:
            raise IndexError("Índice Inválido ou Inexistente")
        return self._queue.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if 0 <= index < self.size():
            return self._queue[index]
        raise IndexError("Índice Inválido ou Inexistentee")

    def size(self):
        return len(self._queue)
