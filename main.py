import create_data as cd
import requests as req
from os import scandir

if __name__ == "__main__":
    n_images = 20
    cd.create_images('MRH',n_images,'send/')

    for arch in scandir('send/'):
        with open(arch,'r') as f:
            r = req.post('http://jro-optics.igp.gob.pe/home/save', f)


            