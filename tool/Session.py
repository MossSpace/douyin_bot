KEY_HUNTER_ID_CACHE = 'hunter_id_cache'
mem = {}
HUNTER_ID_CACHE = {0}


def get(key):
    return mem.get(key)


def put(key, value):
    mem[key] = value
