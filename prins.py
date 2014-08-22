import imp

class prins(object):
    """Printouts Python module source for text files."""
    def __init__(self):
        pass
    def dropto(self, *modules):
        """Prins drops to modules."""
        ms, notfound = [], []
        names = iter(map(str, modules))
        for name in names:
            try:
                ms.append((name, imp.find_module(name)[0]))
            except ImportError:
                notfound.append(name)
        for n,m in ms:
            with open("{0}.txt".format(n), "w") as f:
                f.write(m.read())
                m.close()
        if notfound:
            print("Not Found {0}.".format(", ".join(map(str, notfound))))
