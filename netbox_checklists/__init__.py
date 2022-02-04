from extras.plugins import PluginConfig

class CheckLists(PluginConfig):
    name = 'netbox_checklists'
    verbose_name = 'Checklists'
    description = 'Netbox plugin for creating checklists'
    version = '0.1'
    author = 'Anna Krymina'
    author_email = 'aakrymina@ct-dc.ru'
    base_url = 'checklists'
    required_settings = []
    default_settings = {}

config = CheckLists