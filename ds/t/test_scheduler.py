from ds.proc_sched import Process, Scheduler
p1 = Process(name = 'p1', pid = 1)
p2 = Process(name = 'p2', pid = 2)
p3 = Process(name = 'p3', pid = 3, priority = 5)
p4 = Process(name = 'p4', pid = 4, priority = 15)
s = Scheduler(debug = 1)
s.insert_procs((p1, p2))
s.insert_procs((p3,))
s.proc_priority(p1, 10)
s.proc_priority(p1, -10)
s.proc_priority(p3, 10)
s.proc_priority(p2, 5)
s.proc_priority(p1, 6)
s.insert_procs((p4,))
s.proc_priority(p1, 16)
s.read_qualifier_proc()
s.extract_qualifier_proc()
