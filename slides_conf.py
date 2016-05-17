# %load 'slides_conf.py'
from notebook.services.config import ConfigManager
cm = ConfigManager()
cm.update('livereveal', {
              'theme': 'beige',
              'transition': 'cube',
              'start_slideshow_at': 'selected',
              'width': 1024,
              'height': 768,
})