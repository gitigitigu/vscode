import os as alpha
alpha.system('nvidia-smi')
alpha.system('pip install colabcode')


from colabcode import ColabCode

ColabCode(port='10000', password='d')
