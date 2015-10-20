class Page(object):
    """
    Base class for all Pages.
    """

    sidebar = None
    has_sidebar = None
    default_implicit_wait = 20

    def __init__(self, driver, has_sidebar=False):
        self.driver = driver
        self.has_sidebar = has_sidebar
        self.name = type(self).__name__
