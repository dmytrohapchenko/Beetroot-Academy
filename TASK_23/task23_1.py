class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_worker(self, worker: str):
        if isinstance(worker, Worker):
            self.workers.append(worker)

    def printer_workers(self):
        print(f'{self.name} has these workers: ')
        for worker in self.workers:
            print(worker.name)


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.__boss = boss

    @property
    def boss(self) -> str:
        return self.__boss.name

    @boss.setter
    def boss(self, new_boss: str):
        if isinstance(new_boss, Boss):
            self.__boss = new_boss
            print(f'We have new boss {self.boss}')
            new_boss.add_worker(self)


Daniel = Boss(1, 'Daniel', 'KPMG')
James = Worker(2, 'James', 'KPMG', Daniel)

print(James)
print(James.boss)