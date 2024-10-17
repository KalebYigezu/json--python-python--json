import json

j = '["1", "2", "3", "4", "5", "6", "7", "8", "9"]'

p = json.loads(j)

print(p)

--------------------------------------------------

import json

p = ['1', '2', '3', '4', '5']

j = json.dumps(p)

print(j)
